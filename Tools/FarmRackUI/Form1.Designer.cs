namespace FamrRackUI
{
    partial class mainForm
    {
        /// <summary>
        /// Required designer variable.
        /// </summary>
        private System.ComponentModel.IContainer components = null;

        /// <summary>
        /// Clean up any resources being used.
        /// </summary>
        /// <param name="disposing">true if managed resources should be disposed; otherwise, false.</param>
        protected override void Dispose(bool disposing)
        {
            if (disposing && (components != null))
            {
                components.Dispose();
            }
            base.Dispose(disposing);
        }

        #region Windows Form Designer generated code

        /// <summary>
        /// Required method for Designer support - do not modify
        /// the contents of this method with the code editor.
        /// </summary>
        private void InitializeComponent()
        {
            this.components = new System.ComponentModel.Container();
            this.menuStrip1 = new System.Windows.Forms.MenuStrip();
            this.fileToolStripMenuItem = new System.Windows.Forms.ToolStripMenuItem();
            this.exitToolStripMenuItem = new System.Windows.Forms.ToolStripMenuItem();
            this.aboutToolStripMenuItem = new System.Windows.Forms.ToolStripMenuItem();
            this.aboutToolStripMenuItem1 = new System.Windows.Forms.ToolStripMenuItem();
            this.rackComboBox = new System.Windows.Forms.ComboBox();
            this.label1 = new System.Windows.Forms.Label();
            this.mainPanel = new System.Windows.Forms.Panel();
            this.readLogListBox = new System.Windows.Forms.ListBox();
            this.label20 = new System.Windows.Forms.Label();
            this.logListBox = new System.Windows.Forms.ListBox();
            this.ApplyButton = new System.Windows.Forms.Button();
            this.label21 = new System.Windows.Forms.Label();
            this.label19 = new System.Windows.Forms.Label();
            this.label18 = new System.Windows.Forms.Label();
            this.label17 = new System.Windows.Forms.Label();
            this.label16 = new System.Windows.Forms.Label();
            this.SchedulerGroup = new System.Windows.Forms.GroupBox();
            this.ClearScheduleButton = new System.Windows.Forms.Button();
            this.label15 = new System.Windows.Forms.Label();
            this.label14 = new System.Windows.Forms.Label();
            this.label13 = new System.Windows.Forms.Label();
            this.label12 = new System.Windows.Forms.Label();
            this.label11 = new System.Windows.Forms.Label();
            this.label10 = new System.Windows.Forms.Label();
            this.label9 = new System.Windows.Forms.Label();
            this.label8 = new System.Windows.Forms.Label();
            this.label7 = new System.Windows.Forms.Label();
            this.label6 = new System.Windows.Forms.Label();
            this.endMComboL = new System.Windows.Forms.ComboBox();
            this.endHComboL = new System.Windows.Forms.ComboBox();
            this.startMComboL = new System.Windows.Forms.ComboBox();
            this.startHComboL = new System.Windows.Forms.ComboBox();
            this.label4 = new System.Windows.Forms.Label();
            this.label5 = new System.Windows.Forms.Label();
            this.endMCombo = new System.Windows.Forms.ComboBox();
            this.endHCombo = new System.Windows.Forms.ComboBox();
            this.startMCombo = new System.Windows.Forms.ComboBox();
            this.startHCombo = new System.Windows.Forms.ComboBox();
            this.SchedulerItemCountLabel = new System.Windows.Forms.Label();
            this.SetScheduleButton = new System.Windows.Forms.Button();
            this.label3 = new System.Windows.Forms.Label();
            this.label2 = new System.Windows.Forms.Label();
            this.statusLabel = new System.Windows.Forms.Label();
            this.helpBarText = new System.Windows.Forms.Label();
            this.toolTip1 = new System.Windows.Forms.ToolTip(this.components);
            this.IPLabel = new System.Windows.Forms.Label();
            this.label22 = new System.Windows.Forms.Label();
            this.menuStrip1.SuspendLayout();
            this.mainPanel.SuspendLayout();
            this.SchedulerGroup.SuspendLayout();
            this.SuspendLayout();
            // 
            // menuStrip1
            // 
            this.menuStrip1.Items.AddRange(new System.Windows.Forms.ToolStripItem[] {
            this.fileToolStripMenuItem,
            this.aboutToolStripMenuItem});
            this.menuStrip1.Location = new System.Drawing.Point(0, 0);
            this.menuStrip1.Name = "menuStrip1";
            this.menuStrip1.Size = new System.Drawing.Size(1904, 24);
            this.menuStrip1.TabIndex = 0;
            this.menuStrip1.Text = "menuStrip1";
            // 
            // fileToolStripMenuItem
            // 
            this.fileToolStripMenuItem.DropDownItems.AddRange(new System.Windows.Forms.ToolStripItem[] {
            this.exitToolStripMenuItem});
            this.fileToolStripMenuItem.Name = "fileToolStripMenuItem";
            this.fileToolStripMenuItem.Size = new System.Drawing.Size(37, 20);
            this.fileToolStripMenuItem.Text = "&File";
            // 
            // exitToolStripMenuItem
            // 
            this.exitToolStripMenuItem.Name = "exitToolStripMenuItem";
            this.exitToolStripMenuItem.Size = new System.Drawing.Size(93, 22);
            this.exitToolStripMenuItem.Text = "E&xit";
            this.exitToolStripMenuItem.Click += new System.EventHandler(this.exitToolStripMenuItem_Click);
            // 
            // aboutToolStripMenuItem
            // 
            this.aboutToolStripMenuItem.DropDownItems.AddRange(new System.Windows.Forms.ToolStripItem[] {
            this.aboutToolStripMenuItem1});
            this.aboutToolStripMenuItem.Name = "aboutToolStripMenuItem";
            this.aboutToolStripMenuItem.Size = new System.Drawing.Size(44, 20);
            this.aboutToolStripMenuItem.Text = "&Help";
            // 
            // aboutToolStripMenuItem1
            // 
            this.aboutToolStripMenuItem1.Name = "aboutToolStripMenuItem1";
            this.aboutToolStripMenuItem1.Size = new System.Drawing.Size(107, 22);
            this.aboutToolStripMenuItem1.Text = "&About";
            this.aboutToolStripMenuItem1.Click += new System.EventHandler(this.aboutToolStripMenuItem1_Click);
            // 
            // rackComboBox
            // 
            this.rackComboBox.DropDownStyle = System.Windows.Forms.ComboBoxStyle.DropDownList;
            this.rackComboBox.FormattingEnabled = true;
            this.rackComboBox.Location = new System.Drawing.Point(72, 37);
            this.rackComboBox.Name = "rackComboBox";
            this.rackComboBox.Size = new System.Drawing.Size(77, 21);
            this.rackComboBox.TabIndex = 1;
            this.rackComboBox.SelectedIndexChanged += new System.EventHandler(this.rackComboBox_SelectedIndexChanged);
            // 
            // label1
            // 
            this.label1.AutoSize = true;
            this.label1.Location = new System.Drawing.Point(23, 41);
            this.label1.Name = "label1";
            this.label1.Size = new System.Drawing.Size(43, 13);
            this.label1.TabIndex = 2;
            this.label1.Text = "Rack #";
            // 
            // mainPanel
            // 
            this.mainPanel.BorderStyle = System.Windows.Forms.BorderStyle.FixedSingle;
            this.mainPanel.Controls.Add(this.label22);
            this.mainPanel.Controls.Add(this.readLogListBox);
            this.mainPanel.Controls.Add(this.label20);
            this.mainPanel.Controls.Add(this.logListBox);
            this.mainPanel.Controls.Add(this.ApplyButton);
            this.mainPanel.Controls.Add(this.label21);
            this.mainPanel.Controls.Add(this.label19);
            this.mainPanel.Controls.Add(this.label18);
            this.mainPanel.Controls.Add(this.label17);
            this.mainPanel.Controls.Add(this.label16);
            this.mainPanel.Controls.Add(this.SchedulerGroup);
            this.mainPanel.Location = new System.Drawing.Point(12, 76);
            this.mainPanel.Name = "mainPanel";
            this.mainPanel.Size = new System.Drawing.Size(1839, 617);
            this.mainPanel.TabIndex = 3;
            // 
            // readLogListBox
            // 
            this.readLogListBox.FormattingEnabled = true;
            this.readLogListBox.Location = new System.Drawing.Point(861, 415);
            this.readLogListBox.Name = "readLogListBox";
            this.readLogListBox.Size = new System.Drawing.Size(652, 95);
            this.readLogListBox.TabIndex = 10;
            // 
            // label20
            // 
            this.label20.AutoSize = true;
            this.label20.Font = new System.Drawing.Font("Microsoft Sans Serif", 18F, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, ((byte)(0)));
            this.label20.Location = new System.Drawing.Point(1308, 15);
            this.label20.Name = "label20";
            this.label20.Size = new System.Drawing.Size(86, 29);
            this.label20.TabIndex = 9;
            this.label20.Text = "PUMP";
            // 
            // logListBox
            // 
            this.logListBox.FormattingEnabled = true;
            this.logListBox.Location = new System.Drawing.Point(203, 415);
            this.logListBox.Name = "logListBox";
            this.logListBox.Size = new System.Drawing.Size(652, 95);
            this.logListBox.TabIndex = 8;
            // 
            // ApplyButton
            // 
            this.ApplyButton.Font = new System.Drawing.Font("Microsoft Sans Serif", 8.25F, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, ((byte)(0)));
            this.ApplyButton.Location = new System.Drawing.Point(859, 556);
            this.ApplyButton.Name = "ApplyButton";
            this.ApplyButton.Size = new System.Drawing.Size(235, 38);
            this.ApplyButton.TabIndex = 7;
            this.ApplyButton.Text = "APPLY";
            this.ApplyButton.UseVisualStyleBackColor = true;
            this.ApplyButton.Click += new System.EventHandler(this.ApplyButton_Click);
            this.ApplyButton.MouseHover += new System.EventHandler(this.ApplyButton_MouseHover);
            // 
            // label21
            // 
            this.label21.AutoSize = true;
            this.label21.Location = new System.Drawing.Point(641, 15);
            this.label21.Name = "label21";
            this.label21.Size = new System.Drawing.Size(15, 13);
            this.label21.TabIndex = 6;
            this.label21.Text = "%";
            // 
            // label19
            // 
            this.label19.AutoSize = true;
            this.label19.Location = new System.Drawing.Point(513, 15);
            this.label19.Name = "label19";
            this.label19.Size = new System.Drawing.Size(39, 13);
            this.label19.TabIndex = 4;
            this.label19.Text = "LIGHT";
            // 
            // label18
            // 
            this.label18.AutoSize = true;
            this.label18.Location = new System.Drawing.Point(360, 15);
            this.label18.Name = "label18";
            this.label18.Size = new System.Drawing.Size(32, 13);
            this.label18.TabIndex = 3;
            this.label18.Text = "PV %";
            // 
            // label17
            // 
            this.label17.AutoSize = true;
            this.label17.Location = new System.Drawing.Point(212, 15);
            this.label17.Name = "label17";
            this.label17.Size = new System.Drawing.Size(65, 13);
            this.label17.TabIndex = 2;
            this.label17.Text = "SCHEDULE";
            // 
            // label16
            // 
            this.label16.AutoSize = true;
            this.label16.Location = new System.Drawing.Point(151, 15);
            this.label16.Name = "label16";
            this.label16.Size = new System.Drawing.Size(39, 13);
            this.label16.TabIndex = 1;
            this.label16.Text = "MODE";
            // 
            // SchedulerGroup
            // 
            this.SchedulerGroup.Controls.Add(this.ClearScheduleButton);
            this.SchedulerGroup.Controls.Add(this.label15);
            this.SchedulerGroup.Controls.Add(this.label14);
            this.SchedulerGroup.Controls.Add(this.label13);
            this.SchedulerGroup.Controls.Add(this.label12);
            this.SchedulerGroup.Controls.Add(this.label11);
            this.SchedulerGroup.Controls.Add(this.label10);
            this.SchedulerGroup.Controls.Add(this.label9);
            this.SchedulerGroup.Controls.Add(this.label8);
            this.SchedulerGroup.Controls.Add(this.label7);
            this.SchedulerGroup.Controls.Add(this.label6);
            this.SchedulerGroup.Controls.Add(this.endMComboL);
            this.SchedulerGroup.Controls.Add(this.endHComboL);
            this.SchedulerGroup.Controls.Add(this.startMComboL);
            this.SchedulerGroup.Controls.Add(this.startHComboL);
            this.SchedulerGroup.Controls.Add(this.label4);
            this.SchedulerGroup.Controls.Add(this.label5);
            this.SchedulerGroup.Controls.Add(this.endMCombo);
            this.SchedulerGroup.Controls.Add(this.endHCombo);
            this.SchedulerGroup.Controls.Add(this.startMCombo);
            this.SchedulerGroup.Controls.Add(this.startHCombo);
            this.SchedulerGroup.Controls.Add(this.SchedulerItemCountLabel);
            this.SchedulerGroup.Controls.Add(this.SetScheduleButton);
            this.SchedulerGroup.Controls.Add(this.label3);
            this.SchedulerGroup.Controls.Add(this.label2);
            this.SchedulerGroup.Location = new System.Drawing.Point(1552, 32);
            this.SchedulerGroup.Name = "SchedulerGroup";
            this.SchedulerGroup.Size = new System.Drawing.Size(235, 284);
            this.SchedulerGroup.TabIndex = 0;
            this.SchedulerGroup.TabStop = false;
            this.SchedulerGroup.Text = "Scheduler";
            // 
            // ClearScheduleButton
            // 
            this.ClearScheduleButton.Location = new System.Drawing.Point(126, 232);
            this.ClearScheduleButton.Name = "ClearScheduleButton";
            this.ClearScheduleButton.Size = new System.Drawing.Size(84, 32);
            this.ClearScheduleButton.TabIndex = 26;
            this.ClearScheduleButton.Text = "<-- Clear";
            this.ClearScheduleButton.UseVisualStyleBackColor = true;
            this.ClearScheduleButton.Click += new System.EventHandler(this.ClearScheduleButton_Click);
            this.ClearScheduleButton.MouseHover += new System.EventHandler(this.ClearScheduleButton_MouseHover);
            // 
            // label15
            // 
            this.label15.AutoSize = true;
            this.label15.Location = new System.Drawing.Point(196, 193);
            this.label15.Name = "label15";
            this.label15.Size = new System.Drawing.Size(16, 13);
            this.label15.TabIndex = 25;
            this.label15.Text = "M";
            // 
            // label14
            // 
            this.label14.AutoSize = true;
            this.label14.Location = new System.Drawing.Point(196, 168);
            this.label14.Name = "label14";
            this.label14.Size = new System.Drawing.Size(16, 13);
            this.label14.TabIndex = 24;
            this.label14.Text = "M";
            // 
            // label13
            // 
            this.label13.AutoSize = true;
            this.label13.Location = new System.Drawing.Point(196, 109);
            this.label13.Name = "label13";
            this.label13.Size = new System.Drawing.Size(16, 13);
            this.label13.TabIndex = 23;
            this.label13.Text = "M";
            // 
            // label12
            // 
            this.label12.AutoSize = true;
            this.label12.Location = new System.Drawing.Point(196, 83);
            this.label12.Name = "label12";
            this.label12.Size = new System.Drawing.Size(16, 13);
            this.label12.TabIndex = 22;
            this.label12.Text = "M";
            // 
            // label11
            // 
            this.label11.AutoSize = true;
            this.label11.Location = new System.Drawing.Point(116, 193);
            this.label11.Name = "label11";
            this.label11.Size = new System.Drawing.Size(15, 13);
            this.label11.TabIndex = 21;
            this.label11.Text = "H";
            // 
            // label10
            // 
            this.label10.AutoSize = true;
            this.label10.Location = new System.Drawing.Point(114, 168);
            this.label10.Name = "label10";
            this.label10.Size = new System.Drawing.Size(15, 13);
            this.label10.TabIndex = 20;
            this.label10.Text = "H";
            // 
            // label9
            // 
            this.label9.AutoSize = true;
            this.label9.Location = new System.Drawing.Point(114, 109);
            this.label9.Name = "label9";
            this.label9.Size = new System.Drawing.Size(15, 13);
            this.label9.TabIndex = 19;
            this.label9.Text = "H";
            // 
            // label8
            // 
            this.label8.AutoSize = true;
            this.label8.Location = new System.Drawing.Point(114, 83);
            this.label8.Name = "label8";
            this.label8.Size = new System.Drawing.Size(15, 13);
            this.label8.TabIndex = 18;
            this.label8.Text = "H";
            // 
            // label7
            // 
            this.label7.AutoSize = true;
            this.label7.Font = new System.Drawing.Font("Microsoft Sans Serif", 10F, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, ((byte)(0)));
            this.label7.Location = new System.Drawing.Point(20, 145);
            this.label7.Name = "label7";
            this.label7.Size = new System.Drawing.Size(44, 17);
            this.label7.TabIndex = 17;
            this.label7.Text = "Light";
            // 
            // label6
            // 
            this.label6.AutoSize = true;
            this.label6.Font = new System.Drawing.Font("Microsoft Sans Serif", 10F, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, ((byte)(0)));
            this.label6.Location = new System.Drawing.Point(20, 51);
            this.label6.Name = "label6";
            this.label6.Size = new System.Drawing.Size(51, 17);
            this.label6.TabIndex = 16;
            this.label6.Text = "Water";
            // 
            // endMComboL
            // 
            this.endMComboL.DropDownStyle = System.Windows.Forms.ComboBoxStyle.DropDownList;
            this.endMComboL.FormattingEnabled = true;
            this.endMComboL.Location = new System.Drawing.Point(135, 190);
            this.endMComboL.MaxLength = 2;
            this.endMComboL.Name = "endMComboL";
            this.endMComboL.Size = new System.Drawing.Size(55, 21);
            this.endMComboL.TabIndex = 15;
            // 
            // endHComboL
            // 
            this.endHComboL.DropDownStyle = System.Windows.Forms.ComboBoxStyle.DropDownList;
            this.endHComboL.FormattingEnabled = true;
            this.endHComboL.Location = new System.Drawing.Point(55, 190);
            this.endHComboL.MaxLength = 2;
            this.endHComboL.Name = "endHComboL";
            this.endHComboL.Size = new System.Drawing.Size(55, 21);
            this.endHComboL.TabIndex = 14;
            // 
            // startMComboL
            // 
            this.startMComboL.DropDownStyle = System.Windows.Forms.ComboBoxStyle.DropDownList;
            this.startMComboL.FormattingEnabled = true;
            this.startMComboL.Location = new System.Drawing.Point(135, 165);
            this.startMComboL.MaxLength = 2;
            this.startMComboL.Name = "startMComboL";
            this.startMComboL.Size = new System.Drawing.Size(55, 21);
            this.startMComboL.TabIndex = 13;
            // 
            // startHComboL
            // 
            this.startHComboL.DropDownStyle = System.Windows.Forms.ComboBoxStyle.DropDownList;
            this.startHComboL.FormattingEnabled = true;
            this.startHComboL.Location = new System.Drawing.Point(55, 165);
            this.startHComboL.MaxLength = 2;
            this.startHComboL.Name = "startHComboL";
            this.startHComboL.Size = new System.Drawing.Size(55, 21);
            this.startHComboL.TabIndex = 12;
            // 
            // label4
            // 
            this.label4.AutoSize = true;
            this.label4.Location = new System.Drawing.Point(20, 193);
            this.label4.Name = "label4";
            this.label4.Size = new System.Drawing.Size(26, 13);
            this.label4.TabIndex = 11;
            this.label4.Text = "End";
            // 
            // label5
            // 
            this.label5.AutoSize = true;
            this.label5.Location = new System.Drawing.Point(20, 168);
            this.label5.Name = "label5";
            this.label5.Size = new System.Drawing.Size(29, 13);
            this.label5.TabIndex = 10;
            this.label5.Text = "Start";
            // 
            // endMCombo
            // 
            this.endMCombo.DropDownStyle = System.Windows.Forms.ComboBoxStyle.DropDownList;
            this.endMCombo.FormattingEnabled = true;
            this.endMCombo.Location = new System.Drawing.Point(135, 105);
            this.endMCombo.MaxLength = 2;
            this.endMCombo.Name = "endMCombo";
            this.endMCombo.Size = new System.Drawing.Size(55, 21);
            this.endMCombo.TabIndex = 9;
            // 
            // endHCombo
            // 
            this.endHCombo.DropDownStyle = System.Windows.Forms.ComboBoxStyle.DropDownList;
            this.endHCombo.FormattingEnabled = true;
            this.endHCombo.Location = new System.Drawing.Point(55, 105);
            this.endHCombo.MaxLength = 2;
            this.endHCombo.Name = "endHCombo";
            this.endHCombo.Size = new System.Drawing.Size(55, 21);
            this.endHCombo.TabIndex = 8;
            // 
            // startMCombo
            // 
            this.startMCombo.DropDownStyle = System.Windows.Forms.ComboBoxStyle.DropDownList;
            this.startMCombo.FormattingEnabled = true;
            this.startMCombo.Location = new System.Drawing.Point(135, 80);
            this.startMCombo.MaxLength = 2;
            this.startMCombo.Name = "startMCombo";
            this.startMCombo.Size = new System.Drawing.Size(55, 21);
            this.startMCombo.TabIndex = 7;
            // 
            // startHCombo
            // 
            this.startHCombo.DropDownStyle = System.Windows.Forms.ComboBoxStyle.DropDownList;
            this.startHCombo.FormattingEnabled = true;
            this.startHCombo.Location = new System.Drawing.Point(55, 80);
            this.startHCombo.MaxLength = 2;
            this.startHCombo.Name = "startHCombo";
            this.startHCombo.Size = new System.Drawing.Size(55, 21);
            this.startHCombo.TabIndex = 6;
            // 
            // SchedulerItemCountLabel
            // 
            this.SchedulerItemCountLabel.AutoSize = true;
            this.SchedulerItemCountLabel.Font = new System.Drawing.Font("Microsoft Sans Serif", 10F, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, ((byte)(0)));
            this.SchedulerItemCountLabel.Location = new System.Drawing.Point(58, 25);
            this.SchedulerItemCountLabel.Name = "SchedulerItemCountLabel";
            this.SchedulerItemCountLabel.Size = new System.Drawing.Size(71, 17);
            this.SchedulerItemCountLabel.TabIndex = 5;
            this.SchedulerItemCountLabel.Text = "Selected";
            // 
            // SetScheduleButton
            // 
            this.SetScheduleButton.Location = new System.Drawing.Point(36, 232);
            this.SetScheduleButton.Name = "SetScheduleButton";
            this.SetScheduleButton.Size = new System.Drawing.Size(84, 32);
            this.SetScheduleButton.TabIndex = 4;
            this.SetScheduleButton.Text = "<-- Set";
            this.SetScheduleButton.UseVisualStyleBackColor = true;
            this.SetScheduleButton.Click += new System.EventHandler(this.SetScheduleButton_Click);
            this.SetScheduleButton.MouseHover += new System.EventHandler(this.SetScheduleButton_MouseHover);
            // 
            // label3
            // 
            this.label3.AutoSize = true;
            this.label3.Location = new System.Drawing.Point(20, 108);
            this.label3.Name = "label3";
            this.label3.Size = new System.Drawing.Size(26, 13);
            this.label3.TabIndex = 1;
            this.label3.Text = "End";
            // 
            // label2
            // 
            this.label2.AutoSize = true;
            this.label2.Location = new System.Drawing.Point(20, 83);
            this.label2.Name = "label2";
            this.label2.Size = new System.Drawing.Size(29, 13);
            this.label2.TabIndex = 0;
            this.label2.Text = "Start";
            // 
            // statusLabel
            // 
            this.statusLabel.AutoSize = true;
            this.statusLabel.Font = new System.Drawing.Font("Microsoft Sans Serif", 12F, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, ((byte)(0)));
            this.statusLabel.Location = new System.Drawing.Point(921, 41);
            this.statusLabel.Name = "statusLabel";
            this.statusLabel.Size = new System.Drawing.Size(59, 20);
            this.statusLabel.TabIndex = 4;
            this.statusLabel.Text = "status";
            // 
            // helpBarText
            // 
            this.helpBarText.AutoSize = true;
            this.helpBarText.Location = new System.Drawing.Point(12, 696);
            this.helpBarText.Name = "helpBarText";
            this.helpBarText.Size = new System.Drawing.Size(29, 13);
            this.helpBarText.TabIndex = 5;
            this.helpBarText.Text = "Help";
            // 
            // IPLabel
            // 
            this.IPLabel.AutoSize = true;
            this.IPLabel.Location = new System.Drawing.Point(164, 40);
            this.IPLabel.Name = "IPLabel";
            this.IPLabel.Size = new System.Drawing.Size(76, 13);
            this.IPLabel.TabIndex = 6;
            this.IPLabel.Text = "None selected";
            // 
            // label22
            // 
            this.label22.AutoSize = true;
            this.label22.Location = new System.Drawing.Point(293, 15);
            this.label22.Name = "label22";
            this.label22.Size = new System.Drawing.Size(35, 13);
            this.label22.TabIndex = 11;
            this.label22.Text = "CTRL";
            // 
            // mainForm
            // 
            this.AutoScaleDimensions = new System.Drawing.SizeF(6F, 13F);
            this.AutoScaleMode = System.Windows.Forms.AutoScaleMode.Font;
            this.BackColor = System.Drawing.SystemColors.ButtonFace;
            this.ClientSize = new System.Drawing.Size(1904, 941);
            this.Controls.Add(this.IPLabel);
            this.Controls.Add(this.helpBarText);
            this.Controls.Add(this.statusLabel);
            this.Controls.Add(this.mainPanel);
            this.Controls.Add(this.label1);
            this.Controls.Add(this.rackComboBox);
            this.Controls.Add(this.menuStrip1);
            this.MainMenuStrip = this.menuStrip1;
            this.Name = "mainForm";
            this.Text = "Farm Rack Controller";
            this.Load += new System.EventHandler(this.Form1_Load);
            this.SizeChanged += new System.EventHandler(this.mainForm_SizeChanged);
            this.menuStrip1.ResumeLayout(false);
            this.menuStrip1.PerformLayout();
            this.mainPanel.ResumeLayout(false);
            this.mainPanel.PerformLayout();
            this.SchedulerGroup.ResumeLayout(false);
            this.SchedulerGroup.PerformLayout();
            this.ResumeLayout(false);
            this.PerformLayout();

        }

        #endregion

        private System.Windows.Forms.MenuStrip menuStrip1;
        private System.Windows.Forms.ToolStripMenuItem fileToolStripMenuItem;
        private System.Windows.Forms.ToolStripMenuItem exitToolStripMenuItem;
        private System.Windows.Forms.ToolStripMenuItem aboutToolStripMenuItem;
        private System.Windows.Forms.ToolStripMenuItem aboutToolStripMenuItem1;
        private System.Windows.Forms.ComboBox rackComboBox;
        private System.Windows.Forms.Label label1;
        private System.Windows.Forms.Panel mainPanel;
        private System.Windows.Forms.Label statusLabel;
        private System.Windows.Forms.Label helpBarText;
        private System.Windows.Forms.GroupBox SchedulerGroup;
        private System.Windows.Forms.ComboBox endMCombo;
        private System.Windows.Forms.ComboBox endHCombo;
        private System.Windows.Forms.ComboBox startMCombo;
        private System.Windows.Forms.ComboBox startHCombo;
        private System.Windows.Forms.Label SchedulerItemCountLabel;
        private System.Windows.Forms.Button SetScheduleButton;
        private System.Windows.Forms.Label label3;
        private System.Windows.Forms.Label label2;
        private System.Windows.Forms.Label label7;
        private System.Windows.Forms.Label label6;
        private System.Windows.Forms.ComboBox endMComboL;
        private System.Windows.Forms.ComboBox endHComboL;
        private System.Windows.Forms.ComboBox startMComboL;
        private System.Windows.Forms.ComboBox startHComboL;
        private System.Windows.Forms.Label label4;
        private System.Windows.Forms.Label label5;
        private System.Windows.Forms.Label label15;
        private System.Windows.Forms.Label label14;
        private System.Windows.Forms.Label label13;
        private System.Windows.Forms.Label label12;
        private System.Windows.Forms.Label label11;
        private System.Windows.Forms.Label label10;
        private System.Windows.Forms.Label label9;
        private System.Windows.Forms.Label label8;
        private System.Windows.Forms.Button ClearScheduleButton;
        private System.Windows.Forms.Label label17;
        private System.Windows.Forms.Label label16;
        private System.Windows.Forms.Label label18;
        private System.Windows.Forms.Label label21;
        private System.Windows.Forms.Label label19;
        private System.Windows.Forms.ToolTip toolTip1;
        private System.Windows.Forms.Button ApplyButton;
        private System.Windows.Forms.ListBox logListBox;
        private System.Windows.Forms.Label IPLabel;
        private System.Windows.Forms.Label label20;
        private System.Windows.Forms.ListBox readLogListBox;
        private System.Windows.Forms.Label label22;
    }
}

