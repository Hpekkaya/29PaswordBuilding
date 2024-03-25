from tkinter import *
from tkinter import messagebox
from random import randint, choice, shuffle
import pyperclip
import json

# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def password_generator():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_letters = [choice(letters) for _ in range(randint(8, 10))]
    password_numbers = [choice(numbers) for _ in range(randint(2, 4))]
    password_symbols = [choice(symbols) for _ in range(randint(2, 4))]

    password_list = password_letters + password_numbers + password_symbols

    shuffle(password_list)

    password = "".join(password_list)

    password_entry.insert(0, password)

    pyperclip.copy(password)


# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    website = website_entry.get()
    username = username_entry.get()
    password = password_entry.get()
    new_data = {
        website: {
            "email": username,
            "password": password,
        }
    }

    if len(website) == 0 or len(password) == 0:
        messagebox.showinfo(title="Ooops :", message="Please do not left any field empty!")
    else:
        with open("data.json", "r") as data_file:
            # Reading old data
            data = json.load(data_file)
            # Updating old data with new data
            data.update(new_data)

        with open("data.json", "w") as data_file:
            # Saving the updated data
            json.dump(new_data, data_file, indent=4)

            website_entry.delete(0, END)
            password_entry.delete(0, END)

# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Password Generator")
window.config(padx=50, pady=50)

canvas = Canvas(width=200, height=200)
logo_image = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo_image)
canvas.grid(row=0, column=1)

# --- Labels

website_label = Label(width=20, text="Website :")
username_label = Label(width=20, text="Email/Username :")
password_label = Label(width=20, text="Password :")
website_label.grid(row=1, column=0)
username_label.grid(row=2, column=0)
password_label.grid(row=3, column=0)

# --- Entries
website_entry = Entry(width=40)
website_entry.focus()
username_entry = Entry(width=40)
password_entry = Entry(width=21)
website_entry.grid(row=1, column=1, columnspan=2)
username_entry.grid(row=2, column=1, columnspan=2)
username_entry.insert(0, "hpek1970@yahoo.com")
password_entry.grid(row=3, column=1)

# --- Buttons
password_button = Button(text="Generate Password", command=password_generator)
add_button = Button(width=36, text="Add", command=save)
password_button.grid(row=3, column=2)
add_button.grid(row=4, column=1, columnspan=2)



window.mainloop()