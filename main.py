from tkinter import *
from tkinter import messagebox
from random import randint, choice, shuffle
import pyperclip
import json

# ---------------------------- PASSWORD GENERATOR ------------------------------- #

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v',
           'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R',
           'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']


# ---------------------------- SAVE PASSWORD ------------------------------- #

def add_button_command():
    data_email = email_entry.get()
    data_password = password_entry.get()
    data_website = website_entry.get()
    new_data = {
        data_website: {
            "email": data_email,
            "password": data_password,
        }
    }

    if len(data_password) == 0:
        messagebox.showerror(title="Error", message="Empty Password!")
    elif len(data_email) == 0:
        messagebox.showerror(title="Error", message="Empty Email!")
    elif len(data_website) == 0:
        messagebox.showerror(title="Error", message="Empty Website!")
    else:
        try:
            with open("data.json", "r") as file:
                # Reading old data
                data = json.load(file)
        except FileNotFoundError:
            with open("data.json", "w") as file:
                json.dump(new_data, file, indent=4)
        else:
            # Update old data with new data
            data.update(new_data)

            with open("data.json", "w") as file:
                # Saving updated data
                json.dump(data, file, indent=4)
        finally:
            password_entry.delete(0, END)
            website_entry.delete(0, END)


# ---------------------------- FUNCTIONS ------------------------------- #

def generate_password():
    password_entry.delete(0, END)
    password_letters = [choice(letters) for char in range(randint(8, 10))]
    password_symbols = [choice(symbols) for char in range(randint(2, 4))]
    password_numbers = [choice(numbers) for char in range(randint(2, 4))]
    password_list = password_numbers + password_letters + password_symbols
    shuffle(password_list)
    pw = "".join(password_list)
    password_entry.insert(0, pw)
    pyperclip.copy(pw)


def find_password():
    user_input = website_entry.get()
    try:
        with open("data.json", "r") as file:
            data = json.load(file)
    except FileNotFoundError:(
        messagebox.showerror(title="ERROR", message="No data found!"))
    else:
        if user_input in data:
            messagebox.showinfo(title=f"Password for {user_input}", message=f"Email: {data[user_input]["email"]}\n"
                                                                            f"Password: {data[user_input]["password"]}")
        else:
            messagebox.showerror(title="Not found", message="No details for the website exists!")


def insert_mail():
    email_entry.insert(0, "jasp.hanson@gmail.com")


# ---------------------------- UI SETUP ------------------------------- #


# Window
window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

# Canvas
canvas = Canvas(width=200, height=200)
pw_img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=pw_img)
# canvas.grid(column=1, row=1)
canvas.grid(column=1, row=0)

# Labels
website = Label(text="Website:")
website.grid(column=0, row=1)

email = Label(text="Email/Username:")
email.grid(column=0, row=2)

password = Label(text="Password:")
password.grid(column=0, row=3)

# Entry
website_entry = Entry(width=35)
website_entry.grid(column=1, row=1)
website_entry.focus()
email_entry = Entry(width=35)
email_entry.grid(column=1, row=2, columnspan=1)
insert_mail()

password_entry = Entry(width=35)
password_entry.grid(column=1, row=3)

# Buttons

generate_button = Button(text="Generate Password", command=generate_password)
generate_button.grid(column=2, row=3)

add_button = Button(text="Add", width=36, command=add_button_command)
add_button.grid(column=1, row=4, columnspan=1)

search_button = Button(text="Search", command=find_password, width=14)
search_button.grid(column=2, row=1, columnspan=1)

window.mainloop()
