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
        DataTable centerDataTable;
        DataTable leftDataTable;

        class resourcesforcenter
        {
            public resourcesforcenter(string id, string nameofcard, string nameofgroup)
            {
                this.id = id;
                this.nameofcard = nameofcard;
                this.nameofgroup = nameofgroup;
            }

            public string id { get; set; }
            public string nameofcard { get; set; }
            public string nameofgroup { get; set; }
            
        }


        public WindowXpassword()
        {
            InitializeComponent();

            string sql = String.Format("select * from группы");
            string sql2 = String.Format("select карт.идкарты, карт.наименование, грп.наименование from сплитгруппыкартотеки as сплит, группы as грп, картотека as карт where сплит.идгруппы = грп.идгруппы and сплит.идкарты = карт.идкарты");
            SQL.SQLConnect(); // Подключение к БД
            leftDataTable = SQL.Inquiry(sql); // Выполняем запрос, возвращаем результат в виде DataTable
            centerDataTable = SQL.Inquiry(sql2); // Выполняем запрос, возвращаем результат в виде DataTable
            SQL.Close();

            var list = new List<resourcesforcenter>();


            string id, nameofcard, nameofgroup;
            int index = 0;
            for (int i = 0; i < centerDataTable.Rows.Count; i++) //Строка
            {
                id = centerDataTable.Rows[i][0].ToString();
                nameofcard = centerDataTable.Rows[i][1].ToString();
                nameofgroup = centerDataTable.Rows[i][2].ToString();

                if (!list.Exists(x => x.id == id))
                {
                    list.Add(new resourcesforcenter(id, nameofcard, nameofgroup));
                    //Console.WriteLine($"Exist{id}");
                }
                else
                {
                    list.Find(x => x.id == id).nameofgroup += $", {nameofgroup}";
                }

            }

            foreach (var item in list)
            {
                Console.WriteLine($"res: {item.id.ToString()}");
                Console.WriteLine($"res: {item.nameofcard.ToString()}");
                Console.WriteLine($"res: {item.nameofgroup.ToString()}");
            }

            ViewCenterMenu.ItemsSource = list;
            ViewLeftMenu.ItemsSource = leftDataTable.AsDataView();

        }

        private void Button_Click(object sender, RoutedEventArgs e)
        {

        }
    }


}
