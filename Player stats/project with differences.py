import csv
from tkinter import *
from PIL import ImageTk, Image
import os
from functools import partial

def signup1():
    def clicked(username,password):
        list1=[]
        list2=[]
        with open("team.csv",'r+') as csvfile:
            reader=csv.reader(csvfile,delimiter=',')
            for i in reader:
                list1.append(i)
        for i in range(len(list1)):
            if username.get()==list1[i][0]:
                print("Username taken")
                tkWindow1=Tk()
                tkWindow1.geometry('50x50')  
                tkWindow1.title('Try again')
                label1=Label(tkWindow1,text="TRY AGAIN\n Username taken").grid(row=0, column=0)
                
                return
            
            else:
                continue
        list2.append(username.get())
        list2.append(password.get())
        list2.append(jersey.get())
        list2.append(team.get())
        
        print(list2)
        for i in range(5):
            list2.append(0)
        list1.append(list2)
        with open("team.csv",'w',newline='') as csv_file:
            csv_rec=csv.writer(csv_file)
            csv_rec.writerows(list1)
            print("Login created")
            mainmenu() 
            tkWindow.destroy()
    tkWindow = Toplevel()  
    tkWindow.geometry('450x160')  
    tkWindow.title('Signup')
    tkWindow.configure(bg="black")

    #username label and text entry box
    usernameLabel = Label(tkWindow, text="\tUser Name\t\t",fg="red",bg="black",font="Consolas 10 bold italic").grid(row=0, column=2)
    username = StringVar()
    usernameEntry = Entry(tkWindow, textvariable=username).grid(row=0, column=5)  

    #password label and password entry box
    passwordLabel = Label(tkWindow,text="\tPassword\t\t",fg="red",bg="black",font="Consolas 10 bold italic").grid(row=1, column=2)  
    password = StringVar()
    passwordEntry = Entry(tkWindow, textvariable=password, show='*').grid(row=1, column=5)
    Jerseylabel = Label(tkWindow, text="\tJersey number\t\t",fg="red",bg="black",font="Consolas 10 bold italic").grid(row=4, column=2)
    jersey = StringVar()
    JerseyEntry = Entry(tkWindow, textvariable=jersey).grid(row=4, column=5)
    Teamlabel=Label(tkWindow, text="\tTeam name\t\t",fg="red",bg="black",font="Consolas 10 bold italic").grid(row=5, column=2)
    team=StringVar()
    TeamEntry=Entry(tkWindow,textvariable=team).grid(row=5, column=5)

    clicked=partial(clicked,username,password)
    #login button
    signupButton = Button(tkWindow, text="Signup",fg="red",bg="black",font="Consolas 14 bold ",command=clicked).grid(row=10, column=4)


    tkWindow.mainloop()



def updateplayer1():
    def updatep(name,points,threepointers,blocks):
            list2=[]
            f=open("team.csv",'r+')
            csv_rec=csv.reader(f)
            for i in csv_rec:
                if i[0]==str(name.get()):
                    sum1=int(i[4])+int(points.get())
                    list1=[i[0],i[1],i[2],i[3],int(i[4])+1,sum1,sum1/(int(i[4])+1),int(i[5])+int(blocks.get())]
                else:
                    list2.append(i)
            list2.append(list1)
            f.close()
            f=open("team.csv",'w+',newline='')
            csv_rec=csv.writer(f)
            csv_rec.writerows(list2)
            f.close()
     
                    
                    
            
                    
    updateplayer = Tk()  
    updateplayer.geometry('450x160')  
    updateplayer.title('Signup')
    updateplayer.configure(bg="black")
    nameLabel = Label(updateplayer, text="\tEnter player name\t\t",fg="red",bg="black",font="Consolas 10 bold italic").grid(row=0, column=2)
    name = StringVar()
    nameentry = Entry(updateplayer, textvariable=name).grid(row=0, column=5)  
    #threepointers label and text entry box
    threepointersLabel = Label(updateplayer, text="\tThree pointers scored\t\t",fg="red",bg="black",font="Consolas 10 bold italic").grid(row=2, column=2)
    threepointers = StringVar()
    threepointersEntry = Entry(updateplayer, textvariable=threepointers).grid(row=2, column=5)  

    #points label and points entry box
    pointsLabel = Label(updateplayer,text="\tEnter points\t\t",fg="red",bg="black",font="Consolas 10 bold italic").grid(row=1, column=2)  
    points = StringVar()
    pointsEntry = Entry(updateplayer, textvariable=points).grid(row=1, column=5)
    assistslabel = Label(updateplayer, text="\tassists number\t\t",fg="red",bg="black",font="Consolas 10 bold italic").grid(row=4, column=2)
    assists = StringVar()
    assistsEntry = Entry(updateplayer, textvariable=assists).grid(row=4, column=5)
    blockslabel=Label(updateplayer, text="\tBlocks\t\t",fg="red",bg="black",font="Consolas 10 bold italic").grid(row=5, column=2)
    blocks=StringVar()
    blocksEntry=Entry(updateplayer,textvariable=blocks).grid(row=5, column=5)


    #login button
    updateButton = Button(updateplayer, text="Update",fg="red",bg="black",font="Consolas 14 bold ",command=lambda:updatep(name,points,threepointers,blocks,assists,    )).grid(row=10, column=4)



        

def mainmenu():
    def display1(name):
        print (name.get())
        f=open("team.csv",'r+')
        csv_rec=csv.reader(f)
        for i in csv_rec:
            if i[0]==str(name.get()):
                um=Toplevel()
                um.title(name.get())
                um.configure(bg="black")
                fields=Label(um,text="NAME  TEAM   MATCHES  POINTS PPG  3PTS "  ,fg="white",bg="black").grid(row=0,column=0)
                str1 =   i[0] + "  "+ i[2] + "  " + i[3] + "  " +i[4] +"  " +i[5] +"  " + i[6] + "   " +i[7]
                str1=str1.upper()
                entername=Label(um,text=str1,fg="white",bg="black").grid(row=2,column=0)
                display.destroy()
                break
        else:
            print("No user found")
        mainloop()
            
        
    def displayplayerstat():
        display=Toplevel()
        display.title("DISPLAY")
        display.geometry("200x200")
        display.configure(bg="black")
        entername=Label(display,text="enter player name",fg="white",bg="black").grid(row=0,column=0)
        name1=StringVar()
        nameentry=Entry(display,textvariable=name1).grid(row=0, column=1)
        command=Button(display,text="DISPLAY",fg='white',bg='black',command=lambda:display1(name1)).grid(row=1, column=0)
        print(name1.get())
        
     
    menu=Toplevel()
    menu.configure(bg='black')
    menu.title("MAIN MENU")
    menu.geometry("500x500")
    label=Label(menu,text="MAIN MENU",fg="white",bg="black",activebackground="red",font="Ariel 16 bold underline").grid(row=0,column=0)
    displaybutton=Button(menu,text="DISPLAY PLAYER STATS",fg="white",bg="black",activebackground="red",font="Helvetica 14 bold",command=displayplayerstat).grid(row=2,column=0)
    displaybutton=Button(menu,text="ADD PLAYER DATA",fg="white",bg="black",activebackground="red",font="Helvetica 14 bold",command=updateplayer1()).grid(row=2,column=1)
    displaybutton=Button(menu,text="DELETE PLAYER ACCOUNT",fg="white",bg="black",activebackground="red",font="Helvetica 14 bold",command=menu.destroy).grid(row=3,column=0)
    displaybutton=Button(menu,text="CHANGE PASSWORD",fg="white",bg="black",activebackground="red",font="Helvetica 14 bold",command=menu.destroy).grid(row=3,column=1)

    mainloop()




def login2():
    def login1(username,password):
        f=open("team.csv",'r+')
        csv_rec=csv.reader(f)
        for i in csv_rec:
            if i[0]==str(username.get()):
                if i[1]==str(password.get()):
                    print(username.get(),"Logged in successfully")
                    tkWindow.destroy()
                    mainmenu()
                    f.close()

                    break
                else:
                    print("incorrect password")
                    break
                    login2()
                    return
               
                    
        else:
            print("wrong Username or password")
            print("try again")
            tkWindow.destroy()
            return
    #window

    tkWindow = Toplevel()  
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

def program():
    def clicked():
        login2()
    def signup():
        signup1()
    window=Tk()
    window.configure(bg='black')
    window.title("WELCOME")

    logo=ImageTk.PhotoImage(Image.open("rose.jpg"))
    img = ImageTk.PhotoImage(Image.open("signup.gif"))
    img1 = ImageTk.PhotoImage(Image.open("login.gif"))

    explanation = """PLAYER STATS."""
    word="""Signup HERE CLICK HERE"""

    w = Label(window, compound = CENTER,text=explanation,fg="white",bg="black",font = "Helvetica 18 bold italic",image=logo).pack(side="left")
    x = Label(window, compound = CENTER,text="""\n \n EXISTING USER? \n LOGIN  """,fg="red2",bg="black",font = "Helvetica 10 bold italic").pack(side="top")
    loginButton = Button(window,bg="red",image=img1,activebackground='black',command=clicked).pack(side="top")
    x = Label(window, compound = CENTER,text="""\n \n NEW MEMBER? \n SIGNUP    """,fg="red2",bg="black",font = "Helvetica 10 bold italic").pack(side="top")
    signupButton=Button(window,bg="red2",image=img,activebackground='black',command=signup).pack(side="top")

    window.mainloop()
program()
