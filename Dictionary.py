import tkinter as tk
from gettext import translation
from importlib.metadata import entry_points
from tkinter import messagebox

igbo_dict = {
    "Hello": "Nnoo",
    "Dog" : "Nkita",
    "Food" : "Nri",
    "Thank you" : "Daalu",
    "Father": "Nna",
    "Mother": "Nne",
    "Brother" : "Nwanne",
    "Bed" : "Akwa",
    "Stomach" : "Afo",
    "Bag" : "Akpa",
    "School" : "Ulo akwukwo",
    "Laptop" : "Laptoopu",
    "Phone" : "Ekwenti",
    "Love" : "Kauna",
    "Money" : "Ego",
    "Hospital" : "Ulö ögwü",
    "Fork" : "Mkpisi",
    "Bag" : "Akpa",
    "Body" : "Ahu",
    "Duck" : "öbögwü"
}

def translate_word():
    english_word = entry.get().capitalize()
    if english_word in igbo_dict:
        translation = igbo_dict[english_word]
        messagebox.showinfo("Translation", f"The igbo translation for f'{english_word}'is '{translation}'.")
    else:
        messagebox.showerror("Error",f"'{english_word}' not found in the dictionary.")

root = tk.Tk()
root.title("igbo Dictionary")

label = tk.Label(root,text="Enter an English Word:",font=("Arial",14))
label.pack(pady=10)
entry = tk.Entry(root, font=("Arial",14),width=30)
entry.pack(pady=5)

translate_button = tk.Button(root, text="Translate", command=translate_word,font=("Arial",14))
translate_button.pack(pady=20)

root.mainloop()




