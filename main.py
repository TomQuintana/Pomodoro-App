import tkinter as tkinter

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
print(x,y)

canvas = tkinter.Canvas(width=350, height=200, highlightthickness=0)
feynman_img = tkinter.PhotoImage(file='Feynman.png')
canvas.create_image(100, 200, image=feynman_img)
canvas.grid(column=1, row=1)

position_center = str((width_screen * height_screen)+ x + y)

window.geometry(f"540x450+{x}+{y}")

window.attributes('-topmost', 1)

window.mainloop()
