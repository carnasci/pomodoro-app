from tkinter import *
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

# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)

canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=tomato_img)
canvas.create_text(100, 130, text="00:00", fill="white", font=(FONT_NAME, 30, "bold"))
canvas.grid(row=1, column=1)

timer_label = Label()
timer_label.config(text="Timer", font=(FONT_NAME, 30, "bold"), fg=GREEN, bg=YELLOW)
timer_label.grid(row=0, column=1)

start_button = Button()
start_button.config(text="Start", font=(FONT_NAME, 10, "bold"))
start_button.grid(row=2, column=0, sticky="E")

reset_button = Button()
reset_button.config(text="Reset", font=(FONT_NAME, 10, "bold"))
reset_button.grid(row=2, column=2, sticky="W")

checkmark_label = Label()
checkmark_label.config(text="✓", font=(FONT_NAME, 16), fg=GREEN, bg=YELLOW)
checkmark_label.grid(row=3, column=1)



window.mainloop()