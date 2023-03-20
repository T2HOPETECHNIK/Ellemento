
namespace ControlUI
{
    partial class configMakerForm
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
            this.configFileLabel = new System.Windows.Forms.Label();
            this.contentListBox = new System.Windows.Forms.ListBox();
            this.groupBox1 = new System.Windows.Forms.GroupBox();
            this.portBox = new System.Windows.Forms.TextBox();
            this.label3 = new System.Windows.Forms.Label();
            this.ipBox = new System.Windows.Forms.TextBox();
            this.label2 = new System.Windows.Forms.Label();
            this.controlGroupBox = new System.Windows.Forms.GroupBox();
            this.updateEntryButton = new System.Windows.Forms.Button();
            this.labelTextBox = new System.Windows.Forms.TextBox();
            this.label5 = new System.Windows.Forms.Label();
            this.bitposComboBox = new System.Windows.Forms.ComboBox();
            this.label4 = new System.Windows.Forms.Label();
            this.addrTextBox = new System.Windows.Forms.TextBox();
            this.label1 = new System.Windows.Forms.Label();
            this.typeGroupBox = new System.Windows.Forms.GroupBox();
            this.radioButton5 = new System.Windows.Forms.RadioButton();
            this.radioButton4 = new System.Windows.Forms.RadioButton();
            this.accessGroupBox = new System.Windows.Forms.GroupBox();
            this.radioButton3 = new System.Windows.Forms.RadioButton();
            this.radioButton2 = new System.Windows.Forms.RadioButton();
            this.radioButton1 = new System.Windows.Forms.RadioButton();
            this.loadConfigButton = new System.Windows.Forms.Button();
            this.saveAsButton = new System.Windows.Forms.Button();
            this.cloneButton = new System.Windows.Forms.Button();
            this.addButton = new System.Windows.Forms.Button();
            this.deleteButton = new System.Windows.Forms.Button();
            this.groupBox1.SuspendLayout();
            this.controlGroupBox.SuspendLayout();
            this.typeGroupBox.SuspendLayout();
            this.accessGroupBox.SuspendLayout();
            this.SuspendLayout();
            // 
            // configFileLabel
            // 
            this.configFileLabel.AutoSize = true;
            this.configFileLabel.Location = new System.Drawing.Point(41, 46);
            this.configFileLabel.Name = "configFileLabel";
            this.configFileLabel.Size = new System.Drawing.Size(50, 15);
            this.configFileLabel.TabIndex = 0;
            this.configFileLabel.Text = "Content";
            // 
            // contentListBox
            // 
            this.contentListBox.FormattingEnabled = true;
            this.contentListBox.ItemHeight = 15;
            this.contentListBox.Location = new System.Drawing.Point(36, 77);
            this.contentListBox.Name = "contentListBox";
            this.contentListBox.ScrollAlwaysVisible = true;
            this.contentListBox.Size = new System.Drawing.Size(423, 499);
            this.contentListBox.TabIndex = 1;
            this.contentListBox.SelectedIndexChanged += new System.EventHandler(this.contentListBox_SelectedIndexChanged);
            // 
            // groupBox1
            // 
            this.groupBox1.Controls.Add(this.portBox);
            this.groupBox1.Controls.Add(this.label3);
            this.groupBox1.Controls.Add(this.ipBox);
            this.groupBox1.Controls.Add(this.label2);
            this.groupBox1.Location = new System.Drawing.Point(578, 63);
            this.groupBox1.Name = "groupBox1";
            this.groupBox1.Size = new System.Drawing.Size(430, 76);
            this.groupBox1.TabIndex = 2;
            this.groupBox1.TabStop = false;
            this.groupBox1.Text = "Global setting";
            // 
            // portBox
            // 
            this.portBox.Location = new System.Drawing.Point(332, 30);
            this.portBox.Name = "portBox";
            this.portBox.Size = new System.Drawing.Size(57, 23);
            this.portBox.TabIndex = 3;
            // 
            // label3
            // 
            this.label3.AutoSize = true;
            this.label3.Location = new System.Drawing.Point(288, 34);
            this.label3.Name = "label3";
            this.label3.Size = new System.Drawing.Size(29, 15);
            this.label3.TabIndex = 2;
            this.label3.Text = "Port";
            // 
            // ipBox
            // 
            this.ipBox.Location = new System.Drawing.Point(100, 30);
            this.ipBox.Name = "ipBox";
            this.ipBox.Size = new System.Drawing.Size(124, 23);
            this.ipBox.TabIndex = 1;
            // 
            // label2
            // 
            this.label2.AutoSize = true;
            this.label2.Location = new System.Drawing.Point(24, 33);
            this.label2.Name = "label2";
            this.label2.Size = new System.Drawing.Size(60, 15);
            this.label2.TabIndex = 0;
            this.label2.Text = "IP address";
            // 
            // controlGroupBox
            // 
            this.controlGroupBox.Controls.Add(this.updateEntryButton);
            this.controlGroupBox.Controls.Add(this.labelTextBox);
            this.controlGroupBox.Controls.Add(this.label5);
            this.controlGroupBox.Controls.Add(this.bitposComboBox);
            this.controlGroupBox.Controls.Add(this.label4);
            this.controlGroupBox.Controls.Add(this.addrTextBox);
            this.controlGroupBox.Controls.Add(this.label1);
            this.controlGroupBox.Controls.Add(this.typeGroupBox);
            this.controlGroupBox.Controls.Add(this.accessGroupBox);
            this.controlGroupBox.Location = new System.Drawing.Point(578, 163);
            this.controlGroupBox.Name = "controlGroupBox";
            this.controlGroupBox.Size = new System.Drawing.Size(429, 293);
            this.controlGroupBox.TabIndex = 3;
            this.controlGroupBox.TabStop = false;
            this.controlGroupBox.Text = "Control";
            // 
            // updateEntryButton
            // 
            this.updateEntryButton.Location = new System.Drawing.Point(159, 240);
            this.updateEntryButton.Name = "updateEntryButton";
            this.updateEntryButton.Size = new System.Drawing.Size(111, 35);
            this.updateEntryButton.TabIndex = 8;
            this.updateEntryButton.Text = "Update entry";
            this.updateEntryButton.UseVisualStyleBackColor = true;
            this.updateEntryButton.Click += new System.EventHandler(this.updateEntryButton_Click);
            // 
            // labelTextBox
            // 
            this.labelTextBox.Location = new System.Drawing.Point(105, 201);
            this.labelTextBox.MaxLength = 32;
            this.labelTextBox.Name = "labelTextBox";
            this.labelTextBox.Size = new System.Drawing.Size(253, 23);
            this.labelTextBox.TabIndex = 7;
            // 
            // label5
            // 
            this.label5.AutoSize = true;
            this.label5.Location = new System.Drawing.Point(24, 204);
            this.label5.Name = "label5";
            this.label5.Size = new System.Drawing.Size(75, 15);
            this.label5.TabIndex = 6;
            this.label5.Text = "Control label";
            // 
            // bitposComboBox
            // 
            this.bitposComboBox.FormattingEnabled = true;
            this.bitposComboBox.Location = new System.Drawing.Point(282, 170);
            this.bitposComboBox.Name = "bitposComboBox";
            this.bitposComboBox.Size = new System.Drawing.Size(76, 23);
            this.bitposComboBox.TabIndex = 5;
            // 
            // label4
            // 
            this.label4.AutoSize = true;
            this.label4.Location = new System.Drawing.Point(170, 173);
            this.label4.Name = "label4";
            this.label4.Size = new System.Drawing.Size(102, 15);
            this.label4.TabIndex = 4;
            this.label4.Text = "Bit position (15..0)";
            // 
            // addrTextBox
            // 
            this.addrTextBox.Location = new System.Drawing.Point(79, 170);
            this.addrTextBox.MaxLength = 5;
            this.addrTextBox.Name = "addrTextBox";
            this.addrTextBox.Size = new System.Drawing.Size(74, 23);
            this.addrTextBox.TabIndex = 3;
            // 
            // label1
            // 
            this.label1.AutoSize = true;
            this.label1.Location = new System.Drawing.Point(24, 173);
            this.label1.Name = "label1";
            this.label1.Size = new System.Drawing.Size(49, 15);
            this.label1.TabIndex = 2;
            this.label1.Text = "Address";
            // 
            // typeGroupBox
            // 
            this.typeGroupBox.Controls.Add(this.radioButton5);
            this.typeGroupBox.Controls.Add(this.radioButton4);
            this.typeGroupBox.Location = new System.Drawing.Point(184, 35);
            this.typeGroupBox.Name = "typeGroupBox";
            this.typeGroupBox.Size = new System.Drawing.Size(140, 112);
            this.typeGroupBox.TabIndex = 1;
            this.typeGroupBox.TabStop = false;
            this.typeGroupBox.Text = "Control Type";
            // 
            // radioButton5
            // 
            this.radioButton5.AutoSize = true;
            this.radioButton5.Location = new System.Drawing.Point(20, 59);
            this.radioButton5.Name = "radioButton5";
            this.radioButton5.Size = new System.Drawing.Size(54, 19);
            this.radioButton5.TabIndex = 1;
            this.radioButton5.TabStop = true;
            this.radioButton5.Text = "Word";
            this.radioButton5.UseVisualStyleBackColor = true;
            // 
            // radioButton4
            // 
            this.radioButton4.AutoSize = true;
            this.radioButton4.Location = new System.Drawing.Point(20, 34);
            this.radioButton4.Name = "radioButton4";
            this.radioButton4.Size = new System.Drawing.Size(68, 19);
            this.radioButton4.TabIndex = 0;
            this.radioButton4.TabStop = true;
            this.radioButton4.Text = "Bit/Bool";
            this.radioButton4.UseVisualStyleBackColor = true;
            // 
            // accessGroupBox
            // 
            this.accessGroupBox.Controls.Add(this.radioButton3);
            this.accessGroupBox.Controls.Add(this.radioButton2);
            this.accessGroupBox.Controls.Add(this.radioButton1);
            this.accessGroupBox.Location = new System.Drawing.Point(23, 36);
            this.accessGroupBox.Name = "accessGroupBox";
            this.accessGroupBox.Size = new System.Drawing.Size(130, 112);
            this.accessGroupBox.TabIndex = 0;
            this.accessGroupBox.TabStop = false;
            this.accessGroupBox.Text = "Access";
            // 
            // radioButton3
            // 
            this.radioButton3.AutoSize = true;
            this.radioButton3.Location = new System.Drawing.Point(17, 75);
            this.radioButton3.Name = "radioButton3";
            this.radioButton3.Size = new System.Drawing.Size(82, 19);
            this.radioButton3.TabIndex = 2;
            this.radioButton3.TabStop = true;
            this.radioButton3.Text = "Read-write";
            this.radioButton3.UseVisualStyleBackColor = true;
            // 
            // radioButton2
            // 
            this.radioButton2.AutoSize = true;
            this.radioButton2.Location = new System.Drawing.Point(17, 49);
            this.radioButton2.Name = "radioButton2";
            this.radioButton2.Size = new System.Drawing.Size(79, 19);
            this.radioButton2.TabIndex = 1;
            this.radioButton2.TabStop = true;
            this.radioButton2.Text = "Write only";
            this.radioButton2.UseVisualStyleBackColor = true;
            // 
            // radioButton1
            // 
            this.radioButton1.AutoSize = true;
            this.radioButton1.Location = new System.Drawing.Point(17, 23);
            this.radioButton1.Name = "radioButton1";
            this.radioButton1.Size = new System.Drawing.Size(77, 19);
            this.radioButton1.TabIndex = 0;
            this.radioButton1.TabStop = true;
            this.radioButton1.Text = "Read only";
            this.radioButton1.UseVisualStyleBackColor = true;
            // 
            // loadConfigButton
            // 
            this.loadConfigButton.BackgroundImage = global::ControlUI.Properties.Resources.load_from_file;
            this.loadConfigButton.BackgroundImageLayout = System.Windows.Forms.ImageLayout.Zoom;
            this.loadConfigButton.Font = new System.Drawing.Font("Segoe UI", 12F, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point);
            this.loadConfigButton.ForeColor = System.Drawing.Color.Red;
            this.loadConfigButton.Location = new System.Drawing.Point(585, 489);
            this.loadConfigButton.Name = "loadConfigButton";
            this.loadConfigButton.Size = new System.Drawing.Size(186, 86);
            this.loadConfigButton.TabIndex = 4;
            this.loadConfigButton.Text = "LOAD CONFIG FILE";
            this.loadConfigButton.UseVisualStyleBackColor = true;
            this.loadConfigButton.Click += new System.EventHandler(this.loadConfigButton_Click);
            // 
            // saveAsButton
            // 
            this.saveAsButton.BackgroundImage = global::ControlUI.Properties.Resources.external_direct_download_web_flaticons_flat_flat_icons;
            this.saveAsButton.BackgroundImageLayout = System.Windows.Forms.ImageLayout.Zoom;
            this.saveAsButton.Font = new System.Drawing.Font("Segoe UI", 12F, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point);
            this.saveAsButton.ForeColor = System.Drawing.Color.Red;
            this.saveAsButton.Location = new System.Drawing.Point(821, 489);
            this.saveAsButton.Name = "saveAsButton";
            this.saveAsButton.Size = new System.Drawing.Size(186, 86);
            this.saveAsButton.TabIndex = 5;
            this.saveAsButton.Text = "SAVE TO FILE";
            this.saveAsButton.UseVisualStyleBackColor = true;
            this.saveAsButton.Click += new System.EventHandler(this.saveAsButton_Click);
            // 
            // cloneButton
            // 
            this.cloneButton.BackgroundImage = global::ControlUI.Properties.Resources.clone;
            this.cloneButton.BackgroundImageLayout = System.Windows.Forms.ImageLayout.Zoom;
            this.cloneButton.Font = new System.Drawing.Font("Segoe UI", 12F, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point);
            this.cloneButton.ForeColor = System.Drawing.Color.Red;
            this.cloneButton.Location = new System.Drawing.Point(475, 77);
            this.cloneButton.Name = "cloneButton";
            this.cloneButton.Size = new System.Drawing.Size(87, 87);
            this.cloneButton.TabIndex = 0;
            this.cloneButton.Text = "CLONE";
            this.cloneButton.TextAlign = System.Drawing.ContentAlignment.BottomCenter;
            this.cloneButton.UseVisualStyleBackColor = true;
            this.cloneButton.Click += new System.EventHandler(this.cloneButton_Click);
            // 
            // addButton
            // 
            this.addButton.BackgroundImage = global::ControlUI.Properties.Resources.insert_clip;
            this.addButton.BackgroundImageLayout = System.Windows.Forms.ImageLayout.Zoom;
            this.addButton.Font = new System.Drawing.Font("Segoe UI", 12F, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point);
            this.addButton.ForeColor = System.Drawing.Color.Red;
            this.addButton.Location = new System.Drawing.Point(475, 180);
            this.addButton.Name = "addButton";
            this.addButton.Size = new System.Drawing.Size(87, 87);
            this.addButton.TabIndex = 1;
            this.addButton.Text = "ADD";
            this.addButton.TextAlign = System.Drawing.ContentAlignment.BottomCenter;
            this.addButton.UseVisualStyleBackColor = true;
            this.addButton.Click += new System.EventHandler(this.addButton_Click);
            // 
            // deleteButton
            // 
            this.deleteButton.BackgroundImage = global::ControlUI.Properties.Resources.del_key1;
            this.deleteButton.BackgroundImageLayout = System.Windows.Forms.ImageLayout.Zoom;
            this.deleteButton.Font = new System.Drawing.Font("Segoe UI", 11.25F, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point);
            this.deleteButton.ForeColor = System.Drawing.Color.Red;
            this.deleteButton.ImageAlign = System.Drawing.ContentAlignment.BottomCenter;
            this.deleteButton.Location = new System.Drawing.Point(475, 286);
            this.deleteButton.Name = "deleteButton";
            this.deleteButton.Size = new System.Drawing.Size(87, 87);
            this.deleteButton.TabIndex = 6;
            this.deleteButton.Text = "DELETE";
            this.deleteButton.TextAlign = System.Drawing.ContentAlignment.BottomCenter;
            this.deleteButton.UseVisualStyleBackColor = true;
            this.deleteButton.Click += new System.EventHandler(this.deleteButton_Click);
            // 
            // configMakerForm
            // 
            this.AutoScaleDimensions = new System.Drawing.SizeF(7F, 15F);
            this.AutoScaleMode = System.Windows.Forms.AutoScaleMode.Font;
            this.ClientSize = new System.Drawing.Size(1064, 621);
            this.Controls.Add(this.deleteButton);
            this.Controls.Add(this.addButton);
            this.Controls.Add(this.saveAsButton);
            this.Controls.Add(this.cloneButton);
            this.Controls.Add(this.loadConfigButton);
            this.Controls.Add(this.controlGroupBox);
            this.Controls.Add(this.groupBox1);
            this.Controls.Add(this.contentListBox);
            this.Controls.Add(this.configFileLabel);
            this.MaximizeBox = false;
            this.MinimizeBox = false;
            this.Name = "configMakerForm";
            this.SizeGripStyle = System.Windows.Forms.SizeGripStyle.Hide;
            this.Text = "Config Maker";
            this.Load += new System.EventHandler(this.configMakerForm_Load);
            this.groupBox1.ResumeLayout(false);
            this.groupBox1.PerformLayout();
            this.controlGroupBox.ResumeLayout(false);
            this.controlGroupBox.PerformLayout();
            this.typeGroupBox.ResumeLayout(false);
            this.typeGroupBox.PerformLayout();
            this.accessGroupBox.ResumeLayout(false);
            this.accessGroupBox.PerformLayout();
            this.ResumeLayout(false);
            this.PerformLayout();

        }

        #endregion

        private System.Windows.Forms.Label configFileLabel;
        private System.Windows.Forms.ListBox contentListBox;
        private System.Windows.Forms.GroupBox groupBox1;
        private System.Windows.Forms.TextBox portBox;
        private System.Windows.Forms.Label label3;
        private System.Windows.Forms.TextBox ipBox;
        private System.Windows.Forms.Label label2;
        private System.Windows.Forms.GroupBox controlGroupBox;
        private System.Windows.Forms.Button updateEntryButton;
        private System.Windows.Forms.TextBox labelTextBox;
        private System.Windows.Forms.Label label5;
        private System.Windows.Forms.ComboBox bitposComboBox;
        private System.Windows.Forms.Label label4;
        private System.Windows.Forms.TextBox addrTextBox;
        private System.Windows.Forms.Label label1;
        private System.Windows.Forms.GroupBox typeGroupBox;
        private System.Windows.Forms.RadioButton radioButton5;
        private System.Windows.Forms.RadioButton radioButton4;
        private System.Windows.Forms.GroupBox accessGroupBox;
        private System.Windows.Forms.RadioButton radioButton3;
        private System.Windows.Forms.RadioButton radioButton2;
        private System.Windows.Forms.RadioButton radioButton1;
        private System.Windows.Forms.Button loadConfigButton;
        private System.Windows.Forms.Button saveAsButton;
        private System.Windows.Forms.Button cloneButton;
        private System.Windows.Forms.Button addButton;
        private System.Windows.Forms.Button deleteButton;
    }
}