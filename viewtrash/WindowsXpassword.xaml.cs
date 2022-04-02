using System;
using System.Collections.Generic;
using System.Collections.ObjectModel;
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
    public class Phone
    {
        public int Id { get; set; }
        public string Title { get; set; } // модель телефона
        public string Company { get; set; } // производитель
        public string ImagePath { get; set; } // путь к изображению
    }



    public partial class WindowsXpassword : Window
    {
        bool leftMenuShowed = true;
        bool animationIsTrue = false;
        public WindowsXpassword()
        {
            InitializeComponent();
            var Phones = new ObservableCollection<Phone>
        {
            new Phone {Id=1, ImagePath="/Images/iphone6s.jpg", Title="iPhone 6S", Company="Apple" },
            new Phone {Id=2, ImagePath="/Images/lumia950.jpg", Title="Lumia 950", Company="Microsoft" },
            new Phone {Id=3, ImagePath="/Images/nexus5x.jpg", Title="Nexus 5X", Company="Google" },
            new Phone {Id=4, ImagePath="/Images/galaxys6.jpg", Title="Galaxy S6", Company="Samsung"}
        };
            phonesList.ItemsSource = Phones;
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