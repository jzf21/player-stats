from tkinter import*
from functools import partial
import csv
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
        updateButton = Button(updateplayer, text="Update",fg="red",bg="black",font="Consolas 14 bold ",command=lambda:updatep(name,points,threepointers,blocks)).grid(row=10, column=4)


        updateplayer.mainloop()
updateplayer1()
