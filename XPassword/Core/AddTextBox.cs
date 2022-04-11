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
    class AddTextBox: IContentOfCard
    {
        public AddTextBox(WindowXpassword _windowsender, string hinttext, string text)
        {
            windowsender = _windowsender;
            MainOutputStackPanel = (StackPanel)windowsender.FindName("MainOutputStackPanel");
            add(hinttext, text);
        }

        private WindowXpassword windowsender;
        private StackPanel MainOutputStackPanel;
        string text;
        TextBox uielement;

        public void add(string _text, string hinttext)
        {
            text = _text;
            Style style = (Style)windowsender.FindResource("TextBoxNotChangable");

            uielement = new TextBox()
            {
                Text = _text,
                Padding = new Thickness(0)
        };
            uielement.Style = style;
            uielement.MouseDoubleClick += CopyTextToClipboard;
            HintAssist.SetHint(uielement, hinttext);
            MainOutputStackPanel.Children.Add(uielement);
        }

        private void CopyTextToClipboard(object sender, RoutedEventArgs e)
        {
            Clipboard.SetData(DataFormats.Text, (Object)text);
            WindowXpassword.ShowInfoFromCopy();
        }

        
    }
}
