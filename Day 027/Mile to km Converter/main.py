
from tkinter import *
from webbrowser import get



window = Tk()
# Set title
window.title("GUI Program")
window.minsize(width=400,height=300)

# Create Label

miles_label = Label(text="Miles")
miles_label.grid(column=3,row=0)

isequalto_label = Label(text="is equal to")
isequalto_label.grid(column=0,row=1)


miles_label = Label(text="Miles")
miles_label.grid(column=3,row=0)

km = Label(text="Km")
km.grid(column=3,row=1)

result_label = Label()
result_label.grid(row=1,column=2)


def button_clicked():
    input_text = input.get()
    km = int(input_text) * 1.60934
    result = round(km)
    result_label.config(text=result)  
button = Button(text="Calculate",command=button_clicked)
button.grid(row=2,column=2)


# Entry 

input = Entry(width=20)
#input.pack(side="left")
input.grid(column=2,row=0)






window.mainloop()