import customtkinter as ctk
import os
from PIL import Image
from typing import Tuple
import tkinter as tk
import datetime

from launcher.backend.backend import create_user, create_gamer, create_publisher

ctk.set_default_color_theme("res/themes/purple.json") 

class Signup:
    def __init__(self, previous_frame : ctk.CTkFrame, previous_app: ctk.CTk) -> None:
        """Initialize the login window and load necessary resources."""
        self.res_path = 'res/'
        self.frame = previous_frame
        self.app = previous_app

        self.app.geometry("900x650")

        # Load images
        self.name_icon = self.load_image("type-square.png", (16, 16))
        self.login_logo = self.load_image("secondary-logo-white.png", (42, 38))
        self.email_icon = self.load_image("email-icon.png", (16, 16))
        self.password_icon = self.load_image("password-icon.png", (16, 16))
        self.birth_icon = self.load_image("calendar.png", (16, 16))
        self.google_icon = self.load_image("google-icon.png", (16, 16))

        # Initialize variables
        self.missed_attempts = 0
        self.is_logged_in = False

        self.destroy_previous_frame()

        # Create widgets
        self.create_widgets()

    def destroy_previous_frame(self) -> None:
        for child in self.frame.winfo_children():
            child.destroy()
        
    def load_image(self, filename: str, size: Tuple[int, int]) -> ctk.CTkImage:
        """Load and return a CTkImage object with the specified size."""
        image_path = os.path.join(self.res_path, filename)
        if not os.path.exists(image_path):
            print(f"Image file not found: {image_path}")
            return None

        image_data = Image.open(image_path)
        return ctk.CTkImage(dark_image=image_data, light_image=image_data, size=size)

    def create_widgets(self) -> None:
        """Create and place all widgets in the window."""

        # Usar CTkScrollableFrame sem largura fixa
        content_frame = ctk.CTkScrollableFrame(master=self.frame, corner_radius=8)
        content_frame.pack(padx=20, pady=20, fill="both", expand=True)

        if self.login_logo:
            ctk.CTkLabel(master=content_frame, text="", image=self.login_logo).pack(anchor="nw", padx=(24, 0), pady=(24, 0))

        # Header
        ctk.CTkLabel(
            master=content_frame,
            text="Create a new account",
            anchor="w",
            justify="left",
            font=("Inter", 24)
        ).pack(anchor="w", pady=(8, 0), padx=(24, 24))

        # Full name entry
        ctk.CTkLabel(
            master=content_frame,
            text="  Full name*",
            anchor="w",
            justify="left",
            image=self.name_icon,
            compound="left"
        ).pack(anchor="w", pady=(8, 0), padx=(24, 24))
        self.full_name_entry = ctk.CTkEntry(
            master=content_frame,
            border_width=2,
            placeholder_text="Enter your full name"
        )
        self.full_name_entry.pack(anchor="w", padx=(24, 24), fill="x", expand=True)

        # Email entry
        ctk.CTkLabel(master=content_frame, text="  Email*", anchor="w", justify="left",
                     image=self.email_icon, compound="left").pack(anchor="w", pady=(8, 0), padx=(24, 24))
        self.email_entry = ctk.CTkEntry(master=content_frame, border_width=2, placeholder_text="Ex: playnexus@youremail.com")
        self.email_entry.pack(anchor="w", padx=(24, 24), fill="x")

        # Password entry
        ctk.CTkLabel(master=content_frame, text="  Password*", anchor="w", justify="left",
                     image=self.password_icon, compound="left").pack(anchor="w", pady=(8, 0), padx=(24, 0))
        self.password_entry = ctk.CTkEntry(master=content_frame, border_width=2, show="*", placeholder_text="Enter your password")
        self.password_entry.pack(anchor="w", padx=(24, 24), fill="x")

        # Confirm password entry
        ctk.CTkLabel(master=content_frame, text="Confirm Password*", anchor="w", justify="left",
                     image=None, compound="left").pack(anchor="w", pady=(8, 0), padx=(24, 0))
        self.confirm_password_entry = ctk.CTkEntry(master=content_frame, border_width=2, show="*", placeholder_text="Please confirm your password")
        self.confirm_password_entry.pack(anchor="w", padx=(24, 24), fill="x")

        # Account Type Selection
        account_type_label = ctk.CTkLabel(master=content_frame, text="Select Account Type*", anchor="w")
        account_type_label.pack(anchor="w", pady=(8, 0), padx=(24, 24))

        self.account_type_var = tk.StringVar(value="Gamer")
        account_type_frame = ctk.CTkFrame(master=content_frame, fg_color="transparent")
        account_type_frame.pack(anchor="w", padx=(24, 24))

        gamer_radio = ctk.CTkRadioButton(master=account_type_frame, text="Gamer", variable=self.account_type_var, value="Gamer")
        gamer_radio.pack(side="left")

        publisher_radio = ctk.CTkRadioButton(master=account_type_frame, text="Publisher", variable=self.account_type_var, value="Publisher")
        publisher_radio.pack(side="left", padx=(10, 0))

        # Additional Fields
        self.additional_fields_frame = ctk.CTkFrame(master=content_frame, fg_color="transparent")
        self.additional_fields_frame.pack(anchor="w", fill="x", padx=(24, 24), pady=(8, 0))

        def update_additional_fields(*args):
            # Limpar campos existentes
            for widget in self.additional_fields_frame.winfo_children():
                widget.destroy()
            
            if self.account_type_var.get() == "Gamer":
                # Campos para Gamer
                ctk.CTkLabel(master=self.additional_fields_frame, text="Username*", anchor="w").pack(anchor="w")
                self.username_entry = ctk.CTkEntry(master=self.additional_fields_frame, placeholder_text="Enter your username")
                self.username_entry.pack(anchor="w", fill="x", pady=(0, 8))
                
                ctk.CTkLabel(master=self.additional_fields_frame, text="Country*", anchor="w").pack(anchor="w")
                self.country_entry = ctk.CTkEntry(master=self.additional_fields_frame, placeholder_text="Enter your country")
                self.country_entry.pack(anchor="w", fill="x", pady=(0, 8))
                
                ctk.CTkLabel(master=self.additional_fields_frame, text="Birth Date (YYYY-MM-DD)*", anchor="w").pack(anchor="w")
                self.birth_date_entry = ctk.CTkEntry(master=self.additional_fields_frame, placeholder_text="YYYY-MM-DD")
                self.birth_date_entry.pack(anchor="w", fill="x", pady=(0, 8))
            else:
                # Campos para Publisher
                ctk.CTkLabel(master=self.additional_fields_frame, text="Publisher Name*", anchor="w").pack(anchor="w")
                self.publisher_name_entry = ctk.CTkEntry(master=self.additional_fields_frame, placeholder_text="Enter publisher name")
                self.publisher_name_entry.pack(anchor="w", fill="x", pady=(0, 8))

        update_additional_fields()
        self.account_type_var.trace("w", update_additional_fields)

            # Label de erro
        self.error_label = ctk.CTkLabel(
            master=content_frame,
            text="",
            text_color="#FF0000",
            anchor="w",
            justify="left",
            wraplength=400  # Ajuste conforme necessário
        )


        # Frame para os botões
        buttons_frame = ctk.CTkFrame(master=content_frame, fg_color="transparent")
        buttons_frame.pack(fill="x", padx=(24, 24), pady=(8, 0), expand=True)

        # Configurar colunas
        buttons_frame.columnconfigure(0, weight=0)  # Botão Cancel
        buttons_frame.columnconfigure(1, weight=1)  # Botão Create Account

        # Botão Cancel
        cancel_button = ctk.CTkButton(
            master=buttons_frame,
            text="Cancel",
            fg_color="transparent",
            hover_color="#4d4d4d",
            border_width=2,
            border_color="#b3b3b3",
            command=self.return_to_previous_page,
            width=100  # Largura definida
        )
        cancel_button.grid(row=0, column=0, padx=(0, 8), pady=(8, 0), sticky="e")

        # Botão Create Account
        signup_button = ctk.CTkButton(
            master=buttons_frame,
            text="Create",
            command=self.process_signup
        )
        signup_button.grid(row=0, column=1, padx=(8, 0), pady=(8, 0), sticky="w")

        # Agreements
        agreements_frame = ctk.CTkFrame(master=content_frame, fg_color="transparent")
        agreements_frame.pack(anchor="w", fill="x", padx=(24, 24))

        self.create_agreement_label(agreements_frame)

    def create_agreement_label(self, master):
        text_widget = tk.Text(master, wrap="word", bg="#1a1a1a", fg="#b3b3b3", font=("Roboto", 12), borderwidth=0, highlightthickness=0)
        text_widget.pack(fill="x")

        text = "By creating a PlayNexus account you’re agreeing with our Privacy Policy and accept our Terms and Conditions."
        text_widget.insert("1.0", text)
        text_widget.config(state=tk.DISABLED)

        text_widget.tag_add("privacy_policy", "1.57", "1.71")
        text_widget.tag_add("terms_conditions", "1.87", "2.00")

        text_widget.tag_config("privacy_policy", foreground="#7C439E", font=("Roboto", 12, "underline"))
        text_widget.tag_config("terms_conditions", foreground="#7C439E", font=("Roboto", 12, "underline"))

        text_widget.tag_bind("privacy_policy", "<Button-1>", self.open_privacy_policy)
        text_widget.tag_bind("terms_conditions", "<Button-1>", self.open_terms_conditions)
        text_widget.tag_bind("privacy_policy", "<Enter>", lambda event: event.widget.config(cursor="hand2"))
        text_widget.tag_bind("privacy_policy", "<Leave>", lambda event: event.widget.config(cursor=""))
        text_widget.tag_bind("terms_conditions", "<Enter>", lambda event: event.widget.config(cursor="hand2"))
        text_widget.tag_bind("terms_conditions", "<Leave>", lambda event: event.widget.config(cursor=""))

    def open_privacy_policy(self, event):
        print("Privacy Policy clicked")

    def open_terms_conditions(self, event):
        print("Terms and Conditions clicked")

    def return_to_previous_page(self):
        from .login import Login 
        
        self.destroy_previous_frame()
        login = Login(self.frame, self.app)
        login.app.mainloop()
    
    def process_signup(self):
        # Collect common data
        email = self.email_entry.get()
        password = self.password_entry.get()
        confirm_password = self.confirm_password_entry.get()
        
        if password != confirm_password:
            self.error_label.configure(text="Passwords do not match")
            self.error_label.pack()
            return

        account_type = self.account_type_var.get()
        
        # Create account in the Account table
        if not create_user(email, password, account_type):
            self.error_label.configure(text="Error creating account. Email may already be in use.")
            self.error_label.pack()
            return
        else:
            print("Conta criada com sucesso no banco de dados.")

        # Create specific details
        if account_type == "Gamer":
            username = self.username_entry.get()
            country = self.country_entry.get()
            birth_date_input = self.birth_date_entry.get()
            
            # Parse and reformat the birth date
            try:
                birth_date_parsed = datetime.datetime.strptime(birth_date_input, '%d/%m/%Y')
                birth_date = birth_date_parsed.strftime('%Y-%m-%d')
            except ValueError:
                self.error_label.configure(text="Invalid birth date format. Please use DD/MM/YYYY.")
                self.error_label.pack()
                return
            
            if not create_gamer(email, username, birth_date, country):
                self.error_label.configure(text="Error creating gamer profile.")
                self.error_label.pack()
                return
        else:
            publisher_name = self.publisher_name_entry.get()
            if not create_publisher(email, publisher_name):
                self.error_label.configure(text="Error creating publisher profile.")
                self.error_label.pack()
                return

        # If everything succeeded, redirect to the login screen or launcher
        self.go_to_login()
    
    def go_to_login(self):
        """Navigate back to the login screen."""
        from .login import Login  # Import the Login class

        self.destroy_previous_frame()  # Destroy the current signup frame
        login = Login(self.frame, self.app)  # Initialize the Login screen
        # No need to call mainloop here

if __name__ == "__main__":
    signup_app = Signup()
    signup_app.app.mainloop()