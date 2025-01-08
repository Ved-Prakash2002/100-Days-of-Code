from tkinter import *  # Import all Tkinter classes for GUI creation.
from tkinter import messagebox  # Import messagebox for displaying alerts and confirmations.
from Test import PasswordGenerator  # Import a custom password generator class.
import pyperclip  # Import pyperclip to copy text to the clipboard.
import json  # Import json for reading and writing data to files.

# ---------------------------- PASSWORD GENERATOR ------------------------------- #


def generate_password():
    """
    Generates a random password using the PasswordGenerator class.
    Inserts the password into the password entry field and copies it to the clipboard.
    """
    generated_password = PasswordGenerator().generate_password()  # Generate a new password.
    password_entry.insert(0, generated_password)  # Insert the password into the password field.
    pyperclip.copy(generated_password)  # Copy the password to the clipboard.


def find_password():
    """
    Searches for a saved password by website name.
    Displays the details if found or an error message if not found.
    """
    website = website_entry.get()  # Get the website name from the entry field.
    try:
        with open("data.json", "r") as file:  # Try to open the data file.
            data = json.load(file)  # Load the data from the file.
            try:
                password = data[website].get("Password")  # Retrieve the password for the given website.
            except KeyError:
                # If the website is not found in the data, show an error message.
                messagebox.showinfo(title=website, message="No details for the website exists")
    except FileNotFoundError:
        # If the data file is not found, show an error message.
        messagebox.showinfo(title="Oops", message="No Data File Found")

    if website in data:
        # If the website exists in the data, display the details in a message box.
        messagebox.askokcancel(title=website, message=f"These are the details you entered:\nWebsite: "
                                                      f"{website}\nPassword: {password}\n")


# ---------------------------- SAVE PASSWORD ------------------------------- #


def save():
    """
    Saves a new website, username, and password entry to the data file.
    Updates the data file if it exists or creates a new one if it doesn't.
    """
    website = website_entry.get()  # Get the website name.
    username = username_entry.get()  # Get the email/username.
    password = password_entry.get()  # Get the password.
    # Create a new dictionary with the website as the key and its details as the value.
    new_data = {website: {
        "E-mail": username,
        "Password": password
    }}

    if website == "" or username == "" or password == "":
        # If any fields are empty, show an error message.
        messagebox.showinfo(title="Oops", message="Please don't leave any fields empty")
    else:
        # Confirm with the user before saving the details.
        is_ok = messagebox.askokcancel(title=website, message=f"These are the details you entered:\nEmail: "
                                                              f"{username}\nPassword: {password}\nIs it OK to save?")
        if is_ok:
            try:
                with open("data.json", "r") as file:  # Try to open the data file.
                    data = json.load(file)  # Load the existing data.
            except FileNotFoundError:
                # If the file doesn't exist, create a new file and write the data.
                with open("data.json", "w") as file:
                    json.dump(new_data, file, indent=4)  # Save the new data.
            else:
                # Update the existing data with the new entry.
                data.update(new_data)

                with open("data.json", "w") as file:
                    json.dump(data, file, indent=4)  # Write the updated data to the file.
            finally:
                # Clear the input fields.
                website_entry.delete(0, END)
                password_entry.delete(0, END)


# ---------------------------- UI SETUP ------------------------------- #

# Set up the main application window.
window = Tk()
window.title("Password Manager")  # Set the window title.
window.config(padx=50, pady=50)  # Add padding around the window.

# Canvas for the logo
canvas = Canvas(width=200, height=200)
lock_image = PhotoImage(file="logo.png")  # Load the logo image.
canvas.create_image(100, 100, image=lock_image)  # Display the logo on the canvas.
canvas.grid(row=0, column=1)

# Labels
website_label = Label(text="Website:")
website_label.grid(row=1, column=0)
username_label = Label(text="Email/Username:")
username_label.grid(row=2, column=0)
password_label = Label(text="Password:")
password_label.grid(row=3, column=0)

# Entry fields
website_entry = Entry(width=17)
website_entry.grid(row=1, column=1)
website_entry.focus()  # Place the cursor in the website entry field by default.

username_entry = Entry(width=35)
username_entry.grid(row=2, column=1, columnspan=2)
username_entry.insert(0, "ved@gmail.com")  # Pre-fill the email field with a default value.

password_entry = Entry(width=17)
password_entry.grid(row=3, column=1)

# Buttons
generate_password_button = Button(text="Generate Password", command=generate_password)
generate_password_button.grid(row=3, column=2)

add_button = Button(text="Add", width=30, command=save)
add_button.grid(row=4, column=1, columnspan=2)

search_button = Button(text="Search", width=15, command=find_password)
search_button.grid(row=1, column=2)

# Start the Tkinter event loop.
window.mainloop()
