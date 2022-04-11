using MaterialDesignThemes.Wpf;
using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows;
using System.Windows.Controls;

namespace XPassword.Core
{

    class AddPasswordBox : IContentOfCard
    {
        public AddPasswordBox(WindowXpassword _windowsender, string hinttext, string text)
        {
            windowsender = _windowsender;
            MainOutputStackPanel = (StackPanel)windowsender.FindName("MainOutputStackPanel");
            add(hinttext, text);
        }

        private WindowXpassword windowsender;
        private StackPanel MainOutputStackPanel;
        TextBox uielement;
        String text;
        bool show = false;

        private void ManagerForShowHidenPassword(object sender, RoutedEventArgs e)
        {
            show = !show;
            if (show)
            {
                uielement.Text = text;
            }
            else
            {
                uielement.Text = new String('*', text.Length);
            }
        }

        private void CopyPasswordToClipboard(object sender, RoutedEventArgs e)
        {
            Clipboard.SetData(DataFormats.Text, (Object)text);
            WindowXpassword.ShowInfoFromCopy();
        }


        public void add(string text, string hinttext)
        {
            this.text = text;
            Style style = (Style)windowsender.FindResource("TextBoxNotChangable");
            ControlTemplate template2 = (ControlTemplate)windowsender.FindResource("BtnEye");


            var grid = new Grid();

            var padding = new Thickness(0);
            padding.Right = 30;
            uielement = new TextBox()
            {
                Text = new String('*', text.Length),
                Style = style,
                Padding = padding
            };
            HintAssist.SetHint(uielement, hinttext);
            grid.Children.Add(uielement);

            var btneye = new Button()
            {
                Content = new String('*', text.Length),
                Template = template2
            };
            grid.Children.Add(btneye);
            btneye.Click += ManagerForShowHidenPassword;
            MainOutputStackPanel.Children.Add(grid);

            uielement.MouseDoubleClick += CopyPasswordToClipboard;
            //((Button)uielement.FindName("BtnEye")).Click += ManagerForShowHidenPassword;
            //var myTextBlock = (Button)uielement.FindName("BtnEye");
            //myTextBlock.Content = 12;

            //var template = MyList.Template;
            //var myControl = (MyControl)template.FindName("MyControlName", MyList);



        }
    }
}
