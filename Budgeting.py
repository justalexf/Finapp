import customtkinter as ctk

def create_budget_button(App, window_width):
    create_budget_button = ctk.CTkButton(App,
            text="Budgeting", 
            command=create_budget_window,
            width = (window_width - 40),
            height = 70
            )
    create_budget_button.grid(row=0, column=0, padx=20, pady=20, sticky="ew", columnspan=2)

    return create_budget_button

def create_budget_window(): # function determines what the command parameter does when a button is pressed 
    budget_window = ctk.CTkToplevel()
    budget_window.title("Budgeting")
    budget_window.geometry("800x400") # temporary size must determine position and size of the screen 


