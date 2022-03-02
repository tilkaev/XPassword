from tkinter import*

def listbox():
    def image_get(list_):
        global image_1
        if int(list_.curselection()[0]) == 0:
            print("Run")
            image_1 = PhotoImage(file="./1.png")
            lab = Label(root, bg="white", image = image_1)
            lab.place(x=10, y=10, width=100, height=100)

    top = Toplevel(root)
    list_ = Listbox(top,width=20)

    list_.insert(END,'image 0','image 1','image 2','image 3','image 4','image 5', 'image 6','image 7','image 8','image 9')
    list_.pack()
    list_.bind("<Double-1>", lambda event: image_get(list_) or top.destroy())


root = Tk()




king = Menu(root, postcommand=lambda: listbox())

root.config(menu=king)
view = Menu(king,tearoff = 0)
#view.add_command(label='Background',command=None)
king.add_cascade(label="View",menu=view)

root.mainloop()