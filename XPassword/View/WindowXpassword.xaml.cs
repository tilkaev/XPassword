using MaterialDesignThemes.Wpf;
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
        DataTable cardEntriesTable;
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

        class cardEntries
        {
            public cardEntries(string id, string nameofcard, string nameofgroup)
            {
                this.id = id;
                this.nameofcard = nameofcard;
                this.nameofgroup = nameofgroup;
            }

            public string id { get; set; }
            public string nameofcard { get; set; }
            public string nameofgroup { get; set; }
        }


        private void addTextBlox(string hinttext, string text)
        {
            ControlTemplate template = new ControlTemplate(typeof(Button));
            var image = new FrameworkElementFactory(typeof(Image));
            template.VisualTree = image;


            var uielement = new TextBox()
            {
                Text = text,
                
                
            };

            uielement.SetValue(Template, "SAdsa");


            HintAssist.SetHint(uielement, hinttext);

            MainOutputStackPanel.Children.Add(MainOutputStackPanel);


        }

        public WindowXpassword()
        {
            InitializeComponent();

            string sql = String.Format("select * from группы");
            string sql2 = String.Format("select карт.идкарты, карт.наименование, грп.наименование from сплитгруппыкартотеки as сплит, группы as грп, картотека as карт where сплит.идгруппы = грп.идгруппы and сплит.идкарты = карт.идкарты");
            string sql3 = String.Format($"select * from запись where запись.идкарты = {2}");
            SQL.SQLConnect();
            leftDataTable = SQL.Inquiry(sql);
            centerDataTable = SQL.Inquiry(sql2); 
            cardEntriesTable = SQL.Inquiry(sql3);
            SQL.Close();

            var list = new List<resourcesforcenter>();


            string id, nameofcard, nameofgroup;
            for (int i = 0; i < centerDataTable.Rows.Count; i++) //Строка
            {
                id = centerDataTable.Rows[i][0].ToString();
                nameofcard = centerDataTable.Rows[i][1].ToString();
                nameofgroup = centerDataTable.Rows[i][2].ToString();

                if (!list.Exists(x => x.id == id))
                    list.Add(new resourcesforcenter(id, nameofcard, nameofgroup));
                else
                    list.Find(x => x.id == id).nameofgroup += $", {nameofgroup}";
            }

            //foreach (var item in list)
            //{
            //    Console.WriteLine($"res: {item.id.ToString()}");
            //    Console.WriteLine($"res: {item.nameofcard.ToString()}");
            //    Console.WriteLine($"res: {item.nameofgroup.ToString()}");
            //}

            string id2;
            for (int i = 0; i < cardEntriesTable.Rows.Count; i++) //Строка
            {
                id2 = cardEntriesTable.Rows[i][2].ToString();
                Console.WriteLine(id2);
            }

            ViewCenterMenu.ItemsSource = list;
            ViewLeftMenu.ItemsSource = leftDataTable.AsDataView();

        }

        private void Button_Click(object sender, RoutedEventArgs e)
        {

        }

        private void Label_MouseDown(object sender, MouseButtonEventArgs e)
        {

        }
    }


}
