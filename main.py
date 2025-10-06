from tkinter import *

root = Tk()
root.geometry("300x150")

choco_label = Label(root,text="Chocos and ice creams")
choco_label.pack()

#Creates a frame
top_frame = Frame(root)
top_frame.pack()

btn1 = Button(top_frame,text = "Choco",fg = "black",bg = "beige")
btn1.pack(side=LEFT,padx=5)

btn2 = Button(top_frame,text="White choco",fg="black",bg="beige")
btn2.pack(side=LEFT,padx=5)

btn3 = Button(top_frame,text="Dark choco",fg="black",bg="beige")
btn3.pack(side=LEFT,padx=5)

bottom_frame = Frame(root)
bottom_frame.pack()

btn4 = Button(bottom_frame,text="Vanilla",fg= "black",bg="beige")
btn4.pack(side=TOP,pady=5)

btn5 = Button(bottom_frame,text = "Chocolate",fg = "white",bg="brown")
btn5.pack(side=TOP,pady=5)

btn6 = Button(bottom_frame,text="Cotton Candy",fg = "white",bg="blue")
btn6.pack(side=TOP,pady=5)






root.mainloop()
