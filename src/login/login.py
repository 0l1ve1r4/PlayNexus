import customtkinter as ctk
import threading 
import os as os

from PIL import Image
from typing import Tuple

ctk.set_default_color_theme("res/themes/purple.json")
class Login:
    def __init__(self) -> None:
        self.res_path = 'res/'
        self.app = ctk.CTk()
        self.app.geometry("300x480")
        self.app.resizable(False, False)
        self.app.title("PlayNexus | Login")
        if (os.name == "nt"):
            self.app.iconbitmap(self.res_path + 'secondary-logo-colored.ico')

        #self.side_img = self.load_image("side-img.png", (300, 480))
        self.login_logo = self.load_image("secondary-logo-white.png", (42, 38))
        self.email_icon = self.load_image("email-icon.png", (16, 16))
        self.password_icon = self.load_image("password-icon.png", (16, 16))
        self.google_icon = self.load_image("google-icon.png", (16, 16))

        self.missed_attempts = 0
        self.is_logged_in = False
        self.name_str = "Example Name"
        self.email_str = ""
        self.passw_str = ""

        self.create_widgets()

    def handle_enter(self, event : str) -> None:
        """Handle the Enter key press event."""
        print(f"{event} pressed")
        self.check_credentials()


    def load_image(self, filename: str, size: tuple) -> ctk.CTkImage:
        """Load and return a CTkImage object with the specified size."""
        image_data = Image.open(self.res_path + filename)
        return ctk.CTkImage(dark_image=image_data, light_image=image_data, size=size)

    def create_widgets(self) -> None:
        """Create and place all widgets in the window."""
        #ctk.CTkLabel(master=self.app, text="", image=self.side_img).pack(expand=True, side="left")

        frame = ctk.CTkFrame(master=self.app, width=300, height=480)
        frame.pack_propagate(False)
        frame.pack(expand=True, fill="both")

        self.login_logo = self.load_image("secondary-logo-white.png", (42, 38))
        ctk.CTkLabel(master=frame, text="", image=self.login_logo).pack(anchor="nw", padx=(24,0), pady=(24, 0))

        # Welcome and instructions
        ctk.CTkLabel(master=frame, text="Welcome back!", anchor="w",
                     justify="left", font=("Inter", 24)).pack(anchor="w", pady=(8, 0), padx=(24, 24))
        ctk.CTkLabel(master=frame, text="Sign in to your account", anchor="w",
                     justify="left").pack(anchor="w", pady=(0,0), padx=(24, 24))

        # Email entry
        ctk.CTkLabel(master=frame, text="  Email", anchor="w", justify="left",
                     image=self.email_icon, compound="left").pack(anchor="w", pady=(16, 0), padx=(24, 24))
        self.email_entry = ctk.CTkEntry(master=frame, border_width=2, placeholder_text="Enter your email")
        self.email_entry.pack(anchor="w", padx=(24, 24), fill="x")

        # Password entry
        ctk.CTkLabel(master=frame, text="  Password:", anchor="w", justify="left",
                     font=("Arial Bold", 12), image=self.password_icon, compound="left").pack(anchor="w", pady=(16, 0), padx=(24, 0))
        self.passw_entry = ctk.CTkEntry(master=frame,
                                        border_width=2, show="*", placeholder_text="Enter your password")
        self.passw_entry.pack(anchor="w", padx=(24, 24), fill="x")

        # Error message label
        self.error_label = ctk.CTkLabel(master=frame, text="Wrong email or password", text_color="#FF0000",
                                       anchor="w", justify="left")
        self.error_label.pack(anchor="w", padx=(25, 0))
        self.error_label.pack_forget()  # Hide initially

        # Login button
        login_button = ctk.CTkButton(master=frame, text="Login", command=self.check_credentials)
        login_button.pack(anchor="w", pady=(32, 8), padx=(24, 24), fill="x")

        # Signup and Google buttons
        ctk.CTkButton(master=frame, text="Sign up", fg_color="#2a2a2a", hover_color="#4d4d4d",
                      font=("Arial Bold", 12), text_color="#fff", border_width=2, border_color="#b3b3b3").pack(anchor="w", pady=(0, 0), padx=(24, 24), fill="x")
        ctk.CTkButton(master=frame, text="Continue With Google", fg_color="#fff", hover_color="#fff",
                      font=("Arial Bold", 12), text_color="#000", image=self.google_icon).pack(anchor="w", pady=(20, 0), padx=(24, 24), fill="x")

        self.handle_enter("<Return>")
        self.app.bind("<Return>", self.handle_enter)
        

    def check_credentials(self) -> None:
        """Check the credentials and display error if necessary."""
        self.email_str = self.email_entry.get()
        self.passw_str = self.passw_entry.get()

        # Replace the following line with actual authentication logic
        wrong_credentials = not self.authenticate_user(self.email_str, self.passw_str)

        # If the user has missed the first attempt, allow one more without error message
        if (wrong_credentials and self.missed_attempts == 0):
            self.missed_attempts += 1
            return
        
        if wrong_credentials:
            self.error_label.pack()
        else:
            self.error_label.pack_forget()
            self.break_loop()

    def authenticate_user(self, email: str, password: str) -> bool:
        """Return true if founded in database, false otherwise."""
        print(f"Email: {email}, Password: {password}")    
        self.is_logged_in = True

        if email == "admin" and password == "admin":
            return True

        return False

    def break_loop(self) -> None:
        """Break and return with user credentials."""   
        self.app.destroy()  
