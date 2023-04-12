import tkinter as tk
import random
import pyperclip
import webbrowser

def generate_password(length):
    lowercase = "abcdefghijklmnopqrstuvwxyz"
    uppercase = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    digits = "0123456789"
    symbols = "!@#$%^&*()_-+={[}]|\:;'<,>.?/"
    all_chars = lowercase + uppercase + digits + symbols

    password =""
    for i in range(length):
        password += random.choice(all_chars)

    return password

def show_password_label_animation():
    password_output_label.config(fg="green")
    password_output_label.after(200, lambda: password_output_label.config(fg="black"))

def generate_password_and_output():
    length = int(password_length_entry.get())
    password = generate_password(length)
    password_output_label.configure(text=password)
    pyperclip.copy(password)  # copy password to clipboard
    show_password_label_animation()
    add_to_password_history(password)

def show_generate_button_animation():
    generate_password_button.config(bg="#1E90FF")
    generate_password_button.after(200, lambda: generate_password_button.config(bg="#3CB371"))

def add_to_password_history(password):
    password_history.append(password)
    if len(password_history) > 5:
        password_history.pop(0)
    password_history_listbox.delete(0, tk.END)
    for p in password_history:
        password_history_listbox.insert(tk.END, "• " + p)

def open_github():
    webbrowser.open_new("https://github.com/ahmetalk")

window = tk.Tk()
window.title("Password Generator")
window.geometry("800x600")
window.resizable(False, False)  # set window size fixed

bg_img = tk.PhotoImage(file="C:/Users/Ahmet/Desktop/tkinter-pass-gen/angryimg.png")
bg_label = tk.Label(window, image=bg_img)
bg_label.place(relx=0.5, rely=0.5, anchor="center")

password_length_label = tk.Label(window, text="Password Length:")
password_length_entry = tk.Entry(window)
password_output_label = tk.Label(window, text="", font=("Arial", 16))

generate_password_button = tk.Button(window, text="Generate Password", command=generate_password_and_output, bg="#3CB371", font=("Arial", 12))
generate_password_button.bind("<Enter>", lambda event: show_generate_button_animation())

copy_password_button = tk.Button(window, text="Copy to Clipboard", command=lambda: pyperclip.copy(password_output_label.cget("text")), bg="#1E90FF", font=("Arial", 12))

password_history_listbox = tk.Listbox(window, height=5, font=("Montserrat", 12))
password_history_listbox.pack(side=tk.BOTTOM, fill=tk.BOTH)

github_logo_img = tk.PhotoImage(file="C:/Users/Ahmet/Desktop/tkinter-pass-gen/github-mark-white.png").subsample(3)
github_logo_button = tk.Button(window, image=github_logo_img, bd=0, command=open_github, cursor="hand2")
github_logo_button.image = github_logo_img
github_logo_button.place(relx=0, rely=0)

password_length_label.place(relx=0.25, rely=0.2, anchor="center")
password_length_entry.place(relx=0.75, rely=0.2, anchor="center")
generate_password_button.place(relx=0.4, rely=0.5, anchor="center")
copy_password_button.place(relx=0.6, rely=0.5, anchor="center")
password_output_label.place(relx=0.5, rely=0.65, anchor="center")

password_history = []

add_to_password_history("Welcome to Password Generator!")
add_to_password_history("Your password is super secure.")
add_to_password_history("Let's keep your accounts safe!")
add_to_password_history("Click the Generate button to get started.")

made_by_label = tk.Label(window, text="Made by github.com/ahmetalk", font=("Arial", 8))
made_by_label.place(relx=1, rely=0, anchor="ne")

window.mainloop()
