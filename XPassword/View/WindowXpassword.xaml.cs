using SpaceBaseApp.Core;
using System;
using System.Collections.Generic;
using System.Data;
using System.Threading.Tasks;
using System.Windows;
using System.Windows.Controls;
using System.Windows.Data;
using System.Windows.Input;
using System.Windows.Media;
using XPassword.Core;
using XPassword.View;

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
        List<resourcesforcenter> centerList;
        static Button btnEdit;
        int LAST_ID_GROUP;
        int LAST_ID_CARD;


        public WindowXpassword()
        {
            InitializeComponent();

            contentOfCard = new List<IContentOfCard>();
            btnEdit = BtnEdit;

            

            SQL.SQLConnect();
            ShowLeft();
            ShowCenter();
            ShowRight(int.Parse(centerDataTable.Rows[0][0].ToString()));
            SQL.Close();

        }

        private void ShowLeft()
        {
            string sql = String.Format("select * from группы");
            leftDataTable = SQL.Inquiry(sql);

            ViewLeftMenu.ItemsSource = leftDataTable.AsDataView();

        }

        private void ShowCenter(int idgroup=0)
        {
            LAST_ID_GROUP = idgroup;
            string sql;
            if (idgroup == 0)
            {
                
                //sql = String.Format("select карт.идкарты, карт.наименование, грп.наименование from сплитгруппыкартотеки as сплит, группы as грп, картотека as карт where сплит.идгруппы = грп.идгруппы and сплит.идкарты = карт.идкарты");
                sql = String.Format("select картотека.идкарты, картотека.наименование, группы.наименование from группы, картотека where группы.идгруппы = картотека.идгруппы");
            }
            else
            {
                sql = String.Format($"select картотека.идкарты, картотека.наименование, группы.наименование from группы, картотека where группы.идгруппы = картотека.идгруппы and группы.идгруппы = {idgroup} ");
            }


            centerDataTable = SQL.Inquiry(sql);

            centerList = new List<resourcesforcenter>();
            string id, nameofcard, nameofgroup;
            for (int i = 0; i < centerDataTable.Rows.Count; i++) //По строке
            {
                id = centerDataTable.Rows[i][0].ToString();
                nameofcard = centerDataTable.Rows[i][1].ToString();
                nameofgroup = centerDataTable.Rows[i][2].ToString();

                if (!centerList.Exists(x => x.id == id))
                    centerList.Add(new resourcesforcenter(id, nameofcard, nameofgroup));
                else
                    centerList.Find(x => x.id == id).nameofgroup += $", {nameofgroup}";
            }


            ViewCenterMenu.ItemsSource = centerList;
            CollectionView view = (CollectionView)CollectionViewSource.GetDefaultView(ViewCenterMenu.ItemsSource);
            view.Filter = UserFilter;
        }

        private void ShowRight(int idcard = 0)
        {
            if (idcard == 0)
            {
                idcard = int.Parse(centerList[0].id.ToString());
            }
            LAST_ID_CARD = idcard;
            string nameofcard, nameofgroup;
            nameofcard = centerList.Find(x => x.id == idcard.ToString()).nameofcard;
            nameofgroup = centerList.Find(x => x.id == idcard.ToString()).nameofgroup;
            labelNameCard.Content = nameofcard;
            labelNameGroup.Content = nameofgroup;




            foreach (var item in contentOfCard)
            {
                MainOutputStackPanel.Children.Remove(item.getuielement());
            }
            contentOfCard = new List<IContentOfCard>();
            string sql = String.Format($"select * from запись where запись.идкарты = {idcard} order by идсортиовки");

            cardEntriesTable = SQL.Inquiry(sql);


            for (int i = 0; i < cardEntriesTable.Rows.Count; i++) //Строка
            {
                int idtype = int.Parse(cardEntriesTable.Rows[i][2].ToString());
                string nameofline = cardEntriesTable.Rows[i][4].ToString();
                string content = cardEntriesTable.Rows[i][5].ToString();
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
        }


        private void LeftButtonMenuClick(object sender, RoutedEventArgs e)
        {
            int idgroup = int.Parse(((Button)sender).Tag.ToString());

            SQL.SQLConnect();
            ShowCenter(idgroup);
            SQL.Close();
        }

        private void CenterButtonMenuClick(object sender, RoutedEventArgs e)
        {
            int idcard = int.Parse(((Button)sender).Tag.ToString());

            SQL.SQLConnect();
            ShowRight(idcard);
            SQL.Close();
        }

        private void btnAllGroup_Click(object sender, RoutedEventArgs e)
        {
            SQL.SQLConnect();
            ShowCenter();
            SQL.Close();
        }

        private void btnAddGroup_Click(object sender, RoutedEventArgs e)
        {
            var win = new ShowInputDialog("Введите название группы:");
            win.Owner = this;
            win.ShowDialog();
            if (!String.IsNullOrEmpty(win.result))
            {
                string sql = String.Format($"INSERT INTO группы (наименование) values ('{win.result}')");
                SQL.SQLConnect();
                SQL.Execute(sql);
                ShowLeft();
                SQL.Close();
            }
        }

        private void btnAddCard_Click(object sender, RoutedEventArgs e)
        {
            var win = new AddCard();
            win.Owner = this;
            win.ShowDialog();
            string result = win.result;
            string result2 = win.result2;

            if (!String.IsNullOrEmpty(win.result))
            {
                string sql = String.Format(
$@"INSERT INTO картотека(наименование, идгруппы) values ('{result2}', '{result}')
DECLARE @lastid INT set @lastid = @@identity
INSERT INTO запись(идсортиовки, идполя, идкарты, Название, содержание) values (1, 1, @lastid, 'Логин', '')
INSERT INTO запись(идсортиовки, идполя, идкарты, Название, содержание) values (2, 2, @lastid, 'Пароль', '')
INSERT INTO запись(идсортиовки, идполя, идкарты, Название, содержание) values (3, 3, @lastid, 'Сайт', '')");

                string sql2 = String.Format($"select max(идкарты) from картотека");

                SQL.SQLConnect();

                SQL.Execute(sql);
                DataTable dt = SQL.Inquiry(sql2);
                ShowCenter(int.Parse(result));
                ShowRight(int.Parse(dt.Rows[0][0].ToString()));
                SQL.Close();
            }
        }



        #region CONTEXT MENU
        private int selectedtypeitem;
        private int selectedid;
        private string selectedname;

        private void ShowContextMenu(UIElement element)
        {
            ContextMenu cm = this.FindResource("cmLeftButton") as ContextMenu;
            cm.PlacementTarget = element;
            cm.IsOpen = true;
        }
        private async void LeftButton_MouseRightButtonDown(object sender, MouseButtonEventArgs e)
        {
            selectedtypeitem = 1;
            selectedid = int.Parse(((Button)sender).Tag.ToString());
            selectedname = ((Button)sender).Content.ToString();

            await Task.Delay(100);
            ShowContextMenu(sender as Button);
            
        }
        private async void Button_MouseRightButtonDown(object sender, MouseButtonEventArgs e)
        {
            selectedtypeitem = 2;
            selectedid = int.Parse(((Button)sender).Tag.ToString());
            selectedname = centerList.Find(x => x.id == selectedid.ToString()).nameofcard;

            await Task.Delay(100);
            ShowContextMenu(sender as Button);
        }


        private void RenameItem_Click(object sender, RoutedEventArgs e)
        {
            ShowInputDialog win;

            if (selectedtypeitem == 1)
            {
                win = new ShowInputDialog($"Имя группы:", selectedname);
                win.Owner = this;
                win.ShowDialog();
                string result = win.result;
                if (String.IsNullOrEmpty(result))
                {
                    return;
                }

                if (result.Trim() != selectedname)
                {
                    string sql = String.Format($"UPDATE группы SET наименование = '{result.Trim()}' where идгруппы = {selectedid}");
                    SQL.SQLConnect();
                    SQL.Execute(sql);
                    ShowLeft();
                    SQL.Close();
                }

            }
            else
            {
                //win = new ShowDialog($"");
                //win.Owner = this;
                //win.ShowDialog();
            }
        }


        private void DeleteItem_Click(object sender, RoutedEventArgs e)
        {
            ShowDialog win;

            if (selectedtypeitem == 1)
            {
                win = new ShowDialog($"Удалить группу '{selectedname}'");
                win.Owner = this;
                win.ShowDialog();
                if (win.result)
                {
                    string sql = String.Format($"DELETE FROM группы where группы.идгруппы = {selectedid}");
                    SQL.SQLConnect();
                    SQL.Execute(sql);
                    ShowLeft();
                    if (LAST_ID_GROUP == selectedid)
                    {
                        ShowCenter();
                        ShowRight();
                    }
                    SQL.Close();
                }
                
            }
            else
            {
                win = new ShowDialog($"Удалить карту '{selectedname}'");
                win.Owner = this;
                win.ShowDialog();
                if (win.result)
                {
                    string sql = String.Format($"DELETE FROM картотека where картотека.идкарты = {selectedid}");
                    SQL.SQLConnect();
                    SQL.Execute(sql);
                    ShowCenter(LAST_ID_GROUP);
                    if (LAST_ID_CARD == selectedid)
                    {
                        if (centerList.Count - 1 < 0)
                        {
                            ShowCenter();
                            ShowRight();
                        }
                        else
                        {
                            ShowRight(int.Parse(centerList[centerList.Count - 1].id.ToString()));
                        }
                    }
                    SQL.Close();
                }
            }


        }
        #endregion


        #region HELPERS
        private void CommentTextBox_TextChanged(object sender, TextChangedEventArgs e) // Поиск по центру
        {
            CollectionViewSource.GetDefaultView(ViewCenterMenu.ItemsSource).Refresh();
        }
        private bool UserFilter(object item) // Поиск по центру
        {
            if (String.IsNullOrEmpty(CommentTextBox.Text))
                return true;
            else
                return ((item as resourcesforcenter).nameofcard.IndexOf(CommentTextBox.Text, StringComparison.OrdinalIgnoreCase) >= 0);
        }

        private void TextBox_SelectionChanged(object sender, RoutedEventArgs e) // Для НЕ выделения TextBox
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


        public void Drag_Win(Window sender, double x, double y) // Размещение окна
        {
            sender.Left = x;
            sender.Top = y;
        }


        private void TopMenu_MouseDown(object sender, MouseButtonEventArgs e)
        {
            if (e.ChangedButton == MouseButton.Left)
            {
                this.DragMove();
            }
        }


        private void BtnMinimizedWindow_Click(object sender, RoutedEventArgs e)
        {
            this.WindowState = WindowState.Minimized;
        }

        private void BtnMaximizedWindow_Click(object sender, RoutedEventArgs e)
        {
            if (this.WindowState == WindowState.Maximized)
            {
                this.WindowState = WindowState.Normal;
            }
            else
            {
                this.WindowState = WindowState.Maximized;
            }
        }

        private void BtnCloseWindow_Click(object sender, RoutedEventArgs e)
        {
            this.Close();
        }
        #endregion

    }


}
