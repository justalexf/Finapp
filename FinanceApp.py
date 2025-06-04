import customtkinter as ctk
from Budgeting import budget_button
class App(ctk.CTk):
    def __init__(self, window_width, window_height): # This is the constructor method from other classes 
        super().__init__() # The super function calls all the same functions from the parent class customtkinter in this case 
        self.title("Finapp") # Sets object title 
        screen_width = self.winfo_screenwidth() # Determines the user window screen width
        screen_height = self.winfo_screenheight() # Determines the user window screen height
        x = (screen_width - window_width) // 2
        y = (screen_height - window_height) // 2
        self.geometry(f"{window_width}x{window_height}+{x}+{y}") # Centers the window 
        ctk.set_default_color_theme("green") 
        # self.grid_columnconfigure((0, 1), weight=1) #idk what this does 
        budget_buttonn = budget_button(self, window_width)
        portfolio_button = ctk.CTkButton(self, 
            text="Portfolio", 
            command=self.button_callback,
            width = (window_width - 40),
            height = 70
            )
        portfolio_button.grid(row=1, column=0, padx=20, pady=20, sticky="ew", columnspan=2)
        paycheck_button = ctk.CTkButton(self, 
            text="Paycheck tracker", 
            command=self.button_callback,
            width = (window_width - 40),
            height = 70
            )
        paycheck_button.grid(row=2, column=0, padx=20, pady=20, sticky="ew", columnspan=2)

    def button_callback(self): # function determines what the command parameter does when a button is pressed 
        print("button pressed")


app = App(480,520) # Default constructor   
app.mainloop()



# NON CLASS WAY OF DOING THINGS NEVER RECOMMENDED 
# # An app is a window with a number of widgets stacked onto each other 
# # The main window on which the text and different functionalities of the app are is called the 
# # root window // it can be named whatever you want 
# app = ctk.CTk()
#     # Titles the window of the app 
# app.title("Finapp")
#     # App size value 
# app_width = 1025
# app_height = 654
#     # Sets a default size for the app window when opened 
#     # Set the position to the middle of the screen when opened (MAKE THIS A FUNCTION LATER MAYBE??)
# screen_width = app.winfo_screenwidth()
# screen_height = app.winfo_screenheight()
# x = (screen_width - app_width) // 2
# y = (screen_height - app_height) // 2
# app.geometry(f"{app_width}x{app_height}+{x}+{y}")
#     # Sets the default color scheme
# ctk.set_default_color_theme("dark-blue")

#     # Functions 
# def button_callback():
#     print("button pressed")

#     # Makes two different frames with scrollable window within the main root window 
#     # Left sidebar 
# option_bar = ctk.CTkFrame(master = app, width = 150,fg_color="#2c2c2c")
#     # .pack displays the information on the main window
# option_bar.pack(side = "left", fill = "y") # fill = "y" fills the whole y axis no matter the size of the window 
#     # Display window
# display_window = ctk.CTkFrame(master = app, corner_radius = 0 )
# display_window.pack(side = "right", fill = "both", expand = True )
#     # Budgeting button
# budgeting = ctk.CTkButton(option_bar, text = "Budgeting",command=button_callback)
# budgeting.grid(row=0, column=0, padx=20, pady=20) 
# # mainloop function is what displays the app in an infinite loop 
# # this must be at the end of the program 
# app.mainloop()