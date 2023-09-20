import tkinter as tk
import random
import pyperclip
from tkinter import messagebox

WHITE = "#E8F6EF"
TEAL = "#1B9C85"
YELLOW = "#FFE194"
NAVY = "#4C4C6D"
DEFAULT_FONT_STYLE = ("Ariel", 14)
BOLD_FONT_STYLE = ("Ariel", 20, "bold")
PASSWORD_CHARACTERS = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz@#$%&*0123456789"

class password_generator:
    def __init__(self):
        #initializing window
        self.window = tk.Tk(sync=True)
        self.window.geometry("800x500")
        self.window.title("Password generator")

        self.length_expresssion = ""

        #crating frames
        self.display_frame = self.create_display_frame()
        self.button_frame = self.create_button_frame()

        #Configuring button frame
        self.button_frame.rowconfigure(0, weight=1)
        for x in range(3):
            self.button_frame.columnconfigure(x, weight=1)

        #creating labels
        self.message_label, self.output , self.password_length = self.create_display_labels()         

        #creating buttons
        self.create_buttons()

        #binding buttons
        self.bind_keys()

    def create_display_frame(self):
        frame = tk.Frame(self.window, height=200, width=600, bg=WHITE)
        frame.pack(expand=True, fill="both")
        return frame

    def create_button_frame(self):
        button_frame = tk.Frame(self.window,height=100 ,width= 600)
        button_frame.pack(expand=True, fill="both")
        return button_frame

    def create_display_labels(self):
        message_label = tk.Label(self.display_frame, text="type the length of password to generate it!", font=BOLD_FONT_STYLE, bg=WHITE, fg=NAVY, anchor=tk.CENTER)
        message_label.pack(expand=True,fill="both")

        output_label = tk.Label(self.display_frame, text="", font=BOLD_FONT_STYLE, fg=NAVY, bg=WHITE, anchor=tk.CENTER)
        output_label.pack()

        length_label = tk.Label(self.display_frame, text="", font=BOLD_FONT_STYLE, fg=NAVY, bg=WHITE, anchor=tk.CENTER)
        length_label.pack()

        return message_label, output_label, length_label
    
    def add_to_expression(self, digit):
        self.length_expresssion += str(digit)
        self.password_length.config(text=self.length_expresssion)

    def generate_password(self):
        self.password = ""
        length = int(self.length_expresssion)
        if length > 20:
            self.password = "Too big password! enter value in between 8 and 20"
        elif length < 8:
            self.password = "Too small password! enter value in between 8 and 20"
        else:
            for _ in range(length):
                self.password += random.choice(PASSWORD_CHARACTERS)
        self.output.config(text=self.password)
    
    def clear_display(self):
        self.output.config(text="")
        self.password_length.config(text="")
        self.length_expresssion = ""

    def create_buttons(self):
        self.create_copy_button()
        self.create_clear_button()
        self.create_generate_button()

    def create_copy_button(self):
        copy_btn = tk.Button(self.button_frame, text="Copy!", font=DEFAULT_FONT_STYLE, borderwidth=0, bg=TEAL, fg=YELLOW, command=self.copy_password)
        copy_btn.grid(row=0,column=2, sticky=tk.NSEW)
    
    def create_clear_button(self):
        copy_btn = tk.Button(self.button_frame, text="Clear!", font=DEFAULT_FONT_STYLE, borderwidth=0, bg=TEAL, fg=YELLOW, command=lambda : self.clear_display())
        copy_btn.grid(row=0,column=0, sticky=tk.NSEW)
    
    def create_generate_button(self):
        copy_btn = tk.Button(self.button_frame, text="Generate!", font=DEFAULT_FONT_STYLE, borderwidth=0, bg=TEAL, fg=YELLOW, command=lambda : self.generate_password())
        copy_btn.grid(row=0,column=1, sticky=tk.NSEW)

    def copy_password(self):
        try:
            if len(self.password) > 20 or 8 > len(self.password):
                raise Exception
            pyperclip.copy(self.password)
            messagebox.showinfo("Success!","Password copied successfully")
        except Exception:
            messagebox.showwarning("Error", "No password found")
        
    def clear_digit(self):
        self.length_expresssion = self.length_expresssion[:-1]
        self.password_length.config(text=self.length_expresssion)

    def bind_keys(self):
        for x in range(10):
            self.window.bind(str(x), lambda event, digit = x: self.add_to_expression(digit))
        self.window.bind("<BackSpace>", lambda event: self.clear_digit())
        self.window.bind("<Return>", lambda event: self.generate_password())
        self.window.bind("<Delete>", lambda event : self.clear_display())
        self.window.bind("<Control-c>", lambda event : self.copy_password())

    def run(self):
        self.window.mainloop()

if __name__ == "__main__":
    myapp = password_generator()    
    myapp.run()