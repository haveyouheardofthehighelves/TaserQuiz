import serial
import tkinter as tk
import pandas
import elevenlabs
import speech_recognition
import subprocess





class ControllerApp:
    elevenlabs.set_api_key("562229f81d2737d38a2c54b0d3d20c6e")
    ser = serial.Serial("COM7", 9600, timeout=0)
    button_press = False
    question_count = 0
    answer_state = 0
    currentQ = ""
    vc_on = False
    processing = False
    recognizer = speech_recognition.Recognizer()
    Expressive = elevenlabs.Voice(
        voice_id='jBpfuIE2acCO8z3wKNLl',
        settings=elevenlabs.VoiceSettings(
            stability=0,
            similarity_boost=.75
        )
    )

    def __init__(self, root, df, q_label, a_label):
        self.root = root
        self.df = df  # Call this method once when the object is created
        self.q_label = q_label
        self.a_label = a_label
        self.update_controller_input()

    def writetoarduino(self, writeall):
        arr = bytes(writeall, 'utf-8')
        self.ser.write(arr)

    def update_controller_input(self):
        # check and update label text
        self.button()
        self.q_label.config(text=self.df.iloc[self.question_count]["Question"])  # Corrected line
        if self.currentQ != self.df.iloc[self.question_count]["Question"]:
            self.currentQ = self.df.iloc[self.question_count]["Question"]
            elevenlabs.play(elevenlabs.generate(
                text=self.currentQ + '?', voice=self.Expressive))
        self.root.after(5, self.update_controller_input)
        if self.vc_on:
            with open('output.txt', 'r') as file:
                ans = file.readlines()
                if len(ans) > 0:
                    self.vc_on = False
                    if ans[0].strip()[0] == self.df.iloc[self.question_count]["Solution"].lower():
                        self.writetoarduino('g')
                    else:
                        self.writetoarduino('r')
                    self.processing = True
                    self.answer_state = 2
            with open('output.txt', 'w') as file:
                if self.answer_state == 2:
                    file.write("")

    def button(self):
        # Read all available bytes from the serial port
        data = self.ser.read(self.ser.in_waiting)
        try:
            if data:
                decoded_data = data.decode('utf-8').replace('\n', '').replace('\r', '')
                if decoded_data:
                    if decoded_data[0] == 'd':
                        self.processing = False
                    else:
                        if not self.processing:
                            if int(decoded_data[0]) == 1 and not self.button_press:
                                self.button_press = True
                                if self.answer_state == 0:
                                    self.answer_state = 1
                                    self.a_label.config(text="State your Answer Choice: ")
                                    if not self.vc_on:
                                        subprocess.Popen(["python", "Voice_MC.py"], shell=True)
                                        self.vc_on = True
                                    # Show the answer when button is pressed first time
                                else:
                                    # Move to the next question and answer options when button is pressed again
                                    if self.answer_state == 2:
                                        if self.question_count < self.df.shape[0] - 1:
                                            self.question_count += 1
                                            self.answer_state = 0
                            elif int(decoded_data[0]) == 0:
                                self.button_press = False
            self.answer_options()
        except UnicodeDecodeError as e:
            print("UnicodeDecodeError: ", e)
            # Handle the error here, or simply pass to ignore it

    def answer_options(self):
        first_choice = ord('A')
        last_choice = ord('C')
        full = ""
        if self.answer_state == 0:
            for i in range(first_choice, last_choice + 1):
                if self.df.iloc[self.question_count][str(chr(i))]:
                    full += f'{chr(i)}: {self.df.iloc[self.question_count][chr(i)]} \n \n'
            self.a_label.config(text=full)
        else:
            if self.answer_state == 2:
                self.a_label.config(
                    text=f"{self.df.iloc[self.question_count]['Solution']}: {self.df.iloc[self.question_count][self.df.iloc[self.question_count]['Solution']]}")
