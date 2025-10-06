from tkinter import *

root = Tk()
root.geometry("300x250")
root.title("Listbox")


food_label = Label(root,text = "Food items")
food_label.pack() 

#Activestyle changes the border of each item
listbox = Listbox(root,height=10,width=15,bg="grey",activestyle='dotbox',font="Helvetica",fg="yellow")
listbox.insert(1,"Nachos")
listbox.insert(2,"Cheeseburger")
listbox.insert(3,"Pizza")
listbox.insert(4,"Sushi")
listbox.insert(5,"French fries")
listbox.pack()




root.mainloop()
