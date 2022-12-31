from tkinter import *
from tkinter import messagebox
from random import *
import pyperclip
import json
# ---------------------------- PASSWORD GENERATOR ------------------------------- #
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y',
           'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

nr_letters = randint(8, 10)
nr_symbols = randint(2, 4)
nr_numbers = randint(2, 4)

letter = [choice(letters) for _ in range(nr_letters)]
symbol = [choice(symbols) for _ in range(nr_symbols)]
number = [choice(numbers) for _ in range(nr_numbers)]

password_list = letter+symbol+number

shuffle(password_list)

password = "".join(password_list)


def passs():
    password_entry.insert(0, password)
    pyperclip.copy(password)

# ---------------------------- SAVE PASSWORD ------------------------------- #


def save():
    website_entry_name = website_entry.get()
    username_entry_name = username_entry.get()
    password_entry_name = password_entry.get()
    data_value = {
        website_entry_name: {
            "user": username_entry_name,
            "pass": password_entry_name,
        }
    }
    if len(website_entry_name) == 0 or len(password_entry_name) == 0:
        messagebox.showinfo(
            title="oops", message="you can't leave the website or password empty!")
    else:
        try:
            with open("C:/Users/karth/OneDrive/Documents/code coffee/Python/100DaysOfCode/day29/db.json", 'r') as db:
                data = json.load(db)
        except FileNotFoundError:
            with open("C:/Users/karth/OneDrive/Documents/code coffee/Python/100DaysOfCode/day29/db.json", 'w') as db:
                json.dump(data_value, db, indent=4)
        else:
            data.update(data_value)
            with open("C:/Users/karth/OneDrive/Documents/code coffee/Python/100DaysOfCode/day29/db.json", 'w') as db:
                json.dump(data, db, indent=4)
        finally:
            website_entry.delete(0, END)
            password_entry.delete(0, END)


def find_password():
    website = website_entry.get()
    try:
        with open("C:/Users/karth/OneDrive/Documents/code coffee/Python/100DaysOfCode/day29/db.json") as db:
            data = json.load(db)
    except FileNotFoundError:
        messagebox.showinfo(title="error", message="no data found")
    else:
        if website in data:
            emaill = data[website]['user']
            passwordd = data[website]['pass']
            messagebox.showinfo(
                title=website, message=f'email:{emaill}\npassword:{passwordd}')
        else:
            messagebox.showinfo(title="error", message="no data found")


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("password generator")
window.config(padx=20, pady=20)

canvas = Canvas(width=200, height=200)
image = PhotoImage(
    file="C:/Users/karth/OneDrive/Documents/code coffee/Python/100DaysOfCode/day29/logo.png")
canvas.create_image(100, 100, image=image)
canvas.grid(row=0, column=1)

website_lable = Label(text="website:")
website_lable.grid(row=1, column=0)

username_lable = Label(text="Email/Lable:")
username_lable.grid(row=2, column=0)

password_lable = Label(text="password:")
password_lable.grid(row=3, column=0)

website_entry = Entry(width=21)
website_entry.focus()
website_entry.grid(row=1, column=1)

username_entry = Entry(width=42)
username_entry.insert(0, 'zinvert')
username_entry.grid(row=2, column=1, columnspan=2)

password_entry = Entry(width=21)
password_entry.grid(row=3, column=1)

generate = Button(text="Generate password", command=passs)
generate.grid(row=3, column=2)

add = Button(text="add", width=42, command=save)
add.grid(row=4, column=1, columnspan=2)

search = Button(text="search", width=21, command=find_password)
search.grid(row=1, column=2)

window.mainloop()
