from tkinter import *
def subm():
    u=e.get()
    f=open(u+'.txt','w')
    f.write(e1.get())
    f=open(u+'.txt','r')
    k=f.read()
    print(k)
def submit():
    u=e.get()
    n=e1.get()
    f=open(u+'.txt','r')
    k=f.read()
    if n==k:
        ro=Tk()
        g=Label(ro,text='welcome').pack()
        ro.mainloop()
    else:
        print("hello")
        ro=Tk()
        g=Label(ro,text='USER NAME OR PASSWORD INCORRECXT').pack()
        ro.mainloop()
def h():
    root=Tk()
    b=Label(root,text='USER NAME',fg='blue')#tkinter GUI
    b.grid(row=0,column=0)
    e=Entry(root)
    e.grid(row=0,column=1)
    b1=Label(root,text='PASSWORD',fg='blue')#tkinter GUI
    b1.grid(row=1,column=0)
    e1=Entry(root)
    e1.grid(row=1,column=1)
    b3=Button(root,text='Login',command=submit)#command is used for calling a function
    b4=Button(root,text='signup',command=subm)#command is used for calling a function

    b3.grid(row=2,column=2)
    b4.grid(row=1,column=2)

    root.mainloop()


main=Tk()
main.geometry("200x200")
button=Button(main,text='login',command=h).grid(row=1,column=2)
button1=Button(main,text='signup',command=h).grid(row=1,column=1)
main.mainloop()
