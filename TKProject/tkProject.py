import tkinter as tk

#Create the main window
root = tk.Tk()
root.title("My First GUI Project")
root.geometry("600x400")

#Create a label
label = tk.Label(root, text = "Welcome to Mohit GUI Project", font=("Arial", 16))
label.pack()

#Create a entry field
entry = tk.Entry(root)
entry.pack()

#Create a button with Functionality

def greet():
    name = entry.get()
    result = label.config(text=f"Hello, {name}!")

btn = tk.Button(root, text="Greet me", command=greet)
btn.pack()

result_label = tk.Label(root, text="")
result_label.pack()

#Start GUI
root.mainloop()