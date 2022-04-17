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
    public partial class ShowInputDialog : Window
    {
        public string result;
        public ShowInputDialog(string str= "Введите", string text="")
        {
            InitializeComponent();
            textBlock.Text = str;
            textBox.Text = text;
        }


        private void btnOk_Click(object sender, RoutedEventArgs e)
        {
            string text = textBox.Text.Trim();
            if (String.IsNullOrEmpty(text))
            {
                MessageBox.Show("Пустое окно ввода!");
            }
            else
            {
                result = textBox.Text;
                this.Close();
            }
            
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
