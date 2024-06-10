import os
import platform
import pyttsx3
import tkinter as tk
from tkinter import messagebox

def speak_text(text):
    system_platform = platform.system()
    
    if system_platform == "Darwin":  # macOS
        os.system(f"say {text}")
    elif system_platform == "Windows":  # Windows
        engine = pyttsx3.init()
        engine.say(text)
        engine.runAndWait()
    else:
        print(f"Text-to-speech not supported on {system_platform}.")

def on_speak_button_click():
    text_to_speak = entry.get()
    if not text_to_speak.strip():
        messagebox.showwarning("Warning", "Please enter some text.")
    else:
        speak_text(text_to_speak)

def on_quit_button_click():
    system_platform = platform.system()
    if system_platform == "Darwin":  # macOS
        os.system("say 'Bye Bye'")
    elif system_platform == "Windows":  # Windows
        engine = pyttsx3.init()
        engine.say('Bye Bye Friend.')
        engine.runAndWait()
    else:
        print(f"Text-to-speech not supported on {system_platform}.")
    root.destroy()

if __name__ == '__main__':
    root = tk.Tk()
    root.title("RoboSpeaker 1.1")

    label = tk.Label(root, text="Enter what you want me to speak:")
    label.pack(pady=20)

    entry = tk.Entry(root, width=60)
    entry.pack(pady=20)

    speak_button = tk.Button(root, text="Speak", command=on_speak_button_click)
    speak_button.pack(pady=5)

    quit_button = tk.Button(root, text="Quit", command=on_quit_button_click)
    quit_button.pack(pady=5)

    root.mainloop()
