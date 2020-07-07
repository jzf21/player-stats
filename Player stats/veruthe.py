from tkinter import*
tkWindow = Tk()

tkWindow.geometry('300x100')  
tkWindow.title('Login')
tkWindow.configure(bg="#b4da55")
#username label and text entry box
usernameLabel = Label(tkWindow, text="User Name",fg="#f42069",bg="#b4da55",font="Helvetica 14 bold").grid(row=0, column=0)
username = StringVar()
usernameEntry = Entry(tkWindow, textvariable=username).grid(row=0, column=1)  

#password label and password entry box
passwordLabel = Label(tkWindow,text="Password",fg="#f42069",bg="#b4da55",font="Helvetica 20 bold").grid(row=1, column=0)  
password = StringVar()
passwordEntry = Entry(tkWindow, textvariable=password, show='*').grid(row=1, column=1)
login1=partial(login1,username,password)



#login button
signupButton=Button(tkWindow,text="Login",fg="#f42069",bg="#b4da55",font="Helvetica 20 bold",activebackground="white").grid(row=6,column=0)
login1=partial(login1,username,password)
tkWindow.mainloop()
