import tkinter as tk
import requests
import pytesseract
import cv2
import os
import pyautogui
import screenshot_organizer as ss_organizer

from tkinter import *
from tkinter import messagebox, ttk , font
from bs4 import BeautifulSoup

def dictionary():
    window = tk.Tk()
    window.configure(background = "#80471C")

    # setting up the dimensions of the window
    window.geometry("700x700")
    window.title("Definition")

    # change "Your Account" to your account's name.
    pytesseract.pytesseract.tesseract_cmd = r"C:\\Users\\Your Account\\AppData\\Local\\Programs\\Tesseract-OCR\\tesseract.exe"

    # button Style:
    style = ttk.Style()
    button = style.configure('TButton',
                    background = "#FFAA33",
                    foreground = "#36454F", 
                    font = ("Yu_Gothic_Medium",8, "bold"))

    # web scraping and url:
    def url_():
        global definition
        url = "https://en.wiktionary.org/wiki/"
        response = requests.get(f"{url}{user_input}")
        soup = BeautifulSoup(response.content, "html.parser")
        definition_n = soup.find("ol")
        definition = definition_n.text    

        if len(definition) < 250:
            first_part = definition[:250]
            definition_label_field.insert(0.4,first_part)
        elif len(definition) > 250:
            first_part = definition[:250] + "..."
            definition_label_field.insert(0.4,first_part)

    # show_definition:
    def get_definition():
        global user_input
        definition_label_field.delete(0.4,END)
        user_input = user_input_label_field.get("1.0","end-1c").strip().lower()
        url_()

        # check if data has been entered:
        if user_input:
            pass
        else:
            definition_label_field.delete(0.5,END)
            messagebox.showwarning("Warning","Please enter a word!")
            
    # take screenshot:
    def take_screenshot():
        pyautogui.hotkey('win', 'shift', 's')

    # convert screenshots to image:
    def _screenshot_():
        global user_input
        definition_label_field.delete(0.5,END)
        ss_organizer.screenshot_organize()
        image = cv2.imread("C:\\SS\\text.png")
        if not os.listdir("C:\\SS\\"):
            messagebox.showwarning("Note","There is no image/screenshot in folder")
        string_image = pytesseract.image_to_string(image).lower().strip()
        string_image = (string_image.replace("'","").replace('"','')
                        .replace(".","").replace(",","").replace("?","")
                        .replace("!","").replace("(","").replace(")",""))
        os.remove("text.png")
        user_input_label_field.delete(0.1, END)
        user_input_label_field.insert(0.1,string_image)
        user_input = string_image
        url_()
        
    # print out more examples:
    def see_more_():
        definition_label_field.delete(0.5,END)
        definition_label_field.insert(0.4,definition)
        
    # row and column:
    window.rowconfigure(0, weight = 1)
    window.rowconfigure(1, weight = 1)
    window.rowconfigure(2, weight = 1)
    window.rowconfigure(3, weight = 1)
    window.rowconfigure(4, weight = 1)
    window.rowconfigure(5, weight = 1)
    window.rowconfigure(6, weight = 1)
    window.rowconfigure(7, weight = 1)

    window.columnconfigure(0, weight = 1)
    window.columnconfigure(1, weight = 1)
    window.columnconfigure(2, weight = 1)

    # user_input field and submit button:
    user_input_label = ttk.Label(window, text = "User Input",
                                background = "#232B2B",
                                foreground = "White",
                                font = ('Yu_Gothic_Medium',12), 
                                justify = "center").grid(row = 0, column = 1)
    user_input_label_field = Text(window, height = 2, width = 40 ,
                                relief = GROOVE, borderwidth = 2,
                                font = ('Yu_Gothic_Medium',10))
    user_input_label_field.grid(row = 1, column = 1, sticky = W+E)
    submit_button = ttk.Button(window, text = "Submit", command = get_definition)
    submit_button.grid(row = 2, column = 1)

    # definition field and 'see more' button: 
    definition_label = ttk.Label(window, text = "Definition / Examples",
                                background = "#232B2B",
                                foreground = "White",
                                font = ('Yu_Gothic_Medium',12),
                                justify = "center").grid(row = 3, column = 1)
    definition_label_field = Text(window, height = 15, width = 60,
                                relief = GROOVE, borderwidth = 2,
                                font = ('Yu_Gothic_Medium',10))
    definition_label_field.grid(row = 4, column = 1)
    see_more_button = ttk.Button(window, text = "See More?", command = see_more_)
    see_more_button.grid(row = 5, column = 1)

    #image to string labels and buttons:
    screenshot_label_button = ttk.Button(window, text = "Convert image to text", command = _screenshot_)
    screenshot_label_button.grid(row = 7, column = 1)
    take_screenshot_button = ttk.Button(window, text = "Take screenshot", command = take_screenshot)
    take_screenshot_button.grid(row = 6, column = 1)

    window.mainloop()

if __name__ == "__main__":
    dictionary() 