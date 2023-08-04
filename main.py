import tkinter as tkinter

def start_timer():
    reps = 0
    reps += 1

    work_sec = 25 * 60
    short_break = 5 * 60
    long_break = 15 * 60

    count_down(work_sec)

def count_down(time):
    print(time)


window = tkinter.Tk()
window.title('Feyndoro')
window.config(padx=100, pady=50, bg="#A5ECFF")

title_label = tkinter.Label(text='Timer', bg="#A5ECFF",fg="#2D2F30", font=("Mono", 50))
title_label.grid(column=1, row=0)

width_screen = window.winfo_screenwidth()
height_screen = window.winfo_screenheight()

width_window = 600
height_window = 400

x = (width_screen - width_window) // 2
y = (height_screen - height_window) // 2

canvas = tkinter.Canvas(width=350, height=200, highlightthickness=0)
feynman_img = tkinter.PhotoImage(file='Feynman.png')
canvas.create_image(100, 200, image=feynman_img)
canvas.grid(column=1, row=1)

position_center = str((width_screen * height_screen)+ x + y)

window.geometry(f"540x450+{x}+{y}")

window.attributes('-topmost', 1)

start_button = tkinter.Button(text='Start', command=start_timer, bg='#A5ECFF', highlightthickness=0)
start_button.grid(column=2, row=2)

reset_button = tkinter.Button(text='Start', command=start_timer, bg='#A5ECFF', highlightthickness=0)
reset_button.grid(column=2, row=3)

window.mainloop()
