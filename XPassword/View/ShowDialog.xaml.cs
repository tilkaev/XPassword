using MaterialDesignThemes.Wpf;
using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows;
using System.Windows.Controls;
using System.Windows.Data;
using System.Windows.Documents;
using System.Windows.Input;
using System.Windows.Media;
using System.Windows.Media.Imaging;
using System.Windows.Shapes;

namespace XPassword.View
{
    /// <summary>
    /// Логика взаимодействия для ShowInputDialog.xaml
    /// </summary>
    public partial class ShowDialog : Window
    {
        public bool result;
        public ShowDialog(string str = "Инфо")
        {
            InitializeComponent();
            textBlock.Text = str;
        }


        private void btnOk_Click(object sender, RoutedEventArgs e)
        {
            result = true;
            this.Close();
            
        }

        private void btnExit_Click(object sender, RoutedEventArgs e)
        {
            this.Close();
        }

        private void MoveWindow(object sender, MouseButtonEventArgs e)
        {
            if (e.ChangedButton == MouseButton.Left)
            {
                this.DragMove();
            }
        }
    }
}
