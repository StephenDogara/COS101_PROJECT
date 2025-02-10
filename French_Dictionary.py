import tkinter as tk
from tkinter import messagebox

# Dictionary data: French to English
french_to_english = {
    "hello": "bonjour",
    "thank you": "merci",
    "love": "amour",
    "house": "maison",
    "cat": "chat",
    "dog": "chien",
    "apple": "pomme",
    "car": "voiture",
    "book": "livre",
    "School": "école"
}

# Function to get translation
def get_translation():
    french_word = entry.get().strip().lower()  # Get the input from the text box
    if french_word in french_to_english:
        translation = french_to_english[french_word]
        messagebox.showinfo("Translation", f"The English translation of '{french_word}' is: {translation}")
    else:
        messagebox.showwarning("Not Found", f"Sorry, no translation found for '{french_word}'.")

# Set up the main application window
root = tk.Tk()
root.title("French to English Dictionary")

# Add a label
label = tk.Label(root, text="Enter a French word:")
label.pack(padx=30, pady=20)

# Add an input box (Entry widget)
entry = tk.Entry(root, width=30)
entry.pack(padx=20, pady=10)

# Add a button to fetch the translation
button = tk.Button(root, text="Translate", command=get_translation)
button.pack(pady=10)

# Run the Tkinter event loop
root.mainloop()
