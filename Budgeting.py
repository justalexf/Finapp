import customtkinter as ctk

def create_budget_button(App, window_width):
    def open_budget_window():
        create_budget_settings_window(App)

    create_budget_button = ctk.CTkButton(App,
            text="Budgeting", 
            command=open_budget_window, # command = expects the function reference not the result of a function call 
            width = (window_width - 40),
            height = 70,
            text_color="white",
            font=("Bold",20)
            )
    create_budget_button.grid(row=0, column=0, padx=20, pady=20, sticky="nsew", columnspan=2)

    return create_budget_button

def create_budget_settings_window(parent): # function determines what the command parameter does when a button is pressed 
    #Attributes
    budget_window = ctk.CTkToplevel(parent)
    budget_window.title("Budgeting")
    budget_window.geometry("400x450")
    # Allow column 0 to stretch 
    budget_window.grid_columnconfigure(0, weight=1)
    # Row 0: Settings Label
    title_label = ctk.CTkLabel(
        budget_window,
        text="Settings",
        text_color="white",
        font=("Bold", 30),
        anchor="center"
    )
    title_label.grid(row=0, column=0, padx=20, pady=(20, 10), sticky="n")

    # Row 1: Initial account balance heading
    initial_account_balance = ctk.CTkLabel(
        budget_window,
        text="Initial Account Balance",
        text_color="white",
        font=("Bold", 16),
        anchor="w"
    )
    initial_account_balance.grid(row=1, column=0, padx=20, pady=(10, 5), sticky="w")

    # Row 2: Initial account balance entry 
    initial_account_balance_entry = ctk.CTkEntry(budget_window, placeholder_text="Enter your initial account balance")
    initial_account_balance_entry.grid(row=2, column=0, padx=20, pady=(0, 15), sticky="ew")

    # Row 3: Choose budgeting rule
    amount_label = ctk.CTkLabel(
        budget_window,
        text="Budgeting rule ( Needs / Wants / Investing )",
        text_color="white",
        font=("Bold", 16),
        anchor="w"
    )
    amount_label.grid(row=3, column=0, padx=20, pady=(5, 10), sticky="w")

    #Row 4: Budgeting rule frame with checkbox
    budgeting_frame = ctk.CTkFrame(budget_window)
    budgeting_frame.grid(row=4, column=0, padx=(20, 20), pady=(20, 30), sticky="nsew")
    checkbox_1 = ctk.CTkCheckBox(budgeting_frame,
                                 text = "70/10/20")
    checkbox_1.grid(row=0, column=0, pady=(20, 0), padx=20, sticky="n")
    checkbox_2 = ctk.CTkCheckBox(budgeting_frame,
                                 text = "40/20/40")
    checkbox_2.grid(row=1, column=0, pady=(20, 0), padx=20, sticky="n")
    checkbox_3 = ctk.CTkCheckBox(budgeting_frame,
                                 text = "50/20/30")
    checkbox_3.grid(row=2, column=0, pady=20, padx=20, sticky="n")

