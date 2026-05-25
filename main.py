from tkinter import *
from tkinter import messagebox
import random
import pyperclip
# ---------------------------- PASSWORD GENERATOR ------------------------------- #
#Password Generator Project

def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    pawword_letters = [random.choice(letters) for _ in range(random.randint(8,10))]
    pawword_symbols = [random.choice(numbers) for _ in range(random.randint(2,4))]
    pawword_numbers = [random.choice(symbols) for _ in range(random.randint(2,4))]

    password_list = pawword_letters + pawword_symbols + pawword_numbers
    password = "".join(password_list)
    input_password.insert(0, password)
    pyperclip.copy(password)


    print(f"Your password is: {password}")

    # ---------------------------- SAVE PASSWORD ------------------------------- #

def save_password():
    website = input_website.get()
    email = input_email.get()
    password = input_password.get()

    if len(website) == 0 or len(password) == 0:
         messagebox.showinfo(title="Opps", message="Please make sure you haven't left any fields empty")
    else:
        is_ok = messagebox.askokcancel(title=website, message=f"These are the details entered: \nEmail: {email}\nPassword: {password} "
                                   f"\n Is it OK to save?")

        if is_ok:
            with open("password.txt", "a") as f:
                password_string = f"{website} | {email} | {password}\n"
                f.write(password_string)
                input_website.delete(0, END)
                input_password.delete(0, END)

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
window.configure(padx=20, pady=20, bg="white")

canvas = Canvas(bg="white", width=200, height=200, highlightthickness=0)
lock_image =PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=lock_image)
canvas.grid(row=0, column=1)

label_1 = Label(text="Website:", bg="white", font=("Arial", 12, "bold"))
label_1.grid(row=1, column=0)
label_2 = Label(text="Email/Username:", bg="white", font=("Arial", 12, "bold"))
label_2.grid(row=2, column=0)
label_3 = Label(text="Password:", bg="white", font=("Arial", 12, "bold"))
label_3.grid(row=3, column=0)

input_website = Entry(width=35)
input_website.grid(row=1, column=1, columnspan=2)
input_website.focus()

input_email= Entry(width=35)
input_email.grid(row=2, column=1, columnspan=2)
input_email.insert(0, "tommy.kuo@slc.com.tw")

input_password = Entry(width=21)
input_password.grid(row=3, column=1)

button = Button(text="Generate Password", command=generate_password)
button.grid(row=3, column=2)

button = Button(text="Add", width=36, command=save_password)
button.grid(row=4, column=1, columnspan=2)

print("Hello Test")

window.mainloop()

