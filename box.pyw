import tkinter as tk
import random

def create_blank_window():
    window = tk.Tk()
    window.title("Bouncing Box")
    window.geometry("400x300")
    window.configure(bg="black")

    canvas = tk.Canvas(window, width=400, height=300, bg="black", highlightthickness=0)
    canvas.pack()

    box_size = 30
    x_speed = random.choice([-3, -2, -1, 1, 2, 3])
    y_speed = random.choice([-3, -2, -1, 1, 2, 3])

    box = canvas.create_rectangle(10, 10, 10 + box_size, 10 + box_size, fill="white")

    def move_box():
        nonlocal x_speed, y_speed
        canvas.move(box, x_speed, y_speed)
        x1, y1, x2, y2 = canvas.coords(box)

        if x1 <= 0 or x2 >= 400:
            x_speed *= -1
        if y1 <= 0 or y2 >= 300:
            y_speed *= -1

        canvas.after(10, move_box)

    move_box()
    window.mainloop()

if __name__ == "__main__":
    create_blank_window()
