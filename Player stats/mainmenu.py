from tkinter import*
import csv
from functools import partial
from PIL import ImageTk, Image
def mainmenu():
    def display1(name):
        print (name.get())
        f=open("team.csv",'r+')
        csv_rec=csv.reader(f)
        for i in csv_rec:
            if i[0]==str(name.get()):
                print(i)
                um=Toplevel()
                um.title(name.get())
                um.configure(bg="black")
                fields=Label(um,text="NAME  TEAM   MATCHES  POINTS PPG  3PTS "  ,fg="white",bg="black").grid(row=0,column=0)
                str1 =   i[0] + "  "+ i[2] + "  " + i[3] + "  " +i[4] +"  " +i[5] +"  " + i[6] + "   " +i[7]
                str1=str1.upper()
                entername=Label(um,text=str1,fg="white",bg="black").grid(row=2,column=0)
                
                break
        else:
            print("No user found")
        mainloop()
            
    def updateplayerdata():
        updateplayer=Toplevel()
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
        
     
    menu=Tk()
    menu.configure(bg='black')
    menu.title("MAIN MENU")
    menu.geometry("500x500")
    label=Label(menu,text="MAIN MENU",fg="white",bg="black",activebackground="red",font="Ariel 16 bold underline").grid(row=0,column=0)
    displaybutton1=Button(menu,text="DISPLAY PLAYER STATS",fg="white",bg="black",activebackground="red",font="Helvetica 14 bold",command=displayplayerstat).grid(row=2,column=0)
    displaybutton2=Button(menu,text="ADD PLAYER DATA",fg="white",bg="black",activebackground="red",font="Helvetica 14 bold",command=displayplayerstat).grid(row=2,column=1)
    displaybutton3=Button(menu,text="DELETE PLAYER ACCOUNT",fg="white",bg="black",activebackground="red",font="Helvetica 14 bold",command=menu.destroy).grid(row=3,column=0)
    displaybutton4=Button(menu,text="CHANGE PASSWORD",fg="white",bg="black",activebackground="red",font="Helvetica 14 bold",command=menu.destroy).grid(row=3,column=1)

    mainloop()
mainmenu()
