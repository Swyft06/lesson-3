from tkinter import *
root = Tk()
root.geometry("300x150")
root.title("Shopping list")

label = Label(root,text="")
label.pack()

scrollbar = Scrollbar(root)
scrollbar.pack(side=RIGHT,fill=Y)

listbox = Listbox(root,yscrollcommand=scrollbar.set)

listbox.insert(1,"Lettuce")
listbox.insert(2,"Tomato")
listbox.insert(3,"Banana")
listbox.insert(4,"Milk")
listbox.insert(5,"Eggs")
listbox.insert(6,"Potato")
listbox.insert(7,"Onion")
listbox.insert(8,"Pasta")
listbox.insert(9,"Apples")
listbox.insert(10,"Orange")

listbox.pack()

scrollbar.config(command=listbox.yview)



root.mainloop()
