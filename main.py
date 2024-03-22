from tkinter import *

# ---------------------------- PASSWORD GENERATOR ------------------------------- #

# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    website = website_entry.get()
    username = username_entry.get()
    password = password_entry.get()

    with open("data.txt", "a") as data_file:
        data_file.write(f"{website} | {username} | {password} \n")
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
password_button = Button(text="Generate Password")
add_button = Button(width=36, text="Add", command=save)
password_button.grid(row=3, column=2)
add_button.grid(row=4, column=1, columnspan=2)



window.mainloop()