from tkinter import *

window =Tk()
window.title("My Firt GUI Program")
window.minsize(width = 500, height=300)

#Label 

my_label =Label(text="I am a Label",font=("Geist",24,"bold"))
my_label.grid(column=0 , row=0)

# Button

def button_clicked():
    my_label.config(text = input.get())
    button.config(text="oh yeah")
    print("I got clicked")
    
button =Button(text="Click Me", command=button_clicked )
button.grid(column=2 , row= 2)

new_button = Button(text="Im New")
new_button.grid(column=3, row = 0)

# Entry

input =Entry(width=10)
input.grid(column=3 , row=3 )



mainloop()