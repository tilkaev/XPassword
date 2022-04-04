using SpaceBaseApp.Core;
using System;
using System.Collections.Generic;
using System.Collections.ObjectModel;
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

namespace XPassword
{



    public partial class WindowXpassword : Window
    {
        DataTable newDataTable;
        DataTable dataTable;

        SQL sqls;
        public WindowXpassword()
        {
            InitializeComponent();
            sqls = new SQL();

            string sql = String.Format("select * from группы");
            sqls.SQLConnect(); // Подключение к БД
            newDataTable = sqls.Inquiry(sql); // Выполняем запрос, возвращаем результат в виде DataTable
            dataTable = newDataTable.Copy();
            sqls.Close();

            ViewLeftMenu.ItemsSource = newDataTable.AsDataView();
        }

        private void Button_Click(object sender, RoutedEventArgs e)
        {

        }
    }


}
