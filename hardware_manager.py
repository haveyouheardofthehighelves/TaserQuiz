import serial
import tkinter as tk
import pandas


def writetoarduino(writeall):
    arr = bytes(writeall, 'utf-8')


class ControllerApp:
    ser = serial.Serial("COM7", 9600, timeout=0)
    button_press = False
    taser_off = True
    question_count = 0

    def __init__(self, root, df, q_label, a_label):
        self.root = root
        self.df = df  # Call this method once when the object is created
        self.q_label = q_label
        self.a_label = a_label
        self.update_controller_input()

    def update_controller_input(self):
        # check and update label text
        self.button()
        self.q_label.config(text=self.df.iloc[self.question_count]["Question"])  # Corrected line
        self.answer_options()
        self.root.after(5, self.update_controller_input)

    def button(self):
        # Read all available bytes from the serial port
        data = self.ser.read(self.ser.in_waiting)
        try:
            if data:
                decoded_data = data.decode('utf-8').replace('\n', '').replace('\r', '')
                if decoded_data:
                    if int(decoded_data[0]) == 1 and not self.button_press:
                        self.button_press = True
                    if int(decoded_data[0]) == 0 and self.button_press:
                        if self.question_count < self.df.shape[0] - 1:
                            self.question_count += 1
                        self.button_press = False

        except UnicodeDecodeError as e:
            print("UnicodeDecodeError: ", e)
            # Handle the error here, or simply pass to ignore it

    def answer_options(self):
        first_choice = ord('A')
        last_choice = ord('C')
        full = ""
        for i in range(first_choice, last_choice + 1):
            if self.df.iloc[self.question_count][str(chr(i))]:
                full += f'{chr(i)}: {self.df.iloc[self.question_count][chr(i)]} \n \n'
        self.a_label.config(text=full)
