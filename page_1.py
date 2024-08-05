from tkinter import *
from tkinter import messagebox
import ast
import tkinter as tk

global root
global root1
global root2

# Create the main window
root = tk.Tk()
root.title('Login')
root.geometry('925x500+300+300')
root.configure(bg="#fff")
root.resizable(1,1)

def Login():
    username=user.get()
    password=pasw.get()

    file=open('datasheet.txt','r')
    d=file.read()
    r=ast.literal_eval(d)
    file.close()

    if username in r.keys() and password==r[username]:
        messagebox.showinfo("login!","login successfull")
        from pagey import police
        police(root)
    else:
        
        messagebox.showerror("Invalid","Invalid username or password")

############################################################################### 
def signin():
    window=Toplevel(root)
    window.title('Sign in')
    window.geometry('925x500+600+800')
    window.configure(bg="#fff")
    window.resizable(False,False)

    def signin():
        username=user.get()
        password=pasw.get()
        conform_password=cp.get()

        if password==conform_password:
            try:
                file=open('datasheet.txt','r+')
                d=file.read()
                r=ast.literal_eval(d)

                dict2={username:password}
                r.update(dict2)
                file.truncate(0)
                file.close()

                file=open('datasheet.txt','w')
                w=file.write(str(r))

                messagebox.showinfo('signin','Sucessful sign in')

            except:
                file=open('datasheet.txt','w')
                pp=str({'username':'password'})
                file.write(pp)
                file.close()

        else:
            messagebox.showerror('Invalid',"Both Password should match")

    def sign():
        window.destroy()

#insert image 
    img = PhotoImage(file='mini_project\police.png')
    Label(window,image=img,bg='white',width=600,height=500).place(x=1,y=1)

#frame foe signin details
    frame = Frame(window,width=350,height=550,bg="white")
    frame.place(x=480,y=50)

#heading of the frame
    heading =Label(frame,text='SIGN IN',fg='#57a1f8',bg='white',font=('Microsoft Yahei UI Light',23,'bold'))
    heading.place(x=100,y=5)

#textbox for username

    def on_entry(e):
        user.delete(0,'end')

    def on_leave(e):
        name=user.get()
        if name=='':
            user.insert(0,'USERNAME')

#---------------------------------------
            
    user= Entry(frame,width=25,fg='black',border=0,bg='white',font=('Microsoft Yahei UI Light',11))
    user.place(x=30,y=80)
    user.insert(0,'USERNAME')
    user.bind('<FocusIn>',on_entry)
    user.bind('<FocusOut>',on_leave)

    Frame(frame,width=295,height=2,bg='#57a1f8').place(x=25,y=107)

#textbox for password

    def on_entry(e):
        pasw.delete(0,'end')

    def on_leave(e):
        name=pasw.get()
        if name=='':
            pasw.insert(0,'PASSWORD')



#-----------------------------------
            
    pasw= Entry(frame,width=25,fg='black',border=0,bg='white',font=('Microsoft Yahei UI Light',11))
    pasw.place(x=30,y=150)
    pasw.insert(0,'PASSWORD')
    pasw.bind('<FocusIn>',on_entry)
    pasw.bind('<FocusOut>',on_leave)

    Frame(frame,width=295,height=2,bg='#57a1f8').place(x=25,y=177)

#textbox for conform password

    def on_entry(e):
        cp.delete(0,'end')

    def on_leave(e):
        name=cp.get()
        if name=='':
            cp.insert(0,'CONFORM PASSWORD')

#--------------------------------
            
    cp= Entry(frame,width=25,fg='black',border=0,bg='white',font=('Microsoft Yahei UI Light',11))
    cp.place(x=30,y=220)
    cp.insert(0,'CONFORM PASSWORD')
    cp.bind('<FocusIn>',on_entry)
    cp.bind('<FocusOut>',on_leave)

    Frame(frame,width=295,height=2,bg='#57a1f8').place(x=25,y=247)

    #insert button 
    Button(frame,width=39,pady=7,text='Sign in',bg='#57a1f8',fg='white',border=0,command=signin).place(x=35,y=280)
    label = Label(frame,text="Already have an account??",fg='black',bg='white',font=('Microsoft Yahei UI Light',9))
    label.place(x=90,y=340)

    Log_in = Button(frame,width=6,text='Login',border=0,bg='white',cursor='hand2',fg='#57a1f8',command=sign)
    Log_in.place(x=240,y=340)
    window.mainloop()


###############################################################

#insert image 
img = PhotoImage(file='mini_project\pic1.png')
Label(root,image=img,bg='white',width=500,height=500).place(x=1,y=1)

#frame foe signin details
frame = Frame(root,width=350,height=350,bg="white")
frame.place(x=480,y=70)

#heading of the frame
heading =Label(frame,text='LOGIN',fg='#57a1f8',bg='white',font=('Microsoft Yahei UI Light',23,'bold'))
heading.place(x=100,y=5)

#textbox for username

def on_entry(e):
    user.delete(0,'end')

def on_leave(e):
    name=user.get()
    if name=='':
        user.insert(0,'USERNAME')

#------------------------------
        
user= Entry(frame,width=25,fg='black',border=0,bg='white',font=('Microsoft Yahei UI Light',11))
user.place(x=30,y=80)
user.insert(0,'USERNAME')
user.bind('<FocusIn>',on_entry)
user.bind('<FocusOut>',on_leave)

Frame(frame,width=295,height=2,bg='#57a1f8').place(x=25,y=107)

#textbox for password

def on_entry(e):
    pasw.delete(0,'end')

def on_leave(e):
    name=pasw.get()
    if name=='':
        pasw.insert(0,'PASSWORD')
#--------------------------------
pasw= Entry(frame,width=25,fg='black',border=0,bg='white',font=('Microsoft Yahei UI Light',11))
pasw.place(x=30,y=150)
pasw.insert(0,'PASSWORD')
pasw.bind('<FocusIn>',on_entry)
pasw.bind('<FocusOut>',on_leave)

Frame(frame,width=295,height=2,bg='#57a1f8').place(x=25,y=177)

#insert button 
Button(frame,width=39,pady=7,text='Login',bg='#57a1f8',fg='white',border=0,command=Login).place(x=35,y=204)
label = Label(frame,text="Do not have an account??",fg='black',bg='white',font=('Microsoft Yahei UI Light',9))
label.place(x=75,y=270)

Log_in = Button(frame,width=6,text='Sign in',border=0,bg='white',cursor='hand2',fg='#57a1f8',command=signin)
Log_in.place(x=215,y=270)

root.mainloop()