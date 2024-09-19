import customtkinter as ctk
import os
from PIL import Image
from typing import Tuple
import tkinter as tk

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

        content_frame = ctk.CTkFrame(master=self.frame, corner_radius=8)
        content_frame.pack()

        if self.login_logo:
            ctk.CTkLabel(master=content_frame, text="", image=self.login_logo).pack(anchor="nw", padx=(24, 0), pady=(24, 0))

        # Header
        ctk.CTkLabel(master=content_frame, text="Create a new account", anchor="w",
                     justify="left", font=("Inter", 24)).pack(anchor="w", pady=(8, 0), padx=(24, 24))

        # Full name entry
        if self.email_icon:
            ctk.CTkLabel(master=content_frame, text="  Full name*", anchor="w", justify="left",
                         image=self.name_icon, compound="left").pack(anchor="w", pady=(8, 0), padx=(24, 24))
        self.email_entry = ctk.CTkEntry(master=content_frame, border_width=2, placeholder_text="Enter your full name")
        self.email_entry.pack(anchor="w", padx=(24, 24), fill="x")

        # Email entry
        if self.email_icon:
            ctk.CTkLabel(master=content_frame, text="  Email*", anchor="w", justify="left",
                         image=self.email_icon, compound="left").pack(anchor="w", pady=(8, 0), padx=(24, 24))
        self.email_entry = ctk.CTkEntry(master=content_frame, border_width=2, placeholder_text="Ex: playnexus@youremail.com")
        self.email_entry.pack(anchor="w", padx=(24, 24), fill="x")

        # Password entry
        if self.password_icon:
            ctk.CTkLabel(master=content_frame, text="  Password*", anchor="w", justify="left",
                         image=self.password_icon, compound="left").pack(anchor="w", pady=(8, 0), padx=(24, 0))
        self.passw_entry = ctk.CTkEntry(master=content_frame, border_width=2, show="*", placeholder_text="Enter your password")
        self.passw_entry.pack(anchor="w", padx=(24, 24), fill="x")

        # Confirm password entry
        if self.password_icon:
            ctk.CTkLabel(master=content_frame, text="Confirm Password*", anchor="w", justify="left",
                         image=None, compound="left").pack(anchor="w", pady=(8, 0), padx=(24, 0))
        self.passw_entry = ctk.CTkEntry(master=content_frame, border_width=2, show="*", placeholder_text="Please, confirm your password")
        self.passw_entry.pack(anchor="w", padx=(24, 24), fill="x")

        # Birthdate entry
        if self.birth_icon:
            ctk.CTkLabel(master=content_frame, text="  Enter your birth date*", anchor="w", justify="left",
                         image=self.birth_icon, compound="left").pack(anchor="w", pady=(8, 0), padx=(24, 0))
        self.birth_entry = ctk.CTkEntry(master=content_frame, border_width=2, placeholder_text="DD/MM/YY")
        self.birth_entry.pack(anchor="w", padx=(24, 24), fill="x")

        # Error message label
        self.error_label = ctk.CTkLabel(master=content_frame, text="Wrong email or password", text_color="#FF0000",
                                        anchor="w", justify="left")
        self.error_label.pack(anchor="w", padx=(25, 0))
        self.error_label.pack_forget()  # Hide initially

        # Login button
        cancel_button = ctk.CTkButton(master=content_frame, text="Cancel", fg_color="transparent", hover_color="#4d4d4d",
                                      border_width=2, border_color="#b3b3b3", width=132, command=self.return_to_previous_page)
        cancel_button.pack(anchor="w", side="left", padx=(24, 0), pady=(8, 0))
        login_button = ctk.CTkButton(master=content_frame, text="Create account", width=132)
        login_button.pack(anchor="w", side="right", padx=(8, 24), pady=(8, 0))

        agreements_frame = ctk.CTkFrame(master=content_frame, fg_color="transparent")
        agreements_frame.pack(anchor="w", fill="x", padx=(24, 24))

        self.create_agreement_label(agreements_frame)

        # self.app.bind("<Return>")

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

if __name__ == "__main__":
    signup_app = Signup()
    signup_app.app.mainloop()
