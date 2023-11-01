import tkinter as tk
import dictionary as _dict_
import os
from tkinter import *
from tkinter import ttk, filedialog

# Creating the window.
window = tk.Tk()
window.title("Notebook")
window.geometry("1000x800")
window.configure(background="#352315")
window.resizable(width=True, height=True)
window_update = window.update()

# Button Style:
def _button_():
    style = ttk.Style()
    button = style.configure("TButton",
                            background="#FFAA33",
                            foreground="#36454F",
                            font=("Yu_Gothic_Medium", 8, "bold"))

# text field: 
def user_field(window):
    global user_input_label_field
    user_input_label_field = Text(window,
                                relief=GROOVE, font=('Yu_Gothic_Medium', 12), background="#008080",
                                foreground="White", insertbackground="white")
    user_input_label_field.pack(expand=TRUE, fill=BOTH)

# dictionary: 
def dict_input():
    _dict_.dictionary()

# Saving the content:
def save_text():
    global user_input_label_field
    file_path = filedialog.asksaveasfilename(defaultextension=".txt", filetypes=[("Text files", "*.txt"), ("All files", "*.*")])
    if file_path:
        with open(file_path, 'w') as file:
            text_content = user_input_label_field.get("1.0", "end-1c")
            file.write(text_content)

# Loading the content:
def load_text(window):
    global user_input_label_field
    global file_paths
    file_path = filedialog.askopenfilename(defaultextension=".txt", filetypes=[("Text files", "*.txt"), ("All files", "*.*")])
    if file_path:
        with open(file_path, "r") as file:
            text_content = file.read()
            user_input_label_field.delete('1.0', END)
            user_input_label_field.insert('1.0', text_content)
        # Store the file path for the current window
        file_paths[window] = file_path
        rename_(window)

# Renaming window when you load a text file:
def rename_(window):
    if file_paths.get(window):
        window.title(os.path.basename(file_paths[window]).replace('.txt', ''))


# New Window Tabs: 
child_windows = []
file_paths = {}
def window_():
    new_window = tk.Toplevel()
    new_window.title("New Window")
    new_window.configure(background="#352315")
    # window x,y:
    new_window.geometry("1000x800")
    new_window.resizable(width=True, height=True)
    new_window_update = new_window.update()
    _button_() 
    
    new_window_button = ttk.Button(new_window, text="New Window", command=window_)
    new_window_button.pack(side=TOP, anchor=N, expand=False)

    dictionary_button = ttk.Button(new_window, text="Dictionary", command=dict_input)
    dictionary_button.pack(side=TOP, anchor=N, expand=False)
    save_bttn = ttk.Button(new_window, text="Save", command=save_text)
    save_bttn.pack(side=TOP, anchor=N, expand=False)

    load_bttn = ttk.Button(new_window, text="Load", command=lambda: load_text(new_window))
    load_bttn.pack(side=TOP, anchor=N, expand=False)
    user_field(new_window)
    child_windows.append(new_window)
    rename_(new_window)

    def on_closing_new_window():
        if tk.messagebox.askokcancel("Quit", "Do you want to close window?"):
            new_window.destroy()

    new_window.protocol("WM_DELETE_WINDOW", on_closing_new_window)

# Buttons: 
new_window_button = ttk.Button(window, text="New Window", command=window_)
new_window_button.pack(side=TOP, anchor=N, expand=False)

dictionary_button = ttk.Button(window, text="Dictionary", command=dict_input)
dictionary_button.pack(side=TOP, anchor=N, expand=False)

save_bttn = ttk.Button(window, text="Save", command=save_text)
save_bttn.pack(side=TOP, anchor=N, expand=False)

load_bttn = ttk.Button(window, text="Load", command=lambda: load_text(window))
load_bttn.pack(side=TOP, anchor=N, expand=False)

def on_closing():
    if tk.messagebox.askokcancel("Quit", "Do you want to quit?"):
        window.destroy()

window.protocol("WM_DELETE_WINDOW", on_closing)

user_field(window)
_button_()
window.mainloop()