from tkinter import*
root=Tk()

def myClick():
    myLabel=Label(root, text="Hi there!")
    myLabel.pack()

myButton=Button(root, text="Click here", command=myClick)
myButton.pack()

#label1=Label(root,text="Hello, World!")
#label1.grid(row=0,column=0)

#label2=Label(root,text="Welcome to the demo application!")
#label2.grid(row=1,column=0)

root.mainloop()
