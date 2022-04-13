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

    class AddWebTextBox : IContentOfCard
    {
        public AddWebTextBox(WindowXpassword _windowsender, string hinttext, string text)
        {
            windowsender = _windowsender;
            MainOutputStackPanel = (StackPanel)windowsender.FindName("MainOutputStackPanel");
            add(hinttext, text);
        }

        private WindowXpassword windowsender;
        private StackPanel MainOutputStackPanel;
        TextBox uielement;
        String text;
        Grid grid;

        public UIElement getuielement() { return grid; }

        private static bool IsValidUri(string uri)
        {
            if (!Uri.IsWellFormedUriString(uri, UriKind.Absolute))
                return false;
            Uri tmp;
            if (!Uri.TryCreate(uri, UriKind.Absolute, out tmp))
                return false;
            return tmp.Scheme == Uri.UriSchemeHttp || tmp.Scheme == Uri.UriSchemeHttps;
        }

        private bool OpenUri(string uri)
        {
            if (!IsValidUri(uri))
                uri = "http://" + uri;
            System.Diagnostics.Process.Start(uri);
            return true;
        }

        private void ManagerForOpenWeb(object sender, RoutedEventArgs e)
        {
            OpenUri(text);
        }

        private void CopyWebToClipboard(object sender, RoutedEventArgs e)
        {
            Clipboard.SetData(DataFormats.Text, (Object)text);
            WindowXpassword.ShowInfoFromCopy();
        }


        public void add(string text, string hinttext)
        {
            this.text = text;
            Style style = (Style)windowsender.FindResource("TextBoxNotChangable");
            ControlTemplate template2 = (ControlTemplate)windowsender.FindResource("BtnWeb");


            grid = new Grid();

            var padding = new Thickness(0);
            padding.Right = 30;
            uielement = new TextBox()
            {
                Text = text,
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
            btneye.Click += ManagerForOpenWeb;
            MainOutputStackPanel.Children.Add(grid);

            uielement.MouseDoubleClick += CopyWebToClipboard;
        }
    }
}
