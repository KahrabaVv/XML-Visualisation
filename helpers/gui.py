import copy
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from tkinter import filedialog
import helpers.validation as validator
import helpers.correction as correction
import helpers.prettify as prettify
import helpers.compressor as compressor
import helpers.converter as converter
import helpers.visualizer as visualizer

from helpers.sna import SNA_Helper
from helpers.graph import GraphOfUsers

# Authors of the project
authors = ["David Ayman - 1900904", "Kerolos Sameh - 1900144", "Andrew Adel - 1900158", "Mark Emad - 1901510",
           "Andrew Samir - 1900242"]

# Global Variables
text_input = None
text_output = None
messagebox = tk.messagebox
listbox, listbox_mutual = None, None
graph = None
pathOfLastFile = None
load_btn, save_btn, convert_btn, minify_btn, beautify_btn, analysis_btn, visualize_btn = None, None, None, None, None, None, None


def compress():
    # Get Text from Text Area
    text = text_input.get("1.0", "end-1c")

    # Check if Text Area is empty
    if text == "":
        messagebox.showerror("Error", "Please enter some text!")
        return

    # Open file dialog
    file = tk.filedialog.asksaveasfile(mode="w", filetypes=[("Compressed Files", "*.cmp")])

    if file is None:
        messagebox.showerror("Error", "File not selected")
        return

    compressor.compress(payload=prettify.minify(text), path=file.name + ".cmp")
    messagebox.showinfo("Success", "Statistics:\n\nInput Size: " + str(len(text)) + " bytes\nOutput Size: " + str(
        len(compressor.to_bytes(compressor.compress(text)))) + " bytes")
    # Show a success message
    messagebox.showinfo("Success", "Data compressed successfully and saved to file\n" + file.name + ".cmp")


def decompress():
    # Open file dialog
    file = tk.filedialog.askopenfile(mode="r", filetypes=[("Compressed Files", "*.cmp")])

    # Check if file is selected
    if file is None:
        return

    # Read the file
    decompressed = compressor.decompress(path=file.name)

    # Show the decompressed text
    text_input.delete("1.0", "end-1c")
    text_input.insert("1.0", decompressed)

    # Clear the Text Area
    text_output.delete("1.0", "end")

    # Show a success message
    messagebox.showinfo("Success", "Data decompressed successfully and loaded in the text area")


def fixErrors(path: str):
    # Fix the errors
    fixedPayload = correction.correction(path=path)

    # Insert the fixed text into the Text Area
    text_input.insert("1.0", fixedPayload)

    # Show a success message
    messagebox.showinfo("Success", "File fixed successfully!")


def loadFile(validate=True):
    # Clear the Text Area
    text_input.delete("1.0", "end")

    # Open file dialog
    file = tk.filedialog.askopenfile(mode="r", filetypes=[("XML Files", "*.xml"), ("Text Files", "*.txt")])

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
        errors = validator.ErrorCheck(path=file.name)
        message = ""
        for error in errors:
            message += str(error) + "\r"

        if message != "":
            # Message box with button to fix
            result = messagebox.askyesno("Error",
                                         "File contains errors:\r\r" + message + "\r\rDo you want to fix the errors?",
                                         icon="warning")
            if result:
                fixErrors(path=file.name)
            else:
                return
        else:
            # Insert the text into the Text Area
            text_input.insert("1.0", text)

    global graph
    graph = GraphOfUsers(99, file.name)

    # Enable buttons
    toggle(state="normal")

    # Show a success message
    messagebox.showinfo("Success", "File loaded successfully!")


def saveFile():
    # Get Text from Text Area
    text = text_output.get("1.0", "end-1c")

    # Check if Text Area is empty
    if text == "":
        messagebox.showerror("Error", "Please enter some text!")
        return

    # Check if Text Area is JSON or XML
    if text[0] == "{":
        filetypes = [("JSON Files", "*.json")]
    else:
        filetypes = [("XML Files", "*.xml")]

    # Open file dialog
    file = tk.filedialog.asksaveasfile(mode="w", filetypes=filetypes)

    # Check if file is selected
    if file is None:
        messagebox.showerror("Error", "File not selected")
        return

    # Write the text into the file
    file.write(text)

    # Show a success message
    messagebox.showinfo("Success", "File saved successfully!")


def convertToJSON():
    # Get Text from Text Area
    text = text_input.get("1.0", "end-1c")

    # Check if Text Area is empty
    if text == "":
        messagebox.showerror("Error", "Please enter some text!")
        return

    # Convert the text to JSON
    json_text = converter.xmlToJSON(prettify.beautify(text))

    # Clear the Text Area
    text_output.delete("1.0", "end")

    # Insert the JSON text into the Text Area
    text_output.insert("1.0", json_text)


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


def beautifyBtn():
    # Get Text from Text Area
    text = text_input.get("1.0", "end-1c")

    # Check if Text Area is empty
    if text == "":
        messagebox.showerror("Error", "Please enter some text!")
        return

    # Beautify the text
    beautified_text = prettify.beautify(text)

    # Clear the Text Area
    text_output.delete("1.0", "end")

    # Insert the beautified text into the Text Area
    text_output.insert("1.0", beautified_text)


def visualize():
    # Get Text from Text Area
    text = text_input.get("1.0", "end-1c")

    # Check if Text Area is empty
    if text == "":
        messagebox.showerror("Error", "Please enter some text!")
        return

    visualizer.visualizeGraph(pathOfLastFile)


def getMutualFriends(user1, user2):
    # Convert user1 and user2 to int
    user1 = graph.getUserFromId(int(user1))
    user2 = graph.getUserFromId(int(user2))
    mutual_friends = SNA_Helper().getMutualFollowers(user1, user2)
    listbox_mutual.delete(0, tk.END)
    if len(mutual_friends) == 0:
        listbox_mutual.insert(tk.END, "No mutual friends found")
    else:
        for friend in mutual_friends:
            listbox_mutual.insert(tk.END, graph.getUserFromId(friend).name)


def getSuggestions(user):
    # Get suggestions for a user
    suggestions = SNA_Helper().suggestFollowers(graph.getUserFromId(int(user)), graph)
    listbox_suggestions.delete(0, tk.END)
    if len(suggestions) == 0:
        listbox_suggestions.insert(tk.END, "No suggestions found")
    else:
        for suggestion in suggestions:
            listbox_suggestions.insert(tk.END, graph.getUserFromId(suggestion).name)


def search(text: str):
    # search for posts that contain the text
    results = SNA_Helper().post_search(graph, text)

    # clear the listbox
    listbox.delete(0, tk.END)

    # list of posts including the author and the content
    for author in results:
        if author == "No Results Found":
            listbox.insert(tk.END, author)
        else:
            listbox.insert(tk.END, author + ": " + results[author])


def populateMatrix(tab):
    global graph
    # Label for the matrix
    ttk.Label(tab, text="Adjacency Matrix", font=("Helvetica", 16)).grid(column=0, row=0, padx=8, pady=4)

    # Get the number of users
    lenOfUsers = graph.numUsers

    # create the tree and scrollbars
    trv = ttk.Treeview(tab, selectmode='browse')
    trv.grid(row=1, column=0, padx=5, pady=5, sticky='nsew')

    # Defining number of columns
    arry = ()
    for i in range(0, lenOfUsers + 1):
        arry = arry + (str(i + 1),)
    trv["columns"] = arry

    # Defining heading
    trv['show'] = 'headings'

    # Formatting columns
    for column in trv["columns"]:
        trv.column(column, width=63, anchor='c')

    # Populating the columns
    for column in trv["columns"]:
        if column == "1":
            trv.heading(column, text="User ID")
        else:
            if graph.vertices[int(column) - 2] is not None:
                trv.heading(column, text=graph.vertices[int(column) - 2].id)
            else:
                break

    # Deep Copy of the edges
    customizedEdges = copy.deepcopy(graph.edges)
    for i in range(0, lenOfUsers):
        for j in range(0, len(customizedEdges[i])):
            customizedEdges[i][j] = str(customizedEdges[i][j])
        customizedEdges[i].insert(0, graph.vertices[i].id)

    # Inserting the data
    for i in range(0, lenOfUsers):
        trv.insert("", 'end', text=graph.vertices[i].id, values=customizedEdges[i])


def visualize():
    visualizer.visualizeGraph(graph)


def toggle(state: str = "disabled"):
    # Toggle all buttons
    save_btn.configure(state=state)
    convert_btn.configure(state=state)
    minify_btn.configure(state=state)
    beautify_btn.configure(state=state)
    analysis_btn.configure(state=state)
    visualize_btn.configure(state=state)


def loadMainGUI():
    # Create instance
    win = tk.Tk()

    # Add a title
    win.title("XML Visualizer")

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

    # Buttons (Validation, Minify, Beautify, Clear, Load, Save, Visualize, Analysis)
    monty2 = ttk.LabelFrame(tab1, text=' Actions ')
    monty2.grid(column=1, row=0, padx=8, pady=0, rowspan=1)

    # Compression and Decompression
    ttk.Button(monty2, text="Compression", width=20, command=compress).grid(column=2, row=0, padx=8, pady=4)
    ttk.Button(monty2, text="Decompression", width=20, command=decompress).grid(column=3, row=0, padx=8, pady=4)

    # Minify and Beautify
    global minify_btn, beautify_btn
    minify_btn = ttk.Button(monty2, text="Minify", width=20, command=minifyBtn)
    minify_btn.grid(column=2, row=1, padx=8, pady=4)
    beautify_btn = ttk.Button(monty2, text="Beautify", width=20, command=beautifyBtn)
    beautify_btn.grid(column=3, row=1, padx=8, pady=4)

    # Clear
    ttk.Button(monty2, text="Clear Output", width=44, command=lambda: text_output.delete("1.0", "end")).grid(column=2,
                                                                                                             row=3,
                                                                                                             padx=8,
                                                                                                             pady=4,
                                                                                                             columnspan=2)
    # Load and Save
    global save_btn
    ttk.Button(monty2, text="Load File", width=20, command=loadFile).grid(column=2, row=4, padx=8, pady=4)
    save_btn = ttk.Button(monty2, text="Save Output", width=20, command=saveFile)
    save_btn.grid(column=3, row=4, padx=8, pady=4)

    # Convert Button
    global convert_btn
    convert_btn = ttk.Button(monty2, text="Convert to JSON", width=44, command=convertToJSON)
    convert_btn.grid(column=2, row=5, padx=8, pady=4, columnspan=2)

    # Analysis Button
    global analysis_btn
    analysis_btn = ttk.Button(monty2, text="Analysis", width=44, command=newWindow)
    analysis_btn.grid(column=2, row=6, padx=8, pady=4, columnspan=2)

    # Visualize Button
    global visualize_btn
    visualize_btn = ttk.Button(monty2, text="Visualize", width=44, command=visualize)
    visualize_btn.grid(column=2, row=7, padx=8, pady=4, columnspan=2)

    # We are creating a container frame to hold all other widgets
    monty3 = ttk.LabelFrame(tab1, text=' Credits ', padding=10)
    monty3.grid(column=1, row=1, padx=8, pady=4, rowspan=5)

    # Credits
    for author in authors:
        ttk.Label(monty3, text=author, width=44).grid(column=0, row=authors.index(author), padx=8, pady=4)

    # We are creating a container frame to hold all other widgets
    monty4 = ttk.LabelFrame(tab1, text='Output')
    monty4.grid(column=2, row=0, padx=8, pady=4, rowspan=2)

    # Text Area for Output
    global text_output
    text_output = tk.Text(monty4, width=50, height=30, takefocus=2)
    text_output.grid(column=3, row=0, padx=8, pady=4)

    # Place cursor into name Entry
    text_input.focus()

    # Disable all buttons
    toggle(state="disabled")

    # Show a success message
    messagebox.showinfo("Welcome", "Welcome to XML Visualizer!")

    # Show a warning message
    messagebox.showwarning("Warning", "Load a file to start!")

    # Start GUI
    win.mainloop()


def newWindow():
    global graph
    mostInf = SNA_Helper().mostInfluencerUser(graph)
    mostAct = SNA_Helper().mostActiveUser(graph)
    mostActiveUser = "Most Active User: #" + str(mostAct.id) + " " + mostAct.name + " follows " + str(
        len(graph.getUserFollowedList(graph.vertices[mostAct.id]))) + " users"
    mostInfluencedUser = "Most Influencer User: #" + str(mostInf.id) + " " + mostInf.name + " with " + str(
        len(mostInf.followers)) + " followers"

    # Create instance
    win = tk.Tk()

    # Add a title
    win.title("Network Analysis")

    # Disable resizing the GUI by passing in False/False
    win.resizable(False, False)

    # Create Matrix Analysis Tab
    tabControl = ttk.Notebook(win)  # Create Tab Control
    tabControl.grid(column=0, row=0, padx=8, pady=4, rowspan=5)
    tab1 = ttk.Frame(tabControl)  # Create a tab
    tabControl.add(tab1, text='Matrix Analysis')  # Add the tab

    # 2D Matrix
    populateMatrix(tab1)

    # Create Network Analysis Tab
    tab2 = ttk.Frame(tabControl)  # Add a second tab
    tabControl.add(tab2, text='SNA Analysis')  # Make second tab visible

    # Create Posts Tab
    tab4 = ttk.Frame(tabControl)  # Add a second tab
    tabControl.add(tab4, text='Posts')  # Make second tab visible

    # We are creating a container frame to hold all other widgets
    monty1 = ttk.LabelFrame(tab1, text=' Matrix Analysis ')
    monty1.grid(column=0, row=0, padx=8, pady=4, rowspan=5)

    # tab 2 contains SNA Analysis (Most Influential (Name and Score), Most Popular (Name and Score), Most Active (Name and Score))
    # We are creating a container frame to hold all other widgets
    monty2 = ttk.LabelFrame(tab2, text=' SNA Statistics ')
    monty2.grid(column=0, row=0, padx=8, pady=4, rowspan=5)

    la = ttk.Label(monty2, text=mostInfluencedUser, width=70)
    la.grid(column=0, row=0, padx=8, pady=4)
    la = ttk.Label(monty2, text=mostActiveUser, width=70)
    la.grid(column=0, row=1, padx=8, pady=4)

    monty21 = ttk.LabelFrame(tab2, text=' Friend Suggestions ')
    monty21.grid(column=0, row=6, padx=8, pady=4, rowspan=5)

    global listbox_suggestions
    listbox_suggestions = tk.Listbox(monty21, width=70, height=5)
    listbox_suggestions.grid(column=0, row=1, padx=8, pady=4, columnspan=2)

    # Text Area for Input
    input_suggestion = ttk.Entry(monty21, width=44)
    input_suggestion.grid(column=0, row=0, padx=8, pady=4)
    input_suggestion.insert(0, "Enter a user ID")

    # Button to find suggestions
    action = ttk.Button(monty21, text="Find", width=20, command=lambda: getSuggestions(input_suggestion.get()))
    action.grid(column=1, row=0, padx=8, pady=4)

    # Monty 22 contains mutual friends
    monty22 = ttk.LabelFrame(tab2, text=' Mutual Friends ')
    monty22.grid(column=0, row=20, padx=8, pady=4, rowspan=5)

    # Listbox for mutual friends
    global listbox_mutual
    listbox_mutual = tk.Listbox(monty22, width=70, height=5)
    listbox_mutual.grid(column=0, row=1, padx=8, pady=4, columnspan=3)

    # Two text areas for first and second user
    input_mutual1 = ttk.Entry(monty22, width=22)
    input_mutual1.grid(column=0, row=0, padx=8, pady=4)
    input_mutual1.insert(0, "ID of first user")

    input_mutual2 = ttk.Entry(monty22, width=22)
    input_mutual2.grid(column=1, row=0, padx=8, pady=4)
    input_mutual2.insert(0, "ID of second user")

    # Find button
    action = ttk.Button(monty22, text="Find", width=15,
                        command=lambda: getMutualFriends(input_mutual1.get(), input_mutual2.get()))
    action.grid(column=2, row=0, padx=8, pady=4)

    # tab 4 contains input for search and search button in same row and scrollable list of posts in another row
    # We are creating a container frame to hold all other widgets
    monty4 = ttk.LabelFrame(tab4, text=' Posts ')
    monty4.grid(column=0, row=0, padx=8, pady=4, rowspan=5)

    # Text Area for Input + Placeholder
    input = ttk.Entry(monty4, width=44)
    input.pack()
    input.grid(column=0, row=0, padx=8, pady=4)
    input.focus()

    global listbox
    listbox = tk.Listbox(monty4, width=70, height=20)
    listbox.grid(column=0, row=1, padx=8, pady=4, columnspan=2)

    action = ttk.Button(monty4, text="Search", width=20, command=lambda: search(input.get()))
    action.grid(column=1, row=0, padx=8, pady=4)

    # Retrieve all posts
    search("")
