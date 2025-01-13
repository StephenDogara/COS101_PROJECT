import tkinter as tk
from gettext import translation
from importlib.metadata import entry_points
from tkinter import messagebox

hausa_dict = {
    "Hello": "Sannu",
    "Goodbye" : "Sai an jima",
    "Please" : "Don Allah",
    "Thank you" : "Na gode",
    "Yes": "Ehh",
    "No": "A'a",
    "House" : "Gida",
    "Water" : "Ruwa",
    "Book" : "Littafi",
    "Food" : "Abinci",
    "School" : "Makaranta",
    "Child" : "Yaro",
    "Friend" : "Aboki",
    "Love" : "Kauna",
    "Money" : "Kudi",
    "Chair" : "Kujera",
    "Work" : "Aiki",
    "Market" : "Kasuwa",
    "Peace" : "Lafiya",
    "Happy" : "Farinciki"
}

def translate_word():
    english_word = entry.get().capitalize()
    if english_word in hausa_dict:
        translation = hausa_dict[english_word]
        messagebox.showinfo("Translation", f"The Hausa translation for f'{english_word}'is '{translation}'.")
    else:
        messagebox.showerror("Error",f"'{english_word}' not found in the dictionary.")

root = tk.Tk()
root.title("Hausa Dictionary")

label = tk.Label(root,text="Enter an English Word:",font=("Arial",14))
label.pack(pady=10)
entry = tk.Entry(root, font=("Arial",14),width=30)
entry.pack(pady=5)

translate_button = tk.Button(root, text="Translate", command=translate_word,font=("Arial",14))
translate_button.pack(pady=20)

root.mainloop()





