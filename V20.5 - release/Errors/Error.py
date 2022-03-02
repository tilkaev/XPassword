from tkinter import Tk, messagebox

def log_uncaught_exceptions(ex_cls, ex, tb):
    text = '{}: {}:\n'.format(ex_cls.__name__, ex)
    import traceback
    text += ''.join(traceback.format_tb(tb))
    print(text)
    if messagebox.askyesno("Неизвестная ошибка", "Сохранить лог с ошибкой?") == True:
        with open('error.txt', 'w', encoding='utf-8') as f:
            f.write(text)
    raise SystemExit


import sys
sys.excepthook = log_uncaught_exceptions

root = Tk()

def m_geometry(win):
    #x = (win.winfo_screenwidth() / 2) - (295 / 2)
    y = (win.winfo_screenheight() / 2) - (395 / 2)
    root.wm_geometry("+%d+%d" % (x, y))

root.after(2000, lambda: m_geometry(root))

root.mainloop()