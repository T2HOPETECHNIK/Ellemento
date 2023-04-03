using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Threading;
using System.Threading.Tasks;
using System.Timers;
using System.Windows.Forms;
using static System.Windows.Forms.VisualStyles.VisualStyleElement;
using TextBox = System.Windows.Forms.TextBox;
using Button = System.Windows.Forms.Button;
using Label = System.Windows.Forms.Label;
using System.IO;


namespace ControlUI
{
    public partial class mainForm : Form
    {
        const string CONFIG_FILE = "ControlUI.conf";

        bool bTerminate;

        FIELD[] dfield = new FIELD[Constants.max_fields];
        SYSTEM_CONFIG sysconfig = new SYSTEM_CONFIG();
        //fakeInterface mbcom;    
        comInterface mbcom;

        public READ_DATA rdData;
        public WRITE_DATA wrData;

        pluginHandler plugin;

        System.Timers.Timer timer;

        bool bControlsLoaded;

        // Error
        ERROR_CODE errCode;

        private string getExeDirectory()
        {
            string strExeFilePath = System.Reflection.Assembly.GetExecutingAssembly().Location;
            string strWorkPath = System.IO.Path.GetDirectoryName(strExeFilePath);

            return (strWorkPath);
        }


        public mainForm()
        {
            string folder;

            Console.WriteLine(">> Start app");

            InitializeComponent();

            sysconfig.appTitle = "Control UI";
            sysconfig.updateCycle_ms = 1000;


            statusLabel.Top = this.Height - 70;
            statusLabel.Left = 10;
            statusLabel.Width = this.Width - 20;
            statusLabel.BorderStyle = BorderStyle.Fixed3D;

            bControlsLoaded = false;

            bTerminate = false;

            plugin = new pluginHandler();

            rdData.tbValue = new ushort[Constants.max_fields];
            rdData.cbValue = new bool[Constants.max_fields];
            wrData.BitValue = new bool[Constants.max_fields];
            wrData.WordValue = new ushort[Constants.max_fields];

            folder = getExeDirectory();

            ReadConfig(folder + "\\" + CONFIG_FILE);   //test
            if (bGotError())
            {
                MessageBoxButtons buttons = MessageBoxButtons.OK;

                // Displays the MessageBox.
                MessageBox.Show("Unable to open config file. Application will not be operational.", "Error", buttons);
                //TerminateApplication();
                return;
            }

            initcomm();

            setupReader();

        }   // mainform


        //===============================================================================
        
        private void initcomm()
        {
            mbcom = new comInterface(sysconfig.ip, sysconfig.port);
            //mbcom = new fakeInterface(sysconfig.ip, sysconfig.port);

            if (!mbcom.connect())
            {
                MessageBoxButtons buttons = MessageBoxButtons.OK;
                DialogResult result;

                // Displays the MessageBox.
                result = MessageBox.Show("Unable to connect. Application will not be operational.", "Error", buttons);
                //TerminateApplication();
                errCode = ERROR_CODE.ERROR_COMM_FAIL;
            }
            else
                errCode = ERROR_CODE.ERROR_NONE;

        }   //initcomm


        private bool validLine(string strline)
        {
            // To do
            if (strline.Trim() == "")
                return (false);

            return (true);
        }


        private DATA_TYPES strToDataType(string s)
        {
            if (s == "WORD")
                return (DATA_TYPES.UINT_TYPE);
            else if (s == "INT")
                return (DATA_TYPES.INT_TYPE);
            else if (s == "FLOAT")
                return (DATA_TYPES.FLOAT_TYPE);
            else if (s == "BYTE")
                return (DATA_TYPES.BYTE_TYPE);
            else if (s == "BIT")
                return (DATA_TYPES.BIT_TYPE);
            else
                return (DATA_TYPES.UNKNOWN_TYPE);
        }


        private ADDRESS_ACCESS_TYPES strToAddrAccessType(string sIn)
        {
            string s = sIn.Trim().ToUpper();

            if (s == "RO")
                return (ADDRESS_ACCESS_TYPES.READ_ONLY);
            else if ((s == "WO") || (s == "WR"))
                return (ADDRESS_ACCESS_TYPES.WRITE_ONLY);
            else if (s == "RW")
                return (ADDRESS_ACCESS_TYPES.READ_WRITE);
            else
                return (ADDRESS_ACCESS_TYPES.UNKNOWN);
        }


        private void assignAddress(uint index, string sinput)
        {
            int iCntr = 0;

            string[] addrIn = sinput.Split('.');

            iCntr = 0;
            foreach (var ktag in addrIn)
            {
                if (iCntr == 0)
                    dfield[index].address = (ushort)Int32.Parse(ktag);
                else
                    dfield[index].bitpos = (ushort)Int32.Parse(ktag);
                iCntr++;
            }

        }

       

        private void ReadConfig(string filename)
        {
            uint dfieldindex, colindex;
            string stmp;
            CONFIG_LINE_TYPE configType = CONFIG_LINE_TYPE.CLT_EMPTY;


            if (File.Exists(filename))
            {
                try 
                { 
                    // Reads file line by line
                    System.IO.StreamReader Textfile = new StreamReader(filename);
                    string line;

                    dfieldindex = 0;

                    while ((line = Textfile.ReadLine()) != null)
                    {
                        Console.WriteLine(line);

                        if (validLine(line.Trim()))
                        {
                            string[] words = line.Split(',');

                            colindex = 0;
                            foreach (var kword in words)
                            {
                                if (colindex == 0)  // line config type
                                {
                                    if (kword.Trim().ToUpper() == "CTRL")
                                    {
                                        configType = CONFIG_LINE_TYPE.CLT_CONTROL;
                                    }
                                    else if (kword.Trim().ToUpper() == "IP")
                                    {
                                        configType = CONFIG_LINE_TYPE.CLT_IP;
                                    }
                                    else
                                    {
                                        configType = CONFIG_LINE_TYPE.CLT_EMPTY;
                                    }
                                }
                                else
                                {

                                    if (configType == CONFIG_LINE_TYPE.CLT_CONTROL)
                                    {

                                        switch (colindex)
                                        {

                                            case 1:
                                                // RO, WR/WO/ RW
                                                dfield[dfieldindex].access = (ADDRESS_ACCESS_TYPES)strToAddrAccessType(kword);
                                                break;

                                            case 2:
                                                // Data type
                                                stmp = kword.Trim();
                                                dfield[dfieldindex].dataType = strToDataType(stmp);
                                                break;

                                            case 3:
                                                // Modbus address and bit pos
                                                stmp = kword.Trim();
                                                if (stmp == "")
                                                {
                                                    dfield[dfieldindex].address = 0;
                                                    dfield[dfieldindex].bitpos = 0;
                                                }
                                                else
                                                {   // Assign address and bitpos to dfield
                                                    assignAddress(dfieldindex, stmp);
                                                }

                                                break;

                                            case 4:
                                                // Control type: 1 - Checkbox, 2 - text box
                                                if (kword.Trim() == "1")
                                                    dfield[dfieldindex].controlType = CONTROL_TYPES.TOGGLE_BIT;
                                                else if (kword.Trim() == "2")
                                                    dfield[dfieldindex].controlType = CONTROL_TYPES.TEXT_IO;
                                                else if (kword.Trim() == "3")
                                                    dfield[dfieldindex].controlType = CONTROL_TYPES.TEXT_IO_HEX;
                                                else
                                                    dfield[dfieldindex].controlType = CONTROL_TYPES.UNKNOWN;
                                                break;

                                            case 5:
                                                // Label
                                                dfield[dfieldindex].textLabel = kword.Trim();
                                                break;

                                            default:
                                                dfield[dfieldindex].textLabel += kword.Trim();
                                                break;

                                        }   //switch

                                    }   // if is control


                                    if (configType == CONFIG_LINE_TYPE.CLT_IP)
                                    {
                                        if (colindex == 1)
                                        {
                                            sysconfig.ip = kword.Trim();
                                        }
                                        else if (colindex == 2)
                                        {
                                            sysconfig.port = (int)Int32.Parse(kword.Trim());
                                            break;
                                        }

                                    }   // if

                                }   // if 2nd col and above, else ...

                                colindex++;

                            }   // foreach

                        }   // validLines

                        if (configType == CONFIG_LINE_TYPE.CLT_CONTROL)
                            dfieldindex++;

                    }   //while

                    sysconfig.numFields = dfieldindex;

                    Textfile.Close();

                    errCode = ERROR_CODE.ERROR_NONE;
                }
                catch
                {
                    errCode = ERROR_CODE.ERROR_CONFIG_FAIL;
                }

            }
            else
            {
                // Error
                errCode = ERROR_CODE.ERROR_NO_CONFIG;
            }

            // close file

        }   // ReadConfig


        private bool bGotError()
        {
            return (errCode != ERROR_CODE.ERROR_NONE);
        }
                       

        //=============================================================================

        private void AddControls()
        {
            
            int index;
            int col;
            int row;

            //Add timer

            timer = new System.Timers.Timer();
            timer.Interval = Constants.iTimerInterval_ms;
            timer.Enabled = true;
            timer.Elapsed += new ElapsedEventHandler(timer_Elapsed);
            timer.Start();


            for (index = 0; index < sysconfig.numFields; index++) {

                col = index / Constants.numfields_per_col;
                row = index % Constants.numfields_per_col;

                if (dfield[index].controlType == CONTROL_TYPES.TOGGLE_BIT)
                {
                    // checkbox
                    var newCheckbox = new CheckBox();

                    newCheckbox.Left = Constants.offset_left + (col * Constants.col_offset);
                    newCheckbox.Top = Constants.offset_top + (row * Constants.height_offset);
                    newCheckbox.Width = Constants.label_width;

                    if (dfield[index].access == ADDRESS_ACCESS_TYPES.READ_ONLY)
                    {
                        newCheckbox.Text = "[R] " + dfield[index].textLabel;
                        newCheckbox.Appearance = Appearance.Normal;
                    }
                    else
                    {
                        newCheckbox.Text = "[W] " + dfield[index].textLabel;
                        newCheckbox.Appearance = Appearance.Button;
                    }
                    newCheckbox.FlatStyle = FlatStyle.Popup;
                    newCheckbox.Name = "Chkbox" + index.ToString();
                    newCheckbox.Tag = index;
                    newCheckbox.CheckedChanged += CheckBox_CheckedChanged;

                    newCheckbox.MouseEnter += new EventHandler(check_MouseHover);
                    newCheckbox.MouseLeave += new EventHandler(check_MouseLeave);

                    mainPanel1.Controls.Add(newCheckbox);

                }
                else if ((dfield[index].controlType == CONTROL_TYPES.TEXT_IO) || (dfield[index].controlType == CONTROL_TYPES.TEXT_IO_HEX))
                {
                    // Text box
                    var newLabel = new Label();
                    var newTextbox = new TextBox();
                    var newLabel2 = new Label();
                    var newButton = new Button();
                    var readLabel = new Label();

                    newLabel.Text = dfield[index].textLabel;
                    newLabel.Left = Constants.offset_left + (col * Constants.col_offset);
                    newLabel.Top = Constants.offset_top + (row * Constants.height_offset);
                    newLabel.Width = Constants.label_width;
                    newLabel.TextAlign = ContentAlignment.MiddleLeft;
                    newLabel.Tag = index;
                    newLabel.MouseEnter += new EventHandler(label_MouseHover);
                    newLabel.MouseLeave += new EventHandler(label_MouseLeave);

                    newTextbox.Left = Constants.offset_left + (col * Constants.col_offset) + Constants.label_width;
                    newTextbox.Top = Constants.offset_top + (row * Constants.height_offset);
                    if (dfield[index].controlType == CONTROL_TYPES.TEXT_IO_HEX)
                    {
                        newTextbox.Width = Constants.textbox_short_width;
                        newTextbox.MaxLength = 4;
                    }
                    else
                    {
                        newTextbox.Width = Constants.textbox_width;
                        newTextbox.MaxLength = 5;
                    }
                    newTextbox.Tag = index;
                    newTextbox.Name = "TxtBox" + index.ToString();
                    newTextbox.MouseEnter += new EventHandler(textBox_MouseHover);
                    newTextbox.MouseLeave += new EventHandler(textBox_MouseLeave);

                    if (dfield[index].controlType == CONTROL_TYPES.TEXT_IO_HEX)
                    {
                        newLabel2 = new Label();
                        newLabel2.Top = Constants.offset_top + (row * Constants.height_offset);
                        newLabel2.Left = Constants.offset_left + (col * Constants.col_offset) + Constants.label_width + Constants.textbox_short_width;
                        newLabel2.Width = Constants.label_width_short;
                        newLabel2.TextAlign = ContentAlignment.MiddleLeft;
                        newLabel2.Height = 20;
                        newLabel2.Text = "H";

                        mainPanel1.Controls.Add(newLabel2);
                    }

                    if (dfield[index].access == ADDRESS_ACCESS_TYPES.WRITE_ONLY) 
                    {
                        newButton.Text = "APPLY";
                        newButton.Top = Constants.offset_top + (row * Constants.height_offset);
                        newButton.Left = Constants.offset_left + (col * Constants.col_offset) + Constants.label_width + Constants.textbox_width + Constants.label_width_short;

                        newButton.Tag = index;

                        newButton.Click += new EventHandler(applyBtn_Click);

                        mainPanel1.Controls.Add(newTextbox);
                        mainPanel1.Controls.Add(newLabel);
                        mainPanel1.Controls.Add(newButton);

                    }
                    else if (dfield[index].access == ADDRESS_ACCESS_TYPES.READ_WRITE) 
                    {
                        newButton.Text = "APPLY";
                        newButton.Left = Constants.offset_left + (col * Constants.col_offset) + Constants.label_width + Constants.textbox_width + Constants.label_width_short;
                        newButton.Top = Constants.offset_top + (row * Constants.height_offset);
                        newButton.Tag = index;
                        newButton.Click += new EventHandler(applyBtn_Click);

                        readLabel.Text = "--";
                        readLabel.Left = Constants.offset_left + (col * Constants.col_offset) + Constants.label_width + Constants.textbox_width + Constants.button_width;
                        readLabel.Top = Constants.offset_top + (row * Constants.height_offset);
                        readLabel.Tag = index;
                        readLabel.MouseEnter += new EventHandler(readlabel_MouseHover);
                        readLabel.MouseLeave += new EventHandler(readlabel_MouseLeave);
                        readLabel.Name = "LblBox" + index.ToString();

                        mainPanel1.Controls.Add(newTextbox);
                        mainPanel1.Controls.Add(newLabel);
                        mainPanel1.Controls.Add(newButton);
                        mainPanel1.Controls.Add(readLabel);
                    }
                    else
                    {
                        // read only
                        readLabel.Text = "--";
                        readLabel.Left = Constants.offset_left + (col * Constants.col_offset) + Constants.label_width;
                        readLabel.Top = Constants.offset_top + (row * Constants.height_offset);
                        readLabel.Name = "LblBox" + index.ToString();
                        readLabel.Tag = index;
                        readLabel.MouseEnter += new EventHandler(readlabel_MouseHover);
                        readLabel.MouseLeave += new EventHandler(readlabel_MouseLeave);

                        mainPanel1.Controls.Add(newLabel);
                        mainPanel1.Controls.Add(readLabel);
                    }

                }   // else
                else
                {
                    // Draw nothing ... empty space
                }

            }   //for

        }   //AddControl


        //===========================================================================

        private void updateControl()
        {
            int i;

            for (i = 0; i < sysconfig.numFields; i++)
            {
                if ((dfield[i].access == ADDRESS_ACCESS_TYPES.READ_ONLY) ||
                    (dfield[i].access == ADDRESS_ACCESS_TYPES.READ_WRITE))
                {
                    if (dfield[i].controlType == CONTROL_TYPES.TOGGLE_BIT) // checkbox,bool
                    {

                        if (rdData.cbValue[i])
                        {   //true
                            setCheckBox(i, true);
                        }
                        else
                        {
                            setCheckBox(i, false);
                        }

                    }
                    else if (dfield[i].controlType == CONTROL_TYPES.TEXT_IO)    // label,value
                    {
                        setLabel(i, rdData.tbValue[i].ToString());
                        
                    }
                    else if (dfield[i].controlType == CONTROL_TYPES.TEXT_IO_HEX)    // label,value
                    {
                        setLabel(i, rdData.tbValue[i].ToString("X4") + "H");
                    }

                }   // if
            }   //for


            // Error indicator
            if (errCode != ERROR_CODE.ERROR_NONE)
            {
                errorLabel.BeginInvoke (new Action(() => {
                    errorLabel.Visible = true;
                    errorLabel.Text = "Error: " + errCode.ToString();
                }));
            }
            else
            {
                errorLabel.BeginInvoke(new Action(() => {
                    errorLabel.Visible = false;
                    errorLabel.Text = "No Error ";
                }));
            }

        }   //updateControl


        private void setCheckBox(int index, bool bCheck)
        {
            CheckBox cb = (CheckBox)mainPanel1.Controls["Chkbox" + index.ToString()];

            if (cb != null)
            {
                if (bCheck)
                {
                    cb.BeginInvoke(new Action(() => { 
                        cb.CheckState = CheckState.Checked;
                        cb.BackColor = Color.LightGreen;
                        cb.Checked = true;
                    }));
                }
                else
                {
                    cb.BeginInvoke(new Action(() => {
                        cb.CheckState = CheckState.Unchecked;
                        cb.BackColor = SystemColors.ButtonFace;
                        cb.Checked = false;
                    }));
                }

            }   //if

        }   //setCheckBox


        private void setLabel(int index, string s)
        {
            Label lb;
            string stmp;

            stmp = rdData.tbValue[index].ToString();

            lb = (Label)mainPanel1.Controls["LblBox" + index.ToString()];

            if (lb != null)
            {
                lb.BeginInvoke(new Action(() => {
                    lb.Text = stmp;
                }));
            }
            
        }



        private string getTextValues(int index)
        {
            string tmpstr;

            tmpstr = ((TextBox)mainPanel1.Controls["TxtBox" + index.ToString()]).Text;

            return (tmpstr);
        }


        private bool isHex(IEnumerable<char> chars)
        {
            bool isHex;
            foreach (var c in chars)
            {
                isHex = ((c >= '0' && c <= '9') ||
                         (c >= 'a' && c <= 'f') ||
                         (c >= 'A' && c <= 'F'));

                if (!isHex)
                    return false;
            }
            return true;
        }


        private ushort HexToDec(string strHex)
        {
            ushort ustmp;

            if (isHex(strHex))
            {
                ustmp = (ushort)Convert.ToUInt16(strHex, 16);
                return (ustmp);
            }

            errCode = ERROR_CODE.ERROR_INVALID_INPUT;

            return (0);
        }


        //===============================================================


        void ReaderThreadFunction()
        {
            int i;

            while (!bTerminate)
            {
                if (errCode != ERROR_CODE.ERROR_NONE)
                    return;

                for (i = 0; i < sysconfig.numFields; i++)
                {
                    if ((dfield[i].access == ADDRESS_ACCESS_TYPES.READ_ONLY) ||
                        (dfield[i].access == ADDRESS_ACCESS_TYPES.READ_WRITE))
                    {
                        if ((dfield[i].dataType == DATA_TYPES.UINT_TYPE) || 
                            (dfield[i].dataType == DATA_TYPES.INT_TYPE) || 
                            (dfield[i].dataType == DATA_TYPES.BYTE_TYPE))
                        {
                            rdData.tbValue[i] = mbcom.getRegister(dfield[i].address);
                        }
                        else if (dfield[i].dataType == DATA_TYPES.BIT_TYPE)
                        {
                            rdData.cbValue[i] = mbcom.getCoil(dfield[i].address, dfield[i].bitpos);
                        }

                        errCode = (ERROR_CODE)mbcom.getError();
                    }   //if

                }   // for

                // Send updated data to plugin
                plugin.dataUpdate(wrData, rdData, sysconfig.numFields);

                Thread.Sleep(sysconfig.updateCycle_ms);
            }   //while

        }   // ReaderThreadFunction


        // Thread starter
        void setupReader()
        {
            Thread thread = new Thread(new ThreadStart(ReaderThreadFunction));
            thread.Start();
        }


        public void TerminateApplication()
        {
            bTerminate = true;
            Environment.Exit(0);
        }

        //=========================================================================================
        // Event handlers
        //=========================================================================================

        private void adjustPanel()
        {
            mainPanel1.Top = 50;
            mainPanel1.Left = 40;

            mainPanel1.Size = new Size(this.Width - 100, this.Height - 120);

            statusLabel.Top = this.Height - 60;
            statusLabel.Left = 40;
            statusLabel.Width = this.Width - 30;

            errorLabel.Top = this.Height - 60;
            errorLabel.Left = this.Width - 200;

        }   // adjustPanel

        //=========================================================================================

        private void timer_Elapsed(object sender, EventArgs e)
        {
            if (bControlsLoaded)
            {
                updateControl();
            }
        }


        private void Form1_Load(object sender, EventArgs e)
        {
            this.Text = sysconfig.appTitle + " " + sysconfig.ip;
            AddControls();

            bControlsLoaded = true;

            adjustPanel();
        }

        // Apply button
        protected void applyBtn_Click(object sender, EventArgs e)
        {
            Button btn = sender as Button;
            int index;
            String str = "";
            int itmp;
            ushort ustmp;
            bool isNumeric;

            if (btn != null)
            {
                // now you know the button that was clicked
                index = (int)btn.Tag;
                if ((dfield[index].access == ADDRESS_ACCESS_TYPES.WRITE_ONLY) ||
                    (dfield[index].access == ADDRESS_ACCESS_TYPES.READ_WRITE))
                {

                    str = getTextValues(index).Trim();

                    if (dfield[index].controlType == CONTROL_TYPES.TEXT_IO_HEX)
                    {
                        isNumeric = true;
                    }
                    else
                    {
                        isNumeric = int.TryParse(str, out int n);
                    }

                    if ((str.Length > 0) && isNumeric)
                    {
                        switch (dfield[index].dataType)
                        {
                            case DATA_TYPES.UINT_TYPE:
                                ustmp = 0;
                                if (dfield[index].controlType == CONTROL_TYPES.TEXT_IO_HEX)
                                    ustmp = HexToDec(str);
                                else
                                {
                                    try
                                    {
                                        ustmp = UInt16.Parse(str);
                                    }
                                    catch
                                    {
                                        errCode = ERROR_CODE.ERROR_INVALID_INPUT;
                                    }
                                }

                                if (mbcom != null)
                                {
                                    mbcom.setRegister((ushort)dfield[index].address, ustmp);
                                }

                                wrData.WordValue[index] = ustmp;

                                break;
                            case DATA_TYPES.INT_TYPE:
                                if (dfield[index].controlType == CONTROL_TYPES.TEXT_IO_HEX)
                                    ustmp = HexToDec(str);
                                else
                                {
                                    itmp = Int32.Parse(str);
                                    ustmp = Convert.ToUInt16(itmp);
                                }
                                if (mbcom != null)
                                {
                                    mbcom.setRegister((ushort)dfield[index].address, ustmp);
                                }

                                wrData.WordValue[index] = ustmp;

                                break;

                        }   //switch
                    }
                }   //if

                //MessageBox.Show(btn.Tag + " Clicked: " + str);
            }
        }


        void CheckBox_CheckedChanged(object sender, System.EventArgs e)
        {
            CheckBox cb = sender as CheckBox;
            int index;

            if (cb != null)
            {
                index = (int)cb.Tag;

                if (dfield[index].access == ADDRESS_ACCESS_TYPES.WRITE_ONLY)
                {

                    // Do something only if can write
                    mbcom.setCoil((ushort)dfield[index].address, (ushort)dfield[index].bitpos, cb.Checked);
                    errCode = (ERROR_CODE) mbcom.getError();

                    if (cb.Checked)
                    {
                        cb.BackColor = Color.LightGreen;
                    }
                    else
                    {
                        cb.BackColor = SystemColors.ButtonFace;
                    }

                    // Update wrData for plugins
                    wrData.BitValue[index] = cb.Checked;

                }

                // Note: We cannot allow RW for checkbox since it's a single control without an apply button unlike textbox.
                // The value will flip-flop between on and off because reading (timer based) the value in the PLC is not in sync with writing (event based)
                //(dfield[index].access == ADDRESS_ACCESS_TYPES.READ_WRITE)

            }   // if
        }


        void label_MouseHover(object sender, EventArgs e)
        {
            Label lb = sender as Label;
            int index;

            if (lb != null)
            {
                index = (int)lb.Tag;
                statusLabel.Text = dfield[index].textLabel;
                //statusLabel.Text = "[" + dfield[index].address + "] " + dfield[index].textLabel;
            }
            else
            {
                statusLabel.Text = "None";
            }

        }   //label_MouseHover


        void label_MouseLeave(object sender, EventArgs e)
        {
            Label lb = sender as Label;
            int index;

            if (lb != null)
            {
                index = (int)lb.Tag;
                statusLabel.Text = "";
            }
            else
            {
                statusLabel.Text = "";
            }

        }   //label_MouseLeave


        void textBox_MouseHover(object sender, EventArgs e)
        {
            TextBox tb = sender as TextBox;
            int index;

            if (tb != null)
            {
                index = (int)tb.Tag;
                statusLabel.Text = dfield[index].address.ToString();
            }
            else
            {
                statusLabel.Text = "None";
            }

        }


        void textBox_MouseLeave(object sender, EventArgs e)
        {
            TextBox tb = sender as TextBox;
            int index;

            if (tb != null)
            {
                index = (int)tb.Tag;
                statusLabel.Text = "";
            }
            else
            {
                statusLabel.Text = "";
            }

        }


        void readlabel_MouseHover(object sender, EventArgs e)
        {
            Label lb = sender as Label;
            int index;

            if (lb != null)
            {
                index = (int)lb.Tag;
                
                statusLabel.Text = "[" + dfield[index].address + "]";
            }
            else
            {
                statusLabel.Text = "None";
            }

        }


        void readlabel_MouseLeave(object sender, EventArgs e)
        {
            Label lb = sender as Label;
            int index;

            if (lb != null)
            {
                index = (int)lb.Tag;
                statusLabel.Text = "";
            }
            else
            {
                statusLabel.Text = "";
            }

        }


        void check_MouseHover(object sender, EventArgs e)
        {
            CheckBox cb = sender as CheckBox;
            int index;

            if (cb != null)
            {
                index = (int)cb.Tag;
                statusLabel.Text = "[" + dfield[index].address + "." + dfield[index].bitpos + "] " + dfield[index].textLabel;
            }
            else
            {
                statusLabel.Text = "None";
            }

        }


        void check_MouseLeave(object sender, EventArgs e)
        {
            CheckBox cb = sender as CheckBox;
            int index;

            if (cb != null)
            {
                index = (int)cb.Tag;
                statusLabel.Text = "";
            }
            else
            {
                statusLabel.Text = "";
            }

        }


        private void mainForm_FormClosing(object sender, FormClosingEventArgs e)
        {
            TerminateApplication();
        }


        private void mainForm_ResizeEnd(object sender, EventArgs e)
        {
            adjustPanel();
        }


        private void configurationEditorToolStripMenuItem_Click(object sender, EventArgs e)
        {
            configMakerForm frm2 = new configMakerForm();
            frm2.ShowDialog();
        }

        private void exitToolStripMenuItem_Click(object sender, EventArgs e)
        {
            TerminateApplication();
        }

        private void aboutToolStripMenuItem_Click(object sender, EventArgs e)
        {
            aboutBoxForm abf = new aboutBoxForm();
            abf.ShowDialog();
        }

        private void mainForm_SizeChanged(object sender, EventArgs e)
        {
            adjustPanel();
        }
    }

}
