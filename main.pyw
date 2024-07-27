# Choose which mode to play

import customtkinter as ctk
import tkinter as tk
import os

def button_click(val):
    if val == "eyes":
        os.system("python scripts/Eyes_Flappy_Bird.pyw")
    else:
        os.system("python scripts/Flappy_Bird.pyw")

window_height = 300
window_width = 500

root = ctk.CTk()
root.title("Let's Play Flappy Bird")

screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()

x_position = int((screen_width/2)-(window_width/4))
y_position = (screen_height - window_height) // 2

root.geometry(f"{window_width}x{window_height}+{x_position}+{y_position}")

heading = ctk.CTkLabel(root, text="Flappy Bird", font=("Arial", 50, "bold"))
heading.pack(pady=10)

subheading = ctk.CTkLabel(root, text="How would you like to play?", font=("Arial", 30))
subheading.pack(pady=20)

button_frame = ctk.CTkFrame(root)
button_frame.pack(pady=30)

button1 = ctk.CTkButton(button_frame, text="Clicking Spacebar 🔼", font=("Arial", 20), command=lambda: button_click("hands"))
button2 = ctk.CTkButton(button_frame, text="Blinking Eyes 👀", font=("Arial", 20), command=lambda: button_click("eyes"))

button1.grid(row=0, column=0, padx=10)
button2.grid(row=0, column=1, padx=10)

root.mainloop()
