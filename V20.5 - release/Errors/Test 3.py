from tkinter import*

from tkinter.colorchooser import*

def getColor():
    color = askcolor()
    print(color)
    text['fg'] = color[1]

root=Tk()
text=Text(root)
text.pack()

king=Menu(root)
root.config(menu=king)

view= Menu(king,tearoff = 0)

view2=Menu(view,tearoff=0)
view2.add_command(label='Color',command=getColor)

view.add_cascade(label='Text',menu=view2)

king.add_cascade(label="View",menu=view)

root.mainloop()