import customtkinter as ctk
import os
from PIL import Image
from typing import Tuple

ctk.set_default_color_theme("res/themes/purple.json")

class Login:
    def __init__(self, previous_frame: ctk.CTkFrame = None, previous_app: ctk.CTk = None) -> None:
        """Initialize the login window and load necessary resources."""
        self.res_path = 'res/'

        if previous_app == None:
            self.app = ctk.CTk()
            self.app.resizable(False, True)
            self.app.title("PlayNexus | Login")
        
        else:
            self.app = previous_app

        self.app.geometry("322x480")
        self.frame = previous_frame


        if os.name == "nt":
            icon_path = os.path.join(self.res_path, 'secondary-logo-colored.ico')
            if os.path.exists(icon_path):
                self.app.iconbitmap(icon_path)
            else:
                print(f"Icon file not found at {icon_path}")

        # Load images
        self.login_logo = self.load_image("secondary-logo-white.png", (42, 38))
        self.email_icon = self.load_image("email-icon.png", (16, 16))
        self.password_icon = self.load_image("password-icon.png", (16, 16))
        self.google_icon = self.load_image("google-icon.png", (16, 16))
        self.login_icon = self.load_image("login.png", (16, 16))


        # Initialize variables
        self.missed_attempts = 0
        self.is_logged_in = False

        # Create widgets
        self.create_widgets()

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
        if self.frame == None:
            self.frame = ctk.CTkFrame(master=self.app, width=300, height=480)
            self.frame.pack_propagate(False)
            self.frame.pack(expand=True, fill="both")

        if self.login_logo:
            ctk.CTkLabel(master=self.frame, text="", image=self.login_logo).pack(anchor="nw", padx=(24, 0), pady=(24, 0))

        # Welcome and instructions
        ctk.CTkLabel(master=self.frame, text="Welcome back!", anchor="w",
                     justify="left", font=("Inter", 24)).pack(anchor="w", pady=(8, 0), padx=(24, 24))
        ctk.CTkLabel(master=self.frame, text="Sign in to your account", anchor="w",
                     justify="left").pack(anchor="w", pady=(0, 0), padx=(24, 24))

        # Email entry
        if self.email_icon:
            ctk.CTkLabel(master=self.frame, text="  Email", anchor="w", justify="left",
                         image=self.email_icon, compound="left").pack(anchor="w", pady=(16, 0), padx=(24, 24))
        self.email_entry = ctk.CTkEntry(master=self.frame, border_width=2, placeholder_text="Enter your email")
        self.email_entry.pack(anchor="w", padx=(24, 24), fill="x")

        # Password entry
        headline_frame = ctk.CTkFrame(master=self.frame, fg_color="transparent")
        headline_frame.pack(anchor="w", padx=(24, 24),pady=(16,0), fill="x")

        if self.password_icon:
            ctk.CTkLabel(master=headline_frame, text="  Password", anchor="w", justify="left",
                         font=("Roboto", 12), image=self.password_icon, compound="left").pack(anchor="w", side="left")
        f_psswrd =ctk.CTkLabel(master=headline_frame, text="Forgot password?", anchor="w", justify="left", text_color="#7C439E",
                     font=("Roboto", 12, "underline"))
        f_psswrd.pack(anchor="w", side="right")
        f_psswrd.bind("<Button-1>", lambda e: print("Forgot password?"))
        f_psswrd.bind("<Enter>", lambda event: event.widget.config(cursor="hand2"))
        f_psswrd.bind("<Leave>", lambda event: event.widget.config(cursor=""))
        
        self.passw_entry = ctk.CTkEntry(master=self.frame, border_width=2, show="*", placeholder_text="Enter your password")
        self.passw_entry.pack(anchor="w", fill="x", padx=(24, 24))

        # Error message label
        self.error_label = ctk.CTkLabel(master=self.frame, text="Wrong email or password", text_color="#FF0000",
                                        anchor="w", justify="left")
        self.error_label.pack(anchor="w", padx=(25, 0))
        self.error_label.pack_forget()  # Hide initially

        # Login button
        login_button = ctk.CTkButton(master=self.frame, text="Login", command=self.check_credentials, image=self.login_icon)
        login_button.pack(anchor="w", pady=(16, 8), padx=(24, 24), fill="x")

        # Signup and Google buttons
        ctk.CTkLabel(master=self.frame, text_color="#2a2a2a",
                     text="_______________________________________________________",
                     fg_color="transparent").pack(fill="x", pady=(0, 0))
        
        ctk.CTkButton(master=self.frame, text="Continue With Google", fg_color="#fff", hover_color="#b3b3b3",
                      font=("Roboto Medium", 12), text_color="#000", image=self.google_icon).pack(anchor="w", pady=(20, 0), padx=(24, 24), fill="x")
        
        # Signup label
        signup_label = ctk.CTkFrame(master=self.frame, fg_color="transparent")
        signup_label.pack(pady=10)

        label1 = ctk.CTkLabel(master=signup_label, text="Don't have an account? ", text_color="#b3b3b3", font=("Roboto", 12))
        label1.pack(side="left")

        label2 = ctk.CTkLabel(master=signup_label, text="Sign up", text_color="#7C439E", font=("Roboto", 12, "underline"))
        label2.pack(side="left")
        label2.bind("<Button-1>", lambda e: self.go_to_signup())
        label2.bind("<Enter>", lambda event: event.widget.config(cursor="hand2"))
        label2.bind("<Leave>", lambda event: event.widget.config(cursor=""))

        self.app.bind("<Return>", self.handle_enter)

    def handle_enter(self, event: str) -> None:
        """Handle the Enter key press event."""
        print(f"{event} pressed")
        self.check_credentials()

    def check_credentials(self) -> None:
        """Check the credentials and display an error if necessary."""
        email = self.email_entry.get()
        password = self.passw_entry.get()

        wrong_credentials = not self.authenticate_user(email, password)

        if wrong_credentials and self.missed_attempts == 0:
            self.missed_attempts += 1
            return

        if wrong_credentials:
            self.error_label.pack()
        else:
            self.error_label.pack_forget()
            self.break_loop()

    def authenticate_user(self, email: str, password: str) -> bool:
        """Return true if credentials are valid, false otherwise."""
        print(f"Email: {email}, Password: {password}")
        self.is_logged_in = True

        return email == "admin" and password == "admin"

    def break_loop(self) -> None:
        """Close the application if login is successful."""
        self.app.destroy()

    def go_to_signup(self):
        # vc vai ter que dar um jeito nessa função, pq ela é a causadora do import circular  
        from .signup import Signup 
        # self.app.destroy()
        signup = Signup(self.frame, self.app)

if __name__ == "__main__":
    login_app = Login()
    login_app.app.mainloop()