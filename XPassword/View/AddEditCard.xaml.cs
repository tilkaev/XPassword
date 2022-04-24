using MaterialDesignThemes.Wpf;
using SpaceBaseApp.Core;
using System;
using System.Collections.Generic;
using System.Data;
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
    public partial class AddEditCard : Window
    {
        public string result;
        public string result2;
        DataTable dataTable;

        public AddEditCard(string text = "", string titlegroup = "")
        {
            InitializeComponent();
            //    string sql = String.Format($"INSERT INTO картотека (наименование) values ('{win.result}')");
            //    SQL.SQLConnect();
            //    SQL.Execute(sql);
            //    ShowCenter();
            //    SQL.Close();

            string sql = String.Format("select * from группы");
            SQL.SQLConnect();
            dataTable = SQL.Inquiry(sql);
            SQL.Close();

            int index = 0;
            foreach (DataRow item in dataTable.Rows)
            {
                if (item[1].ToString() == titlegroup)
                {
                    comboBox.SelectedIndex = index;
                }
                comboBox.Items.Add(item[1].ToString()); // Заполнение КомбоБокса
                index++;
            }
            textBox.Text = text;
        }


        private void btnOk_Click(object sender, RoutedEventArgs e)
        {
            string text = textBox.Text.Trim();
            if (comboBox.SelectedIndex == -1)
            {
                MessageBox.Show("Выберите группу!");
                return;
            }
            if (String.IsNullOrEmpty(text))
            {
                MessageBox.Show("Введите название карты!");
                return;
            }
            result = dataTable.Rows[comboBox.SelectedIndex][0].ToString();
            result2 = textBox.Text;
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
