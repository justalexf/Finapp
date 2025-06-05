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
    budget_window.geometry("450X500")
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
        font=("Bold", 20),
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
        font=("Bold", 20),
        anchor="w"
    )
    amount_label.grid(row=3, column=0, padx=20, pady=(5, 10), sticky="w")

    #Row 4: Budgeting rule frame with radio button
    budgeting_frame = ctk.CTkFrame(budget_window)
    budgeting_frame.grid(row=4, column=0, padx=(20, 20), pady=(20, 30), sticky="nsew")
    budget_var = ctk.StringVar(value="other")
    option_1 = ctk.CTkRadioButton(budgeting_frame,
                                 text = "70/10/20",
                                 value="70/10/20",
                                 variable=budget_var)
    option_1.grid(row=0, column=0, pady=(20, 0), padx=20, sticky="n")
    option_2 = ctk.CTkRadioButton(budgeting_frame,
                                 text = "40/20/40",
                                 value= "40/20/40",
                                 variable=budget_var)
    option_2.grid(row=1, column=0, pady=(20, 0), padx=20, sticky="n")
    option_3 = ctk.CTkRadioButton(budgeting_frame,
                                 text = "50/20/30",
                                 value= "50/20/30",
                                 variable=budget_var)
    option_3.grid(row=2, column=0, pady=20, padx=20, sticky="n")

    # Row 5: Apply button

    apply_button = ctk.CTkButton(budget_window,
            text="Apply", 
            # command = expects the function reference not the result of a function call 
            width = (75),
            height = 20,
            text_color="white",
            font=("Bold",20),
            anchor="center"
            )
    apply_button.grid(row=5, column=0, padx=20, pady=(0,20), columnspan=2)

