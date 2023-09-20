import tkinter as tk 

# Fonts
DEFAULT_FONT_STYLE = ("Ariel", 20)
SMALL_FONT_STYLE = ("Ariel", 12)
LARGE_FONT_STYLE = ("Ariel", 32, "bold")
DIGIT_FONT_STYLE = ("Ariel", 20, "bold")

# Colors
WHITE = "#FDF8FF"
PURPLE = "#8951E7"
LIGHT_PURPLE = "#DBC9FA"
VIVID_GAMBOGE = "#FF9900"
LIGHT_VIVID_GAMBOGE = "#FFD699"
BLACK = "#1C1C1C"
GRAY = "#848482"


class Calculator:
    def __init__(self):
        # Initializing Window
        self.window = tk.Tk(sync=True)
        self.window.geometry("375x667")
        self.window.resizable(0,0)
        self.window.title("Calculator")

        #Initializing variables
        self.total_expression = ""
        self.current_expression = ""
        self.digits = {
            7:(1,1), 8:(1,2), 9:(1,3),
            4:(2,1), 5:(2,2), 6:(2,3),
            1:(3,1), 2:(3,2), 3:(3,3),
            '.':(4,1), 0:(4,2)
        }
        self.operations = {
            "/":"\u00F7", "*":"\u00D7", "-":"-", "+":"+"
        }

        # Create a frame to hold the widgets
        self.display_frame = self.create_display_frame()
        self.button_frame = self.create_button_frame()
        self.button_frame.rowconfigure(0, weight=1)
        for x in range(1,5):
            self.button_frame.rowconfigure(x, weight=1)
            self.button_frame.columnconfigure(x, weight=1)

        # Create labels
        self.total_label, self.current_label = self.create_display_label()

        # Create Buttons
        self.create_buttons()

        # bind keys
        self.bind_keys()

    def create_display_frame(self):
        frame = tk.Frame(self.window, height=221, bg=WHITE)
        frame.pack(expand=True, fill="both")
        return frame
    
    def create_display_label(self):
        total_label = tk.Label(self.display_frame, text=self.total_expression, anchor=tk.E, bg = WHITE, fg = GRAY, padx=24, font=SMALL_FONT_STYLE)
        total_label.pack(expand=True, fill='both')

        current_label = tk.Label(self.display_frame, text=self.current_expression, anchor=tk.E, bg = WHITE, fg = BLACK, padx=24, font=LARGE_FONT_STYLE)
        current_label.pack(expand=True, fill='both')

        return total_label, current_label

    def create_button_frame(self):
        frame = tk.Frame(self.window, bg=WHITE)
        frame.pack(expand=True, fill="both")
        return frame

    def create_digit_buttons(self):
        for digit,grid_value in self.digits.items():
            button = tk.Button(self.button_frame, text=str(digit), bg = WHITE, fg= BLACK, font=DIGIT_FONT_STYLE, borderwidth=0, command= lambda x=digit : self.add_to_expression(x))  
            button.grid(row=grid_value[0], column=grid_value[1], sticky=tk.NSEW)

    def create_equals_button(self):
        button = tk.Button(self.button_frame, text="=", bg = PURPLE, fg = WHITE, font=DEFAULT_FONT_STYLE, borderwidth=0, command=lambda : self.evaluate())
        button.grid(row=4,column=4, sticky=tk.NSEW)
    
    def create_clear_button(self):
        button = tk.Button(self.button_frame, text="CE", bg = VIVID_GAMBOGE, fg = WHITE, font=DEFAULT_FONT_STYLE, borderwidth=0, command= lambda : self.clear_expression())
        button.grid(row=0,column=1, sticky=tk.NSEW)

    def create_clear_digit_button(self):
        button = tk.Button(self.button_frame, text="DEL", bg = LIGHT_VIVID_GAMBOGE, fg = VIVID_GAMBOGE, font=DEFAULT_FONT_STYLE, borderwidth=0, command= lambda : self.clear_digit())
        button.grid(row=4, column=3, sticky=tk.NSEW)

    def create_square_button(self):
        button = tk.Button(self.button_frame, text="X\u00b2", bg = LIGHT_VIVID_GAMBOGE, fg = VIVID_GAMBOGE, font=DEFAULT_FONT_STYLE, borderwidth=0, command= lambda : self.square())
        button.grid(row=0, column=2, sticky=tk.NSEW)

    def create_sqrt_button(self):
        button = tk.Button(self.button_frame, text="\u221aX", bg = LIGHT_VIVID_GAMBOGE, fg = VIVID_GAMBOGE, font=DEFAULT_FONT_STYLE, borderwidth=0, command= lambda : self.sqrt())
        button.grid(row=0, column=3, sticky=tk.NSEW)

    def create_operator_buttons(self):
        i = 0
        for operator, symbol in self.operations.items():
            button = tk.Button(self.button_frame, text=symbol, font=DEFAULT_FONT_STYLE, bg=LIGHT_PURPLE, fg= PURPLE, borderwidth=0, command= lambda x=operator : self.add_to_expression(x))
            button.grid(row=i, column=4, sticky=tk.NSEW)
            i+=1

    def create_buttons(self):
        self.create_digit_buttons()
        self.create_operator_buttons()
        self.create_equals_button()
        self.create_clear_button()
        self.create_clear_digit_button()
        self.create_square_button()
        self.create_sqrt_button()

    def update_total_label(self):
        expression = self.total_expression
        for operator, symbol in self.operations.items():
            expression = expression.replace(operator, f' {symbol} ')
        self.total_label.config(text=expression)

    def update_current_label(self):
        expression = self.current_expression
        for operator, symbol in self.operations.items():
            expression = expression.replace(operator, f' {symbol} ')
        self.current_label.config(text=expression)

    def add_to_expression(self, value):
        self.current_expression += str(value)
        self.update_current_label()

    def clear_expression(self):
        self.current_expression = ""
        self.total_expression = ""
        self.update_current_label()
        self.update_total_label()

    def clear_digit(self):
        self.current_expression = self.current_expression[:-1]
        self.update_current_label()

    def evaluate(self):
        self.total_expression = self.current_expression
        self.update_total_label()

        try:
            x = eval(self.current_expression)
            if x > 99999999999999:
                raise OverflowError
            self.current_expression = str(x)
            self.current_expression = self.current_expression[:14]
            self.total_expression = ""
        except OverflowError as e:
            self.current_expression = "Overflow Error!"
            self.total_expression = "Overflow Error"
            self.update_total_label()
        except Exception as e:
            self.current_expression = "Error!"
            self.total_expression = "Error"
            self.update_total_label()
        finally:
            self.update_current_label()

    def square(self):
        self.total_expression = self.current_expression
        self.update_total_label()
        try:
            x = eval(f'{self.current_expression}**2')
            if x > 99999999999999:
                raise OverflowError
            self.current_expression = str(x)
            self.total_expression = ""
        except OverflowError as e:
            self.current_expression = "Overflow Error!"
            self.total_expression = "Overflow Error"
            self.update_total_label()
        except Exception as e:
            self.current_expression = "Error!"
            self.total_expression = "Error"
            self.update_total_label()
        finally:
            self.update_current_label()
    
    def sqrt(self):
        self.total_expression = self.current_expression
        self.update_total_label()

        try:
            x = eval(f'{self.current_expression}**0.5')
            if x < 0.000000000000001:
                raise OverflowError
            self.current_expression = str(x)
            self.total_expression = ""
        except OverflowError as e:
            self.current_expression = "Overflow Error!"
            self.total_expression = "Overflow Error"
            self.update_total_label()
        except Exception as e:
            self.current_expression = "Error!"
            self.total_expression = "Error"
            self.update_total_label()
        finally:
            self.update_current_label()

    def bind_keys(self):
        self.window.bind("<Return>", lambda event: self.evaluate())
        self.window.bind("<BackSpace>", lambda event: self.clear_expression())
        self.window.bind("<Delete>", lambda event: self.clear_digit())
        for key in self.digits:
            self.window.bind(str(key), lambda event, digit = key: self.add_to_expression(digit))
        for key in self.operations:
            self.window.bind(key, lambda event, operator= key: self.add_to_expression(operator) )

    def run(self):
        self.window.mainloop()

if __name__ == "__main__":
    calculator_app= Calculator()
    calculator_app.run()