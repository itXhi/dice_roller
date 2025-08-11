import tkinter as tk
import random

dice_faces = {
    1: "⚀",
    2: "⚁",
    3: "⚂",
    4: "⚃",
    5: "⚄",
    6: "⚅"
}

def roll1():
    die1 = random.randint(1,6)

    die1_label.config(text= dice_faces[die1]) 

    status1_label.config(text= f"You have rolled a {die1}")


def roll2():
    die2 = random.randint(1,6)
    
    die2_label.config(text= dice_faces[die2]) 

    status2_label.config(text= f"You have rolled a {die2}")


window = tk.Tk()
window.title("Dice Roller")
window.geometry("350x300")
window.config(bg="#f0f0f0")

die1_label = tk.Label(window,text="🎲",font=("Ariel",40),bg="#f0f0f0")
die2_label = tk.Label(window,text="🎲",font=("Ariel",40),bg="#f0f0f0")

die1_label.grid(row=0, column=0, padx=20)
die2_label.grid(row=0, column=3, padx=20)


status1_label = tk.Label(window,text="click to roll",font=("Ariel",12),bg="#f0f0f0")
status2_label = tk.Label(window,text="click to roll",font=("Ariel",12),bg="#f0f0f0")

status1_label.grid(row=2, column=0 ,padx=10)
status2_label.grid(row=2, column=3, padx=10)


roll_button1 = tk.Button(window,text="Roll dice",command=roll1)
roll_button1.grid(row=4, column=0, padx=20)

roll_button2 = tk.Button(window,text="Roll dice",command=roll2)
roll_button2.grid(row=4, column=3, padx=20)

window.mainloop()