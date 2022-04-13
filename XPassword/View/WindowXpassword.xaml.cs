using SpaceBaseApp.Core;
using System;
using System.Collections.Generic;
using System.Data;
using System.Threading.Tasks;
using System.Windows;
using System.Windows.Controls;
using System.Windows.Input;
using System.Windows.Media;
using XPassword.Core;

namespace XPassword
{



    public partial class WindowXpassword : Window
    {

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


        DataTable leftDataTable;
        DataTable centerDataTable;
        DataTable cardEntriesTable;
        List<IContentOfCard> contentOfCard;
        static Button btnEdit;


        public WindowXpassword()
        {
            InitializeComponent();

            contentOfCard = new List<IContentOfCard>();

            btnEdit = BtnEdit;
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
            /*
            foreach (var item in list)
            {
                Console.WriteLine($"res: {item.id.ToString()}");
                Console.WriteLine($"res: {item.nameofcard.ToString()}");
                Console.WriteLine($"res: {item.nameofgroup.ToString()}");
            }*/


            string id2;
            for (int i = 0; i < cardEntriesTable.Rows.Count; i++) //Строка
            {
                id2 = cardEntriesTable.Rows[i][2].ToString();
                Console.WriteLine(id2);
            }

            ViewCenterMenu.ItemsSource = list;
            ViewLeftMenu.ItemsSource = leftDataTable.AsDataView();

            


        }

       

        private void TextBox_SelectionChanged(object sender, RoutedEventArgs e)
        {
            if (sender != null)
            {
                e.Handled = true;
                if ((sender as TextBox).SelectionLength != 0)
                    (sender as TextBox).SelectionLength = 0;
            }
        }

        public static async void ShowInfoFromCopy()
        {
            btnEdit.Content = "Текст скопирован";
            btnEdit.Background = Brushes.White;
            btnEdit.Foreground = Brushes.Black;
            btnEdit.Opacity = 1;
            await Task.Delay(500);
            btnEdit.Content = "Изменить";
            btnEdit.Background = Brushes.Transparent;
            btnEdit.Foreground = Brushes.White;
            btnEdit.Opacity = .3;
        }

        private void LeftButtonMenu(object sender, RoutedEventArgs e)
        {
            int idofgroup = int.Parse(((Button)sender).Tag.ToString());
            ViewCenterMenu.ItemsSource = null;

            string sql = String.Format($"select карт.идкарты, карт.наименование, грп.наименование from сплитгруппыкартотеки as сплит, группы as грп, картотека as карт where сплит.идгруппы = грп.идгруппы and сплит.идкарты = карт.идкарты  and грп.идгруппы = {idofgroup} ");

            SQL.SQLConnect();
            centerDataTable = SQL.Inquiry(sql);
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


            ViewCenterMenu.ItemsSource = list;
        }

        private void CenterButtonMenu(object sender, RoutedEventArgs e)
        {
            foreach (var item in contentOfCard)
            {
                MainOutputStackPanel.Children.Remove(item.getuielement());
            }
            contentOfCard = new List<IContentOfCard>();
            int idcard = int.Parse(((Button)sender).Tag.ToString());
            string sql = String.Format($"select * from запись where запись.идкарты = {idcard} order by идсортиовки");

            SQL.SQLConnect();
            centerDataTable = SQL.Inquiry(sql);
            SQL.Close();



            for (int i = 0; i < centerDataTable.Rows.Count; i++) //Строка
            {
                int idtype = int.Parse(centerDataTable.Rows[i][2].ToString());
                string nameofline = centerDataTable.Rows[i][4].ToString();
                string content = centerDataTable.Rows[i][5].ToString();
                switch (idtype)
                {
                    case 1:
                        contentOfCard.Add(new AddTextBox(this, content, nameofline));
                        break;
                    case 2:
                        contentOfCard.Add(new AddPasswordBox(this, content, nameofline));
                        break;
                    case 3:
                        contentOfCard.Add(new AddWebTextBox(this, content, nameofline));
                        break;
                }
            }

            


            //contentOfCard.Add(new AddTextBox(this, "asdas", "Логин"));
            //contentOfCard.Add(new AddPasswordBox(this, "asdasasdasasdasasdasasdasasdasasdasasdasasdasasdas", "Пароль"));
            //contentOfCard.Add(new AddPasswordBox(this, "6657", "Пароль"));
            //contentOfCard.Add(new AddPasswordBox(this, "123", "Пароль"));
            //contentOfCard.Add(new AddWebTextBox(this, "mail.ru", "Сайт"));
        }
    }


}
