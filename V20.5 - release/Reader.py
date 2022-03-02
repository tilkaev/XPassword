from tkinter import*

import pyAesCrypt
from os import remove
from os.path import splitext


root = Tk()
root.wm_attributes("-topmost", 1)
root.geometry("565x150")
root.wm_geometry("+%d+%d" % (-10, 0))


def default():
    root.title("")
default()

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
            print(file)
            pyAesCrypt.decryptFile(str(file), str(file[:-4]) + ".txt", password, bufferSize)
            
            #remove(file)
        except FileNotFoundError:
            return "[x] File is not found!"
        except ValueError:
            return "[x] Password is False!"
        else:
            print("[+] File '" + str(splitext(file)[0]) + ".pfc' overwritten!")
            text = open(str(file[0:-4]) + ".txt", "r")
            base = text.read()
            text.close()
            return base, str(str(splitext(file)[0]) + ".txt")




def save():

    file = entr1.get()
    password = entr2.get()

    base = open(file, "w")
    base.write(text.get("1.0", END))
    base.close()

    print(encryptDecrypt("E", file, password, text.get("1.0",END)))



def reader():
    global base
    print("Read")

    file = entr1.get()
    password = entr2.get()

    base,rem = encryptDecrypt("D", file, password)
    #print(base)
    remove(rem)

    CoNfigure(base)

    text.delete("1.0", END)
    text.insert("1.0", base)

def copy():

    root.clipboard_clear()
    root.clipboard_append(text.get("1.0", END))

    root.title("copy")
    id = root.after(1600, default)

def CoNfigure(base="None"):

    x = root.winfo_width()
    y = root.winfo_height()
    #print(x, y)
    text.place(width=x-110, height=y+50)
    but1.place(x=x - 105)
    but2.place(x=x - 105)
    but3.place(x=x - 105)
    but4.place(x=x - 65)
    entr1.place(x=x - 105)
    entr2.place(x=x - 105)
    but5.place(x=x - 50)

def Mode_Select():
    global mods
    if mods == "pf":
        print("Error")
        but4["text"] = "D"
        mods = "pfc"
        entr1.delete(0, END)
        entr1.insert(0, "XPassword."+mods)
        but1["state"] = "activ"
        but2["state"] = "disabled"
        return
    if mods == "pfc":
        but4["text"] = "E"
        mods = "pf"
        entr1.delete(0, END)
        entr1.insert(0, "XPassword." + mods)
        but1["state"] = "disabled"
        but2["state"] = "activ"
        return


def open_win():
    but5.configure(text='-', command=curtail_win)
    root.geometry("{}x{}".format(wid, hei))
    root.wm_geometry("+%d+%d" % (wid_, hei_))

def curtail_win():
    global wid, hei, wid_, hei_
    wid = root.winfo_width()
    hei = root.winfo_height()

    wid_ = root.winfo_rootx()
    hei_ = root.winfo_rooty()

    root.wm_geometry("+%d+%d" % (-10, 995))
    but5.configure(text='+', command=open_win)
    root.geometry(str(root.winfo_width())+"x13")



base = "None"
root.bind("<Configure>",lambda event: CoNfigure(base))

text = Text(root,height=10)
text.place(x=0,y=0,width=455)

but1 = Button(text="Read",command=reader, state="disabled")
but1.place(x=460,y=0)

but2 = Button(text="Save",command=save)
but2.place(x=460,y=25)

but3 = Button(text="Copy",command=copy)
but3.place(x=460,y=50)

but5 = Button(text="-",command=curtail_win, relief=FLAT, overrelief=FLAT)
but5.place(x=500, y=-5, height=20, width=50)

mods="pf"
but4 = Button(text="E", command=Mode_Select)
but4.place(x=500,y=50)

entr1 = Entry()
entr1.insert(1,"XPassword."+mods)
entr1.place(x=460,y=75,width=100)

entr2 = Entry()
entr2.insert(1,"1242")
entr2.place(x=460,y=100,width=100)



root.mainloop()

