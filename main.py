# step 1 create the basic version of the product
# step 2 add web server
# step 3 add sql database of users

import serial
import tkinter as tk
import elevenlabs
import pandas
import hardware_manager


def writetoarduino(writeall):
    arr = bytes(writeall, 'utf-8')


def switch_light():
    pass


def button_press():
    pass


def activate_taser():
    pass


def update_flashcard(q_count):
    print("hello")
    Question.config(text=df.iloc[q_count]['Question'])


df = pandas.read_csv("test.csv")

root = tk.Tk()
root.title("FlashCard")
root.geometry("420x720")
root.grid_rowconfigure(0, weight=1)
root.grid_columnconfigure(0, weight=1)
# Create widgets
frame_main = tk.Frame(root, background="white")
frame_main.grid(row=0, column=0, sticky="nesw")

Question = tk.Label(frame_main, text='Question', width=45, height=19, borderwidth=2, relief="solid",
                    font=("Arial", 12), fg="green", bg="white", wraplength=400)
Question.grid(row=0, column=0, sticky="n", padx=3, columnspan=2)  # Adjusted columnspan to 2

Answer = tk.Label(frame_main, text='Answer', width=45, height=20, borderwidth=2, relief="solid",
                  font=("Arial", 12), fg="red", bg="white", wraplength=400)
Answer.grid(row=1, column=0, sticky="s", padx=3, pady=1, columnspan=2)  # Adjusted row to 1

control_manage = hardware_manager.ControllerApp(root, df, Question, Answer)

root.mainloop()
