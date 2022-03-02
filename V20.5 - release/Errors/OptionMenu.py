
class Option_Menu():
    import tkinter as tk
    def __init__(self, master, value=("Пример 1","Пример 2","Пример 3"), default=0,**kw):
        self.master = master
        self.value = value
        self.default = default
        self.max = len(value)

        self.lab = Label(master, text=str(value[default]), **kw)

        self.menu = Menu(tearoff=0)

        for i, txt in enumerate(value):
            self.menu.add_command(label=txt, command=lambda num=int(i): self.remap_default(num, value))
        #self.menu.add_command(label="Пример 1", command=lambda: self.remap_default(0))
        #self.menu.add_command(label="Пример 2", command=lambda: self.remap_default(1))
        self.relief()


    def func(self, event):
        self.menu.post(event.x_root, event.y_root)

    def remap_default(self, num, value):
        print(num)
        self.default = num
        self.lab["text"] = value[num]

    def relief(self, rel1=tk.FLAT, rel2=tk.RIDGE):
        self.lab.bind("<Leave>", lambda event: self.config(relief=rel1))
        self.lab.bind("<Enter>", lambda event: self.config(relief=rel2))

        self.lab.bind("<ButtonPress>", lambda event: self.config(relief=SUNKEN))
        self.lab.bind("<ButtonRelease>", self.func)

    def pack(self, cnf={}, **kw):
        self.lab.pack(cnf, **kw)

    def place(self, cnf={}, **kw):
        self.lab.place(cnf, **kw)

    def config(self, cnf=None, **kw):
        self.lab.config(cnf, **kw)
    configure = config




if __name__ == '__main__':
    from tkinter import*
    root = Tk()
    root.geometry("200x100")
    opt = Option_Menu(root, ("Text","sads"),cursor='hand2', relief=RIDGE)
    opt.relief(RIDGE, RAISED)
    opt.pack()



    root.mainloop()