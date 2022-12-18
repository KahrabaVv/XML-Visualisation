import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from tkinter import filedialog
import helpers.prettify as prettify

# Global Variables
text_input = None
text_output = None
messagebox = tk.messagebox

def loadFile(validate = False):
    # Open file dialog
    file = tk.filedialog.askopenfile(mode="r", filetypes=[("XML Files", "*.xml")])

    # Check if file is selected
    if file is None:
        return

    # Read the file
    text = file.read()

    # Check if file is empty
    if text == "":
        messagebox.showerror("Error", "File is empty!")
        return

    # Validate the file
    if validate:
        errors = validator.ErrorCheck(text)
        if errors:
            messagebox.showerror("Error", "File is not valid!")
            return

    # Clear the Text Area
    text_input.delete("1.0", "end")

    # Insert the text into the Text Area
    text_input.insert("1.0", text)

    # Show a success message
    messagebox.showinfo("Success", "File loaded successfully!")

def saveFile():
    # Get Text from Text Area
    text = text_output.get("1.0", "end-1c")

    # Check if Text Area is empty
    if text == "":
        messagebox.showerror("Error", "Please enter some text!")
        return

    # Open file dialog
    file = tk.filedialog.asksaveasfile(mode="w", filetypes=[("XML Files", "*.xml")])

    # Check if file is selected
    if file is None:
        messagebox.showerror("Error", "File not selected")
        return

    # Write the text into the file
    file.write(text)

    # Show a success message
    messagebox.showinfo("Success", "File saved successfully!")


def minifyBtn():
    # Get Text from Text Area
    text = text_input.get("1.0", "end-1c")

    # Check if Text Area is empty
    if text == "":
        messagebox.showerror("Error", "Please enter some text!")
        return

    # Minify the text
    minified_text = prettify.minify(text)

    # Clear the Text Area
    text_output.delete("1.0", "end")

    # Insert the minified text into the Text Area
    text_output.insert("1.0", minified_text)

    # Show a success message
    messagebox.showinfo("Success", "Text minified successfully!")

def beautifyBtn():
    # Get Text from Text Area
    text = text_input.get("1.0", "end-1c")

    # Check if Text Area is empty
    if text == "":
        messagebox.showerror("Error", "Please enter some text!")
        return

    # Beautify the text
    beautified_text = prettify.prettify(text)

    # Clear the Text Area
    text_output.delete("1.0", "end")

    # Insert the beautified text into the Text Area
    text_output.insert("1.0", beautified_text)

    # Show a success message
    messagebox.showinfo("Success", "Text beautified successfully!")

def loadMainGUI():
    # Create instance
    win = tk.Tk()

    # Add a title
    win.title("XML to JSON Conversion")

    # Disable resizing the GUI
    win.resizable(0, 0)

    # Tab Control introduced here --------------------------------------
    tabControl = ttk.Notebook(win)  # Create Tab Control

    # Create a tab
    tab1 = ttk.Frame(tabControl)

    # Add the tab
    tabControl.add(tab1, text='XML to JSON', padding=10)  # Add the tab
    tabControl.pack(expand=1, fill="both")  # Pack to make visible

    # Tab Control introduced here --------------------------------------
    # We are creating a container frame to hold all other widgets
    monty = ttk.LabelFrame(tab1, text='Input')
    monty.grid(column=0, row=0, padx=8, pady=4, rowspan=5)

    # Text Area for Input
    global text_input
    text_input = tk.Text(monty, width=50, height=30)
    text_input.grid(column=0, row=0, padx=8, pady=4)

    # Buttons (Validation, Minify, Beautify, Clear, Load, Save)
    monty2 = ttk.LabelFrame(tab1, text=' Actions ')
    monty2.grid(column=1, row=0, padx=8, pady=0, rowspan=1)

    action = ttk.Button(monty2, text="Compression", width=20)
    action.grid(column=2, row=0, padx=8, pady=4)

    action = ttk.Button(monty2, text="Decompression", width=20)
    action.grid(column=3, row=0, padx=8, pady=4)

    action = ttk.Button(monty2, text="Minify", width=20, command=minifyBtn)
    action.grid(column=2, row=1, padx=8, pady=4)

    action = ttk.Button(monty2, text="Beautify", width=20, command=beautifyBtn)
    action.grid(column=3, row=1, padx=8, pady=4)

    action = ttk.Button(monty2, text="Clear Output", width=44, command=lambda: text_output.delete("1.0", "end"))
    action.grid(column=2, row=2, padx=8, pady=4, columnspan=2)

    action = ttk.Button(monty2, text="Load", width=20,command=loadFile)
    action.grid(column=2, row=3, padx=8, pady=4)

    action = ttk.Button(monty2, text="Save", width=20, command=saveFile)
    action.grid(column=3, row=3, padx=8, pady=4)

    action = ttk.Button(monty2, text="Convert", width=44)
    action.grid(column=2, row=4, padx=8, pady=4, columnspan=2)

    # We are creating a container frame to hold all other widgets
    monty3 = ttk.LabelFrame(tab1, text=' Credits ', padding=10)
    monty3.grid(column=1, row=1, padx=8, pady=4, rowspan=5)

    credits = ttk.Label(monty3, text="David Ayman - 1900904", width=44)
    credits.grid(column=0, row=0, padx=8, pady=4)

    credits = ttk.Label(monty3, text="S2 - 0", width=44)
    credits.grid(column=0, row=1, padx=8, pady=4)

    credits = ttk.Label(monty3, text="S3 - 0", width=44)
    credits.grid(column=0, row=2, padx=8, pady=4)

    credits = ttk.Label(monty3, text="S4 - 0", width=44)
    credits.grid(column=0, row=3, padx=8, pady=4)

    credits = ttk.Label(monty3, text="S5 - 0", width=44)
    credits.grid(column=0, row=4, padx=8, pady=4)

    # We are creating a container frame to hold all other widgets
    monty4 = ttk.LabelFrame(tab1, text='Output')
    monty4.grid(column=2, row=0, padx=8, pady=4, rowspan=2)

    # Text Area for Output
    global text_output
    text_output = tk.Text(monty4, width=50, height=30, takefocus=2)
    text_output.grid(column=3, row=0, padx=8, pady=4)

    # Place cursor into name Entry
    text_input.focus()

    # Show a success message
    messagebox.showinfo("Welcome", "Welcome to XML to JSON Conversion!")

    # Start GUI
    win.mainloop()




