from tkinter import *



window = Tk()
# Set title
window.title("GUI Program")
window.minsize(width=400,height=300)

# Create Label

my_label = Label(text="I am a label")
#my_label.pack(side="left")
#my_label.place(x=50,y=0)
my_label.grid(column=0,row=0)
# Button 
def button_clicked():
    my_label.config(text=input.get())
    
button = Button(text="Click ME",command=button_clicked)
button.grid(row=0,column=2)


# Entry 

input = Entry(width=20)
#input.pack(side="left")
input.grid(column=4,row=0)






window.mainloop()