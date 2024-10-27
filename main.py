from tkinter import *
import math

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
reps = 0
timer = None

# ---------------------------- TIMER RESET ------------------------------- # 

def reset_timer():
    window.after_cancel(timer)
    canvas.itemconfig(timer_text, text="00:00")
    title_label.config(text="Timer")
    check_marks.config(text="")
    global reps
    reps = 0


# ---------------------------- TIMER MECHANISM ------------------------------- # 

def start_work():
    title_label.config(text="Work", fg=GREEN)
    count_down(WORK_MIN * 60)

def start_break():
    title_label.config(text="Break", fg=PINK)
    count_down(SHORT_BREAK_MIN * 60)


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
def count_down(count):
    count_min = math.floor(count / 60)
    count_sec = count % 60
    if count_sec < 10:
        count_sec = f"0{count_sec}"

    canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}")
    if count > 0:
        global timer
        timer = window.after(1000, count_down, count - 1)
    else:
        marks = ""
        global reps
        reps += 1
        work_sessions = reps // 2
        for _ in range(work_sessions):
            marks += "✔"
        check_marks.config(text=marks)


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)

title_label = Label(text="Timer", fg=GREEN, bg=YELLOW, font=(FONT_NAME, 50))
title_label.grid(column=0, row=0, columnspan=3, pady=(0, 20))

canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=tomato_img)
timer_text = canvas.create_text(100, 130, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))
canvas.grid(column=1, row=1)

# Spacer Label to add space before buttons
spacer = Label(bg=YELLOW)  # A blank label to act as a spacer
spacer.grid(column=1, row=2, pady=(20, 0))  # Adjust 'pady' to move buttons down

# Work Button
work_button = Button(text="Work", highlightbackground=GREEN, font=(FONT_NAME, 12, "bold"), command=start_work)
work_button.grid(column=0, row=3)

# Break Button
break_button = Button(text="Break", highlightbackground=PINK, font=(FONT_NAME, 12, "bold"), command=start_break)
break_button.grid(column=1, row=3)

# Reset Button
reset_button = Button(text="Reset", highlightbackground=RED, font=(FONT_NAME, 12, "bold"), command=reset_timer)
reset_button.grid(column=2, row=3)

check_marks = Label(fg=GREEN, bg=YELLOW, font=(FONT_NAME, 12))
check_marks.grid(column=1, row=4)


window.mainloop()
