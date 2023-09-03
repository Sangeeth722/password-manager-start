from tkinter import *
from tkinter import messagebox
from random import choice , shuffle ,randint
import  pyperclip

# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def genarate_password():

    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    #nr_letters = random.randint(8, 10)
    #nr_symbols = random.randint(2, 4)
    #nr_numbers = random.randint(2, 4)



    password_letter = [choice(letters) for item in range(randint(8,10))]


    password_number = [choice(numbers) for item in range(randint(2,4))]

    passwor_symbols = [choice(symbols) for item in range(randint(2,4))]

    password_list = password_number  + passwor_symbols + password_letter

    shuffle(password_list)

    #password = ""
    #for char in password_list:
    #  password += char
    password = "".join(password_list)

    #delete previious password
    entry_pass.delete(0,END)
    pyperclip.copy(password)
    entry_pass.insert(0,password)

    # ---------------------------- SAVE PASSWORD ------------------------------- #


def save():
    website = entry_website.get()
    email = entry_email.get()
    password = entry_pass.get()
    if len(website) <= 0 or len(password) <= 0:
        messagebox.showerror(title="ERROR",message="Nothing enterd")
    else:
        is_ok = messagebox.askokcancel(title=website,message=f"These are detailed entered "
                                                    f"\n Email :{email} \n Password : {password} ")
        if is_ok:
           with open("data1.txt" , "a") as file:
               file.write(f"{website} | {email} | {password} \n")
               entry_website.delete(0,END)
               entry_pass.delete(0,END)

# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.config(padx=50,pady=50)
window.title("PASSWORD MANAGER")
canvas = Canvas(width=200,height=200)
logo = PhotoImage(file="logo.png")

canvas.create_image(100,100,image = logo)
canvas.grid(row=0,column=1)

#labels
website_label = Label(text="Website:")

website_label.grid(row=1,column=0)

email_user_label = Label(text="Email/Username : ")
email_user_label.grid(row=2,column=0)

password_label = Label(text="Password:")
password_label.grid(row=3,column=0)

#entries

entry_website = Entry(width=52)
entry_website.focus()
entry_website.grid(row=1,column=1,columnspan=2)

entry_email = Entry(width=52)
#entry_email.insert(0,"saths431@.com")
entry_email.grid(row=2,column=1,columnspan=2)

entry_pass = Entry(width=33)
entry_pass.grid(row=3,column=1)

#button
password_button = Button(text="Generate Password",command=genarate_password)
password_button.grid(row=3,column=2,columnspan=2)

add_button = Button(text="Add",width=44,command=save)
add_button.grid(row=4,column=1,columnspan=2)














window.mainloop()