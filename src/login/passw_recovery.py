import customtkinter as ctk
import os
from PIL import Image
from typing import Tuple
import tkinter as tk

ctk.set_default_color_theme("res/themes/purple.json") 

class PasswRecovery:
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

        content_frame = ctk.CTkFrame(master=self.frame, fg_color="transparent")
        content_frame.pack(anchor="w")

        if self.login_logo:
            ctk.CTkLabel(master=content_frame, text="", image=self.login_logo).pack(anchor="nw", padx=(24, 0), pady=(24, 0))

        # Header
        ctk.CTkLabel(master=content_frame, text="Account Recovery", anchor="w",
                     justify="left", font=("Inter", 24)).pack(anchor="w", pady=(8, 0), padx=(24, 24))

        # Email entry
        if self.email_icon:
            ctk.CTkLabel(master=content_frame, text="  Email*", anchor="w", justify="left",
                         image=self.email_icon, compound="left").pack(anchor="w", pady=(8, 0), padx=(24, 24))
        self.email_entry = ctk.CTkEntry(master=content_frame, border_width=2, placeholder_text="Ex: playnexus@youremail.com")
        self.email_entry.pack(anchor="w", padx=(24, 24), fill="x")

        # Birthdate entry
        if self.birth_icon:
            ctk.CTkLabel(master=content_frame, text="  Enter the account creating date*", anchor="w", justify="left",
                         image=self.birth_icon, compound="left").pack(anchor="w", pady=(8, 0), padx=(24, 0))
        self.birth_entry = ctk.CTkEntry(master=content_frame, border_width=2, show="*", placeholder_text="DD/MM/YY")
        self.birth_entry.pack(anchor="w", padx=(24, 24), fill="x")


        if self.name_icon:
            ctk.CTkLabel(master=content_frame, text="  More Information", anchor="w", justify="left",
                            image=self.name_icon, compound="left").pack(anchor="w", pady=(8, 0), padx=(24, 0))

            ctk.CTkTextbox(master=content_frame, border_width=2, height=100, width=300, 
                           bg_color="#1a1a1a").pack(anchor="w", padx=(24, 24), pady=(8, 0))

        # Login button


        # Login button
        login_button = ctk.CTkButton(master=content_frame, text="Send Recovery Request", width=230, command=self.send_recovery_request)
        login_button.pack(anchor="center", padx=(0, 0), pady=(16, 0))

        cancel_button = ctk.CTkButton(master=content_frame, text="Cancel", fg_color="transparent", hover_color="#4d4d4d",
                                    border_width=2, border_color="#b3b3b3", width=230, command=self.return_to_previous_page)
        cancel_button.pack(anchor="center", padx=(0, 0), pady=(16, 0))

    def send_recovery_request(self):
        self.destroy_previous_frame()

        content_frame = ctk.CTkFrame(master=self.frame, fg_color="transparent")
        content_frame.pack(anchor="center")

        if self.email_icon:
            ctk.CTkLabel(master=content_frame, text="  Recovery Request Sent!", anchor="w", justify="left", text_color="#E8F5E9",
                        image=self.email_icon, compound="left").pack(anchor="w", pady=(8, 0), padx=(24, 24))
        
        cancel_button = ctk.CTkButton(master=content_frame, text="Return", fg_color="transparent", hover_color="#4d4d4d",
                                    border_width=2, border_color="#b3b3b3", width=230, command=self.return_to_previous_page)
        cancel_button.pack(anchor="center", padx=(0, 0), pady=(16, 0))

        
    def return_to_previous_page(self):
        from .login import Login  
        
        self.destroy_previous_frame()
        login = Login(self.frame, self.app)
        login.app.mainloop()