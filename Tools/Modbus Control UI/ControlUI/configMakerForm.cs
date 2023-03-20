using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Forms;
using System.IO;

namespace ControlUI
{
    public partial class configMakerForm : Form
    {

        int currentIndex;
        string currentSetting;
        string currentEntry;
        string currentFile;
        int errCode;


        public configMakerForm()
        {
            InitializeComponent();

            currentIndex = 0;
            currentEntry = "";
            currentSetting = "";

            errCode = 0;

            configFileLabel.Text = "Content";
        }



        void loadConfigFile(string infile)
        {
            bool bIsIP = false;
            int index;

            if (File.Exists(infile))
            {
                // Reads file line by line
                System.IO.StreamReader Textfile = new StreamReader(infile);
                string line;

                contentListBox.Items.Clear();

                while ((line = Textfile.ReadLine()) != null)
                {
                    bIsIP = false;

                    if (line.Trim().Length > 0)
                    {

                        index = 0;

                        string[] words = line.Split(',');

                        foreach (var kword in words)
                        {
                            if ((index == 0) && (kword == "IP"))
                            {
                                bIsIP = true;
                            }
                            index++;

                            if (bIsIP)
                            {
                                if (index == 2)
                                {
                                    // just add to IP box
                                    ipBox.Text = kword;
                                }
                                else if (index == 3)
                                {
                                    portBox.Text = kword;
                                }

                            }


                        }   //for

                        if (!bIsIP)
                        {
                            // Just add to list box
                            contentListBox.Items.Add(line);
                        }

                    }   // if line is not empty
                }   //while

                Textfile.Close();

            }   // file exists

        }   // loadConfigFile


        void saveConfigFile(string outfile)
        {
            int iLineCount;
            string stmp;

            currentSetting = "IP," + ipBox.Text + "," + portBox.Text;

            try
            {

                using StreamWriter file = new(outfile);

                file.WriteLine(currentSetting);

                iLineCount = contentListBox.Items.Count;
                for (int i = 0; i < iLineCount; i++)
                {
                    stmp = contentListBox.Items[i].ToString();
                    file.WriteLine(stmp);
                }

                file.Close();
            }
            catch
            {
                errCode = 4;
            }

        }   // saveConfigFile


        void getCurrentUISetting()
        {
            currentSetting = "IP," + ipBox.Text;
            currentEntry = "CTRL,";

            // Access
            if (radioButton1.Checked)
                currentEntry = currentEntry + "RO,";
            else if (radioButton2.Checked)
                currentEntry = currentEntry + "WO,";
            else if (radioButton3.Checked)
            {
                // only allow RW if not checkbox, due to race condition between reading and writing
                if (radioButton4.Checked)   // bit
                    currentEntry = currentEntry + "RO,";
                else
                    currentEntry = currentEntry + "RW,";
            }
            else
                currentEntry = currentEntry + ",";

            // Type
            if (radioButton4.Checked)
                currentEntry = currentEntry + "BIT,";
            else if (radioButton5.Checked)
                currentEntry = currentEntry + "WORD,";
            else
                currentEntry = currentEntry + ",";

            //  Address
            if (bitposComboBox.Text.Trim() == "") {
                if (addrTextBox.Text.Trim() != "")
                {
                    currentEntry = currentEntry + addrTextBox.Text;
                }
                else
                    currentEntry = currentEntry + ",";
            }
            else {
                if (addrTextBox.Text.Trim() != "")
                    currentEntry = currentEntry + addrTextBox.Text + "." + bitposComboBox.Text + ",";
                else
                    currentEntry = currentEntry + ",";
            }


            // Radio or text input (determined also by radio Bit or Word
            if (radioButton4.Checked)
                currentEntry = currentEntry + "1,"; // radio button
            else if (radioButton5.Checked)
                currentEntry = currentEntry + "2,"; // input textbox
            else
                currentEntry = currentEntry + ",";

            // Label
            if (labelTextBox.Text.Trim() == "")
                currentEntry = currentEntry + "Undefined";
            else
                currentEntry = currentEntry + labelTextBox.Text;

        }   //getCurrentUISetting


        void updateCurrentUISetting(string strLine)
        {
            int index, index2;


            // Reset all first
            radioButton1.Checked = false;
            radioButton2.Checked = false;
            radioButton3.Checked = false;
            radioButton4.Checked = false;
            radioButton5.Checked = false;
            addrTextBox.Text = "";
            bitposComboBox.Text = "";
            labelTextBox.Text = "";

            //s = ((ListBoxItem)contentListBox.SelectedItem).Content.ToString;

            string[] words = strLine.Split(',');
            index = 0;
            foreach (var kword in words)
            {
                switch(index)
                {
                    case 0:
                        break;

                    case 1:
                        if (kword == "RO")
                            radioButton1.Checked = true;
                        else if (kword == "WO")
                            radioButton2.Checked = true;
                        else if (kword == "RW")
                            radioButton3.Checked = true;
                        break;

                    case 2:
                        if (kword == "BIT")
                            radioButton4.Checked = true;
                        else if (kword == "WORD")
                            radioButton5.Checked = true;

                        break;

                    case 3:
                        // Address and bitposition
                        string[] addr = kword.Split('.');
                        index2 = 0;
                        foreach (var addrtmp in addr) {
                            if (index2 == 0)
                                addrTextBox.Text = addrtmp.ToString();
                            else
                            {
                                bitposComboBox.Text = addrtmp.ToString();
                            }
                            index2++;
                        }
                        break;

                    case 4:
                        // control type
                        break;

                    case 5:
                        labelTextBox.Text = kword;
                        break;


                }   //switch

                index++;
            }

        }



        void MsgBox(string s)
        {
            MessageBoxButtons buttons = MessageBoxButtons.OK;

            // Displays the MessageBox.
            MessageBox.Show(s, "Indo", buttons);
        }



        private void loadConfigButton_Click(object sender, EventArgs e)
        {
            //var fileContent = string.Empty;
            var filePath = string.Empty;

            OpenFileDialog openFileDialog = new OpenFileDialog();
            openFileDialog.InitialDirectory = ".\\";
            openFileDialog.Filter = "Config files (*.conf)|*.conf|All files (*.*)|*.*";
            openFileDialog.FilterIndex = 2;
            openFileDialog.RestoreDirectory = true;

            if (openFileDialog.ShowDialog() == DialogResult.OK)
            {
                filePath = openFileDialog.FileName;
                loadConfigFile(filePath);

                currentFile = filePath;

                this.Text = "Config Maker [" + currentFile + "]";
            }
            
        }   //load

        private void saveAsButton_Click(object sender, EventArgs e)
        {
            SaveFileDialog saveFileDialog1 = new SaveFileDialog();
            saveFileDialog1.Filter = "Config file|*.conf|All files|*.*";
            saveFileDialog1.Title = "Save a config file";
            saveFileDialog1.ShowDialog();

            // If the file name is not an empty string open it for saving.
            if (saveFileDialog1.FileName != "")
            {
                saveConfigFile(saveFileDialog1.FileName);

                currentFile = saveFileDialog1.FileName;

                this.Text = "Config Maker [" + currentFile + "]";


                MsgBox("File saved. Please restart application to apply the new configuration.");
            }
        }

        private void updateEntryButton_Click(object sender, EventArgs e)
        {
            int index;

            getCurrentUISetting();

            index = contentListBox.SelectedIndex;
            // Replace entry
            contentListBox.Items.RemoveAt(index);
            contentListBox.Items.Insert(index, currentEntry);
        }

        private void contentListBox_SelectedIndexChanged(object sender, EventArgs e)
        {
            string stmp;

            controlGroupBox.Text = "Control #" + contentListBox.SelectedIndex.ToString();
            stmp = contentListBox.GetItemText(contentListBox.SelectedItem); 

            //stmp = ((ListBoxItem)contentListBox.SelectedItem).Content.ToString;
            updateCurrentUISetting(stmp);
        }

        private void configMakerForm_Load(object sender, EventArgs e)
        {
            bitposComboBox.Items.Clear();

            bitposComboBox.Items.Add("");
            for (int i=0;i<16;i++)
                bitposComboBox.Items.Add(i.ToString());
        }

        private void cloneButton_Click(object sender, EventArgs e)
        {

            string stmp = contentListBox.GetItemText(contentListBox.SelectedItem);
            int index = contentListBox.SelectedIndex;

            if (index > -1) // something is selected
            {
                contentListBox.Items.Insert(index, stmp);
            }

        }

        private void addButton_Click(object sender, EventArgs e)
        {
            int index = contentListBox.SelectedIndex;
            if (index > -1)
            {
                contentListBox.Items.Insert(index, "");
            }
            else
            {
                contentListBox.Items.Add("");
            }

            contentListBox.SelectedIndex = contentListBox.Items.Count - 1;
        }

        private void deleteButton_Click(object sender, EventArgs e)
        {
            int index = contentListBox.SelectedIndex;
            contentListBox.Items.RemoveAt(index);
        }

    }
}
