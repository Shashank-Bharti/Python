from tkinter import *

window = Tk()
window.title("Pomodoro Timer")

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20

# ---------------------------- TIMER RESET ------------------------------- # 

# ---------------------------- TIMER MECHANISM ------------------------------- # 

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
def coun_down(count):
    
    window.after(1000,coun_down,count-1)
# ---------------------------- UI SETUP ------------------------------- #

window.config(padx=100, pady=80 , bg= YELLOW)

label = Label(text="Timer" , font=(FONT_NAME,30,"bold"),fg=GREEN,bg=YELLOW)
label.grid(column=1,row=0)

canvas = Canvas(width= 200 , height = 224 ,bg = YELLOW ,highlightbackground= YELLOW)
tomato_img = PhotoImage(file="E:/100 Days Of Python/028 DAY 28/tomato.png")
canvas.create_image(102,112,image = tomato_img)
timer_text = canvas.create_text(100,130, text="00:00" , fill= "white",font=(FONT_NAME,24,"bold"))
canvas.grid(column=1,row=1)

start_button = Button(text="Start")
start_button.grid(column=0 ,row=3)

reset_button = Button(text="Reset")
reset_button.grid(column=2 ,row=3)

check_mark = Label(text="✔️", fg=GREEN ,bg = YELLOW)
check_mark.grid(column=1,row=3)

































mainloop()