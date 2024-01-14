from tkinter import *
import datetime

#Basic Window Creation
window = Tk()
window.iconbitmap("Icon.ico")
window.title("ToDo List")
window.geometry("1610x1680")
window.minsize(width =1610,height=1680)
window.configure(bg = "yellow")

#Functions
def addtask(argument = None):
    addedtask = entry.get()
    listbox.insert(END,addedtask)
    entry.delete(0,END)
    listbox.yview(END)
    
def delete(argument = None):
    selectedtext = listbox.curselection()
    if selectedtext:
        listbox.delete(selectedtext)

#Pics
pic = PhotoImage(file="picc.png")

# Label for pics
lbpic1 = Label(window, image=pic)
lbpic1.place(x=0, y=23)



#Buttons
button_add = Button(window,text = "Add task", bg = "Black", fg = "white",font = ("Georgia",10,"bold"),command = addtask )
button_add.place( x = 1302, y = 788)

button_del = Button(window,text = "Delete", bg = "Black", fg = "white",font = ("Georgia",10,"bold"),command = delete)
button_del.place( x = 1381, y = 788)

button_enter = Button(window,text = "Enter", bg = "Black", fg = "white",font = ("Georgia",10,"bold"),width = 14,height=1,command = addtask)
button_enter.place( x = 1302, y = 756)

#Date and time creation
nowtime = datetime.datetime.now()

#Frames Creation
frametop= Frame(window)
frametop.pack()                

framebottom= Frame(window,bg = "yellow")
framebottom.pack(side = "bottom")

frameright= Frame(window,bg = "yellow")
frameright.pack(side = "right")

#Labels for frames
lbframetop = Label(frametop, text = "                           Welcome to the ToDo App", fg = "black",bg = "yellow",height=3,font= ("Georgia",18,"italic","bold")).pack()
lbdatetime = Label(frameright, text=f"{nowtime:%B %d,%Y}\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n{nowtime.strftime('%I:%M %p')}", font=('Arial', 12,'bold','italic'),fg='black',bg = "yellow")
lbdatetime.pack()
lbframebottom = Label(framebottom, text = "                                We Hope ToDo Helped You! :)",bg = "yellow", fg = "black",font=('Arial', 12,'bold','italic'),width = 35)
lbframebottom.pack()

#Entry Box
var = StringVar()
entry = Entry(window,textvariable = var,width = 105,bg = "white", fg = "black",font = ("Arial",15,"italic"))
entry.place(x = 280, y= 824)

#List box
listbox = Listbox(window,bg = "white",fg = "black",font = ("Arial",13,"italic"))
listbox.place(x = 280, y = 92,width = 1161, height = 650)

#Scroll bar
scrll = Scrollbar(window,width= 20)
scrll.pack(side= RIGHT,fill = Y)
scrll.config(command = listbox.yview)


#Binding for enter button
entry.bind("<Return>",addtask)
window.bind("<Delete>",delete)
window.bind("<Up>", lambda event: listbox.yview_scroll(-1, "units"))
window.bind("<Down>", lambda event: listbox.yview_scroll(1, "units"))


window.mainloop()