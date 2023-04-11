
namespace ControlUI
{
    partial class scriptlogForm
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
            this.msglistBox = new System.Windows.Forms.ListBox();
            this.SuspendLayout();
            // 
            // msglistBox
            // 
            this.msglistBox.FormattingEnabled = true;
            this.msglistBox.ItemHeight = 15;
            this.msglistBox.Location = new System.Drawing.Point(21, 12);
            this.msglistBox.Name = "msglistBox";
            this.msglistBox.Size = new System.Drawing.Size(418, 514);
            this.msglistBox.TabIndex = 0;
            // 
            // scriptlogForm
            // 
            this.AutoScaleDimensions = new System.Drawing.SizeF(7F, 15F);
            this.AutoScaleMode = System.Windows.Forms.AutoScaleMode.Font;
            this.ClientSize = new System.Drawing.Size(462, 548);
            this.Controls.Add(this.msglistBox);
            this.FormBorderStyle = System.Windows.Forms.FormBorderStyle.FixedSingle;
            this.MaximizeBox = false;
            this.Name = "scriptlogForm";
            this.Text = "Logs";
            this.Load += new System.EventHandler(this.scriptlogForm_Load);
            this.ResumeLayout(false);

        }

        #endregion

        private System.Windows.Forms.ListBox msglistBox;
    }
}