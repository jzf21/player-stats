import csv
from tkinter import *
from functools import partial

def login2():
    def login1(username,password):
        f=open("team.csv",'r+')
        csv_rec=csv.reader(f)
        for i in csv_rec:
            if i[0]==str(username.get()):
                if i[1]==str(password.get()):
                    print(username.get(),"Logged in successfully")
                    import mainmenu.py
                    f.close()

                    break
                else:
                    print("incorrect password")
                    break
                    import login.py
                    return
               
                    
        else:
            print("wrong Username or password")
            print("try again")
            tkWindow.destroy()
            return
    #window

    tkWindow = Tk()  
    tkWindow.geometry('200x100')  
    tkWindow.title('Login')
    tkWindow.configure(bg="black")
    #username label and text entry box
    usernameLabel = Label(tkWindow, text="User Name",fg="red2",bg="black",font="Helvetica 14 bold").grid(row=0, column=0)
    username = StringVar()
    usernameEntry = Entry(tkWindow, textvariable=username).grid(row=0, column=1)  

    #password label and password entry box
    passwordLabel = Label(tkWindow,text="Password",fg="red2",bg="black",font="Helvetica 14 bold").grid(row=1, column=0)  
    password = StringVar()
    passwordEntry = Entry(tkWindow, textvariable=password, show='*').grid(row=1, column=1)

    #login button
    signupButton=Button(tkWindow,text="Login",fg="red2",bg="black",font="Helvetica 14 bold",activebackground="white",command=lambda:login1(username,password)).grid(row=6,column=0)
    tkWindow.mainloop()
login2()
