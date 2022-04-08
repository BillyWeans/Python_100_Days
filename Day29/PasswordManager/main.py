import json
from tkinter import *
from tkinter import messagebox
import random
import pyperclip

WHITE = "white"
BLACK = "black"
GRAY = "gray"
FONT_LABEL = ("Courier", 15, "bold")


def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
               'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)

    pass_letters = [random.choice(letters) for _ in range(nr_letters)]
    pass_symbols = [random.choice(symbols) for _ in range(nr_symbols)]
    pass_numbers = [random.choice(numbers) for _ in range(nr_numbers)]

    password_list = pass_letters + pass_symbols + pass_numbers
    random.shuffle(password_list)

    password = "".join(password_list)

    entry_passwd.delete(0, END)
    entry_passwd.insert(0, password)


def add_entry():
    website = entry_website.get()
    email_user = entry_email_user.get()
    passwd = entry_passwd.get()

    if website == "" or email_user == "" or passwd == "":
        messagebox.showinfo(title="Error", message="Please enter a value for all fields.")
        return

    save_confirm = messagebox.askyesno(title="Save Password?", message=f"Website: {website}\n"
                                                                       f"Username: {email_user}\n "
                                                                       f"Password: {passwd}\n\n"
                                                                       f"Are you sure you want to save this data?")
    if save_confirm:
        new_passwd_data = {website:
                    {"username": email_user,
                     "password": passwd
                     }
                }

        # Open Password File
        try:
            with open("data.json", mode="r") as f_pass:
                old_passwd_data = json.load(f_pass)
        except FileNotFoundError:
            with open("data.json", mode="w") as f_pass:
                json.dump(new_passwd_data, f_pass, indent=4)
        else:
            # Update our json object with the existing file data
            new_passwd_data.update(old_passwd_data)
            # Save/Update Password File
            with open("data.json", mode="w") as f_pass:
                json.dump(new_passwd_data, f_pass, indent=4)
        finally:
            entry_website.delete(0, END)
            entry_passwd.delete(0, END)
            entry_website.focus()

            pyperclip.copy(passwd)


def search_passwds():
    search_website = entry_website.get()

    try:
        with open("data.json") as p_file:
            password_entries = json.load(p_file)
    except FileNotFoundError:
        messagebox.showerror(title="File Not Found", message="File 'data.json' could not be found!")
        return

    if search_website in password_entries:
        messagebox.showinfo(title="Match Found", message=f"Website: {search_website}\n"
                                                         f"Username: {password_entries[search_website]['username']}\n"
                                                         f"Password: {password_entries[search_website]['password']}\n")
    else:
        messagebox.showerror(title="No matching website", message=f"Website '{search_website}' was not found")


window = Tk()
window.minsize(width=800, height=600)
window.config(padx=100, pady=50, bg=WHITE)
window.title("Password Manager")

logo = PhotoImage(file="logo.png")
canvas = Canvas(width=400, height=400, bg="white", highlightthickness=0)
canvas.create_image(200, 200, image=logo)

lbl_website = Label(text="Website", bg=WHITE, fg=BLACK, font=FONT_LABEL)
lbl_email_user = Label(text="Email/Username", bg=WHITE, fg=BLACK, font=FONT_LABEL)
lbl_passwd = Label(text="Password", bg=WHITE, fg=BLACK, font=FONT_LABEL)

entry_website = Entry(width=22, bg=WHITE, fg=BLACK, highlightbackground=GRAY, highlightthickness=1)
entry_email_user = Entry(width=43, bg=WHITE, fg=BLACK, highlightbackground=GRAY, highlightthickness=1)
entry_passwd = Entry(width=22, bg=WHITE, fg=BLACK, highlightbackground=GRAY, highlightthickness=1)

btn_gen_passwd = Button(text="Generate Password", bg=WHITE, fg=BLACK, highlightbackground=WHITE, font=FONT_LABEL,
                        command=generate_password)
btn_add = Button(width=35, text="Add", bg=WHITE, fg=BLACK, highlightbackground=WHITE, font=FONT_LABEL,
                 command=add_entry)
btn_search = Button(width=17, text="Search", bg=WHITE, fg=BLACK, highlightbackground=WHITE, font=FONT_LABEL,
                    command=search_passwds)

canvas.grid(column=1, row=0, columnspan=2)
lbl_website.grid(column=0, row=1)
entry_website.grid(column=1, row=1, columnspan=1)
btn_search.grid(column=2, row=1)
lbl_email_user.grid(column=0, row=2)
entry_email_user.grid(column=1, row=2, columnspan=2)
lbl_passwd.grid(column=0, row=3)
entry_passwd.grid(column=1, row=3)
btn_gen_passwd.grid(column=2, row=3)
btn_add.grid(column=1, row=4, columnspan=2)

entry_email_user.insert(0, "latterkw@gmail.com")  # 0 at the beginning indicates at the start of the text box, as opposed to END at the...end

entry_website.focus()

window.mainloop()
