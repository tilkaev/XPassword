from tkinter import*

root = Tk()
root.title("Окно #1")
root.geometry("300x200")
root.wm_geometry("+%d+%d" % (500, 200))


top = Toplevel()
top.title("Окно #2")
top.geometry("300x200")
root.after(50, lambda: top.wm_geometry("+%d+%d" % (root.winfo_x()-320, root.winfo_y())))


class magnet_win():
    def __init__(self, win_2):
        self.top = win_2
        root.bind("<Configure>", lambda event: self.replace_win_2())
        #self.top.bind("<Configure>", lambda event: self.replace_win_1())


    def replace_win_2(self):#Drag root

        x = root.winfo_x()
        y = root.winfo_y()

        if (root.winfo_rootx() - 310) < 0:
            top.wm_geometry("+%d+%d" % (x + 300+20, y))
        else:
            top.wm_geometry("+%d+%d" % (x - 300-20, y))


    def replace_win_1(self):#Drag top

        x = self.top.winfo_x()
        y = self.top.winfo_y()

        if (root.winfo_rootx() - 310) < 0:
            root.wm_geometry("+%d+%d" % (x - 320, y))
        else:
            root.wm_geometry("+%d+%d" % (x + 320, y))

root.after(100, lambda: magnet_win(top))



root.mainloop()