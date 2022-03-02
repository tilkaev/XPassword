from tkinter import messagebox, Tk, Toplevel, Button



root = Tk()



top = Toplevel()
tops = Toplevel()

def start():
    tops.wait_visibility();
    tops.grab_set();
    tops.transient(top)

but = Button(root, text="Press", command=lambda: start() or messagebox.showinfo("Error", "Error"))
but.pack()

root.mainloop()