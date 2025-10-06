from tkinter import *
root = Tk()
root.geometry("200x150")
root.title("Scroll")

label = Label(root,text= "Hello")
label.pack()

scrollbar = Scrollbar(root)
scrollbar.pack(side=RIGHT,fill=Y)

#yscrollcommand allows it to scroll inside the listbox
listbox = Listbox(root,yscrollcommand=scrollbar.set)
listbox.pack()

#End is label value
for i in range(1,21):
    listbox.insert(END,"Hi " + str(i))

scrollbar.config(command=listbox.yview)







root.mainloop()
