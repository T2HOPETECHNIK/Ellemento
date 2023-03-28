using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Forms;
using System.Timers;

namespace FamrRackUI
{
    public partial class mainForm : Form
    {

        FARM farm;
        int iActiveRack;
        MBInterface mbi;
        FarmSetup fsetup;

        System.Timers.Timer timer;

        bool bEnableTimerUpdate;
        bool bRackSelected;

        ERROR_CODE errCode;


        Label[] ctrl_shelfLabel;
        TextBox[] ctrl_valveSetting;
        CheckBox[] ctrl_lightControl;
        TrackBar[] ctrl_lightIntensity;
        Label[] label_lightIntensity;
        ComboBox[] ctrl_shelfMode;
        CheckBox[] ctrl_useSchedule;

        int iSelectedWaterCount, iSelectedLightCount;

        Label[] ctrl_waterSchedule;
        Label[] ctrl_lightSchedule;

        CheckBox[] ctrl_pumpMode;
        CheckBox[] ctrl_pumpControl;
        TextBox[] ctrl_pumpFlowRate;
        Label[] feedback_pumpFlowRate;
        Label[] unit_flowRate;
        Label[] feedback_pumpStatus;

        CheckBox[] ctrl_filldrain;
        TextBox[] ctrl_fd_fillduration;
        TextBox[] ctrl_fd_drainduration;
        TextBox[] ctrl_fd_fillrate;
        TextBox[] ctrl_fd_drainrate;

        Label[] label_placeholder1;
        Label[] label_placeholder2;
        Label[] label_placeholder3;
        Label[] label_placeholder4;

        Button[] ctrl_recoverPump;


        bool[] waterSchedList = new bool[Constants.maxShelf];
        bool[] lightSchedList = new bool[Constants.maxLight];

        int iWaterScheduleIndex, iLightScheduleIndex;

        bool[] bFeedbackPumpOn;
        ushort[] uFeedbackPumpSpeed;
        bool[] bPumpFilling;

        // ------------------------
        // ------------------------

        public mainForm()
        {
            InitializeComponent();
            initModule();
        }

        private void Form1_Load(object sender, EventArgs e)
        {
            initUI();
        }


        void initModule()
        {
            bEnableTimerUpdate = false;

            fsetup = new FarmSetup();

            farm = fsetup.setup();

            //iActiveRack = 1;
        }


        public void initUI()
        {
            bRackSelected = false;

            adjustUIElements();

            rackComboBox.Items.Clear();
            for (int i = 1; i <= Constants.numRacks; i++)
            {
                rackComboBox.Items.Add(i.ToString());
            }

            statusLabel.Text = Constants.STATUS_INDICATOR[Constants.STAT_IDX_UNKNOWN];
            statusLabel.Top = 40;
            statusLabel.Width = 100;
            statusLabel.Left = this.Width - 150;

            ctrl_shelfLabel = new Label[Constants.maxShelf];
            ctrl_valveSetting = new TextBox[Constants.maxShelf];
            ctrl_lightControl = new CheckBox[Constants.maxLight];
            ctrl_lightIntensity = new TrackBar[Constants.maxLight];
            label_lightIntensity = new Label[Constants.maxLight];

            ctrl_shelfMode = new ComboBox[Constants.maxShelf];
            ctrl_useSchedule = new CheckBox[Constants.maxLight];    // for both light and water

            ctrl_waterSchedule = new Label[Constants.maxShelf];
            ctrl_lightSchedule = new Label[Constants.maxLight];

            ctrl_pumpControl = new CheckBox[Constants.maxPump];
            ctrl_pumpFlowRate = new TextBox[Constants.maxPump];
            feedback_pumpFlowRate = new Label[Constants.maxPump];

            feedback_pumpStatus = new Label[Constants.maxPump];

            ctrl_pumpMode = new CheckBox[Constants.maxPump];
            unit_flowRate = new Label[Constants.maxPump];
            ctrl_recoverPump = new Button[Constants.maxPump];

            ctrl_filldrain = new CheckBox[Constants.maxPump];
            ctrl_fd_fillduration = new TextBox[Constants.maxPump];
            ctrl_fd_drainduration = new TextBox[Constants.maxPump];
            ctrl_fd_fillrate = new TextBox[Constants.maxPump];
            ctrl_fd_drainrate = new TextBox[Constants.maxPump];

            label_placeholder1 = new Label[Constants.maxPump];
            label_placeholder2 = new Label[Constants.maxPump];
            label_placeholder3 = new Label[Constants.maxPump];
            label_placeholder4 = new Label[Constants.maxPump];

            PopulateShelfControls();

            StartTimer();
        }


        private void mainForm_SizeChanged(object sender, EventArgs e)
        {
            adjustUIElements();
        }


        private void adjustUIElements()
        {
            int index;

            if (iActiveRack > 0)
                index = iActiveRack - 1;
            else
                index = 0;

            mainPanel.Top = 70;
            mainPanel.Left = 50;
            mainPanel.Width = this.Width - 100;
            mainPanel.Height = this.Height - 150;

            // Top status Error indicator
            statusLabel.Top = 40;
            statusLabel.Width = 100;
            statusLabel.Left = this.Width - 150;

            helpBarText.Top = this.Height - 70;
            helpBarText.Left = 50;
            helpBarText.BorderStyle = BorderStyle.Fixed3D;
            helpBarText.Text = "---";
            helpBarText.Width = 300;

            SchedulerGroup.Left = 850;

            logListBox.Top = farm.rack[index].numShelf * (Constants.CTRL_HEIGHT + Constants.PUMP_CTRL_GAP);
            logListBox.Left = 2;
            logListBox.Height = mainPanel.Height - logListBox.Top;
            logListBox.Width = (mainPanel.Width/2) - 5;

            readLogListBox.Top = farm.rack[index].numShelf * (Constants.CTRL_HEIGHT + Constants.PUMP_CTRL_GAP);
            readLogListBox.Left = logListBox.Left + logListBox.Width + 2;
            readLogListBox.Height = mainPanel.Height - logListBox.Top;
            readLogListBox.Width = (mainPanel.Width/2)- 5;
        }


        void StartTimer()
        {
            timer = new System.Timers.Timer();
            timer.Interval = Constants.TIMER_INTERVAL_MS;
            timer.Enabled = true;
            timer.Elapsed += new ElapsedEventHandler(timer_Elapsed);
            timer.Start();
        }

        private void timer_Elapsed(object sender, EventArgs e)
        {
            if (bEnableTimerUpdate)
            {
                updateStatus();
                update_UI_from_Feedback();

                updateLogs();
            }
        }



        private void rackComboBox_SelectedIndexChanged(object sender, EventArgs e)
        {
            if (rackComboBox.Text.Trim() != "")
            {
                iActiveRack = Int32.Parse(rackComboBox.Text);

                bRackSelected = true;

                switchActiveRack(iActiveRack);

                IPLabel.Text = "[" + farm.rack[iActiveRack-1].IP + "]";

                //PopulateShelfControls();
                UpdateShelfControls();

                logListBox.Items.Clear();
                readLogListBox.Items.Clear();
            }
        }


        // Rack number starts at 1
        private void switchActiveRack(int racknum)
        {
            int index = racknum - 1;
            mbi = new MBInterface(farm.rack[index].IP, farm.rack[index].port);
            if (mbi != null)
                errCode = mbi.getLastError();

            bEnableTimerUpdate = true;

        }   //



        private void updateStatus()
        {
            if (errCode == ERROR_CODE.ERROR_NONE)
            {
                statusLabel.BeginInvoke(new Action(() => {
                    statusLabel.Text = Constants.STATUS_INDICATOR[Constants.STAT_IDX_NORMAL]; ;
                    statusLabel.BackColor = Color.LightGreen;
                }));
            }
            else
            {
                statusLabel.BeginInvoke(new Action(() => {
                    statusLabel.Text = Constants.STATUS_INDICATOR[Constants.STAT_IDX_ERROR];
                    statusLabel.BackColor = Color.Red;
                }));

            }
 
        }   // updateStatus



        //
        //  This is either enable or disable the controls that are not valid. eg. Type A racks don't have up to 14 shelfs and only 1 pump
        //
        private void UpdateShelfControls()
        {
            ComboBox cmb;
            CheckBox cb;
            TextBox tb;
            Label lb;
            TrackBar trb;
            Button btn;

            bool bControlEnabled;
            if (farm.rack[iActiveRack-1].numShelf == 11)
                // 11
                bControlEnabled = false;
            else
                // 14
                bControlEnabled = true;

            mainPanel.BeginInvoke(new Action(() => {

                cmb = (ComboBox)mainPanel.Controls["Ctrl_mode_11"];
                cmb.Enabled = bControlEnabled;
                cmb = (ComboBox)mainPanel.Controls["Ctrl_mode_12"];
                cmb.Enabled = bControlEnabled;
                cmb = (ComboBox)mainPanel.Controls["Ctrl_mode_13"];
                cmb.Enabled = bControlEnabled;

                cb = (CheckBox)mainPanel.Controls["Ctrl_use_water_schedule_11"];
                cb.Enabled = bControlEnabled;
                cb = (CheckBox)mainPanel.Controls["Ctrl_use_water_schedule_12"];
                cb.Enabled = bControlEnabled;
                cb = (CheckBox)mainPanel.Controls["Ctrl_use_water_schedule_13"];
                cb.Enabled = bControlEnabled;

                tb = (TextBox)mainPanel.Controls["Ctrl_valve_setting_11"];
                tb.Enabled = bControlEnabled;
                tb = (TextBox)mainPanel.Controls["Ctrl_valve_setting_12"];
                tb.Enabled = bControlEnabled;
                tb = (TextBox)mainPanel.Controls["Ctrl_valve_setting_13"];
                tb.Enabled = bControlEnabled;

                lb = (Label)mainPanel.Controls["Ctrl_water_schedule_11"];
                lb.Enabled = bControlEnabled;
                lb = (Label)mainPanel.Controls["Ctrl_water_schedule_12"];
                lb.Enabled = bControlEnabled;
                lb = (Label)mainPanel.Controls["Ctrl_water_schedule_13"];
                lb.Enabled = bControlEnabled;

                cb = (CheckBox)mainPanel.Controls["Ctrl_light_control_11"];
                cb.Enabled = bControlEnabled;
                cb = (CheckBox)mainPanel.Controls["Ctrl_light_control_12"];
                cb.Enabled = bControlEnabled;
                cb = (CheckBox)mainPanel.Controls["Ctrl_light_control_13"];
                cb.Enabled = bControlEnabled;

                trb = (TrackBar)mainPanel.Controls["Ctrl_light_intensity_11"];
                trb.Enabled = bControlEnabled;
                trb = (TrackBar)mainPanel.Controls["Ctrl_light_intensity_12"];
                trb.Enabled = bControlEnabled;
                trb = (TrackBar)mainPanel.Controls["Ctrl_light_intensity_13"];
                trb.Enabled = bControlEnabled;

                lb = (Label)mainPanel.Controls["Ctrl_light_schedule_11"];
                lb.Enabled = bControlEnabled;
                lb = (Label)mainPanel.Controls["Ctrl_light_schedule_12"];
                lb.Enabled = bControlEnabled;
                lb = (Label)mainPanel.Controls["Ctrl_light_schedule_13"];
                lb.Enabled = bControlEnabled;

                // ==========================================
                // Pump Control

                cb = (CheckBox)mainPanel.Controls["Ctrl_pump_control_1"];
                cb.Enabled = bControlEnabled;

                cb = (CheckBox)mainPanel.Controls["Ctrl_pump_mode_1"];
                cb.Enabled = bControlEnabled;

                tb = (TextBox)mainPanel.Controls["Ctrl_pump_flowrate_1"];
                tb.Enabled = bControlEnabled;

                lb = (Label)mainPanel.Controls["Feedback_pump_flowrate_1"];
                lb.Enabled = bControlEnabled;

                cb = (CheckBox)mainPanel.Controls["CTRL_fill_drain_1"];
                cb.Enabled = bControlEnabled;

                lb = (Label)mainPanel.Controls["Feedback_pump_status_1"];
                lb.Enabled = bControlEnabled;

                tb = (TextBox)mainPanel.Controls["CTRL_fill_duration_1"];
                tb.Enabled = bControlEnabled;

                tb = (TextBox)mainPanel.Controls["CTRL_fill_rate_1"];
                tb.Enabled = bControlEnabled;

                tb = (TextBox)mainPanel.Controls["CTRL_drain_duration_1"];
                tb.Enabled = bControlEnabled;

                tb = (TextBox)mainPanel.Controls["CTRL_drain_rate_1"];
                tb.Enabled = bControlEnabled;

                btn = (Button)mainPanel.Controls["CTRL_recover_1"];
                btn.Enabled = bControlEnabled;
            }));


        }   // UpdateShelfControls


        // Create the controls that are not static
        private void PopulateShelfControls()
        {
            //ushort index;
            int positionX;
            int positionY;

            int iRackIndex;

            if (iActiveRack > 0)
                iRackIndex = iActiveRack - 1;
            else
                iRackIndex = 0;


            //Static controls
            startHCombo.Items.Clear();
            endHCombo.Items.Clear();
            startHComboL.Items.Clear();
            endHComboL.Items.Clear();
            for (int i = 0; i < 24; i++)
            {
                startHCombo.Items.Add(i.ToString("D2"));
                endHCombo.Items.Add(i.ToString("D2"));
                startHComboL.Items.Add(i.ToString("D2"));
                endHComboL.Items.Add(i.ToString("D2"));
            }

            startMCombo.Items.Clear();
            endMCombo.Items.Clear();
            startMComboL.Items.Clear();
            endMComboL.Items.Clear();
            for (int i = 0; i < 60; i++)
            {
                startMCombo.Items.Add(i.ToString("D2"));
                endMCombo.Items.Add(i.ToString("D2"));
                startMComboL.Items.Add(i.ToString("D2"));
                endMComboL.Items.Add(i.ToString("D2"));
            }


            SchedulerItemCountLabel.BorderStyle = BorderStyle.FixedSingle;

            // Log box
            logListBox.Top = 630;   // farm.rack[iActiveRack].numShelf * (Constants.CTRL_HEIGHT + Constants.PUMP_CTRL_GAP);
            logListBox.Left = 2;
            logListBox.Height = mainPanel.Height - logListBox.Top;
            logListBox.Width = (mainPanel.Width/2) - 5;
            logListBox.Items.Clear();

            readLogListBox.Top = 630;   // farm.rack[iActiveRack].numShelf * (Constants.CTRL_HEIGHT + Constants.PUMP_CTRL_GAP);
            readLogListBox.Left = logListBox.Left + logListBox.Width + 2;
            readLogListBox.Height = mainPanel.Height - readLogListBox.Top;
            readLogListBox.Width = (mainPanel.Width/2) - 5;
            readLogListBox.Items.Clear();

            // Dynamic controls

            for (int index = (ushort)(farm.rack[iRackIndex].numShelf - 1); index >= 0; index--)
            {
                if (farm.rack[iRackIndex].shelf[index].bIsAvailable)
                {
                    positionY = (farm.rack[iRackIndex].numShelf - index) * Constants.CTRL_HEIGHT;
                    positionX = Constants.POS_LABEL_LEFT;

                    ctrl_shelfLabel[index] = new Label();
                    ctrl_shelfLabel[index].Top = Constants.POS_TOP + positionY;
                    ctrl_shelfLabel[index].Left = positionX;
                    ctrl_shelfLabel[index].Text = "SHELF " + (index + 1).ToString();
                    mainPanel.Controls.Add(ctrl_shelfLabel[index]);

                    positionX += Constants.WIDTH_LABEL;

                    ctrl_shelfMode[index] = new ComboBox();
                    ctrl_shelfMode[index].Items.Add("AUTO");
                    ctrl_shelfMode[index].Items.Add("SEMI");
                    ctrl_shelfMode[index].Items.Add("MANU");
                    ctrl_shelfMode[index].SelectedIndex = 0;
                    ctrl_shelfMode[index].DropDownStyle = ComboBoxStyle.DropDown;
                    ctrl_shelfMode[index].Left = positionX;
                    ctrl_shelfMode[index].Top = Constants.POS_TOP + positionY;
                    ctrl_shelfMode[index].Width = Constants.WIDTH_CHECKBOX - 10;
                    ctrl_shelfMode[index].FlatStyle = FlatStyle.Popup;
                    ctrl_shelfMode[index].BackColor = Color.LightBlue;
                    ctrl_shelfMode[index].Tag = index;
                    ctrl_shelfMode[index].Name = "Ctrl_mode_" + index.ToString();
                    ctrl_shelfMode[index].MouseHover += ModeCombo_MouseHover;
                    ctrl_shelfMode[index].MouseLeave += Clear_HelpText;
                    ctrl_shelfMode[index].SelectedValueChanged += ModeComboBox_CheckedChanged;
                    mainPanel.Controls.Add(ctrl_shelfMode[index]);

                    positionX += Constants.WIDTH_CHECKBOX;

                    ctrl_useSchedule[index] = new CheckBox();
                    ctrl_useSchedule[index].Top = Constants.POS_TOP + positionY;
                    ctrl_useSchedule[index].Left = positionX;
                    ctrl_useSchedule[index].Width = Constants.WIDTH_CHECKBOX - 10;
                    ctrl_useSchedule[index].Text = "OFF";
                    ctrl_useSchedule[index].TextAlign = ContentAlignment.MiddleCenter;
                    ctrl_useSchedule[index].FlatStyle = FlatStyle.Popup;
                    ctrl_useSchedule[index].Appearance = Appearance.Button;
                    ctrl_useSchedule[index].Tag = index;
                    ctrl_useSchedule[index].Name = "Ctrl_use_water_schedule_" + index.ToString();
                    ctrl_useSchedule[index].MouseHover += UseScheduler_MouseHover;
                    ctrl_useSchedule[index].MouseLeave += Clear_HelpText;
                    ctrl_useSchedule[index].CheckedChanged += WaterLightScheduleCheckBox_Changed;
                    mainPanel.Controls.Add(ctrl_useSchedule[index]);

                    positionX += Constants.WIDTH_CHECKBOX;

                    ctrl_valveSetting[index] = new TextBox();
                    ctrl_valveSetting[index].Top = Constants.POS_TOP + positionY;
                    ctrl_valveSetting[index].Left = positionX;
                    ctrl_valveSetting[index].Width = Constants.WIDTH_TEXTBOX - 10;
                    ctrl_valveSetting[index].BorderStyle = BorderStyle.Fixed3D;
                    ctrl_valveSetting[index].Tag = index;
                    ctrl_valveSetting[index].Name = "Ctrl_valve_setting_" + index.ToString();
                    ctrl_valveSetting[index].Text = "0";
                    ctrl_valveSetting[index].MaxLength = 3;
                    ctrl_valveSetting[index].Visible = true;
                    ctrl_valveSetting[index].MouseHover += ValveSetting_MouseHover;
                    ctrl_valveSetting[index].MouseLeave += Clear_HelpText;
                    ctrl_valveSetting[index].LostFocus += UpdateValveSetting;
                    mainPanel.Controls.Add(ctrl_valveSetting[index]);

                    positionX += Constants.WIDTH_TEXTBOX;

                    ctrl_waterSchedule[index] = new Label();
                    ctrl_waterSchedule[index].Top = Constants.POS_TOP + positionY;
                    ctrl_waterSchedule[index].Left = positionX;
                    ctrl_waterSchedule[index].Width = Constants.WIDTH_SCHEDULE;
                    ctrl_waterSchedule[index].Text = "00:00-00:00";
                    ctrl_waterSchedule[index].TextAlign = ContentAlignment.MiddleCenter;
                    ctrl_waterSchedule[index].Tag = index;
                    ctrl_waterSchedule[index].Name = "Ctrl_water_schedule_" + index.ToString();
                    ctrl_waterSchedule[index].MouseClick += WaterScheduleClicked;
                    mainPanel.Controls.Add(ctrl_waterSchedule[index]);

                    positionX += Constants.WIDTH_SCHEDULE + Constants.SPACER;

                    if (farm.rack[iRackIndex].light[index].bIsAvailable) {

                        ctrl_lightControl[index] = new CheckBox();
                        ctrl_lightControl[index].Top = Constants.POS_TOP + positionY;
                        ctrl_lightControl[index].Left = positionX;
                        ctrl_lightControl[index].Width = Constants.WIDTH_CHECKBOX - 10;
                        ctrl_lightControl[index].Text = "LED";
                        ctrl_lightControl[index].TextAlign = ContentAlignment.MiddleCenter;
                        ctrl_lightControl[index].FlatStyle = FlatStyle.Popup;
                        ctrl_lightControl[index].Appearance = Appearance.Button;
                        ctrl_lightControl[index].Tag = index;
                        ctrl_lightControl[index].Name = "Ctrl_light_control_" + index.ToString();
                        ctrl_lightControl[index].MouseHover += LightCheckBox_MouseHover;
                        ctrl_lightControl[index].MouseLeave += Clear_HelpText;
                        ctrl_lightControl[index].CheckedChanged += LightCheckBox_CheckedChanged;
                        mainPanel.Controls.Add(ctrl_lightControl[index]);

                        positionX += Constants.WIDTH_CHECKBOX;


                        ctrl_lightIntensity[index] = new TrackBar();
                        ctrl_lightIntensity[index].Top = Constants.POS_TOP + positionY;
                        ctrl_lightIntensity[index].Left = positionX;
                        ctrl_lightIntensity[index].Width = Constants.WIDTH_BAR - 10;
                        ctrl_lightIntensity[index].Minimum = 0;
                        ctrl_lightIntensity[index].Maximum = 100;
                        ctrl_lightIntensity[index].SmallChange = 1;
                        ctrl_lightIntensity[index].TickStyle = TickStyle.Both;
                        ctrl_lightIntensity[index].Tag = index;
                        ctrl_lightIntensity[index].MouseHover += LightIntensity_MouseHover;
                        ctrl_lightIntensity[index].MouseLeave += Clear_HelpText;
                        ctrl_lightIntensity[index].ValueChanged += UpdateLightIntensityLabel;
                        ctrl_lightIntensity[index].LostFocus += UpdateLightIntensity;
                        ctrl_lightIntensity[index].Name = "Ctrl_light_intensity_" + index.ToString();
                        mainPanel.Controls.Add(ctrl_lightIntensity[index]);

                        positionX += Constants.WIDTH_BAR;

                        label_lightIntensity[index] = new Label();
                        label_lightIntensity[index].Top = Constants.POS_TOP + positionY;
                        label_lightIntensity[index].Left = positionX;
                        label_lightIntensity[index].Width = Constants.WIDTH_UNIT_LABEL;
                        label_lightIntensity[index].BorderStyle = BorderStyle.FixedSingle;
                        label_lightIntensity[index].TextAlign = ContentAlignment.MiddleCenter;
                        label_lightIntensity[index].Tag = index;
                        label_lightIntensity[index].Text = "0";
                        label_lightIntensity[index].Name = "label_light_intensity_" + index.ToString();
                        mainPanel.Controls.Add(label_lightIntensity[index]);


                        positionX += Constants.WIDTH_UNIT_LABEL;

                        ctrl_lightSchedule[index] = new Label();
                        ctrl_lightSchedule[index].Top = Constants.POS_TOP + positionY;
                        ctrl_lightSchedule[index].Left = positionX;
                        ctrl_lightSchedule[index].Width = Constants.WIDTH_SCHEDULE;
                        ctrl_lightSchedule[index].Text = "00:00-00:00";
                        ctrl_lightSchedule[index].TextAlign = ContentAlignment.MiddleCenter;
                        ctrl_lightSchedule[index].Tag = index;
                        ctrl_lightSchedule[index].Name = "Ctrl_light_schedule_" + index.ToString();
                        ctrl_lightSchedule[index].MouseClick += LightScheduleClicked;
                        mainPanel.Controls.Add(ctrl_lightSchedule[index]);

                    }   // if light available

                }   // if is shelf available

            }   // for

            //========================================================

            positionY = Constants.POS_PUMP_TOP;

            // Pumps
            for (int i = 0; i < farm.rack[iRackIndex].numPump; i++)
            {
                if (farm.rack[iRackIndex].pump[i].bIsAvailable)
                {
                    positionX = Constants.POS_PUMP_LEFT;
                    positionY = positionY + (((Constants.POS_PUMP_HEIGHT + Constants.PUMP_CTRL_GAP) * 3 ) * i);

                    ctrl_pumpControl[i] = new CheckBox();
                    ctrl_pumpControl[i].Top = positionY;
                    ctrl_pumpControl[i].Left = positionX;
                    ctrl_pumpControl[i].Width = Constants.POS_PUMP_WIDTH;
                    ctrl_pumpControl[i].Height = Constants.POS_PUMP_HEIGHT;
                    ctrl_pumpControl[i].Appearance = Appearance.Button;
                    ctrl_pumpControl[i].Tag = i;
                    ctrl_pumpControl[i].Name = "Ctrl_pump_control_" + i.ToString();
                    ctrl_pumpControl[i].Text = "PUMP " + (i + 1).ToString();
                    ctrl_pumpControl[i].TextAlign = ContentAlignment.MiddleCenter;
                    ctrl_pumpControl[i].MouseHover += PumpControl_MouseHover;
                    ctrl_pumpControl[i].MouseLeave += Clear_HelpText;
                    ctrl_pumpControl[i].CheckedChanged += PumpClicked;
                    mainPanel.Controls.Add(ctrl_pumpControl[i]);

                    ctrl_pumpMode[i] = new CheckBox();
                    ctrl_pumpMode[i].Top = positionY;
                    ctrl_pumpMode[i].Left = positionX + ctrl_pumpControl[i].Width + Constants.PUMP_CTRL_GAP;
                    ctrl_pumpMode[i].Width = Constants.POS_PUMP_WIDTH;
                    ctrl_pumpMode[i].Height = Constants.POS_PUMP_HEIGHT;
                    ctrl_pumpMode[i].Appearance = Appearance.Button; ;
                    ctrl_pumpMode[i].Tag = i;
                    ctrl_pumpMode[i].Name = "Ctrl_pump_mode_" + i.ToString();
                    ctrl_pumpMode[i].Text = "AUTO";
                    ctrl_pumpMode[i].MouseHover += PumpMode_MouseHover;
                    ctrl_pumpMode[i].MouseLeave += Clear_HelpText;
                    ctrl_pumpMode[i].TextAlign = ContentAlignment.MiddleCenter;
                    ctrl_pumpMode[i].CheckedChanged += PumpModeClicked;
                    mainPanel.Controls.Add(ctrl_pumpMode[i]);

                    ctrl_pumpFlowRate[i] = new TextBox();
                    ctrl_pumpFlowRate[i].Top = positionY;
                    ctrl_pumpFlowRate[i].Left = positionX + ctrl_pumpMode[i].Width + Constants.PUMP_CTRL_GAP + ctrl_pumpControl[i].Width + Constants.PUMP_CTRL_GAP;
                    ctrl_pumpFlowRate[i].Width = Constants.POS_PUMP_WIDTH; 
                    ctrl_pumpFlowRate[i].Height = Constants.POS_PUMP_HEIGHT;
                    ctrl_pumpFlowRate[i].BorderStyle = BorderStyle.Fixed3D;
                    ctrl_pumpFlowRate[i].MaxLength = 4;
                    ctrl_pumpFlowRate[i].Tag = i;
                    ctrl_pumpFlowRate[i].MouseHover += PumpFlowrate_MouseHover;
                    ctrl_pumpFlowRate[i].MouseLeave += Clear_HelpText;
                    ctrl_pumpFlowRate[i].LostFocus += PumpFlowrateChanged;
                    ctrl_pumpFlowRate[i].Name = "Ctrl_pump_flowrate_" + i.ToString();
                    ctrl_pumpFlowRate[i].Visible = true;
                    mainPanel.Controls.Add(ctrl_pumpFlowRate[i]);
                                       

                    feedback_pumpFlowRate[i] = new Label();
                    feedback_pumpFlowRate[i].Top = positionY + ctrl_pumpFlowRate[i].Height + Constants.PUMP_CTRL_GAP; 
                    feedback_pumpFlowRate[i].Left = positionX + ctrl_pumpMode[i].Width + Constants.PUMP_CTRL_GAP + ctrl_pumpControl[i].Width + Constants.PUMP_CTRL_GAP;
                    feedback_pumpFlowRate[i].Text = "Feedback";
                    feedback_pumpFlowRate[i].Tag = i;
                    feedback_pumpFlowRate[i].Name = "Feedback_pump_flowrate_" + i.ToString();
                    mainPanel.Controls.Add(feedback_pumpFlowRate[i]);

                    unit_flowRate[i] = new Label();
                    unit_flowRate[i].Top = positionY ;
                    unit_flowRate[i].Left = positionX + 
                                                    ctrl_pumpMode[i].Width + Constants.PUMP_CTRL_GAP + 
                                                    ctrl_pumpControl[i].Width + Constants.PUMP_CTRL_GAP + 
                                                    ctrl_pumpFlowRate[i].Width + Constants.PUMP_CTRL_GAP;
                    unit_flowRate[i].Text = "l/min";
                    mainPanel.Controls.Add(unit_flowRate[i]);

                    //==========================================================================


                    positionY = ctrl_pumpControl[i].Top + ctrl_pumpControl[i].Height + Constants.POS_PUMP_HEIGHT;

                    feedback_pumpStatus[i] = new Label();
                    feedback_pumpStatus[i].Top = positionY;
                    feedback_pumpStatus[i].Left = positionX;
                    feedback_pumpStatus[i].Width = Constants.POS_PUMP_WIDTH * 3;
                    feedback_pumpStatus[i].BorderStyle = BorderStyle.FixedSingle;
                    feedback_pumpStatus[i].Name = "Feedback_pump_status_" + i.ToString();
                    feedback_pumpStatus[i].Text = "Status";
                    mainPanel.Controls.Add(feedback_pumpStatus[i]);

                    //==========================================================================

                    positionY = feedback_pumpStatus[i].Top + feedback_pumpStatus[i].Height + Constants.PUMP_CTRL_GAP;

                    ctrl_filldrain[i] = new CheckBox();
                    ctrl_filldrain[i].Top = positionY;
                    ctrl_filldrain[i].Left = positionX;
                    ctrl_filldrain[i].Width = Constants.POS_PUMP_WIDTH;
                    ctrl_filldrain[i].Height = Constants.POS_PUMP_HEIGHT;
                    ctrl_filldrain[i].Tag = i;
                    ctrl_filldrain[i].Name = "CTRL_fill_drain_" + i.ToString();
                    ctrl_filldrain[i].Appearance = Appearance.Button;
                    ctrl_filldrain[i].Text = "Normal";
                    ctrl_filldrain[i].TextAlign = ContentAlignment.MiddleCenter;
                    ctrl_filldrain[i].MouseHover += FillDrain_MouseHover;
                    ctrl_filldrain[i].MouseLeave += Clear_HelpText;
                    ctrl_filldrain[i].LostFocus += FillDrainClicked;
                    mainPanel.Controls.Add(ctrl_filldrain[i]);


                    positionY = ctrl_filldrain[i].Top + ctrl_filldrain[i].Height + Constants.PUMP_CTRL_GAP ;


                    //Fill Drain Settings

                    label_placeholder1[i] = new Label();
                    label_placeholder1[i].Top = positionY;
                    label_placeholder1[i].Left = positionX;
                    label_placeholder1[i].Height = Constants.POS_PUMP_HEIGHT;
                    label_placeholder1[i].Width = Constants.POS_PUMP_WIDTH;
                    label_placeholder1[i].TextAlign = ContentAlignment.MiddleCenter;
                    label_placeholder1[i].Text = "Fill duration";
                    mainPanel.Controls.Add(label_placeholder1[i]);

                    positionX = positionX + ctrl_pumpControl[i].Width + Constants.PUMP_CTRL_GAP;

                    ctrl_fd_fillduration[i] = new TextBox();
                    ctrl_fd_fillduration[i].Top = positionY;
                    ctrl_fd_fillduration[i].Left = positionX;
                    ctrl_fd_fillduration[i].Height = Constants.POS_PUMP_HEIGHT;
                    ctrl_fd_fillduration[i].Width = Constants.POS_PUMP_WIDTH;
                    ctrl_fd_fillduration[i].MaxLength = 4;
                    ctrl_fd_fillduration[i].Tag = i;
                    ctrl_fd_fillduration[i].Name = "CTRL_fill_duration_" + i.ToString();
                    ctrl_fd_fillduration[i].LostFocus += FillDurationChanged;
                    mainPanel.Controls.Add(ctrl_fd_fillduration[i]);

                    label_placeholder2[i] = new Label();
                    label_placeholder2[i].Top = positionY;
                    label_placeholder2[i].Left = ctrl_fd_fillduration[i].Left + ctrl_fd_fillduration[i].Width + Constants.PUMP_CTRL_GAP;
                    label_placeholder2[i].Height = Constants.POS_PUMP_HEIGHT;
                    label_placeholder2[i].Width = Constants.POS_PUMP_WIDTH;
                    label_placeholder2[i].TextAlign = ContentAlignment.MiddleCenter;
                    label_placeholder2[i].Text = "Fill rate";
                    mainPanel.Controls.Add(label_placeholder2[i]);

                    ctrl_fd_fillrate[i] = new TextBox();
                    ctrl_fd_fillrate[i].Top = positionY;
                    ctrl_fd_fillrate[i].Left = label_placeholder2[i].Left + label_placeholder2[i].Width + Constants.PUMP_CTRL_GAP;
                    ctrl_fd_fillrate[i].Height = Constants.POS_PUMP_HEIGHT;
                    ctrl_fd_fillrate[i].Width = Constants.POS_PUMP_WIDTH;
                    ctrl_fd_fillrate[i].MaxLength = 4;
                    ctrl_fd_fillrate[i].Tag = i;
                    ctrl_fd_fillrate[i].Name = "CTRL_fill_rate_" + i.ToString();
                    ctrl_fd_fillrate[i].LostFocus += FillRateChanged;
                    mainPanel.Controls.Add(ctrl_fd_fillrate[i]);
                                        
                    positionY = positionY + ctrl_fd_fillduration[i].Height + Constants.PUMP_CTRL_GAP;

                    positionX = Constants.POS_PUMP_LEFT;

                    label_placeholder3[i] = new Label();
                    label_placeholder3[i].Top = positionY;
                    label_placeholder3[i].Left = positionX;
                    label_placeholder3[i].Height = Constants.POS_PUMP_HEIGHT;
                    label_placeholder3[i].Width = Constants.POS_PUMP_WIDTH;
                    label_placeholder3[i].TextAlign = ContentAlignment.MiddleCenter;
                    label_placeholder3[i].Text = "Drain duration";
                    mainPanel.Controls.Add(label_placeholder3[i]);

                    ctrl_fd_drainduration[i] = new TextBox();
                    ctrl_fd_drainduration[i].Top = positionY;
                    ctrl_fd_drainduration[i].Left = label_placeholder3[i].Left + label_placeholder3[i].Width + Constants.PUMP_CTRL_GAP;
                    ctrl_fd_drainduration[i].Height = Constants.POS_PUMP_HEIGHT;
                    ctrl_fd_drainduration[i].Width = Constants.POS_PUMP_WIDTH;
                    ctrl_fd_drainduration[i].MaxLength = 4;
                    ctrl_fd_drainduration[i].Tag = i;
                    ctrl_fd_drainduration[i].Name = "CTRL_drain_duration_" + i.ToString();
                    ctrl_fd_drainduration[i].LostFocus += DrainDurationChanged;
                    mainPanel.Controls.Add(ctrl_fd_drainduration[i]);

                    label_placeholder4[i] = new Label();
                    label_placeholder4[i].Top = positionY;
                    label_placeholder4[i].Left = ctrl_fd_fillduration[i].Left + ctrl_fd_fillduration[i].Width + Constants.PUMP_CTRL_GAP;
                    label_placeholder4[i].Height = Constants.POS_PUMP_HEIGHT;
                    label_placeholder4[i].Width = Constants.POS_PUMP_WIDTH;
                    label_placeholder4[i].TextAlign = ContentAlignment.MiddleCenter;
                    label_placeholder4[i].Text = "Drain rate";
                    mainPanel.Controls.Add(label_placeholder4[i]);

                    ctrl_fd_drainrate[i] = new TextBox();
                    ctrl_fd_drainrate[i].Top = positionY;
                    ctrl_fd_drainrate[i].Left = label_placeholder4[i].Left + label_placeholder4[i].Width + Constants.PUMP_CTRL_GAP;
                    ctrl_fd_drainrate[i].Height = Constants.POS_PUMP_HEIGHT;
                    ctrl_fd_drainrate[i].Width = Constants.POS_PUMP_WIDTH;
                    ctrl_fd_drainrate[i].Tag = i;
                    ctrl_fd_drainrate[i].Name = "CTRL_drain_rate_" + i.ToString();
                    ctrl_fd_drainrate[i].MaxLength = 4;
                    ctrl_fd_drainrate[i].LostFocus += DrainRateChanged;
                    mainPanel.Controls.Add(ctrl_fd_drainrate[i]);

                    positionY = label_placeholder4[i].Top + label_placeholder4[i].Height + Constants.PUMP_CTRL_GAP;
                    positionX = Constants.POS_PUMP_LEFT;

                    ctrl_recoverPump[i] = new Button();
                    ctrl_recoverPump[i].Top = positionY;
                    ctrl_recoverPump[i].Left = positionX ;
                    ctrl_recoverPump[i].Width = Constants.POS_PUMP_WIDTH;
                    ctrl_recoverPump[i].Height = Constants.POS_PUMP_HEIGHT;
                    ctrl_recoverPump[i].Tag = i;
                    ctrl_recoverPump[i].Name = "CTRL_recover_" + i.ToString();
                    ctrl_recoverPump[i].BackColor = SystemColors.ButtonFace;
                    ctrl_recoverPump[i].Text = "Recover";
                    ctrl_recoverPump[i].TextAlign = ContentAlignment.MiddleCenter;
                    ctrl_recoverPump[i].MouseHover += PumpRecover_MouseHover;
                    ctrl_recoverPump[i].MouseLeave += Clear_HelpText;
                    ctrl_recoverPump[i].MouseClick += RecoverClicked;
                    ctrl_recoverPump[i].Enabled = false;
                    mainPanel.Controls.Add(ctrl_recoverPump[i]);

                }   //if

            }   // for pumps

        }   //AddControl



        private void PumpClicked(object sender, System.EventArgs e)
        {
            CheckBox cb = sender as CheckBox;
            ushort index;
            if (cb != null)
            {
                index = (ushort)(int)cb.Tag;

                if (cb.Checked)
                {
                    cb.Text = "PUMP " + (index+1).ToString() + " ON";
                    cb.BackColor = Color.LightGreen;
                }
                else
                {
                    cb.Text = "PUMP " + (index+1).ToString();
                    cb.BackColor = Color.Red;
                }

                if (mbi != null)
                    mbi.pumpControl(index, cb.Checked);
            }

        }


        private void PumpModeClicked(object sender, System.EventArgs e)
        {
            CheckBox cb = sender as CheckBox;
            ushort index;
            if (cb != null)
            {
                index = (ushort)(int)cb.Tag;

                if (cb.Checked)
                {
                    cb.BackColor = Color.LightBlue;
                    cb.Text = "MANUAL";
                }
                else
                {
                    cb.BackColor = Color.LightGreen;
                    cb.Text = "AUTO";
                }

                if (mbi != null)
                    mbi.pumpModeControl(index, cb.Checked);
            }

        }


        private void PumpFlowrateChanged(object sender, System.EventArgs e)
        {
            TextBox cb = sender as TextBox;
            int index;
            ushort ival;

            if (cb != null)
            {
                index = (int)cb.Tag;

                ival = sToNum(cb.Text.Trim());

                if (mbi != null)
                {
                    mbi.setPumpFlowRate(index, ival);
                }
                
            }
        }


        private ushort sToNum(string s)
        {
            ushort ustmp;

            try
            {
                ustmp = (ushort)ushort.Parse(s);
                return (ustmp);
            }
            catch
            {
                return (0);
            }
        }


        private void FillDrainClicked(object sender, System.EventArgs e)
        {
            CheckBox cb = sender as CheckBox;
            int index;

            if (cb != null)
            {
                index = (int)cb.Tag;

                if (cb.Checked)
                {
                    cb.Text = "Fill-Drain";
                    cb.BackColor = Color.LightGreen;
                }
                else
                {
                    cb.Text = "Normal";
                    cb.BackColor = SystemColors.ButtonFace;
                }
            }
        }


        private void RecoverClicked(object sender, System.EventArgs e)
        {
            Button cb = sender as Button;
            int index;

            if (cb != null)
            {
                index = (int)cb.Tag;

                if (mbi != null)
                    mbi.recoverPumpClick(index);
            }
        }


        private void LightCheckBox_CheckedChanged(object sender, System.EventArgs e)
        {
            CheckBox cb = sender as CheckBox;
            ushort index;

            if (cb != null)
            {
                index = (ushort)(int)cb.Tag;

                if (cb.Checked)
                {
                    cb.BackColor = Color.Yellow;
                }
                else
                {
                    cb.BackColor = SystemColors.ButtonFace;
                }

                if (mbi != null)
                    mbi.lightControl(index, cb.Checked);
            }

        }


        private void UpdateLightIntensityLabel(object sender, System.EventArgs e)
        {
            TrackBar cb = sender as TrackBar;
            int index;
            uint uval;

            if (cb != null)
            {
                index = (int)cb.Tag;

                uval = (uint)cb.Value;

                Label lb = (Label)mainPanel.Controls["Label_light_intensity_" + index.ToString()];
                lb.Text = uval.ToString();

            }

        }

        private void UpdateLightIntensity(object sender, System.EventArgs e)
        {
            TrackBar cb = sender as TrackBar;
            ushort index;
            ushort uval;

            if (cb != null)
            {
                index = (ushort)((int)cb.Tag);
                uval = (ushort)cb.Value;

                if (mbi != null)
                {
                    mbi.lightIntensityControl((ushort)index, uval);
                }
            }

        }



        private void ModeComboBox_CheckedChanged(object sender, System.EventArgs e)
        {
            ComboBox cb = sender as ComboBox;
            ushort index;

            if (cb != null)
            {
                index = (ushort)(int)(cb.Tag);

                if (cb.SelectedIndex == 2)
                {
                    cb.BackColor = Color.LightPink;
                }
                if (cb.SelectedIndex == 1)
                {
                    cb.BackColor = Color.LightGreen;
                }
                else
                {
                    cb.BackColor = Color.LightBlue;
                }

                if (mbi != null)
                    mbi.setMode(index, (ushort)cb.SelectedIndex);

            }   // if

        }   // ModeComboBox_CheckedChanged


        private void UpdateValveSetting(object sender, System.EventArgs e)
        {
            TextBox tb = sender as TextBox;
            ushort index;
            ushort iValue;

            if (tb != null)
            {
                index = (ushort)(int)tb.Tag;
                
                iValue = sToNum(tb.Text.Trim());
                if ((iValue <= 100) && (iValue >= 0))
                {
                    if (mbi != null)
                        mbi.setValve(index, iValue);
                }
            }
        }   // UpdateValveSetting


        private void WaterLightScheduleCheckBox_Changed(object sender, System.EventArgs e)
        {
            CheckBox cb = sender as CheckBox;
            ushort index;

            if (cb != null)
            {
                index = (ushort)(int)cb.Tag;

                if (cb.Checked)
                {
                    cb.Text = "ON";
                    cb.BackColor = Color.LightGreen;
                }
                else
                {
                    cb.Text = "OFF";
                    cb.BackColor = SystemColors.ButtonFace;
                }

                if (mbi != null)
                    mbi.setScheduleOnOff(index, cb.Checked);

            }

        }



        private void WaterScheduleClicked(object sender, System.EventArgs e)
        {
            Label lb = sender as Label;

            iWaterScheduleIndex = (int)lb.Tag;

            if (addToSelectedList(iWaterScheduleIndex, true))
            {
                lb.BackColor = Color.Orange;
            }
            else
            {
                lb.BackColor = SystemColors.ButtonFace;
            }

            helpBarText.Text = iWaterScheduleIndex.ToString();
        }


        private string filterS(string s)
        {
            if (s.Trim() == "")
                return ("00");
            else
                return (s);
        }

        private void SetScheduleButton_Click(object sender, EventArgs e)
        {
            string stmp;

            SetScheduleButton.Enabled = false;

            for (int i = farm.rack[iActiveRack-1].numShelf - 1; i >= 0; i--)
            {
                if (waterSchedList[i])
                {
                    stmp = filterS(startHCombo.Text) + ":" + filterS(startMCombo.Text) + "-" + filterS(endHCombo.Text) + ":" + filterS(endMCombo.Text);
                    if (stmp != ctrl_waterSchedule[i].Text)
                    {
                        ctrl_waterSchedule[i].Text = stmp;
                        if (mbi != null)
                        {
                            mbi.setWaterSchedule(i, stmp);
                        }

                    }

                }   // if

            }   // SetScheduleButton_Click

            for (int i = farm.rack[iActiveRack-1].numLight - 1; i >= 0; i--)
            {
                if (lightSchedList[i])
                {
                    stmp = filterS(startHComboL.Text) + ":" + filterS(startMComboL.Text) + "-" + filterS(endHComboL.Text) + ":" + filterS(endMComboL.Text);
                    if (stmp != ctrl_lightSchedule[i].Text)
                    {
                        ctrl_lightSchedule[i].Text = stmp;
                        if (mbi != null)
                        {
                            mbi.setLightSchedule(i, stmp);
                        }
                    }
                }   //if
            }   //for

            SetScheduleButton.Enabled = true;

        }   // SetScheduleButton_Click


        private void ClearScheduleButton_Click(object sender, EventArgs e)
        {
            string stmp;

            for (int i = farm.rack[iActiveRack-1].numShelf - 1; i >= 0; i--)
            {
                if (waterSchedList[i])
                {
                    stmp = "00:00-00:00";
                    ctrl_waterSchedule[i].Text = stmp;
                    if (mbi != null)
                    {
                        mbi.setWaterSchedule(i, stmp);
                    }
                }
            }

            for (int i = farm.rack[iActiveRack-1].numLight - 1; i >= 0; i--)
            {
                if (lightSchedList[i])
                {
                    stmp = "00:00-00:00";
                    ctrl_lightSchedule[i].Text = stmp;
                    if (mbi != null)
                    {
                        mbi.setLightSchedule(i, stmp);
                    }
                }
            }
        }


        private void FillDurationChanged(object sender, EventArgs e)
        {
            TextBox tb = sender as TextBox;
            ushort index;
            ushort iValue;
            string stmp;

            if (tb != null)
            {
                index = (ushort)(int)tb.Tag;

                stmp = tb.Text.Trim();
                if (stmp != "") {
                    iValue = sToNum(stmp);
                    if (mbi != null)
                    {
                        mbi.setFillDuration(index, iValue);
                    }
                }
            }
        }

        private void DrainDurationChanged(object sender, EventArgs e)
        {
            TextBox tb = sender as TextBox;
            ushort index;
            ushort iValue;
            string stmp;

            if (tb != null)
            {
                index = (ushort)(int)tb.Tag;

                stmp = tb.Text.Trim();
                if (stmp != "")
                {
                    iValue = sToNum(stmp);
                    if (mbi != null)
                    {
                        mbi.setDrainDuration(index, iValue);
                    }
                }
            }

        }

        private void FillRateChanged(object sender, EventArgs e)
        {
            TextBox tb = sender as TextBox;
            ushort index;
            ushort iValue;
            string stmp;

            if (tb != null)
            {
                index = (ushort)(int)tb.Tag;

                stmp = tb.Text.Trim();
                if (stmp != "")
                {
                    iValue = sToNum(stmp);
                    if (mbi != null)
                    {
                        mbi.setFillRate(index, iValue);
                    }
                }
            }

        }


        private void DrainRateChanged(object sender, EventArgs e)
        {
            TextBox tb = sender as TextBox;
            ushort index;
            ushort iValue;
            string stmp;

            if (tb != null)
            {
                index = (ushort)(int)tb.Tag;

                stmp = tb.Text.Trim();
                if (stmp != "")
                {
                    iValue = sToNum(stmp);
                    if (mbi != null)
                    {
                        mbi.setDrainRate(index, iValue);
                    }
                }
            }

        }   // DrainRateChanged




        private void SetScheduleButton_MouseHover(object sender, EventArgs e)
        {
            toolTip1.SetToolTip(SetScheduleButton, "Click on the water or light schedule of all shelves to set.");
        }


        private void LightCheckBox_MouseHover(object sender, EventArgs e)
        {
            helpBarText.Text = "Click to toggle Light ON/OFF";
        }


        private void ModeCombo_MouseHover(object sender, EventArgs e)
        {
            helpBarText.Text = "Select control mode";
        }


        private void ValveSetting_MouseHover(object sender, EventArgs e)
        {
            helpBarText.Text = "Set valve % opening";
        }

        private void LightIntensity_MouseHover(object sender, EventArgs e)
        {
            helpBarText.Text = "Slide to adjust light intensity";
        }

        private void PumpControl_MouseHover(object sender, EventArgs e)
        {
            helpBarText.Text = "Toggle to turn off/on pump (for quick off)";
        }

        private void PumpMode_MouseHover(object sender, EventArgs e)
        {
            helpBarText.Text = "Toggle between auto mode and fix flowrate mode";
        }

        private void PumpFlowrate_MouseHover(object sender, EventArgs e)
        {
            helpBarText.Text = "Set pump flowrate in liter per minute";
        }

        private void FillDrain_MouseHover(object sender, EventArgs e)
        {
            helpBarText.Text = "Toggle between normal and fill-drain mode";
        }

        private void PumpRecover_MouseHover(object sender, EventArgs e)
        {
            helpBarText.Text = "Recover from pump error cuased by overspin";
        }

        private void UseScheduler_MouseHover(object sender, EventArgs e)
        {
            helpBarText.Text = "Toggle to use normal mode control or scheduler";
        }


        private void Clear_HelpText(object sender, EventArgs e)
        {
            helpBarText.Text = "";
        }


        private void ApplyButton_Click(object sender, EventArgs e)
        {
            if (mbi != null)
                mbi.applyControl();
        }



        private void LightScheduleClicked(object sender, System.EventArgs e)
        {
            Label lb = sender as Label;

            iLightScheduleIndex = (int)lb.Tag;

            if (addToSelectedList(iLightScheduleIndex, false))
            {
                lb.BackColor = Color.Orange;
            }
            else
            {
                lb.BackColor = SystemColors.ButtonFace;
            }

            helpBarText.Text = iLightScheduleIndex.ToString();

        }   // LightScheduleClicked


        private void TerminateApplication()
        {
            Environment.Exit(0);
        }



        //=====================================================================
        //=====================================================================

        //===================================================================
        // Schedule editor
        //===================================================================


        void updateCount()
        {
            SchedulerItemCountLabel.Text = "Water: " + iSelectedWaterCount.ToString() + " Light: " + iSelectedLightCount.ToString();
        }

        private void aboutToolStripMenuItem1_Click(object sender, EventArgs e)
        {
            AboutBox1 abf = new AboutBox1();
            abf.ShowDialog();
        }

        private void exitToolStripMenuItem_Click(object sender, EventArgs e)
        {
            TerminateApplication();
        }

        private void ClearScheduleButton_MouseHover(object sender, EventArgs e)
        {
            toolTip1.SetToolTip(ClearScheduleButton, "Click on the water or light schedule of all shelves to clear.");
        }

        private void ApplyButton_MouseHover(object sender, EventArgs e)
        {
            toolTip1.SetToolTip(ApplyButton, "Let the PLC transfer everything from temporary memory to final.");
        }

        private bool addToSelectedList(int index, bool isWater)
        {
            bool bres = true;

            if (isWater)
            {
                waterSchedList[index] = !waterSchedList[index];
                if (waterSchedList[index])
                    iSelectedWaterCount++;
                else
                    iSelectedWaterCount--;

                updateCount();
                return (waterSchedList[index]);
            }
            else
            {
                lightSchedList[index] = !lightSchedList[index];

                if (lightSchedList[index])
                    iSelectedLightCount++;
                else
                    iSelectedLightCount--;

                updateCount();
                return (lightSchedList[index]);
            }

            return (bres);

        }   // addToSelectedList


        //==============================================
        //==============================================

        private void update_UI_from_Feedback()
        {
            ushort[] utmp;
            int index = iActiveRack - 1;

            if (mbi != null)
            {
                mainPanel.BeginInvoke(new Action(() => {
                    utmp = mbi.getPumpFlowrateFeedback();

                    for (int i = 0; i < farm.rack[index].numPump; i++)
                    {
                        Label lb = (Label)mainPanel.Controls["Feedback_pump_flowrate_" + i.ToString()];
                        if (lb != null)
                            lb.Text = utmp[i].ToString() + " l/min";
                    }

                    bFeedbackPumpOn = mbi.getPumpOnStatus();
                    uFeedbackPumpSpeed = mbi.getPumpSpeed();
                    bPumpFilling = mbi.getPumpIsFilling();

                    for (int i=0; i<farm.rack[index].numPump; i++)
                    {
                        Label lb = (Label)mainPanel.Controls["Feedback_pump_status_" + i.ToString()];
                        lb.Text = "Status: " + (bFeedbackPumpOn[i] ? "ON" : "OFF") + " Speed: " + uFeedbackPumpSpeed[i].ToString() + " Filling: " + (bPumpFilling[i] ? "YES":"NO");
                    }

                }));
                
            }
        }   // update_UI_from_Feedback


        //==============================================
        //==============================================

        private void updateLogs()
        {
            logListBox.BeginInvoke(new Action(() => {

                string[] sLogs;

                if (mbi != null)
                {
                    sLogs = mbi.getMessageList();

                    if (sLogs != null)
                    {
                        foreach (var stmp in sLogs)
                        {
                            if (stmp != null)
                            {
                                if (stmp.Trim().Length > 0)
                                {
                                    logListBox.Items.Add(stmp);
                                    logListBox.SelectedIndex = logListBox.Items.Count - 1;
                                }
                            }
                        }

                        mbi.clearMessageList();
                    }   // if

                }   // if

            }));

            readLogListBox.BeginInvoke(new Action(() => {

                string[] sLogs;

                if (mbi != null)
                {
                    sLogs = mbi.getMessageList2();

                    if (sLogs != null)
                    {
                        foreach (var stmp in sLogs)
                        {
                            if (stmp != null)
                            {
                                if (stmp.Trim().Length > 0)
                                {
                                    readLogListBox.Items.Add(stmp);
                                    readLogListBox.SelectedIndex = readLogListBox.Items.Count - 1;
                                }
                            }
                        }

                        mbi.clearMessageList2();
                    }

                }

            }));
        }


    }   




    /*
    private void collectData()
    {
        mainPanel.BeginInvoke(new Action(() => {

            for (int idx = 0; idx < farm.rack[iActiveRack].numShelf; idx++)
            {

                CheckBox cb = (CheckBox)mainPanel.Controls["Ctrl_mode_" + idx.ToString()];
                farm.rack[iActiveRack].shelf[idx].mode = cb.Checked;

                TextBox tb = (TextBox)mainPanel.Controls["Ctrl_valve_setting_" + idx.ToString()];
                farm.rack[iActiveRack].shelf[idx].iPVvalue = (uint)Int32.Parse(tb.Text.Trim());

                CheckBox cb2 = (CheckBox)mainPanel.Controls["Ctrl_use_water_schedule_" + idx.ToString()];
                farm.rack[iActiveRack].shelf[idx].bUseWaterSchedule = cb2.Checked;

                Label lb = (Label)mainPanel.Controls["Ctrl_water_schedule_" + idx.ToString()];
                farm.rack[iActiveRack].shelf[idx].sWaterSchedule = lb.Text;

            }   // for


            for (int idx = 0; idx < farm.rack[iActiveRack].numLight; idx++) 
            {

                CheckBox cb = (CheckBox)mainPanel.Controls["Ctrl_light_control_" + idx.ToString()];
                farm.rack[iActiveRack].light[idx].bOnOff = cb.Checked;

                TrackBar trb = (TrackBar)mainPanel.Controls["Ctrl_light_intensity_" + idx.ToString()];
                farm.rack[iActiveRack].light[idx].iIntensity = (uint)trb.Value;

                CheckBox cb2 = (CheckBox)mainPanel.Controls["Ctrl_use_light_schedule_" + idx.ToString()];
                farm.rack[iActiveRack].light[idx].bUseLightSchedule = cb2.Checked;

                Label lb = (Label)mainPanel.Controls["Ctrl_light_schedule_" + idx.ToString()];
                farm.rack[iActiveRack].light[idx].sLightSchedule = lb.Text;

            }   // for


            for (int idx = 0; idx < farm.rack[iActiveRack].numPump; idx++)
            {

            }


        }));

    }   // collectData
    */


}   // public







