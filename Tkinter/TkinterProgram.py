from tkinter import *

#Create Window
window = Tk()

def converter():
    #print("Hello")   #Print hello in console
    #print(e1_value.get())
    #t1.insert(END, e1_value.get())
    miles = float(e1_value.get())*1.6
    t1.insert(END, miles)

b1 = Button(window, text = 'Execute', command=converter)
#b1.pack()    #
b1.grid(row=0, column=0) #grid() have more control than pack()

e1_value = StringVar()
e1 = Entry(window, textvariable=e1_value)
e1.grid(row=0, column=1)

t1 = Text(window, height=1, width=20)
t1.grid(row=0, column=2)

window.mainloop()

