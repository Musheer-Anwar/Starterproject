'''from tkinter import *
#create the window
root=Tk()
#set the dimensions
root.geometry("300x300")
#create a button
btn=Button(root,text="Musheer",bd="10",command=root.destroy)
#set the position of the button---pack,place,grid
btn.pack(side="right")
#main loop
root.mainloop()''




#messgae box using a button having user defined function.
import tkinter
from tkinter import messagebox
root=tkinter.Tk()
def hello():
    messagebox.showinfo("Welcome","1:- Hello! My name is Mohammad Musheer Anwar. I lived in Aligarh(UP)")
btn=tkinter.Button(root,text="click me", command=hello)
root.geometry("400x400")
btn.pack()
root.mainloop()



'' 
import tkinter
from tkinter import *
root=Tk()
cv=tkinter.Canvas(root, bg="blue",height=300, width=300)
cv.pack()
root.mainloop()'''

'''
import tkinter
from tkinter import *
root=tkinter.Tk()
cv=tkinter.Canvas(root,bg="red",height=500,width=500)
coordinate= 30,70,150,210
arc=cv.create_arc(coordinate,start=0,extent=120,fill="black")
cv.pack()
root.mainloop()

''

from tkinter import *
root=Tk()
root.geometry("400x400")
#create a label
lb1=Label(root,text="Name")
lb1.grid(row=1,column=1)

lb1=Label(root,text="Roll no")
lb1.grid(row=2,column=1)

lb1=Label(root,text="section")
lb1.grid(row=3,column=1)

lb1=Label(root,text="class")
lb1.grid(row=4,column=1)

lb1=Label(root,text="DOB")
lb1.grid(row=5,column=1)

ent1=Entry(root, bd=5)
ent1.grid(row=1,column=2)


ent1=Entry(root, bd=5)
ent1.grid(row=2,column=2)


ent1=Entry(root, bd=5)
ent1.grid(row=3,column=2)


ent1=Entry(root, bd=5)
ent1.grid(row=4,column=2)



ent1=Entry(root, bd=5)
ent1.grid(row=5,column=2)


btn=Button(root,text="Enter")
btn.grid(row=6,column=2)

root.mainloop()

''

from tkinter import *
root=Tk()
root.geometry("500x600")
sutdname=Label(root,text="Name")
studname.pack(side=LEFT)
regno=Label(root, text="Regno")
regno.pack(side=LEFT)
password=Label(root,text="Password")
password.pack(side=LEFT)

submitbtn=Button(root,text="Submit",activebackground="pink",activeforeground="blue").place(x=30,y=170)

ent1=Entry(root).pack(side=RIGHT)
ent2=Entry(root).pack(side=RIGHT)
ent3=Entry(root).pack(side=RIGHT)

root.mainloop()



from tkinter import *
root=Tk()

lb1=Label(root,text="Nmae")
lb2=Label(root,text="Section")
lb3=Label(root,text="Rollno")
lb4=Label(root,text="MobNo")
lb5=Label(root,text="RegNo")

lb1.pack(side=LEFT)
lb2.pack(side=LEFT)
lb3.pack(side=LEFT)
lb4.pack(side=LEFT)
lb5.pack(side=LEFT)

en1=Entry(root, bd=5)
en2=Entry(root, bd=5)
en3=Entry(root, bd=5)
en4=Entry(root, bd=5)
en5=Entry(root, bd=5)

en1.pack(side=RIGHT)
en2.pack(side=RIGHT)
en3.pack(side=RIGHT)
en4.pack(side=RIGHT)
en5.pack(side=RIGHT)

root.mainloop()


''

#Frame consistinf different buttons

from tkinter import *
root=Tk()

topfr=Frame(root).pack()
#topfr.pack()
bottomfr=Frame(root).pack(side=BOTTOM)
#bottomfr.pack(side=BOTTOM)
redbtn=Button(topfr, text="Red",bg="Red")
redbtn.pack()
bluebtn=Button(topfr, text="Blue",fg="Blue")
bluebtn.pack()
greenbtn=Button(topfr, text="Green",fg="Green")
greenbtn.pack()
blackbtn=Button(bottomfr, text="Black",fg="Black")
blackbtn.pack(side=BOTTOM)
root.mainloop()

''
from tkinter import *
root=Tk()

root.geometry("300x300")
topfr=Frame(root)
topfr.pack()
btmfr=Frame(root)

lb1=Label(topfr,text="Username")
lb1.grid(row=1,column=1)

lb2=Label(topfr,text="Password")
lb2.grid(row=2,column=1)

en1=Entry(topfr,bd=5)
en1.grid(row=1,column=2)

en2=Entry(topfr,bd=5)
en2.grid(row=2,column=2)
btmfr.pack(side=BOTTOM)
btn=Button(topfr,text="name")
btn.grid(row=3,column=3)

lb3=Label(btmfr,text="name")
lb3.grid(row=1,column=1)

ent3=Entry(btmfr,bd=5)
ent3.grid(row=1,column=2)

btmfr.pack(side=BOTTOM)
btn=Button(btmfr,text="register",bd=5)
btn.grid(row=3,column=3)
root.mainloop()
          
''

from tkinter import *
root=Tk()

lb=Listbox(root)
lb.insert(1,"1-Python")
lb.insert(2,"2-C++")
lb.insert(3,"3-java")
lb.insert(4,"4-C")
lb.insert(5,"5-Python")

lb.pack(anchor=N)
root.mainloop()

''

#Radio Button

from tkinter import *
root=Tk()

var=IntVar()
def select():
    display="Your selection is:"+ str(var.get())
    lbl.config(text=display)

rd1=Radiobutton(root,text="option 1",variable=var,value=1,command=select)
rd1.grid(row=1,column=1)

rd2=Radiobutton(root,text="option 2",variable=var,value=2,command=select)
rd2.grid(row=1,column=2)

rd3=Radiobutton(root,text="option 3",variable=var,value=3,command=select)
rd3.grid(row=1,column=3)

lbl=Label(root)
lbl.grid(row=2,column=2)

root.mainloop()

''


# Connecting two windows
from tkinter import *
root=Tk()
root.geometry("300x300")

def select():
    roott=Tk()
    roott.geometry("200x200")
    roott.mainloop()
btn=Button(root,text="open",command=select)
btn.pack()
root.mainloop()

''
#Relief styles

from tkinter import*
root=Tk()

b1=Button(root, text="FLAT", relief=FLAT, bd=8)
b2=Button(root, text="RAISED", relief=RAISED, bd=10)
b3=Button(root, text="SUNKEN", relief=SUNKEN, bd=10)
b4=Button(root, text="GROOVE", relief=GROOVE,bd=5)
b5=Button(root, text="RIDGE", relief=RIDGE, bd=5)

b1.pack()
b2.pack()
b3.pack()
b4.pack()
b5.pack()

root.mainloop() 

''
from tkinter import *
root=Tk()

lb1=Label(root, text="Name")
lb1.pack(side=LEFT)
e1=Entry(root,bd=4)
e1.pack()

root.mainloop()

''

import tkinter
from tkinter import *
root=Tk()
cv=tkinter.Canvas(root,bg="seagreen",height=300,width=400)
coordinate= 50,50,350,200  #right, top, left, bottom
arc=cv.create_arc(coordinate, start=0, extent=120,fill="blue")

cv.pack()

root.mainloop()

''


import tkinter
from tkinter import *
root=Tk()
root.geometry("300x300")
''
lb1=Label(root,text="Name").place(x=10,y=10)
lb2=Label(root,text="Section").place(x=10,y=30)
lb3=Label(root,text="Roll.No").place(x=10,y=50)
lb4=Label(root,text="Reg.No").place(x=10,y=70)
lb5=Label(root,text="Mob.No").place(x=10,y=90)

en1=Entry(root,bd=5).place(x=100,y=10)
en2=Entry(root,bd=5).place(x=100,y=30)
en3=Entry(root,bd=5).place(x=100,y=50)
en4=Entry(root,bd=5).place(x=100,y=70)
en5=Entry(root,bd=5).place(x=100,y=90)
''
#or packing using grid 

lb1=Label(root,text="Name").grid(row=1,column=1)
lb2=Label(root,text="Section").grid(row=2,column=1)
lb3=Label(root,text="Roll.No").grid(row=3,column=1)
lb4=Label(root,text="Reg.No").grid(row=4,column=1)
lb5=Label(root,text="Mob.No").grid(row=5,column=1)

en1=Entry(root,bd=5).place(x=100,y=10)
en2=Entry(root,bd=5).place(x=100,y=30)
en3=Entry(root,bd=5).place(x=100,y=50)
en4=Entry(root,bd=5).place(x=100,y=70)
en5=Entry(root,bd=5).place(x=100,y=90)
''
btn=Button(root,text="Submit",activebackground="seagreen",activeforeground="yellow", relief=RAISED).place(x=150,y=120)

root.mainloop()
''

# Frames consisiting of different Buttons:-

import tkinter
from tkinter import *
root=Tk()
topfr=Frame(root)
topfr.pack()
bottomfr=Frame(root)
bottomfr.pack(side=BOTTOM)

btn1=Button(topfr,text="Musheer",relief=GROOVE,bd=10).pack(side=RIGHT)
btn2=Button(topfr,text="SmartBoy",relief=RAISED,bd=8).pack(side=RIGHT)

btn3=Button(bottomfr,text="Hello",relief=FLAT,bd=5).pack(side=TOP)
btn4=Button(bottomfr,text="Sorry",relief=RIDGE,bd=5).pack()

root.mainloop()
''


import tkinter
from tkinter import *
root=Tk()
login=Frame(root)
registration=Frame(root)

lb1=Label(login,text="UserName").grid(row=1,column=1)
lb2=Label(login,text="Password").grid(row=2,column=1)

en1=Entry(login,bd=5).grid(row=1,column=2)
en2=Entry(login,bd=5).grid(row=2,column=2)
btn=Button(login,text="OK", relief=RIDGE, fg="blue").grid(row=3,column=2)

login.pack(anchor=NW)

lb3=Label(registration,text="EnterName").grid(row=1,column=1)
lb4=Label(registration,text="Create Password").grid(row=2,column=1)

en3=Entry(registration,bd=5).grid(row=1,column=2)
en4=Entry(registration,bd=5).grid(row=2,column=2)
btn=Button(registration,text="Click", relief=RIDGE, fg="green").grid(row=3,column=2)

registration.pack(side=BOTTOM)

root.mainloop()
'''

from tkinter import *
root=Tk()
lb=Listbox(root)
lb.insert(1,"Musheer")
lb.insert(2,"Arham")
lb.insert(3,"Ravi")
lb.insert(4,"Sudeep")
lb.insert(5,"Harsh")

lb.pack()
root.mainloop()
'''

# Radio Buttons

from tkinter import *
root=Tk()
def select():
    display="Your selection is:" +str(var.get())
    lbl.config(text=display)         

var=IntVar()
             
rd1=Radiobutton(root,text="Option 1",value=1,variable=var,command=select).grid(row=1,column=1)
rd2=Radiobutton(root,text="Option 2",value=2,variable=var,command=select).grid(row=1,column=2)
rd3=Radiobutton(root,text="Option 3",value=3,variable=var,command=select).grid(row=1,column=3)
rd4=Radiobutton(root,text="Option 4",value=4,variable=var,command=select).grid(row=1,column=4)

lbl=Label(root)
lbl.grid(row=2,column=2)
             
root.mainloop()

''

#Practice
from tkinter import *
root=Tk()

rd1=Radiobutton(root,text="mohammad",value=5).grid(row=1,column=1)
rd2=Radiobutton(root,text="musheer",value=2).grid(row=1,column=2)
rd3=Radiobutton(root,text="anwar",value=8).grid(row=1,column=3)

root.mainloop()
''


#Check button practice
from tkinter import *
root=Tk()

ch1=Checkbutton(root,text="Mohammad",onvalue=1,offvalue=2).place(x=10,y=10)
ch2=Checkbutton(root,text="Musheer",onvalue=1,offvalue=2).place(x=100,y=10)
ch3=Checkbutton(root,text="Anwar",onvalue=1,offvalue=2).place(x=170,y=10)
 

root.mainloop()
''

#MENU BUTTON AND SUB MENU
from tkinter import *
root=Tk()

mb=Menubutton(root,text="Open")

mb.menu=Menu(mb)
mb["menu"]=mb.menu

var1=IntVar()
var2=IntVar()
var3=IntVar()

mb.menu.add_checkbutton(label="Class",variable=var1)
mb.menu.add_checkbutton(label="Section",variable=var2)
mb.menu.add_checkbutton(label="Roll.No",variable=var3)
mb.pack()

root.mainloop()
''

#CONNECTING ONE WINDOW TO ANOTHER
from tkinter import *
root=Tk()

def new():
    roott=Tk()
    btn=Button(roott, text="Click or select").pack(side=RIGHT)
    roott.mainloop()

btn=Button(root,text="new window",command=new).pack(anchor=NW)

root.mainloop()
'''    

























