import tkinter
from tkinter import*
from tkinter import messagebox as mb
root=Tk()

root.title("space invaders")
root.geometry("400x400")
c = Canvas(root, width=400, height=400, bg='black')
c.focus_set()
c.pack()
flag=1
x=180
k =0
nomeri=["nomer0","nomer1","nomer2","nomer3","nomer4","nomer5","nomer6","nomer7","nomer8","nomer9","nomer10","nomer11"]
line1=c.create_line(10,0,10,400, fill="white", width=7)
line2=c.create_line(390,0,390,400, fill="white", width=7)
tri = c.create_polygon(x+20, 345, x, 385, x+40, 385, fill='white')
#funcs
#motion
def right(self):
    c.move(tri, 6, 0)
    t = c.coords(tri)
    if t[4] >390:
        root.after(1, left(self))
def left(self):
      c.move(tri, -6, 0)
      c.update()
      if c.coords(tri)[2]<10:
          root.after(1,right(self))
#shoooting
def shooting(event):
    global k
    global nomer
    global flag
    if k==11:
        k=0
    elif flag==1:
     t = c.coords(tri)
     enemy=c.create_line(t[0], t[1], t[0], t[1]+20, width=5, fill="yellow", tag="shot")
     flag=0
     move_shot("shot")
def draw_enemy():
    global enemy

    # enemy=c.create_polygon(20,20,50,20,50,50,20,50, fill="white")
    line=c.create_line(50,50,20,50, fill="red", width=7)
    enemy = c.create_rectangle(20, 20, 50,50,fill="white",tag="enemy")


def move_shot(name):
        global enemy
        global k
        global flag
        c.move(name, 0, -20)
        c.update()
        if c.coords("shot") == c.find_overlapping(20, 20, 50,50):
            c.delete(name)
            flag = 1
            k = k + 1

        elif c.coords(name)[3]>0:
            root.after(50, move_shot, name)

        else:
            c.delete(name)
            flag=1
            k=k+1


        def kill(event):
            global flag
            global k
            if "shot" in c.fing_overlapping(20,20,50,50):
                c.delete("shot")
                c.delete(enemy)
                flag=1
                k=k+1

draw_enemy()
# move_enemy()
c.bind('<Left>', left)
c.bind('<Right>',right)
c.bind('<Up>',shooting )


root.mainloop()