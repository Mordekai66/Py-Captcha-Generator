import os
import sys

from tkinter import *
from tkinter import messagebox

from core.image_captcha import generate_image_captcha
from core.audio_captcha import generate_audio_captcha
from utils.random_capcha_text import random_captcha_text


if getattr(sys, 'frozen', False):
    script_path = sys.executable
else:
    script_path = os.path.abspath(__file__)

script_dir = os.path.dirname(script_path)
voice_dir = os.path.join(script_dir, "Voices", "Man")
print(script_dir)

pro = Tk()
pro.title("Captcha Generator")
pro.geometry("500x500")
pro.config(bg="#F8F9FA")
pro.resizable(0, 0)

def random_captcha(length=4):
    text = random_captcha_text(length)
    captcha_key_entry.delete(0, END)
    captcha_key_entry.insert(0, text)

def generate_captcha(type_of_captcha):
    data = captcha_key_entry.get()
    if not data:
        messagebox.showerror("Error", "Please enter a captcha text.")
        return
    
    elif type_of_captcha == "Image":
        generate_image_captcha(data, script_dir)
        image_file = os.path.join(script_dir, "captcha.png")
        captcha_image = PhotoImage(file=image_file)
        captcha_label.config(image=captcha_image)
        captcha_label.image = captcha_image
        messagebox.showinfo("Success", f"Captcha image generated: {data}")
        
    elif type_of_captcha == "Audio":
        generate_audio_captcha(data, script_dir, voice_dir)
        messagebox.showinfo("Success", f"Captcha audio generated: {data}")

captcha_key_label = Label(pro, text="Enter captcha using only letters, digits, or both", fg="#343A40", bg="#F8F9FA", font=("Arial", 12))
captcha_key_label.pack(pady=10)

captcha_key_entry = Entry(pro, font=("Arial", 15), bg="white", fg="#343A40")
captcha_key_entry.pack(pady=5)

captcha_type_label = Label(pro, text="Select Captcha Type", fg="#343A40", bg="#F8F9FA", font=("Arial", 12))
captcha_type_label.pack(pady=10)

type_of_captcha = StringVar(pro)
type_of_captcha.set("Image")

captcha_type_menu = OptionMenu(pro, type_of_captcha, "Image", "Audio")
captcha_type_menu.config(font=("Arial", 12), bg="#F8F9FA", fg="#343A40")
captcha_type_menu.pack(pady=5)

captcha_label = Label(pro, bg="#F8F9FA")
captcha_label.pack(pady=10)

ranodm_captcha_button = Button(pro, text="Generate Random Captcha", command=random_captcha, bg="#E9ECEF", fg="#343A40", font=("Arial", 15))
ranodm_captcha_button.pack(pady=20)

generate_button = Button(pro, text="Generate Captcha", command=lambda: generate_captcha(type_of_captcha.get()), bg="#E9ECEF", fg="#343A40", font=("Arial", 15))
generate_button.pack(pady=20)

pro.mainloop()