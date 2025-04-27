from tkinter import *

window =Tk()
window.title("Mile to Kilometers Converter")

def mile_to_km():
    miles = float(miles_val.get())
    km =(miles * 1.609)
    km_val.config(text=f"{km}")
    
# Label 
mile = Label(text="Miles", font=("Raleway",12))
mile.grid(column= 2, row = 0)

km_val = Label(text = 0 ,font = ("Raleway",12))
km_val.grid(column=1,row=2)

km = Label(text="Km",font=("Raleway",12))
km.grid(column=2,row=2)

is_equals_to = Label(text="is equals to",font=("Raleway",12))
is_equals_to.grid(column=0,row=2)

# Buttons

convert = Button(text = "Convert",font=("Raleway",11), command= mile_to_km)
convert.grid(column=1 , row=3)

# Inputs
miles_val =  Entry(width= 9)
miles_val.grid(column=1 , row=0)

mainloop()