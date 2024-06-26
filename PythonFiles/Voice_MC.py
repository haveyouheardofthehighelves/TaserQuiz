# ARCPXXCX6O2KDQZRIMP3XIZSUHPHRXX3
import speech_recognition
import elevenlabs
import pyttsx3
import re
import os
import sys
import time
# 11labsapikey: 562229f81d2737d38a2c54b0d3d20c6e

elevenlabs.set_api_key("562229f81d2737d38a2c54b0d3d20c6e")

# Replace 'your_audio_file.mp3' with the path to your audio file
'''voices = elevenlabs.voices()
pattern = '(name=\'\w*\').*(labels={.*})'
for v in voices:
    match = re.findall(pattern, str(v))
    if match:
        print(f'{match[0][0]}, {match[0][1]} ')'''

Expressive = elevenlabs.Voice(
    voice_id='jBpfuIE2acCO8z3wKNLl',
    settings=elevenlabs.VoiceSettings(
        stability=0,
        similarity_boost=.75
    )
)

# voice_id=('jBpfuIE2acCO8z3wKNLl', name='Gigi', category='premade', description=None, labels={'accent': 'american', 'description': 'childl)
repeat_dialogue = elevenlabs.generate(
    text="could you repeat that?", voice=Expressive
)
recognizer = speech_recognition.Recognizer()
Piggy_listen = False


answer = ""
print("wait...")
time.sleep(1)
print("speak...")
listen = False
while True:
    try:
        with speech_recognition.Microphone() as mic:
            recognizer.adjust_for_ambient_noise(mic, duration=1.15)
            audio = recognizer.listen(mic)
            text = recognizer.recognize_google(audio)
            text = str(text).strip().lower()
            if 'a' <= text[0] <= 'c':  # Check if the first character is between 'a' and 'd' inclusive
                with open('output.txt', 'w+', newline='') as file:
                    file.write(text)
                    break
            else:
                print("Try again, invalid answer")
    except speech_recognition.UnknownValueError:
        if Piggy_listen:
            elevenlabs.play(repeat_dialogue)
    except speech_recognition.RequestError as e:
        print(f"Error with the speech recognition service: {e}")
    except Exception as e:
        print(e)
    except KeyboardInterrupt:
        break


print("process closed")
