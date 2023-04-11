using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Forms;

namespace ControlUI
{
    public partial class scriptlogForm : Form
    {
        public scriptlogForm()
        {
            InitializeComponent();
        }

        private void scriptlogForm_Load(object sender, EventArgs e)
        {
            msglistBox.Items.Clear();
        }


        public void addLog(string s)
        {
            msglistBox.BeginInvoke(new Action(() => {
                msglistBox.Items.Add(s);
            }));
           
        }
    }
}
