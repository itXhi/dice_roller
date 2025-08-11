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

def roll_dice():
    result = random.randint(1, 6)
    dice_label.config(text=dice_faces[result])
    status_label.config(text=f"You rolled a {result}!")
     

window = tk.Tk()
window.title("Dice Roller")
window.geometry("300x300")
window.config(bg="#F0F0F0")


dice_label = tk.Label(window, text="🎲", font=("Arial", 100), bg="#F0F0F0")
dice_label.pack(pady=20)


status_label = tk.Label(window, text="Click to roll", font=("Arial", 14), bg="#F0F0F0")
status_label.pack()


roll_button = tk.Button(window, text="Roll Dice", font=("Arial", 16), command=roll_dice)
roll_button.pack(pady=20)


window.mainloop()
