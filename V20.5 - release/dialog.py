# dialog.py -- Tkinter interface to the tk_dialog script.

from tkinter import *
from tkinter import _cnfmerge

DIALOG_ICON = 'questhead'


class Dialog(Widget):
    def __init__(self, master=None, cnf={}, **kw):
        cnf = _cnfmerge((cnf, kw))
        self.widgetName = '__dialog__'
        Widget._setup(self, master, cnf)
        self.num = self.tk.getint(
                self.tk.call(
                      'tk_dialog', self._w,
                      cnf['title'], cnf['text'],
                      cnf['bitmap'], cnf['default'],
                      *cnf['strings']))
        try: Widget.destroy(self);
        except TclError: pass
    def destroy(self): pass

def open(title, text, string):
    d = Dialog(None, {'title': str(title),
                      'text': str(text),
                      'bitmap': DIALOG_ICON,
                      'default': 0,
                      'strings': string})
    return d.num

if __name__ == '__main__':
    root = Tk()
    open("Ошибка","Файл: {1} не найден",("Создать","Отрыть","Отмена"))

    root.mainloop()