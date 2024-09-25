import customtkinter as ctk
import os
from PIL import Image, ImageTk
from typing import Tuple
import launcher
from launcher.backend import backend

ctk.set_default_color_theme("res/themes/purple.json")

class Login:
    def __init__(self, previous_frame: ctk.CTkFrame = None, previous_app: ctk.CTk = None) -> None:
        """Initialize the login window and load necessary resources."""
        self.res_path = 'res/'

        if previous_app == None:
            self.app = ctk.CTk()
            self.app.resizable(False, True)
            self.app.title("Welcome to PlayNexus")     
        else:
            self.app = previous_app

        self.app.geometry("900x650")
        self.frame = previous_frame
        self.center_window(900, 650)

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

        self.set_background_image()
        # Create widgets
        self.create_widgets()

    def center_window(self, width: int, height: int):
        """Center the window on the screen."""
        screen_width = self.app.winfo_screenwidth()
        screen_height = self.app.winfo_screenheight()
        x = (screen_width // 2) - (width // 2)
        y = (screen_height // 2) - (height // 2)
        self.app.geometry(f'{width}x{height}+{x}+{y}')

    def set_background_image(self):
        bg_image_path = os.path.join(self.res_path, 'Prancheta 2.png')
        if os.path.exists(bg_image_path):
            bg_image = Image.open(bg_image_path)
            self.bg = ctk.CTkImage(dark_image=bg_image, light_image=bg_image, size=(900, 650))
            bg_label = ctk.CTkLabel(master=self.app, image=self.bg)
            bg_label.place(x=0, y=0, relwidth=1, relheight=1)
            bg_label.lower()  # Ensure the background label is at the bottom
        else:
            print(f"Background image file not found at {bg_image_path}")

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
            self.frame = ctk.CTkFrame(master=self.app, width=300, height=500, corner_radius=8)
            self.frame.pack_propagate(False)
            self.frame.pack(pady=(64, 0), anchor="center")

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
        f_psswrd.bind("<Button-1>", lambda e: self.goto_passw_recovery())

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

        authentication = backend.authenticate_user(email, password)
        wrong_credentials = not authentication['success']
        account = authentication['account']

        if wrong_credentials and self.missed_attempts == 0:
            self.missed_attempts += 1
            return

        if wrong_credentials:
            self.error_label.pack()
        else:
            self.error_label.pack_forget()
            self.break_loop()
            launcher.Launcher(email)


    def break_loop(self) -> None:
        """Close the application if login is successful."""
        self.app.destroy()

    def goto_passw_recovery(self):
        from .passw_recovery import PasswRecovery
        passw_recovery = PasswRecovery(self.frame, self.app)

    def go_to_signup(self):
        from .signup import Signup 
        # self.app.destroy()
        signup = Signup(self.frame, self.app)

if __name__ == "__main__":
    login_app = Login()
    login_app.app.mainloop()