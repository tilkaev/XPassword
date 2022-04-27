﻿using SpaceBaseApp.Core;
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
using System.Windows.Navigation;
using System.Windows.Shapes;

namespace XPassword
{
    /// <summary>
    /// Логика взаимодействия для MainWindow.xaml
    /// </summary>
    public partial class LoginWindow : Window
    {

        public LoginWindow()
        {
            InitializeComponent();
            //TextBoxOutputGeneratedPassword.Text = "";
            passwordBox.Password = "admin";

        }

        private void MoveWindow(object sender, MouseButtonEventArgs e)
        {
            if (e.ChangedButton == MouseButton.Left)
            {
                this.DragMove();
            }
        }

        public void Show_Win(Window win, double x = 0, double y = 0) // Создание окна закрытие старого
        {
            double cor_width = 0;
            if (this.Width < win.Width)
            { cor_width = win.Width / 4; }

            this.Visibility = System.Windows.Visibility.Collapsed;
            Drag_Win(win, Left - cor_width - x, Top - y);
            win.Closed += (sender2, e2) =>
            {
                passwordBox.Password = "";

                Drag_Win(this, win.Left + cor_width + x, win.Top + y);

                this.Visibility = System.Windows.Visibility.Visible;
            };
            win.ShowDialog();
        }

        public void Drag_Win(Window sender, double x, double y) // Размещение окна
        {
            sender.Left = x;
            sender.Top = y;

        }
        private void btnLogin_Click(object sender, RoutedEventArgs e)
        {
            string password = passwordBox.Password;

            if (password is "")
            {
                MessageBox.Show("Введите пароль!");
                return;
            }

            string sql = String.Format($"select * from auth where password collate Latin1_General_CS_AS like '{password}'");
            SQL.SQLConnect();
            DataTable dt = SQL.Inquiry(sql);
            SQL.Close();

            if (dt.Rows.Count != 0)
            {
                Show_Win(new WindowXpassword());
            }
            else
            {
                MessageBox.Show("Неверный пароль!");
            }

        }

        private void btnExit_Click(object sender, RoutedEventArgs e)
        {
            this.Close();
        }

        
    }
}
