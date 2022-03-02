#++Modules==============================================================================================================
from tkinter import Listbox, RIGHT, BOTH, LEFT, NORMAL, Tk, Frame, Label, SEL, RIDGE, Button, messagebox, Entry, Text, \
    PhotoImage, Canvas, StringVar, TclError, Checkbutton, Spinbox, END, Scrollbar, Menu, mainloop, Toplevel, W, FLAT, \
    GROOVE, DISABLED, ACTIVE, INSERT, SUNKEN, RAISED
#from tkinter import tkFileDialog
from tkinter.filedialog import askopenfile, asksaveasfile
from random import choice
import os
import webbrowser
import time

import simpledialog as simpl
import dialog as dialog

import pyAesCrypt
from os import remove
from os.path import splitext
import pyautogui as pgui
#=======================================================================================================================




#$%$%$%$%$%$%$%$%$%$%$%$%$%$%$%$%$%$%$%$%$%$%$%$%$%$%$
def enter_password():
    def start():
        global password_d_e
        password_d_e = "1242"
        try: create()
        except: return
    root.after(700, lambda: start())
#$%$%$%$%$%$%$%$%$%$%$%$%$%$%$%$%$%$%$%$%$%$%$%$%$%$%$




#==Create root window===================================================================================================
import sys
root = Tk()
root.wm_attributes("-alpha",0)
#sys.excepthook = log_uncaught_exceptions
#root.report_callback_exception = log_uncaught_exceptions

root.geometry("295x395")
root.resizable(width=False, height=False)  # sd
root.title("XPassword")
root.event_add('<<Paste>>', '<Control-igrave>')
root.event_add("<<Copy>>", "<Control-ntilde>")
root.event_add("<<Cut>>", "<Control-division>")
#root.iconbitmap('NewIcon.ico')
#root.after(1000, lambda: enter_password())
def run_root():
    h = root.winfo_height()
    w = root.winfo_width()
    scrh = root.winfo_screenheight()
    scrw = root.winfo_screenwidth()
    root.deiconify()
    root.wm_geometry("+%d+%d" % (scrw / 2 - (w / 2) - 10, scrh / 2 - (h / 2 + 40)))
    root.after(1000, lambda: effect_run(root, 350))
    root.after(300, lambda: root.wm_geometry("+%d+%d" % (scrw / 2 - (w / 2) - 10, scrh / 2 - (h / 2 + 40))))
root.after(400, run_root)
#=======================================================================================================================





#+++Values==============================================================================================================
file_d = os.getcwd() + "\\XPassword.pfc"
file_e = os.getcwd() + "\\XPassword.pf"

#===========================================================
passw = ""

return_ico = PhotoImage(file="./data/ico/return.ico")
delete_icon = PhotoImage(file="./data/ico/redx.png")
edit_ico = PhotoImage(file="./data/ico/edit_icon.ico")
edit_ico2 = PhotoImage(file="./data/ico/save_button_icon2.ico")
rename_ico = PhotoImage(file="./data/ico/edit.ico")
eye_open = PhotoImage(file="./data/ico/eye_open2.ico")
eye_close = PhotoImage(file="./data/ico/eye_close2.ico")
base_ico = PhotoImage(file="./data/ico/base.ico")
browser_ico = PhotoImage(file="./data/ico/browser.ico")

check_mark_ico = PhotoImage(file="./data/ico/check_mark.ico")
check_delete_ico = PhotoImage(file="./data/ico/redx.ico")
open_widnow_ico = PhotoImage(file="./data/ico/window.ico")
close_window_ico = PhotoImage(file="./data/ico/window2.ico")
add_ico = PhotoImage(file="./data/ico/add.ico")
cancel_ico = PhotoImage(file="./data/ico/cancel_icon.ico")
copy_ico1 = PhotoImage(file="./data/ico/copy_ico.ico") #"./data/ico/copy_icon.ico"
copy_ico2 = PhotoImage(file="./data/ico/check_mark.ico") #"./data/ico/check_mark_icon.ico"
test_ico = PhotoImage(file="./data/ico/TEST2.ico")

cancel_ico_stbl = PhotoImage(file="./data/ico/close_stabl.ico")
cancel_ico_disstbl = PhotoImage(file="./data/ico/close_distbl.ico")

up_ico = PhotoImage(file="./data/ico/up.ico")
down_ico = PhotoImage(file="./data/ico/down.ico")
#===========================================================


#=======================================================================================================================






#++Classes==============================================================================================================
class CreateToolTip(object):
    def __init__(self, widget, text='widget info', param=True):
        self.waittime = 700  # miliseconds
        self.wraplength = 180  # pixels
        self.widget = widget
        self.text = text
        if param == True:
            self.widget.bind("<Enter>", self.enter)
            self.widget.bind("<Leave>", self.leave)
            self.widget.bind("<ButtonPress>", self.leave)
        self.id = None
        self.tw = None

    def enter(self, event=None):
        self.schedule()

    def leave(self, event=None):
        self.unschedule()
        self.hidetip()

    def schedule(self):
        self.unschedule()
        self.id = self.widget.after(self.waittime, self.showtip)

    def unschedule(self):
        id = self.id
        self.id = None
        if id:
            self.widget.after_cancel(id)

    def showtip(self, event=None):
        x = y = 0
        x, y, cx, cy = self.widget.bbox("insert")
        x += root.winfo_pointerx()
        y += root.winfo_pointery() + 20
        # print(x,y)
        # creates a toplevel window
        self.tw = Toplevel(self.widget)
        self.tw.wm_attributes("-topmost", 1)
        # Leaves only the label and removes the app window
        self.tw.wm_overrideredirect(True)
        self.tw.wm_geometry("+%d+%d" % (x, y))
        label = Label(self.tw, text=self.text, font=("Calibri", 10), justify='left',
                      background="white", relief=GROOVE, borderwidth=1,
                      wraplength=self.wraplength)
        label.pack(ipadx=1)
        effect_run(self.tw, 150)

    def hidetip(self):
        tw = self.tw
        self.tw = None
        if tw:
            tw.destroy()

    def remap_text(self, text):
        self.text = text


class Main_list_box():
    def __init__(self):
        self.menu = Menu(tearoff=0)

        def start_root2(event=None):
            self = list_all
            self._do_ = None
            self.close_tops()
            root.after(200, lambda: self.open_tops(event))

        self.menu.add_command(label="Открыть", command=lambda: start_root2())
        self.menu.add_command(label="Изменить", command=lambda: start_root2(False) or root.after(1000, lambda: list_all.edit_()))  #
        self.menu.add_command(label="Переименовать", command=lambda: list_all.rename())
        self.menu.add_separator()
        self.menu.add_command(label="Открыть ссылку", command=self.open_brws)
        self.menu.add_command(label="Удалить", command=lambda: list_all.get_val() or list_all.delete_list())
        list_all._list_.bind("<Button-3>", self.func)

    def open_brws(self):
        text = text_second[list_all._list_.curselection()[0]][0]
        if text == "0": webbrowser.open('https://'); return
        else: list_all.start_brows(text); return

    def func(self, event):
        pgui.click()
        root.after(100, lambda: self.menu.post(event.x_root, event.y_root))


class Main():
    def __init__(self):
        super().__init__()
        self.menu = Menu(tearoff=0)
        self.menu.add_command(label="Вырезать", accelerator="Ctrl+X", command=lambda: self.w.focus_force() or self.w.event_generate("<<Cut>>"))
        self.menu.add_command(label="Копировать", accelerator="Ctrl+С", command=lambda: self.w.focus_force() or self.w.event_generate("<<Copy>>"))
        self.menu.add_command(label="Вставить", accelerator="Ctrl+V", command=lambda: self.w.focus_force() or self.w.event_generate("<<Paste>>"))
        self.menu.add_command(label="Удалить", accelerator="Delete", command=lambda: self.w.focus_force() or self.w.event_generate("<<Clear>>"))
        self.menu.add_separator()
        self.menu.add_command(label="Очистить поле", command=lambda: self.w.focus_force() or self.w.event_generate("<<SelectAll>>") or self.w.event_generate("<<Clear>>"))
        self.menu.add_command(label="Выделить все", accelerator="Ctrl+A", command=lambda: self.w.focus_force() or self.w.event_generate("<<SelectAll>>"))
        text1.bind("<Button-3>", self.func)
        root.bind_class("Entry", "<Button-3><ButtonRelease-3>", self.func)
        root.bind_class("Spinbox", "<Button-3><ButtonRelease-3>", self.func)


    def func(self, event):
        pgui.click()
        def func2():
            self.menu.post(event.x_root, event.y_root)
            self.w = event.widget
        root.after(50, lambda: func2())


####
class effect_run():
    def __init__(self, window, time=350):
        self.window = window
        self.time = time
        self.persent = 0
        self.try_run()

    def try_run(self):
        try:
            if str(self.persent)[0:3] == "1.0": root.after(5000, self.destroy); return
            self.window.wm_attributes("-alpha", self.persent)
            self.persent += 0.1
            root.after(int(self.time/10), lambda: self.try_run())
        except: pass

    def destroy(self):
        del self

class effect_close():
    def __init__(self, window, time=150, param=True):
        self.window = window
        self.time = time
        self.persent = 11
        self.list = ["STOP", 0, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]
        self.param = param
        self.try_close()

    def try_close(self):
        try:
            #print(self.window, self.list[self.persent])
            if self.list[self.persent] == "STOP":
                root.after(1000, self.destroy)
                if self.param == True: self.window.destroy(); return
                if self.param == "ROOT.CLOSE": class_prev.close()
                if self.param == "ROOT.WITHDRAW": self.window.withdraw()
                if self.param == "ROOT": exit(); return
                return
            #print(self.window, self.list[self.persent])
            self.window.wm_attributes("-alpha", self.list[self.persent])
            self.persent -= 1
            root.after(int(self.time/10), lambda: self.try_close())
        except: pass

    def destroy(self):
        del self
#####


class magnet_win():
    def __init__(self):
        self.bind()

    def drag_win(self):
        self.x = 0
        self.y = 0
        root.after(100, lambda: root.wm_geometry("+%d+%d" % (root.winfo_x(), root.winfo_y())))

    def remap_x_y(self, event):
        if event.widget != root: return
        self.drag_win()

    def bind(self):
        self.block = True
        self.Up = False
        self.Down = False
        self.x = root.winfo_x()
        self.y = root.winfo_y()

        root.bind("<Map>", self.remap_x_y)
        root.bind("<Configure>", lambda event: self.replace_win())

    def unbind(self):
        root.focus_set()
        root.unbind("<Configure>")

    def replace_win(self):
        x = root.winfo_x()
        y = root.winfo_y()
        if y == self.y and x == self.x: return
        self.x = root.winfo_x()
        self.y = root.winfo_y()

        if self.block == False: return

        def StopHam_Left(self):
            x = root.winfo_x()
            y = root.winfo_y()
            self.block = False
            root.wm_geometry("+%d+%d" % (x+5, y))
            if x > 6: self.block = True; return
            else: root.after(10, lambda: StopHam_Left(self))

        def StopHam_Right(self):
            x = root.winfo_x()
            y = root.winfo_y()
            self.block = False
            root.wm_geometry("+%d+%d" % (x - 5, y))
            if root.winfo_screenwidth()-root.winfo_width()-15 > x: self.block = True; return
            else: root.after(10, lambda: StopHam_Right(self))

        def StopHam_Down(self):
            x = root.winfo_x()
            y = root.winfo_y()
            self.block = False
            root.wm_geometry("+%d+%d" % (x, y-5))
            if root.winfo_screenheight()-root.winfo_height()/3 > y: self.block = True; return
            else: root.after(10, lambda: StopHam_Down(self))

        if x < 5:
            self.block = False
            StopHam_Left(self)

        if root.winfo_screenwidth()-root.winfo_width()-20 < x:
            self.block = False
            StopHam_Right(self)

        if root.winfo_screenheight()-root.winfo_height()/3 < y:
            self.block = False
            StopHam_Down(self)

        try: root2.geometry(str(root2.winfo_width())+"x"+str(root2.winfo_height()))
        except: return

        def Stop_Ham_Up(self):
            x = root.winfo_x()
            y = root.winfo_y()
            root.wm_geometry("+%d+%d" % (x, y + 5))
            if y > 120: self.block = True; return
            else: root.after(10, lambda: Stop_Ham_Up(self))

        try:
            list_all.tops.geometry(str(list_all.tops.winfo_width())+"x"+str(list_all.tops.winfo_height()))
            if y <= 88:
                #pgui.press("enter")
                self.block = False
                root.after(100, lambda: Stop_Ham_Up(self))

        except: pass

        try: list_all.tops.deiconify()
        except: pass
        finally: root2.deiconify()

        if (root.winfo_rootx() - 230) < 0: root2.wm_geometry("+%d+%d" % (x + 300+20, y))
        else: root2.wm_geometry("+%d+%d" % (x - 220-20, y))


        try:
            if (root.winfo_rootx() - 230) < 0: list_all.tops.wm_geometry("+%d+%d" % (x, y-86))
            else: list_all.tops.wm_geometry("+%d+%d" % (x - 222-18, y-86-10))
            #print(list_all.tops.winfo_height())
        except: pass
#=======================================================================================================================
magnit = magnet_win()




#==OC debug tools=======================================================================================================
oc_debug_value = 0
def log_uncaught_exceptions(ex_cls, ex, tb):
    global oc_debug_value
    text = '{}: {}:\n'.format(ex_cls.__name__, ex)
    import traceback
    text += ''.join(traceback.format_tb(tb))
    oc_debug_value+=1
    print(oc_debug_value)
    if oc_debug_value == 1:
        text = "{}{}\nTime: {} \n {}".format("\n"+"_"*200+"\n","_"*200, time.ctime(), text)
    else: text = "\nTime: {}\n{}".format(time.ctime(),text)
    print(text)

    if messagebox.askyesno("Неизвестная ошибка", "Сохранить лог с ошибкой?") == True:
        if os.path.isfile("./error.log") == True:
            with open("./error.log", "r", encoding='utf-8') as file:
                text = str(file.read())+str(text)
        with open('error.log', 'w', encoding='utf-8') as f:
            f.write(text)
#=======================================================================================================================





def first_start():
    if os.path.isfile(os.getcwd() + "\XPassword.pfc") != True:
        button2.configure(text="Создать базу", command=lambda: create_base(True))

def restart_prog():
    if os.path.isfile(os.getcwd() + "\\" + "XPassword.exe"): os.startfile(os.getcwd() + "\\" + "XPassword.exe")
    else: os.startfile(os.getcwd() + "\\" + "passwordV20_5.pyw")
    root.destroy()
    raise SystemExit



'''
if os.path.isfile(os.getcwd() + "\\" + "PFC.exe") == True:
    x = (root.winfo_screenwidth() / 2) - (295 / 2)
    y = (root.winfo_screenheight() / 2) - (395 / 2)
    #root.wm_geometry("+%d+%d" % (x, y))
    scrh = root.winfo_screenheight()
    scrw = root.winfo_screenwidth()
else:
    h = root.winfo_height()
    w = root.winfo_width()
    scrh = root.winfo_screenheight()
    scrw = root.winfo_screenwidth()
    #root.after(1000, lambda: root.wm_geometry("+%d+%d" % (scrw / 2 - (w / 2), scrh / 2 - (h / 2 + 40))))'''

'''
tops = Toplevel()
tops.geometry(str(root.winfo_screenwidth())+"x"+str(root.winfo_screenheight()))
cane = Canvas(tops, bg="red")

#cane.create_line(-4,-1,root.winfo_screenwidth()+2,root.winfo_screenheight()+2)
#cane.create_line(root.winfo_screenwidth()+4,0,-3,root.winfo_screenheight()+4)
cane.create_line(-4,-1,root.winfo_screenwidth()+2,root.winfo_screenheight()+2-40)
cane.create_line(root.winfo_screenwidth()+4,0,-3,root.winfo_screenheight()+4-40)

cane.create_line(0,root.winfo_screenheight()/2+2,root.winfo_screenwidth()+2, root.winfo_screenheight()/2+2)
cane.create_line(root.winfo_screenwidth()/2+2,0,root.winfo_screenwidth()/2+2,root.winfo_screenheight()+2)

cane.place(x=-2,y=-2,width=root.winfo_screenwidth()+4,height=root.winfo_screenheight()+4)
tops.wm_attributes("-alpha",0.5)
tops.wm_attributes("-fullscreen",1)
cane.bind("<Button-2>",lambda event: tops.destroy())'''

def encryptDecrypt(mode, file, password, text=''):
    bufferSize = 64 * 1024
    if mode == 'E':
        base = open(file, "w")
        base.write(str(text))
        base.close()
        try:
            pyAesCrypt.encryptFile(str(file), str(file) + "c", password, bufferSize)
            remove(file)
        except FileNotFoundError:
            return "[x] File is not found!"
        else:
            return "[+] File '" + str(file) + "' overwritten!"
    else:
        try:
            print("password:",password)
            pyAesCrypt.decryptFile(str(file), str(file[0:-4]) + ".txt", password, bufferSize)
            # remove(file)
        except FileNotFoundError:
            return "[x] File is not found!"
        except IOError:
            return "[x] Password is False!"
        else:
            print("[+] File '" + str(splitext(file)[0]) + ".pfc' overwritten!")
            text = open(str(file[0:-4]) + ".txt", "r")
            base = text.read()
            text.close()
            return base, str(str(splitext(file)[0]) + ".txt")


#==Generation password==================================================================================================
def create_password(event):
    global x, x, v0, v1, v2, v3, copy1
    v0 = str(var0.get())
    v1 = str(var1.get())
    v3 = str(var2.get())
    v2 = str(var3.get())
    x = entry1.get()
    copy1 = str(var4.get())

    try:
        x = int(x) - 1
        passw = ""
    except:
        messagebox.showerror("Ошибка!", "Ввод веден не корректно!")
        return

    if x > 999:
        messagebox.showerror("Ошибка!", "Максимальное число 1000")
        return
    if x < -1:
        messagebox.showerror("Ошибка!", "Длина не может быть меньше нуля!")
        return
    if x == -1:
        messagebox.showerror("Ошибка!", "Длина не может нулем!")
        return

    lt1 = [chr(int(x+97)) for x in range(26)] #["q", "w", "e", "r", "t", "y", "u", "i", "o", "p", "a", "s", "d", "f", "g", "h", "j", "k", "l", "z", "x", "c", "v", "b", "n", "m"]
    lt2 = [chr(int(x+65)) for x in range(26)] #["Q", "W", "E", "R", "T", "Y", "U", "I", "O", "P", "A", "S", "D", "F", "G", "H", "J", "K", "L", "Z", "X", "C", "V", "B", "N", "M"]
    lt3 = [x for x in range(10)] #["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
    lt4 = ["`", "!", "@", "#", "$", "%", "^", "&", "*", "(", ")", "_", "-", "=", "+", "[", "]", "{", "}", "/", "|", ";",
           ":", "'", ",", ".", "<", ">", "?"]

    if v0 == "0":
        if v1 == "0":
            if v2 == "0":
                if v3 == "0":
                    messagebox.showerror("Ошибка!", "Выберите из чего \nсоздать пароль"); return

    choices = []
    if v0 == "1":
        for lst in lt3:
            choices.append(str(lst))
    if v1 == "1":
        for lst in lt2:
            choices.append(lst)
    if v2 == "1":
        for lst in lt1:
            choices.append(lst)
    if v3 == "1":
        for lst in lt4:
            choices.append(lst)

    while len(passw) <= int(x):
        passw += choice(choices)

    if copy1 == "1":
        root.clipboard_clear()
        root.clipboard_append(passw)
    text1.delete("1.0", END)
    text1.insert("1.0", passw)
#=======================================================================================================================


def return_adress(adress):
    if len(adress.split("/")) != len(adress): adress = str(adress).replace("/", "\\")
    fail = open("./data/base/base.dll", "w")
    fail.writelines(adress)
    fail.close()

def start_win(adress, fp=False):
    global file_d, file_e, password_d_e
    print("\nStart: {}".format(adress))

    try: close_win_()
    except: pass

    if os.path.isfile(os.getcwd() + "\\start.txt") == True:
        with open(os.getcwd() + "\\start.txt") as file:
            if file.read() == "1": param_start = True
            else: param_start = None
        if fp == True:
            with open(os.getcwd() + "\\start.txt", 'w') as file: file.write('1')
    else:
        with open(os.getcwd() + "\\start.txt", 'w') as file:
            file.write('0');
            param_start = None

    print('Параметр:', param_start, fp)
    if fp == True: return

    if param_start == None: create_base()

    if os.path.isfile(adress) == False:
        if param_start != None: messagebox.showerror("Ошибка", 'База XPassword.pfc не найдена или повреждена\n\nПрограмма будет закрыта'); root.destroy(); raise SystemExit

    if param_start == True:
        with open(adress, mode="rb") as file:
            text = file.read()[0:3].decode('utf-8')
            file.close()
            if text != "AES":
                print("AES Error")
                # messagebox.askokcancel("Ошибка с файлом XPassword", "Файл: {} не может быть прочитан, так как он был поврежден или не является файлом программы".format(adress.split("\\")[-1]))
                messagebox.showerror("Ошибка",
                                     'База XPassword.pfc не найдена или повреждена\n\nПрограмма будет закрыта');
                root.destroy();
                raise SystemExit

        def check_passw():
            global password_d_e
            password_d_e = simpl.askstring(str(adress.split("\\")[-1]), "Введите пароль:", "*")
            if password_d_e == None: password_d_e = None; return False
            try:
                create(); return False
            except:
                messagebox.showerror(adress.split("\\")[-1], "Пароль введен не верно!"); button2["state"]=NORMAL

        if check_passw() == False: return
        if check_passw() == False: return
        if check_passw() == False: return
        messagebox.showerror("Ошибка", "Введен был 3 раза не правильно,\nПовторите еще раз позже!")



def create_base():
    global password_d_e, chek_password, file_d, file_e
    try: close_win_()
    except: pass

    adress = os.getcwd() + "\\XPassword.pf"

    def create_new_base():
        check_win = Toplevel()
        check_win.title("")
        check_win.geometry("180x140")
        check_win.geometry("+%d+%d" % (root.winfo_rootx() + (check_win.winfo_width() + root.winfo_width()) / 6, root.winfo_rooty() + (check_win.winfo_height() + root.winfo_height()) / 6))
        check_win.resizable(False, False)
        check_win.protocol('WM_DELETE_WINDOW', lambda: cancel())
        check_win.bind("Map", lambda event: check_win.geometry("+%d+%d" % (root.winfo_rootx() + 50, root.winfo_rooty() + 50)))

        # check_win.overrideredirect(True)
        # print(root.winfo_rooty()+(check_win.winfo_height()+root.winfo_height())/6)
        # print(root.winfo_height())

        def update_root(win):
            x = win.winfo_rootx()
            y = win.winfo_rooty()
            try:
                check_win.wm_geometry("+%d+%d" % (root.winfo_rootx() + (check_win.winfo_width() + root.winfo_width()) / 10,
                                                  root.winfo_rooty() + (
                                                              check_win.winfo_height() + root.winfo_height()) / 8))
            except:
                root.unbind("<Configure>")
                root.bind("<Configure>", lambda event: magnit.bind())
        check_win.bind("<Configure>", lambda event: update_root(root))
        root.bind("<Configure>", lambda event: update_root(root))

        # check_c = Canvas(check_win, bg="blue")
        # check_c.pack(fill=BOTH, padx=5)

        def eye_win(x_eye, y_eye, parent):
            lab_eye = Label(parent, image=eye_close, bg="white", cursor='hand2')
            lab_eye.place(x=x_eye, y=y_eye, height=18)
            lab_eye.bind("<Enter>", lambda event: lab_eye.config(relief=GROOVE))
            lab_eye.bind("<Leave>", lambda event: lab_eye.config(relief=FLAT))
            lab_eye.bind("<ButtonPress>", lambda event: lab_eye.config(relief=GROOVE, image=eye_open) or parent.config(show=""))
            lab_eye.bind("<ButtonRelease>", lambda event: lab_eye.config(relief=GROOVE, image=eye_close) or parent.config(show="*"))

        Label(check_win, text="Создание базы XPassword", fg="red", anchor=W, bg="#030069").pack(fill=BOTH)

        Label(check_win, text="Введите пароль:").pack(fill=BOTH, padx=5)
        entr2 = Entry(check_win, show="*")
        entr2.pack(fill=BOTH, padx=5);
        eye_win(145, 0, entr2)
        root.after(100, lambda: entr2.focus_set())

        Label(check_win, text="Повторите пароль:").pack(fill=BOTH, padx=5)
        entr3 = Entry(check_win, show="*")
        entr3.pack(fill=BOTH, padx=5);
        eye_win(145, 0, entr3)

        def ok():
            global file_d, file_e, password_d_e
            password_1 = entr2.get()
            password_2 = entr3.get()
            if password_1 != password_2:
                messagebox.showinfo("Ошибка", "Пароли не совпадают");
                entr2.focus_set();
                entr2.event_generate("<<SelectAll>>")
                return
            else:
                check_win.unbind("<Configure>")
                check_win.destroy()

                password_d_e = password_2
                print(adress)
                file_d = str(adress + "c").replace("/", "\\")
                file_e = str(adress).replace("/", "\\")

                start_win(adress + "c", True)
                encryptDecrypt("E", adress, password_d_e, "Группа 0 0 0")
                check2()
                create()

        def cancel():
            check_win.unbind("<Configure>")
            check_win.destroy()
            # os.remove(adress)

        w = Button(check_win, text="OK", width=10, command=ok, default=ACTIVE)
        w.pack(side=LEFT, padx=5, pady=5)
        w = Button(check_win, text="Отмена", width=10, command=cancel)
        w.pack(side=RIGHT, padx=5, pady=5)

        #check_win.deiconify()
        check_win.wait_visibility();
        check_win.grab_set();
        #check_win.wait_window(root)
        check_win.transient(root)

    create_new_base()

    '''
    os_path = "./data/base/test.dll"
    if (os.path.exists("./tk/demos/images")):
        os_path = "./tk/demos/images/test.dll"



    password_d_e = param
    return_adress(adress+"c")
    file_d = str(adress+"c").replace("/","\\")
    file_e = str(adress).replace("/","\\")


    encryptDecrypt("E", adress, password_d_e, "Группа 0 0 0")
    create()

    if Do == "0":
        root.after(1500, lambda: list_all.open_tops(None, 2))
        root.after(2000, lambda: list_all.edit_())
        root.after(3000, lambda: list_all.url_entr.focus_set())

    root.title("База: "+str(file_d.split("\\")[-1][0:-4]))'''


def check2():
    global base, basa

    try: base = open(file_d, "r")
    except:
        text = open(file_e, "w")
        text.write("Группа 0 0 0")
        text.close()
        encryptDecrypt("E", file_e, password_d_e, "Группа 0 0 0")
        base = [["0", ["0", "0", "0"]]]
        return
    print('File:', file_d)
    (base, rem) = encryptDecrypt("D", file_d, password_d_e)
    #except: messagebox.showerror("Ошибка",'Не возможно работать с базой, перезапустите программу!'); return
    print(base, rem)
    test = open(rem, "r")
    basa = []
    base = []
    kor = []
    for line in test:
        if line[0] == " ": continue
        for numb, string in enumerate(line.split()):
            if numb == 0:
                base.append(string); continue
            else:
                kor.append(string)
            # print(numb%3)
            if numb % 3 == 0:
                base.append(kor)
                kor = []
                continue
        basa.append(base)
        base = []
    base = basa

    test.close()
    remove(rem)


def return_text(text):
    new_text = ""
    for i in text:
        if i == " ":
            continue
        else:
            new_text += i

    # print("Text:"+new_text)
    if new_text == "":
        return False
    else:
        return new_text




def open_create():
    if (os.path.isfile(os.getcwd() + "\\XPassword.pfc")) == True: create()

##
def remap_list(lst, idx1, idx2):
    if idx1 == idx2: print("Atributes Error\n"*10)
    ls1 = lst[idx1]
    ls2 = lst[idx2]
    lst[idx2] = ls1
    lst[idx1] = ls2
##

def edit_list_open(self, master):
    global all_label, list_box, sel_lab
    try: close_win_()
    except: pass

    check2()
    root.deiconify()

    edit_top = Toplevel()
    edit_top.focus_set()

    def update_root(win):
        x = win.winfo_rootx()
        y = win.winfo_rooty()
        try:    edit_top.wm_geometry( "+%d+%d" % (root.winfo_rootx(), root.winfo_rooty()-15))
        except:
            root.unbind("<Configure>")
            root.bind("<Configure>", lambda event: magnit.replace_win())

    edit_top.bind("<Configure>", lambda event: update_root(root))
    root.bind("<Configure>", lambda event: update_root(root))


    #edit_top.overrideredirect(True)
    #root.wm_attributes("-topmost", False)
    edit_top.resizable(width=False, height=False)
    edit_top.geometry(str(root.winfo_width())+"x"+str(60+22*(len(base))))
    edit_top.wm_geometry("+%d+%d" % (root.winfo_rootx(), root.winfo_rooty()-20))
    edit_can = Canvas(edit_top, bg="white")
    edit_can.place(x=-5, y=-5, width=root.winfo_width()+10, height=62+22*len(base)+5)

    root.after(1500, lambda: button2.config(state = DISABLED))
    sel_lab = None

    up = Label(edit_can, image=up_ico, relief=FLAT, cursor='hand2')
    up.place(x=root.winfo_width() - 15, y=5, height=18, width=20)
    up.bind("<Enter>", lambda event: up.config(relief=GROOVE))
    up.bind("<Leave>", lambda event: up.config(relief=FLAT))
    up.bind("<ButtonPress>", lambda event: up.config(relief=RIDGE))

    down = Label(edit_can, image=down_ico, relief=FLAT, cursor='hand2')
    down.place(x=root.winfo_width() - 36, y=5, height=18, width=20)
    down.bind("<Enter>", lambda event: down.config(relief=GROOVE))
    down.bind("<Leave>", lambda event: down.config(relief=FLAT))
    down.bind("<ButtonPress>", lambda event: down.config(relief=RIDGE))

    def save_edit():
        if messagebox.askokcancel("Сохранение", "Вы действительно хотите сохранить изменения?") == False: return
        text = ''''''
        for i in all_label:
            #print(list(i.text))
            i = list(i.text)
            text += "{} {} {} {}\n".format(i[0], i[1][0], i[1][1], i[1][2])
        edit_top.destroy()
        try:
            base_ = open(file_e, "w")
            base_.write("PFC")
            base_.close()
            encryptDecrypt("E", file_e, password_d_e, text)
        except:
            messagebox.showerror("Ошибка!", "Неизвестная ошика\nВыполнение операции будет остановлена");
        messagebox.showinfo("Выполнение операции", "Операция успешно завершена!")
        create()

    def close_edit():
        if sel_lab != None:
            if messagebox.askokcancel("Внимание!", "Вы действительно хотите отменить все сделанные действия?") == True: edit_top.destroy(); create()
        else: edit_top.destroy(); create()

    ok = Button(edit_can, text="Сохранить", command=lambda: save_edit(), relief=GROOVE, overrelief=RIDGE, cursor="hand2", bg="white", activebackground="white")
    cancel = Button(edit_can, text="Отмена", command=lambda: close_edit(), relief=GROOVE, overrelief=RIDGE, cursor="hand2", bg="white", activebackground="white")
    edit_top.wm_protocol("WM_DELETE_WINDOW", lambda: close_edit())

    edit_can.create_line(7, 25, root.winfo_width() + 2, 25)
    edit_can.create_line(7, 25, 7, 62 + 22 * len(base))


    edit_can.create_line(7, 32+22*len(base), root.winfo_width()+3, 32+22*len(base))
    edit_can.create_line(7, 62+22*len(base), root.winfo_width()+3, 62+22*len(base))
    edit_can.create_line(root.winfo_width()+2, 25, root.winfo_width()+2, 62+22*len(base))

    '''class Lab_List__():
        def __init__(self, num, text):
            print("\n")
            self.num = num
            num = 5+22*(num)

            self.lab = Label(edit_can, text=text[0],bg="white", relief=GROOVE, font=10, anchor=W)
            self.lab.place(x=5,y=num, width=root.winfo_width()+1)

            self.up = Label(self.lab,image=up_ico, relief=FLAT, cursor='hand2')
            self.up.place(x=root.winfo_width()-25,y=0, height=20, width=20)
            self.up.bind("<Enter>", lambda event: self.up.config(relief=GROOVE))
            self.up.bind("<Leave>", lambda event: self.up.config(relief=FLAT))
            self.up.bind("<ButtonPress>", lambda event: self.up.config(relief=RIDGE))
            self.up.bind("<ButtonRelease>", lambda event: self.up.config(relief=GROOVE) or self.uping())

            self.down = Label(self.lab,image=down_ico, relief=FLAT, cursor='hand2')
            self.down.place(x=root.winfo_width()-45,y=0, height=20, width=20)
            self.down.bind("<Enter>", lambda event: self.down.config(relief=GROOVE))
            self.down.bind("<Leave>", lambda event: self.down.config(relief=FLAT))
            self.down.bind("<ButtonPress>", lambda event: self.down.config(relief=RIDGE))
            self.down.bind("<ButtonRelease>", lambda event: self.down.config(relief=GROOVE) or self.downing())
            """
            lab_eye = Label(parent, image=eye_close, bg="white", cursor='hand2')
            lab_eye.place(x=x_eye, y=y_eye, height=18)
            lab_eye.bind("<Enter>", lambda event: lab_eye.config(relief=GROOVE))
            lab_eye.bind("<Leave>", lambda event: lab_eye.config(relief=FLAT))
            lab_eye.bind("<ButtonPress>",
                         lambda event: lab_eye.config(relief=GROOVE, image=eye_open) or parent.config(show=""))
            lab_eye.bind("<ButtonRelease>",
                         lambda event: lab_eye.config(relief=GROOVE, image=eye_close) or parent.config(show="*"))
            return lab_eye
            """

        def uping(self, start=True):
            #self.lab.place(x=5,y=5+(self.num)*22)
            if self.num == 0: return
            #print(start, "Up1:", self.num, "=", self.num-1)

            def st(self, num):
                self.lab.place(x=5, y=num)

            self.num = self.num-1
            if start == True: all_label[self.num].downing(False); all_label[self.num].num = self.num+1; remap_list(all_label, self.num, self.num+1)

            #print(start, "Up2:", all_label[self.num].num)

            #print(5+(self.num-1)*22)
            self.up.place_forget()
            self.down.place_forget()
            root.after(100, lambda: st(self, (5 + (self.num + 1) * 22) - 1))
            root.after(200, lambda: st(self, (5 + (self.num + 1) * 22) - 4.4))
            root.after(300, lambda: st(self, (5 + (self.num + 1) * 22) - 8.8))
            root.after(400, lambda: st(self, (5 + (self.num + 1) * 22) - 13.2))
            root.after(500, lambda: st(self, (5 + (self.num + 1) * 22) - 17.6))
            root.after(600, lambda: st(self, (5 + (self.num + 1) * 22) - 22))
            root.after(650, lambda: self.up.place(x=root.winfo_width()-25,y=0, height=20, width=20) or self.down.place(x=root.winfo_width()-45,y=0, height=20, width=20))



        def downing(self, start=True):
            # self.lab.place(x=5,y=5+(self.num-1)*22)
            #if self.num == 1: return
            #print(start, "Down:", self.num, "=", self.num+1)

            def st(self, num):
                self.lab.place(x=5, y=num)


            self.num = self.num + 1
            if start == True: all_label[self.num].uping(False); all_label[self.num].num = self.num-1; remap_list(all_label, self.num, self.num-1)

            for i, sulf in enumerate(all_label):
                sulf.up.place_forget()
                sulf.down.place_forget()
                sulf.place_show()

            root.after(100, lambda: st(self, (5 + (self.num - 1) * 22) + 1))
            root.after(200, lambda: st(self, (5 + (self.num - 1) * 22) + 4.4))
            root.after(300, lambda: st(self, (5 + (self.num - 1) * 22) + 8.8))
            root.after(400, lambda: st(self, (5 + (self.num - 1) * 22) + 13.2))
            root.after(500, lambda: st(self, (5 + (self.num - 1) * 22) + 17.6))
            root.after(600, lambda: st(self, (5 + (self.num - 1) * 22) + 22))
            self.place_show()

        def place_show(self):
            root.after(650, lambda: self.up.place(x=root.winfo_width() - 25, y=0, height=20, width=20) or self.down.place(x=root.winfo_width() - 45, y=0, height=20, width=20))

        def destroy(self):
            self.lab.destroy()'''

    class Lab_List():
        def __init__(self, num, text):
            print("\n")
            self.num = num
            num = 5+22*(num)
            self.text = text



            self.lab = Label(edit_can, text=str(text[0]).replace("`", " "), bg="white", relief=GROOVE, font=10, anchor=W)
            self.lab.place(x=10,y=num+23, width=root.winfo_width()-9)
            self.lab.bind("<Button-1>", lambda event: self.select())

        def select(self):
            global sel_lab
            try: sel_lab.deselect()
            except:
                down.bind("<ButtonRelease>", lambda event: down.config(relief=GROOVE) or sel_lab.downing())
                up.bind("<ButtonRelease>", lambda event: up.config(relief=GROOVE) or sel_lab.uping())

            self.lab["fg"] = "white"
            self.lab["bg"] = "#0078D7"
            self.lab["relief"] = FLAT
            self.lab.place(width=root.winfo_width()-10)
            sel_lab = self

        def deselect(self):
            self.lab["fg"] = "black"
            self.lab["bg"] = "white"
            self.lab["relief"] = GROOVE
            self.lab.place(width=root.winfo_width()-9)

        def uping(self, start=True):
            #self.lab.place(x=10,y=num+23, width=root.winfo_width()-9)
            if self.num == 0: return

            def st(self, num):
                self.lab.place(x=10, y=num+23)

            self.num = self.num-1
            if start == True: all_label[self.num].downing(False); all_label[self.num].num = self.num+1; remap_list(all_label, self.num, self.num+1)

            move = True
            if move == True:
                root.after(50, lambda: st(self, (5 + (self.num + 1) * 22) - 1))
                root.after(100, lambda: st(self, (5 + (self.num + 1) * 22) - 4.4))
                root.after(150, lambda: st(self, (5 + (self.num + 1) * 22) - 8.8))
                root.after(200, lambda: st(self, (5 + (self.num + 1) * 22) - 13.2))
                root.after(250, lambda: st(self, (5 + (self.num + 1) * 22) - 17.6))
                root.after(300, lambda: st(self, (5 + (self.num + 1) * 22) - 22))
            else: st(self, (5 + (self.num + 1) * 22) - 22)


        def downing(self, start=True):
            if self.num == len(all_label)-1: return
            def st(self, num):
                self.lab.place(x=10, y=num+23)


            self.num = self.num + 1
            if start == True: all_label[self.num].uping(False); all_label[self.num].num = self.num-1; remap_list(all_label, self.num, self.num-1)

            move = True
            if move == True:
                root.after(50, lambda: st(self, (5 + (self.num - 1) * 22) + 1))
                root.after(100, lambda: st(self, (5 + (self.num - 1) * 22) + 4.4))
                root.after(150, lambda: st(self, (5 + (self.num - 1) * 22) + 8.8))
                root.after(200, lambda: st(self, (5 + (self.num - 1) * 22) + 13.2))
                root.after(250, lambda: st(self, (5 + (self.num - 1) * 22) + 17.6))
                root.after(300, lambda: st(self, (5 + (self.num - 1) * 22) + 22))
            else: st(self, (5 + (self.num - 1) * 22) + 22)

        def destroy(self):
            self.lab.destroy()

    '''class Lab_List():
        def __init__(self, num, text):
            print("\n")
            list_box.insert(num, text[0])
            self.num = num
            num = 5+22*(num)


            #edit_can.create_line(5, num+19, root.winfo_width()+10, num+19)
            #edit_can.create_line(5, 25, 5, 45+22*len(all_label))
            #edit_can.create_line(5, 25+22*len(all_label), root.winfo_width()+10, 25+22*len(all_label))

            self.lab = Label(edit_can, text=text[0], bg="white", relief=GROOVE, font=10, anchor=W)
            #self.lab.place(x=6,y=num+20, width=root.winfo_width()-1)

            self.up = Label(edit_can,image=up_ico, relief=FLAT, cursor='hand2')
            self.up.place(x=root.winfo_width()-25,y=5, height=20, width=20)

            self.down = Label(edit_can,image=down_ico, relief=FLAT, cursor='hand2')
            self.down.place(x=root.winfo_width()-45,y=5, height=20, width=20)


        def uping(self, start=True):

            if self.num == 0: return

            def st(self, num):
                self.lab.place(x=5, y=num)

            self.num = self.num-1
            if start == True: all_label[self.num].downing(False); all_label[self.num].num = self.num+1; remap_list(all_label, self.num, self.num+1)

            #self.up.place_forget()
            #self.down.place_forget()
            root.after(100, lambda: st(self, (5 + (self.num + 1) * 22) - 1))
            root.after(200, lambda: st(self, (5 + (self.num + 1) * 22) - 4.4))
            root.after(300, lambda: st(self, (5 + (self.num + 1) * 22) - 8.8))
            root.after(400, lambda: st(self, (5 + (self.num + 1) * 22) - 13.2))
            root.after(500, lambda: st(self, (5 + (self.num + 1) * 22) - 17.6))
            root.after(600, lambda: st(self, (5 + (self.num + 1) * 22) - 22))
            root.after(650, lambda: self.up.place(x=root.winfo_width()-25,y=0, height=20, width=20) or self.down.place(x=root.winfo_width()-45,y=0, height=20, width=20))



        def downing(self, start=True):

            def st(self, num):
                self.lab.place(x=5, y=num)


            self.num = self.num + 1
            if start == True: all_label[self.num].uping(False); all_label[self.num].num = self.num-1; remap_list(all_label, self.num, self.num-1)

            return
            for i, sulf in enumerate(all_label):
                sulf.up.place_forget()
                sulf.down.place_forget()
                sulf.place_show()

            root.after(100, lambda: st(self, (5 + (self.num - 1) * 22) + 1))
            root.after(200, lambda: st(self, (5 + (self.num - 1) * 22) + 4.4))
            root.after(300, lambda: st(self, (5 + (self.num - 1) * 22) + 8.8))
            root.after(400, lambda: st(self, (5 + (self.num - 1) * 22) + 13.2))
            root.after(500, lambda: st(self, (5 + (self.num - 1) * 22) + 17.6))
            root.after(600, lambda: st(self, (5 + (self.num - 1) * 22) + 22))
            self.place_show()

        def place_show(self):
            root.after(650, lambda: self.up.place(x=root.winfo_width() - 25, y=0, height=20, width=20) or self.down.place(x=root.winfo_width() - 45, y=0, height=20, width=20))

        def destroy(self):
            self.lab.destroy()'''

    #list_box = Listbox(edit_can, font=("Calibri", 14), height=len(self.text), fg="black")
    #list_box.place(x=5, y=30, width=root.winfo_width())
    #self._list_ = Listbox(self.frame, foаnt=("Calibri", 11), height=len(self.text), relief=FLAT, fg="black")

    all_label = []
    for i, text in enumerate(base):
        all_label.append(Lab_List(i, text))

    ok.place(x=10, y=35+22*(len(all_label)))
    cancel.place(x=root.winfo_width()-53, y=35+22*(len(all_label)))

    # edit_top.deiconify()
    edit_top.wait_visibility();
    edit_top.grab_set();
    # edit_top.wait_window(root)
    edit_top.transient(root)



def close_win_():
    try:
        button2["state"] = DISABLED
        button2["command"] = lambda: open_create()

        button2["text"] = "Открыть базу"
        button2["state"] = NORMAL

        root2.destroy();
        list_all.tops.destroy()
    except: pass

# ______________________________________________________________________________________________________Создание окна
def create(start_val=True):
    global close_win_, text_first, text_second, list_all, base, root2, reset_list

    button2["state"]=DISABLED
    if start_val == True: check2()
    else: pass

    root.after(1500, lambda: button2.config(state = NORMAL))



    button2["command"] = close_win_
    button2["text"] = "Закрыть базу"

    def check_size(master):
        if master.winfo_height() < 76:
            messagebox.showinfo("Ошибка","Код: windows havn`t normal size")
            list_all.update()

    root2 = Toplevel()
    root2.title(str(file_d.split("\\")[-1][0:-4]))
    root2.resizable(width=False, height=False)
    magnit.drag_win()

    root.after(500, lambda: check_size(root2))

    if (root.winfo_rootx() - ((310 - 295) + 215)) < 0: root2.wm_geometry("+%d+%d" % (root.winfo_x() + 300 + 20, root.winfo_y()))
    else: root2.wm_geometry("+%d+%d" % (root.winfo_x() - ((300 - 295) + 215) - 20, root.winfo_y()))

    text_first = []
    text_second = []
    for i in base:
        text_second.append(i[1])
        if len(i[0].split("`")) >= 2:
            z = i[0].replace("`", " ")
            text_first.append(z)
        else:
            text_first.append(i[0])

    root2.geometry("215x" + str(8 + int(17 * len(text_first)) + 25))

    def update(_list_, frame, root, but_1, but_2, but_3, but_4, can, gmt):
        try: y = _list_.winfo_height()
        except: return

        def update_2():
            try: frame["height"] = y + 28
            except: pass

        root.geometry(gmt + str(8 + y + 45))
        but_1.place(x=8, y=30 + y, width=30, height=25)
        but_2.place(x=215-30, y=30 + y, width=30-4, height=23)
        but_3.place(x=215-34-23, y=30 + y, width=26, height=25)
        but_4.place(x=9 + 30, y=30 + y, width=60*2-2, height=25)

        can["height"] = 8 + y + 45
        root.after(50, update_2)

    def delete_list(_list_, text):
        global base, text_first, text_second
        try: list_all.tops.destroy()
        except: pass

        curren_selection = _list_.curselection()
        if str(curren_selection) == "()": return

        root2.wm_attributes("-disabled", True)
        answer = str(messagebox.askokcancel("Операция удаления данных",
                                            "Вы действительно хотите безвозвратно удалить данную карту?"))
        root2.wm_attributes("-disabled", False)
        _list_.focus_set()

        if str(answer) == "True": print("Eror")
        if str(answer) == "False": return

        _list_.delete(curren_selection)
        text.remove(text[int(curren_selection[0])])
        _list_["height"] = len(text)
        base.remove(base[int(curren_selection[0])])

        text = """"""
        for i in base:
            text += "{} {} {} {}\n".format(i[0], i[1][0], i[1][1], i[1][2])

        base_ = open(file_e, "w")
        base_.write("PFC")
        base_.close()
        encryptDecrypt("E", file_e, password_d_e, text)

        check2()
        text_first = []
        text_second = []
        for i in base:
            text_second.append(i[1])
            if len(i[0].split("`")) >= 2:
                z = i[0].replace("`", " ")
                text_first.append(z)
            else:
                text_first.append(i[0])
        list_all.text = text_first
        list_all.text_2 = text_second

    def add_list(text, _list_):
        global base, text_first, text_second
        list_all._do_ = None
        new_list = simpl.askstring("Создание блока", "Введите название нового блока:")
        _list_.focus_set()
        if new_list == None: return
        num = 1
        for i, string in enumerate(new_list):
            if string == ' ':
                num = int(i) + 1
            else:
                num = int(i); break
        new_list = new_list[num:]
        if new_list == "": messagebox.showinfo("Ошибка", "Блок не может быть пустым"); return

        list_ = ""
        for i in new_list:
            if i == " ":
                list_ += "`"; continue
            else:
                list_ += i
        new_list = list_

        text.append(new_list)
        _list_.insert("end", new_list.replace("`", " "))
        _list_["height"] = len(text)

        base.append([new_list, ["0", "0", "0"]])
        text = """"""
        for i in base:
            text += "{} {} {} {}\n".format(i[0], i[1][0], i[1][1], i[1][2])

        base_ = open(file_e, "w")
        base_.write("PFC")
        base_.close()
        encryptDecrypt("E", file_e, password_d_e, text)

        check2()

        text_first = []
        text_second = []
        for i in base:
            text_second.append(i[1])
            if len(i[0].split("`")) >= 2:
                z = i[0].replace("`", " ")
                text_first.append(z)
            else:
                text_first.append(i[0])
        list_all.text = text_first
        list_all.text_2 = text_second
        def open_new(size_list,_list_):
            print(size_list, _list_.winfo_height())
            x,y = root2.winfo_rootx(),root2.winfo_rooty()
            print(x,y)
            #pgui.moveTo(x+20,y+10+_list_.winfo_height(),0.3)
            pgui.doubleClick(x+20,y+10+_list_.winfo_height())
            root.after(600, lambda: list_all.edit_())
        _list_.activate(2)
        root.after(100, lambda: open_new(_list_.size(),_list_))
        root2.focus_set()

    def reset_list(id,master):
        global base
        id.opt.destr()
        close_win_()
        check2()
        print(sorted(base))
        base = sorted(base)
        root.after(1000, lambda: create(False))

    class listbox():
        def __init__(self, text):

            from tkinter import CENTER, W
            self.text = text

            self._do_ = None



            self.c1 = Canvas(root2, bg="white", height=455, width=330)
            self.c1.place(x=-2, y=-2)

            self.edit_list = Button(self.c1, command=lambda: edit_list_open(self, root2), text="Сортировка",bg="white", fg="blue", relief=FLAT, overrelief=GROOVE, activebackground="blue", activeforeground="white")
            self.edit_list.place(x=295-79*2-2, y=2, height=19)

            #Label(self.c1, text='Блоки данных:', font=("Calibri", 12), bg="white", anchor=W, fg="blue").place(x=5, y=0, width=105)
            self.frame = Frame(self.c1, bg="white")
            self.frame.place(x=0, y=20, width=295)

            self._list_ = Listbox(self.frame, font=("Calibri", 11), height=len(self.text), relief=FLAT, fg="black")
            self._list_.bind("<Double-Button-1>", func=self.open_tops)

            self._list_.bind("<<ListboxSelect>>", func=self.select_but)

            self._list_.bind("<Return>", func=self.open_tops)
            # self._list_.bind("<<ListboxSelect>>", func=self.close_tops)
            self._list_.place(x=8, y=2, width=203)
            for i, text in enumerate(self.text):
                if text == "0": text = " "
                self._list_.insert(i, text)
            self._list_.focus_set()
            self.del_but = Button(self.c1, image=delete_icon, cursor="arrow", command=self.delete_list, relief=FLAT,
                                  bg="white", overrelief=GROOVE, activebackground="white", anchor=CENTER)
            self.add_but = Button(self.c1, image=add_ico, command=self.add_list, relief=FLAT, bg="white",
                                  overrelief=GROOVE, activebackground="white", anchor=CENTER)
            self.rename_but = Button(self.c1, image=rename_ico, command=lambda: self.rename(), relief=FLAT,
                                     overrelief=GROOVE, bg="white", activebackground="white", anchor=W)
            self.open_but = Button(self.c1, text="Открыть", command=lambda: self.open_tops(), relief=FLAT,
                                   overrelief=GROOVE, bg="white", activebackground="white")

            root2.bind("<BackSpace>", lambda event: self.delete_list())
            root2.bind("<Delete>", lambda event: self.delete_list())

            CreateToolTip(self.del_but, "Удалить")
            CreateToolTip(self.add_but, "Добавить")
            CreateToolTip(self.rename_but, "Переименовать")

            root.after(50, self.bind_all)
            root.after(50, self.update)
            root.after(100, lambda: Main_list_box())


        def rename(self):
            try: effect_close(self.tops)
            except: pass
            try: cur_select = self._list_.curselection()[0]
            except: return

            new_list = simpl.askstring("Операция", "Переименовать '{}' на:".format(self.text[self._list_.curselection()[0]]), None,text=self.text[self._list_.curselection()[0]])

            if new_list == None: return
            name = return_text(new_list)

            if name == False: messagebox.showinfo("Ошибка", "Недопустимый формат названия"); return

            list_ = ""
            for i in new_list:
                if i == " ":
                    list_ += "`"; continue
                else:
                    list_ += i
            new_list = list_

            base[cur_select][0] = new_list
            text = """"""

            for i in base:
                text += "{} {} {} {}\n".format(i[0], i[1][0], i[1][1], i[1][2])

            base_ = open(file_e, "w")
            base_.write("PFC")
            base_.close()
            encryptDecrypt("E", file_e, password_d_e, text)

            check2()

            text_first = []
            text_second = []
            for i in base:
                text_second.append(i[1])
                if len(i[0].split("`")) >= 2:
                    z = i[0].replace("`", " ")
                    text_first.append(z)
                else:
                    text_first.append(i[0])
            list_all.text = text_first
            list_all.text_2 = text_second

            self.destr_all()

            # self._list_.focus_set()
            # self._do_ = None

        def destr_all(self):
            global list_all, text_first, text_second
            check2()
            text_first = []
            text_second = []
            for i in base:
                text_second.append(i[1])
                if len(i[0].split("`")) >= 2:
                    z = i[0].replace("`", " ")
                    text_first.append(z)
                else:
                    text_first.append(i[0])
            self.frame.destroy()
            self._list_.destroy()
            self.c1.destroy()
            list_all = listbox(text_first)

        def bind_all(self):
            try:
                root2.protocol("WM_DELETE_WINDOW", lambda: self.close_win())
            except:
                root2.destroy()

            # root2.bind('<Unmap>', self.curtail_win)
            # root2.bind("<Configure>", func=self.curtail_win)
            # root.bind("<Configure>", func=self.dstr_tops)

        def update(self):
            update(self._list_, self.frame, root2, self.del_but, self.add_but, self.rename_but, self.open_but, self.c1, "215x")

        def delete_list(self):
            delete_list(self._list_, self.text)
            root.after(50, self.update)

        def add_list(self):
            try: effect_close(self.tops)
            except: pass
            add_list(self.text, self._list_)
            root.after(50, self.update)

        def close_win(self):
            try: effect_close(self.tops)
            except: pass
            finally: root.unbind("<Configure>"); close_win_();  return

        def curtail_win(self, event):
            if event.widget is not root2: return
            try:
                self.tops.destroy(); self._list_.unbind("<<ListboxSelect>>"); self._list_.bind(
                    "<<ListboxSelect>>", self.dstr_tops); root.unbind("<Configure>")
            except:
                pass

        def close_tops(self, event=None):
            try:
                if self._do_ == self._list_.curselection()[0]:
                    return
                else:
                    self._do_ = None
                    try:
                        effect_close(self.tops)
                    except:
                        pass
            except IndexError:
                print("IndexError")

        def dstr_tops(self, event=None):
            try:
                self.tops.destroy()
            except:
                pass
            self._do_ = None

        def get_val(self):
            try: self._do_ = self._list_.curselection()[0]
            except: print("IndexError: tuple index out of range"); self._do_ = 0; return False

        def select_but(self, event=None):
            def select_but_2():
                try:
                    # print('Start',self._list_.curselection()[0],self._do_)
                    if self._list_.curselection()[0] == self._do_:
                        self.open_but["text"] = "Закрыть"
                    if self._list_.curselection()[0] != self._do_:
                        self.open_but["text"] = "Открыть"
                except: pass

            root.after(100, select_but_2)

        def open_tops(self, event=None, do_start=None):
            global url, login, passw
            root.after(100, self.select_but)
            magnit.drag_win()



            try:
                if self._do_ == self._list_.curselection()[0]: effect_close(self.tops); self._do_ = None; return
                else: pass
            except: pass

            do_start = self.get_val()
            root.after(50, self.get_val())

            try: self.tops.destroy()
            except: pass

            if do_start == None:
                try: self.text_2 = text_second[self._list_.curselection()[0]]
                except: self.add_list();  return

            if do_start == 2: self._do_ = 0

            self.tops = Toplevel()
            try: self.tops.title('Блок: '+ str(self._list_.get(self._list_.curselection()[0])))
            except IndexError: self.tops.title('Блок: '+ str(self._list_.get(0))); self.text_2 = text_second[0]


            print(text_second[self._do_][0],text_second[self._do_][1],text_second[self._do_][2])
            if event == None:
                if text_second[self._do_][0] == "0":
                    if text_second[self._do_][1] == "0":
                        if text_second[self._do_][2] == "0":
                            root.after(200, self.edit_)

            # print(root2.winfo_rootx(), root2.winfo_rooty())
            self.tops.wm_geometry("+%d+%d" % (root2.winfo_rootx() - 8, root2.winfo_rooty() - 150+3))

            self.tops.geometry("{}x{}".format(str(int(root.winfo_width()+root2.winfo_width())+5+20), str(int(root.winfo_height()/8))))
            self.tops.wm_attributes("-alpha", 0)
            self.tops.resizable(width=False, height=False)
            self.tops.protocol("WM_DELETE_WINDOW", lambda: self.dstr_tops())
            self.tops.focus_set()
            # root.after(1000, lambda: self.tops.bind("<Return>", self.edit_()))

            self.c2 = Canvas(self.tops, bg="white")
            self.c2.place(x=-5, y=-5, height=65, width=680)

            self.c2.create_line(0, 5, 673, 5)
            self.c2.create_line(0, 29, 442, 29)
            self.c2.create_line(0, 53, 673, 53)

            self.c2.create_line(57, -5, 57, 70, dash=1)
            self.c2.create_line(223, -10, 223, 30)
            self.c2.create_line(276, -11, 276, 30, dash=1)
            self.c2.create_line(442, -10, 442, 70)
            # self.c2.create_line(578, -10, 578, 70)

            url = self.text_2[0]
            if url == "0": url = ""
            login = self.text_2[1]
            if login == "0": login = ""
            passw = self.text_2[2]
            if passw == "0": passw = ""
            from tkinter import S
            self.url = Label(self.c2, text=url, height=1, bg="white", anchor=W)
            self.url.bind("<Double-Button-1>", lambda event: self.create_check_mark(1, url))
            self.url_label_ = Label(self.c2, text="Сайт", bg="white", fg="blue", anchor=W)
            self.url_label_.place(x=6, y=7, height=21, width=49)
            self.url.place(x=60, y=7, height=21, width=161)#, width=150

            self.login = Label(self.c2, text=login, height=1, bg="white", anchor=W, width=20)
            self.login.bind("<Double-Button-1>", lambda event: self.create_check_mark(2, login))
            self.login_labell = Label(self.c2, text="Логин", bg="white", fg="blue", anchor=W)
            self.login_labell.place(x=225, y=7, height=21, width=49)
            self.login.place(x=276+3, y=7, height=21, width=161 )

            self.passw = Label(self.c2, text=len(passw) * "*", height=1, bg="white", anchor=W)
            self.passw.bind("<Double-Button-1>", lambda event: self.create_check_mark(3, passw))
            self.passw_label = Label(self.c2, text="Пароль", bg="white", fg="blue", anchor=W)
            self.passw_label.place(x=6, y=31, height=21, width=49)
            self.passw.place(x=60, y=31, height=21, width=442-62)#, width=185

            self.url_entr = Entry(self.c2, bg="#00EEFF", fg='#030069')  # 00EEFF and #030069
            self.login_entr = Entry(self.c2, bg="#00EEFF", fg='#030069')
            self.passw_entr = Entry(self.c2, bg="#00EEFF", fg='#030069')

            self._do_eye = 0
            self.check_do = 0# 596
            self.look_but_ = Button(self.c2, image=eye_close, cursor="hand2", command=self.eye, relief=FLAT,
                                    overrelief=GROOVE, bg="white")
            self.edit_but_ = Button(self.c2, image=edit_ico, command=self.edit_, relief=FLAT,
                                    overrelief=GROOVE, bg="white", cursor="hand2")
            self.edit_brows = Button(self.c2, image=browser_ico, command=lambda: self.start_brows(self.text_2[0], True),
                                     relief=FLAT, overrelief=GROOVE, bg="white", cursor="hand2")
            self.edit_brows.bind("<3>", lambda event: self.open_brows())

            self.bind_tops()
            self.edit_but_.place(x=517-26*3+5+10, y=17, width=25, height=25)
            self.look_but_.place(x=517-26*2+5+10, y=17, width=25, height=25)
            self.edit_brows.place(x=517-26*1+5+10, y=17, width=25, height=25)

            self.label_copy = Label(self.c2, image=copy_ico1)
            self.check_redx_copy = Label(self.c2, image=copy_ico2)

            self.edit_tool_tip = CreateToolTip(self.edit_but_, "Изменить")
            CreateToolTip(self.edit_brows, "Открыть браузер")

            effect_run(self.tops, 350)

        def bind_tops(self):
            self.tops.bind("<space>", lambda event: self.eye())
            self.tops.bind("<Double-Key-1>", lambda event: self.create_check_mark(1, url))
            self.tops.bind("<Double-Key-2>", lambda event: self.create_check_mark(2, login))
            self.tops.bind("<Double-Key-3>", lambda event: self.create_check_mark(3, passw))

        def unbind_tops(self):
            try:
                self.tops.unbind("<space>")
                self.tops.unbind("<Double-Key-1>")
                self.tops.unbind("<Double-Key-2>")
                self.tops.unbind("<Double-Key-3>")
            except:
                self.open_tops(); self.edit_()

        def create_check_mark(self, numb, text):
            if self.check_do == 1: return
            self.check_do = 1

            root.clipboard_clear()
            root.clipboard_append(str(text))

            '''
            txt = str(root.clipboard_get())
            if txt != str(text):
                root.clipboard_clear()
                txt = str(root.clipboard_get())
                if txt != str(text):
                    messagebox.showerror("Ошибка","Текст не возможно скопировать, перезапустите программу!"); return
            '''
            def select(self, numb, text, num=0):
                if num == 2:
                    messagebox.showerror("Ошибка","Текст не возможно скопировать, перезапустите программу!"); return
                num+=1
                txt = str(root.clipboard_get())
                if txt != str(text):
                    root.clipboard_clear()
                    root.clipboard_append(str(text))
                    root.after(50, lambda: select(self, numb, text, num))
                    return


                def default_do(self):
                    self.check_do = 0
                    self.label_copy.place_forget()
                    self.check_redx_copy.place_forget()

                if numb == 1:
                    self.label_copy.place(x=31, y=6, width=23, height=23)
                    self.check_redx_copy.place(x=8, y=6, width=23, height=23)
                elif numb == 2:
                    self.label_copy.place(x=320-43-3-23, y=6, width=23, height=23)
                    self.check_redx_copy.place(x=320-43-3-23*2, y=6, width=23, height=23)
                elif numb == 3:
                    self.label_copy.place(x=31, y=30, width=23, height=23)
                    self.check_redx_copy.place(x=8, y=30, width=23, height=23)
                root.after(300, lambda: default_do(self))

            root.after(50, lambda: select(self, numb, text))


        def start_brows(self, browser_url, do=False):

            if browser_url == "0": webbrowser.open_new('https://'); return

            if browser_url[0:7] not in ["http://", "https:/"]:
                webbrowser.open("https://" + browser_url)
            if browser_url[0:7] in ["http://", "https:/"]:
                if browser_url[0:7] == "http://":
                    webbrowser.open("https://" + browser_url[7:])
                else:
                    webbrowser.open(browser_url)
            if do == True: self.open_brows()

        def protocol_delete(self):
            x = self.tops.winfo_rootx()
            y = self.tops.winfo_rooty()

            root.wm_attributes("-alpha", 0)
            root.wm_attributes("-alpha", 1)
            root.deiconify()
            root2.deiconify()

            root.after(50, lambda: root.wm_geometry("+%d+%d" % (x + 400, y - 30)))
            root.after(50, lambda: root2.wm_geometry("+%d+%d" % (x + 100, y - 30)))

            root.after(100, lambda: effect_run(root, 350))
            root.after(100, lambda: effect_run(root2, 350))

            self.dstr_tops()
            self._list_.focus_set()

        def open_brows(self):
            self.edit_brows.unbind("<3>")
            self.edit_brows.configure(command=lambda: self.start_brows(self.text_2[0]))

            self.tops.protocol("WM_DELETE_WINDOW", lambda: self.protocol_delete())

            self.tops.wm_attributes("-topmost", 1)
            self.tops.wm_attributes("-alpha", 0.8)

            # root.withdraw()
            # root2.withdraw()

            root.iconify()
            root2.iconify()

            if (root.winfo_rootx() - 310) < 0: self.tops.wm_geometry("+%d+%d" % (root.winfo_x(), root.winfo_y()-90+2))
            else: self.tops.wm_geometry("+%d+%d" % (x - 300-2, y-90+2))
            self._do_eye = 1
            self.eye()
            self.edit_cancel()
            self.edit_but_["state"] = DISABLED
            return

        def eye(self):
            if self._do_eye == 0:
                self.look_but_["image"] = eye_open
                passw = self.text_2[2]
                if passw == "0": passw = ""
                self.passw["text"] = str(passw)
                self._do_eye = 1
                return
            if self._do_eye == 1:
                self.look_but_["image"] = eye_close
                passw = self.text_2[2]
                if passw == "0": passw = ""
                self.passw["text"] = str(len(passw) * "*")
                self._do_eye = 0
                return

        def edit_cancel(self):
            self.bind_tops()
            self._do_eye = 1
            self.edit_tool_tip.remap_text("Изменить")
            self.url.place(x=60, y=7, height=21, width=161)
            self.login.place(x=276+3, y=7, height=21, width=161 )
            self.passw.place(x=60, y=31, height=21, width=442-62)
            # self.passw["text"]=str(len(self.text_2[2])*"*")

            self.url_entr.place_forget()
            self.login_entr.place_forget()
            self.passw_entr.place_forget()
            self.edit_but_.configure(image=edit_ico, command=self.edit_)
            self.look_but_.config(image=eye_close, command=self.eye)

            self.edit_brows["state"] = ACTIVE; self.eye()

        def edit_save(self):
            def unband(self):
                self.tops.protocol('WM_DELETE_WINDOW', lambda: self.dstr_tops())
                root.protocol('WM_DELETE_WINDOW', lambda: root.destroy())
                root2.protocol('WM_DELETE_WINDOW', lambda: self.close_win())
                button2["state"] = NORMAL

            button2["state"] = DISABLED
            self.tops.protocol('WM_DELETE_WINDOW', lambda: None)
            root.protocol('WM_DELETE_WINDOW', lambda: None)
            root2.protocol('WM_DELETE_WINDOW', lambda: None)
            root.after(2000, lambda: unband(self))

            self.edit_but_["state"] = DISABLED
            self.bind_tops()
            self._do_eye = 0
            self.edit_tool_tip.remap_text("Изменить")

            ind = int([self._do_][0])

            cort = []
            url_entr = self.url_entr.get()
            login_entr = self.login_entr.get()
            passw_entr = self.passw_entr.get()

            do = return_text(url_entr)
            if do == False:
                url_entr = "0"
            else:
                url_entr = do

            do = return_text(login_entr)
            if do == False:
                login_entr = "0"
            else:
                login_entr = do

            do = return_text(passw_entr)
            if do == False:
                passw_entr = "0"
            else:
                passw_entr = do

            print(url_entr, login_entr, passw_entr)

            # return
            base[ind][1][0] = url_entr
            base[ind][1][1] = login_entr
            base[ind][1][2] = passw_entr

            text = """"""
            for i in base:
                text += "{} {} {} {}\n".format(i[0], i[1][0], i[1][1], i[1][2])

            try:
                base_ = open(file_e, "w")
                base_.write("PFC")
                base_.close()
                encryptDecrypt("E", file_e, password_d_e, text)
            except:
                messagebox.showerror("Ошибка", "Неизвестная ошика\nВыполнение операции будет остановлена");return

            if url_entr == "0": url_entr = ""
            if login_entr == "0": login_entr = ""
            if passw_entr == "0": passw_entr = ""

            self.url["text"] = str(url_entr)
            self.login["text"] = str(login_entr)
            self.passw["text"] = str(len(passw_entr) * "*")

            self.url.place(x=60, y=7, height=21, width=161)
            self.login.place(x=276+3, y=7, height=21, width=161 )
            self.passw.place(x=60, y=31, height=21, width=442-62)

            self.url_entr.place_forget()
            self.login_entr.place_forget()
            self.passw_entr.place_forget()
            self.edit_but_.configure(image=edit_ico, command=self.edit_)
            self.look_but_.config(image=eye_close, command=self.eye)
            self.edit_brows["state"] = ACTIVE
            root.after(1000, lambda: self.edit_but_.config(state=NORMAL))


        def edit_(self):
            self.unbind_tops()
            self.edit_tool_tip.remap_text("Сохранить")
            # self.c2["bg"]="gray"

            self.url.place_forget()
            self.login.place_forget()
            self.passw.place_forget()

            self.look_but_.config(image=cancel_ico, command=lambda: self.edit_cancel())
            self.edit_but_.config(image=edit_ico2, command=lambda: self.edit_save())
            self.edit_brows["state"] = DISABLED

            url = self.text_2[0]
            if url == "0": url = ""
            login = self.text_2[1]
            if login == "0": login = ""
            passw = self.text_2[2]
            if passw == "0": passw = ""

            def delet(entr):
                entr.event_generate("<<SelectAll>>")
                entr.event_generate("<<Clear>>")
            self.url_entr.place(x=self.url.winfo_x()+1, y=self.url.winfo_y(), height=self.url.winfo_height(), width=self.url.winfo_width()-1)
            delet(self.url_entr)
            self.url_entr.insert(1, url)

            self.login_entr.place(x=self.login.winfo_x()+1, y=self.login.winfo_y(), height=self.login.winfo_height(), width=self.login.winfo_width()-1)
            delet(self.login_entr)
            self.login_entr.insert(1, login)

            self.passw_entr.place(x=self.passw.winfo_x()+1, y=self.passw.winfo_y(), height=self.passw.winfo_height(), width=self.passw.winfo_width()-1)
            delet(self.passw_entr)
            self.passw_entr.insert(1, passw)

            do_edit = 0

            self.url_entr.bind("<Up>", lambda event: self.login_entr.focus_set())
            self.login_entr.bind("<Up>", lambda event: self.passw_entr.focus_set())
            self.passw_entr.bind("<Up>", lambda event: self.url_entr.focus_set())
            self.url_entr.bind("<Down>", lambda event: self.passw_entr.focus_set())
            self.login_entr.bind("<Down>", lambda event: self.url_entr.focus_set())
            self.passw_entr.bind("<Down>", lambda event: self.login_entr.focus_set())

            def focus_get_(self):
                try: self.url_entr.focus_set()
                except:
                    self._do_ = None; self.dstr_tops(); double_click_button(); return

            root.after(50, lambda: focus_get_(self))

            def qestion_save(self):
                focus = self.tops.focus_get()
                if messagebox.askokcancel("Сохранить", "Вы действительно хотите сохранить файл?") == True:
                    self.edit_save()
                    self.tops.unbind("<Return>")
                    self.tops.unbind("<Esc>")
                    self.tops.focus_set()
                else:
                    focus.focus_set();return

            def qestion_cancel(self):
                focus = self.tops.focus_get()
                if messagebox.askokcancel("Отменить",
                                          "Вы действительно хотите отменить введенные вами данные?") == True:
                    self.tops.unbind("<Escape>")
                    self.tops.unbind("<Return>")
                    self.edit_cancel()
                    self.tops.focus_set()
                    return
                else:
                    focus.focus_set(); return

            self.tops.bind("<Return>", lambda event: qestion_save(self))
            self.tops.bind("<Escape>", lambda event: qestion_cancel(self))

    list_all = listbox(text_first)









# ___________________________________________________________________________________________________Генерация пароля
def start():
    global but_1, but_2, but_3, var1, var2, var0, var3, ch0, ch1, ch2, ch3, label1, label2, entry1, button1, button2, text1, var4, ch4, scrollbar, c

    c = Canvas(root, bg="#030069", height=400, width=300, state=DISABLED)
    c.place(x=-5, y=-5)

    var0 = StringVar()
    var1 = StringVar()
    var3 = StringVar()
    var2 = StringVar()

    ch0 = Checkbutton(c, text="Цифры", variable=var0, onvalue="1", offvalue="0", font=10, fg="#ff0505", bg="#030069",
                      overrelief=RIDGE, activeforeground="#ff0505", activebackground="#030069"); ch0["activeforeground"]="yellow"
    ch1 = Checkbutton(c, text="А", variable=var1, onvalue="1", offvalue="0", font=10, fg="#ff0505", bg="#030069",
                      overrelief=RIDGE, activeforeground="#ff0505", activebackground="#030069"); ch1["activeforeground"]="yellow"
    ch3 = Checkbutton(c, text="Символы", variable=var2, onvalue="1", offvalue="0", font=10, fg="#ff0505", bg="#030069",
                      overrelief=RIDGE, activeforeground="#ff0505", activebackground="#030069"); ch3["activeforeground"]="yellow"
    ch2 = Checkbutton(c, text="а", variable=var3, onvalue="1", offvalue="0", font=10, fg="#ff0505", bg="#030069",
                      overrelief=RIDGE, activeforeground="#ff0505", activebackground="#030069"); ch2["activeforeground"]="yellow"

    ch0.select()
    ch1.select()
    ch3.select()
    ch2.select()

    ch0.place(x=13, y=47)
    ch1.place(x=100, y=47)
    ch2.place(x=150, y=47)
    ch3.place(x=194, y=47)

    var4 = StringVar()
    ch4 = Checkbutton(c, text="Скопировать", variable=var4, onvalue="1", offvalue="0", fg="#ff0505", bg="#030069",
                      activebackground="#030069", activeforeground="yellow", cursor="hand2")
    ch4.select()
    ch4.place(x=10, y=335)

    label1 = Label(c, text="X Password", bg="#030069", font=("Times New Roman", 20), fg="#FFFF00")
    label1.place(x=5, y=10, width=300, height=35)

    label2 = Label(c, text="Длина пароля:", bg="#030069", font=10, fg="yellow")
    label2.place(x=13, y=75)

    entry1 = Spinbox(c, from_=1, to=1000)
    entry1.delete(0, last=1)
    entry1.insert(END, "8")
    entry1.place(x=130, y=78, width=85, height=20)

    but_1 = Button(c, text="8", bg="#030069", font=10, fg="yellow", overrelief=RIDGE, cursor="hand2", command=lambda: entry1.delete(0, last=16) or entry1.insert(END, "8"))
    but_1.place(x=218, y=78, height=20, width=22)
    but_2 = Button(c, text="12", bg="#030069", font=10, fg="yellow", overrelief=RIDGE, cursor="hand2", command=lambda: entry1.delete(0, last=16) or entry1.insert(END, "12"))
    but_2.place(x=243, y=78, height=20, width=22)
    but_3 = Button(c, text="16", bg="#030069", font=10, fg="yellow", overrelief=RIDGE, cursor="hand2", command=lambda: entry1.delete(0, last=16) or entry1.insert(END, "16"))
    but_3.place(x=268, y=78, height=20, width=22)

    button1 = Button(c, text="Сгенерировать", bg="#030069", repeatdelay=500, repeatinterval=100, font=10, fg="yellow", command=lambda: create_password(1))
    button1["overrelief"] = RIDGE
    button1["cursor"] = "hand2"
    button1.place(x=15, y=100, height=35, width=276)

    root.bind("<Return>", create_password)

    text1 = Text(c, font=("proportionally spaced", 10))
    text1.place(x=15, y=140, height=195, width=257)
    scrollbar = Scrollbar(c)
    scrollbar.place(x=273, y=140, height=195)
    scrollbar['command'] = text1.yview
    text1['yscrollcommand'] = scrollbar.set

    def chek_but(but):
        if os.path.isfile(os.getcwd() + "\\start.txt") == True:
            with open(os.getcwd() + "\\start.txt") as file:
                if file.read() == "0": but['text'] = "Создать базу"
        else:
            with open(os.getcwd() + "\\start.txt", 'w') as file:
                file.write('0');
                but['text'] = "Создать базу"

    button2 = Button(c, text="Открыть базу", bg="#030069", font=10, fg="yellow", command=lambda: start_win(os.getcwd() + "\\XPassword.pfc"), overrelief=RIDGE, cursor="hand2")
    button2.bind("Double-1", lambda event: root.after(200, func=lambda: messagebox.showwarning("Ошибка", "Слишком частый вызов на кнопку!")))
    button2.place(x=15, y=360, height=30, width=276);
    chek_but(button2)

    CreateToolTip(button1, "Сгенерировать пароль по выше указанным параметрам")
    # CreateToolTip(button2, "Создать окно с сохраненными данными от ваших аккаунтов")
    CreateToolTip(ch4, "Если ДА, то созданный пароль скопируется")
    CreateToolTip(entry1, "Создание пароля в N символов")

    CreateToolTip(but_1, "Длина пароля будет 8 символов")
    CreateToolTip(but_2, "Длина пароля будет 12 символов")
    CreateToolTip(but_3, "Длина пароля будет 16 символов")

start()
Main()

def exit():
    root.destroy()
    raise SystemExit


def about():
    global toplevel_about
    try:
        toplevel_about.destroy()
    except:
        pass
    toplevel_about = Toplevel(root)
    toplevel_about.geometry("350x100")

    c_about = Canvas(toplevel_about, bg="#030069", height=105, width=405)
    c_about.place(x=-5, y=-5)

    toplevel_about.title("PFCP")
    label1_about = Label(toplevel_about, text="Program for create your password 2018 16", font=20, bg="#030069",
                         fg="yellow").place(x=0, y=0, width=350)
    label2_about = Label(toplevel_about, text="Powered by", bg="#030069", fg="yellow").place(x=0, y=30)
    label3_about = Label(toplevel_about, text="Timur Tecnology", font=20, bg="#030069", fg="yellow").place(x=80,
                                                                                                           y=25)
    label4_about = Label(toplevel_about, text="@2017-2018 All rights reserved", bg="#030069", fg="yellow").place(x=0,
                                                                                                                 y=80)
    label5_about = Label(toplevel_about, text="Нашли ошибку? Пишите ...@mail.ru", bg="#030069", fg="yellow").place(
        x=0, y=60)


# root.wm_attributes("-disabled", 1)
# print(os.getcwd()+"\\"+"passwordV16.py")
def remap_password():
    global repassw_base


    try: close_win_()
    except: pass

    adress = os.getcwd() + '\XPassword.pfc'

    def repassw_base(passw, adress):
        print('Oper Repassw:', passw, adress)

        print(adress.split('\\')[-1].split(".")[0] + ".txt")
        with open(adress.split('\\')[-1].split(".")[0] + ".txt") as file:
            text = file.read()
        os.remove(adress[:-3] + "txt")
        os.remove(adress)

        encryptDecrypt("E", adress[:-1], passw, text)
        messagebox.showinfo("Выполнение операции", "Смена пароля успешно завершена, программа будет перезапущена")
        restart_prog()

    def check_passw():
        global password_d_e, check_win

        if os.path.isfile(adress) != True:
            messagebox.showerror(adress.split("\\")[-1], "Файл не найден!");
            return

        with open(adress, mode="rb") as file:
            text = file.read()[0:3].decode('utf-8')
            file.close()
            if text != "AES":
                print("AESasd")
                do_canncel = messagebox.askokcancel("Ошибка с файлом: {}".format(adress.split("\\")[-1]),
                                                    "Файл: {} не может быть прочитан, так как он был поврежден или не является файлом программы \nНажмите ОК, если хотите удалить поврежденный файл".format(
                                                        adress.split("\\")[-1]))
                if do_canncel == True:
                    os.remove(adress);
                    messagebox.showinfo("Операция с фалом", "Файл был успешно удален")
                else: return
            else: pass

        check_win = Toplevel()
        check_win.title("")
        # check_win.resizable(False, False)
        check_win.geometry("+%d+%d" % (root.winfo_rootx() + 50, root.winfo_rooty() + 50))
        check_win.geometry("180x180")
        check_win.resizable(False, False)
        check_win.protocol('WM_DELETE_WINDOW', lambda: check_win.destroy())
        check_win.bind("Map",
                       lambda event: check_win.geometry("+%d+%d" % (root.winfo_rootx() + 50, root.winfo_rooty() + 50)))

        check_c = Canvas(check_win, bg="blue")
        check_c.pack(fill=BOTH, padx=5)
        '''
        Label(check_win, text="Введите старый пароль:").place(x=0,y=0)
        Entry(check_win).place(x=3,y=20,width=150)

        Label(check_win, text="Введите новый пароль:").place(x=0,y=60)
        Entry(check_win).place(x=3,y=80,width=150)

        Label(check_win, text="Повторите новый пароль:").place(x=0, y=100)
        Entry(check_win).place(x=3, y=120, width=150)'''

        def eye_win(x_eye, y_eye, parent):
            lab_eye = Label(parent, image=eye_close, bg="white", cursor='hand2')
            lab_eye.place(x=x_eye, y=y_eye, height=18)
            lab_eye.bind("<Enter>", lambda event: lab_eye.config(relief=GROOVE))
            lab_eye.bind("<Leave>", lambda event: lab_eye.config(relief=FLAT))
            lab_eye.bind("<ButtonPress>",
                         lambda event: lab_eye.config(relief=GROOVE, image=eye_open) or parent.config(show=""))
            lab_eye.bind("<ButtonRelease>",
                         lambda event: lab_eye.config(relief=GROOVE, image=eye_close) or parent.config(show="*"))
            return lab_eye

        Label(check_c, text="Введите старый пароль:").pack(fill=BOTH)
        entr1 = Entry(check_c, show="*")
        entr1.pack(fill=BOTH)
        lab_eye_1 = eye_win(145, 0, entr1)

        root.after(50, lambda: entr1.focus_set())

        Label(check_c).pack(fill=BOTH)

        Label(check_c, text="Введите новый пароль:").pack(fill=BOTH)
        entr2 = Entry(check_c, show="*")
        entr2.pack(fill=BOTH)
        lab_eye_1 = eye_win(145, 0, entr2)

        Label(check_c, text="Повторите новый пароль:").pack(fill=BOTH)
        entr3 = Entry(check_c, show="*")
        entr3.pack(fill=BOTH)
        lab_eye_1 = eye_win(145, 0, entr3)

        def ok():
            password_d_e = entr1.get()
            do_2 = encryptDecrypt("D", adress, password_d_e)
            if do_2 == "[x] Password is False!":
                messagebox.showerror(adress.split("\\")[-1], "Пароль введен не верно!"); entr1.event_generate(
                    "<<SelectAll>>"); return
            else:
                pass
            print(do_2)

            password_1 = entr2.get()
            password_2 = entr3.get()
            if password_1 != password_2:
                messagebox.showinfo("Пароль", "Пароли не совпадают");
                entr2.focus_set();
                entr2.event_generate("<<SelectAll>>");
                print(adress);
                return
            else:
                check_win.destroy(); repassw_base(password_2, adress)

        def cancel():
            check_win.destroy()

        w = Button(check_win, text="OK", width=10, command=ok, default=ACTIVE)
        w.pack(side=LEFT, padx=5, pady=5)
        w = Button(check_win, text="Cancel", width=10, command=cancel)
        w.pack(side=RIGHT, padx=5, pady=5)

        # edit_top.deiconify()
        check_win.wait_visibility();
        check_win.grab_set();
        # edit_top.wait_window(root)
        check_win.transient(root)

    try: password_d_e = password_d_e;
    except: check_passw()



def copy_base(adress=os.getcwd() + "\\XPassword.pfc", adress_copy=os.environ["public"] + "\\XPasswcopy.pfc"):

    try: close_win_()
    except: pass

    def check_passw():
        password_d_e = simpl.askstring(str(adress.split("\\")[-1]), "Введите текущий пароль:", "*")
        if password_d_e == None: password_d_e = None; return False

        do_2 = encryptDecrypt("D", adress, password_d_e)
        print(adress)
        if do_2 == "[x] Password is False!": messagebox.showerror(adress.split("\\")[-1], "Пароль введен не верно!"); return
        os.remove(adress[:-3] + 'txt')

        if os.path.isfile(adress_copy) == True:
            if messagebox.askokcancel("Создание копии базы", "Копия базы будет перезаписана!?") == False: return False

        with open(os.getcwd() + '\\XPassword.pfc', 'rb') as file:
                text = file.read()
                file2 = open(adress_copy, 'wb')
                print('SDA:',adress_copy)
                file2.write(text)
                file2.close()
        if os.path.isfile(adress_copy) == True: messagebox.showinfo('Создание копии', 'Копия успешно создана\n'+adress_copy)
        else: messagebox.showerror("Ошибка",'Копия не может быть создана!')
        restoring_copy(True)
        return False

    if check_passw() == False: return
    if check_passw() == False: return
    if check_passw() == False: return
    messagebox.showerror("Ошибка", "Введен был 3 раза не правильно,\nПовторите еще раз позже!")

def checking_file(adress):
    try:
        if "." + adress.split("/")[-1].split(".")[-1] != ".pfc": messagebox.showwarning( "Ошибка с файлом:" + adress.split("/")[-1], "{}\nНе может быть прочитан, так как он не является файлом программы".format(adress)); return False
        with open(adress, mode="rb") as file:
            text = file.read()[0:3].decode('utf-8')
            if text != "AES":
                messagebox.showwarning("Ошибка с файлом:" + adress.split("/")[-1], "{}\nНе может быть прочитан, так как он был поврежден!".format(adress)); return False
    except UnicodeDecodeError: messagebox.showwarning("Ошибка с файлом:" + adress.split("/")[-1], "{}\nНе может быть прочитан, так как он был поврежден!".format(adress));return False



def restoring_copy(doing=False, adress=os.environ["Public"]+"\\XPasswcopy.pfc"):
    if doing == None:
        try: close_win_()
        except: pass

        if os.path.isfile(adress) == False: file_name = ""
        else: file_name = "XPasswcopy.pfc"
        adress = askopenfile(initialdir=os.environ["Public"], defaultextension=".pfc",initialfile=file_name, title="Выбор копии для восстановления"); print("Adress: ", adress);
        try:adress.close()
        except: return

        adress = str(adress)[25:-29]
        if checking_file(adress) == False: return
        print("Restoring copy:", adress)
        if os.path.isfile(adress) == False: messagebox.showerror("Ошибка", "Копия не может быть восстановлена\nОшибка: FileNotFoundError: XPasswcopy.pfc")
        else:
            restoring_copy(False, adress)
            start_adress = ""
            with open(os.getcwd() + "\\start.txt", "w") as file: file.write("1")
            close_win_()
        return

    if doing == False:
        close_win_()

        def check_passw():
            adress_copy = adress

            password_d_e = simpl.askstring(str('Восстановление копии'), "Введите пароль от копии:", "*")
            if password_d_e == None: password_d_e = None; return False
            if os.path.isfile(adress) == False: messagebox.showerror("Ошибка", "Копия не может быть востановлена\nОшибка: FileNotFoundError: XPasswcopy.pfc"); return False

            do_2 = encryptDecrypt("D", adress_copy, password_d_e)
            if do_2 == "[x] Password is False!": messagebox.showerror('Ошибка', "Пароль введен не верно!"); return
            else:
                try: os.remove(os.getcwd() + '\\XPassword.pfc')
                except: pass
                with open(adress_copy, 'rb') as file:
                    text = file.read()
                    with open(os.getcwd() + '\\XPassword.pfc', 'wb') as file2:
                        file2.write(text)
                os.remove(adress_copy[:-3] + 'txt');

                messagebox.showinfo("Восстановление копии", 'Копия была успешно восстановлена!\n\nПрограмма будет перезапущена!')
                #button2['command'] = lambda: start_win(os.getcwd() + "\XPassword.pfc")
                restart_prog()

        if check_passw() == False: return
        if check_passw() == False: return
        if check_passw() == False: return
        messagebox.showerror("Ошибка", "Введен был 3 раза не правильно,\nПовторите еще раз позже")

    if doing == True:
        if os.path.isfile(os.getcwd()+"\\XPassword.pfc") == False:
            m1.delete(0)
            m1.insert_command(0, label="Создать копию", state=DISABLED)
        else:
            m1.delete(0)
            m1.insert_command(0, label="Создать копию", command=lambda: copy_base())

        if os.path.isfile(adress) == True:
            m1.delete(2);
            m1.insert_command(2, label='Удалить копию', command=lambda: delete_copy())
        else:
            m1.delete(2);
            m1.insert_command(2, label='Удалить копию', state=DISABLED)


def delete_copy(event=None,adress_copy=os.environ["Public"]+"\\XPasswcopy.pfc"):
    info = messagebox.askokcancel("Удаление копии", 'Вы действительно хотите безвозвратно удалить копию?')
    if info == True:
        if os.path.isfile(adress_copy) == False: messagebox.showerror("Ошибка", "Копия не может быть востановлена\nКод ошибки: FileNotFoundError: "+adress_copy); return
        os.remove(adress_copy)
        if os.path.isfile(adress_copy) == False: messagebox.showinfo("Удаление копии",'Копия была успешно удалена!')
        root.after(100, lambda: restoring_copy(True))



# 'C:\\'+os.getlogin()+'\\XPassword.pfc', 'wb'

m = Menu(root, postcommand=lambda: root.after(0, lambda: restoring_copy(True)))
root.configure(menu=m)

m1 = Menu(m, tearoff=0)
m.add_cascade(label="Файл", menu=m1)
m1.add_command(label="Создать копию", command=lambda: copy_base())

submenu = Menu(m, tearoff=0)
submenu.add_command(label="Выбрать файл", command=lambda: restoring_copy(None))
m1.add_cascade(label="Восстановление копии", menu=submenu)
m1.add_command(label="Удалить копию", state=DISABLED)
m1.add_command(label="Сменить пароль", command=lambda: remap_password())


m1.add_separator()
m1.add_command(label="Выход", command=exit)

m2 = Menu(root, tearoff=0)
m.add_cascade(label="Помощь", menu=m2)
m2.add_command(label="О программе", command=about)

root = mainloop()
