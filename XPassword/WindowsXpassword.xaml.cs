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

namespace XPassword
{
    /// <summary>
    /// Логика взаимодействия для WindowsXpassword.xaml
    /// </summary>
    public partial class WindowsXpassword : Window
    {
        bool leftMenuShowed = true;
        bool animationIsTrue = false;
        public WindowsXpassword()
        {
            InitializeComponent();
        }

        private void Button_Click(object sender, RoutedEventArgs e)
        {
            if (!animationIsTrue) 
                animation();
        }

        async void animation()
        {
            int widthStart = leftMenuShowed ? 140 : 50;
            int widthStop = leftMenuShowed ? 50 : 140;
            int unit = leftMenuShowed ? -10 : 10;
            animationIsTrue = true;


            do
            {
                await Task.Delay(5);
                widthStart += unit;
                leftmenu.Width = widthStart;

            } while (widthStart != widthStop);

            leftMenuShowed = !leftMenuShowed;
            animationIsTrue = false;

        }

        private void ListBoxItem_Selected(object sender, RoutedEventArgs e)
        {

        }
    }
}
