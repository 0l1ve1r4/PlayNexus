import customtkinter as ctk

from PIL import Image
from typing import Tuple

class Login:
    def __init__(self) -> None:
        self.res_path = 'res/'
        self.app = ctk.CTk()
        self.app.geometry("300x480")
        self.app.resizable(False, False)
        self.app.title("PlayNexus | Login")
        self.app.iconbitmap(self.res_path + 'secondary-logo-colored.ico')

        #self.side_img = self.load_image("side-img.png", (300, 480))
        self.login_logo = self.load_image("secondary-logo-white.png", (42, 38))
        self.email_icon = self.load_image("email-icon.png", (20, 20))
        self.password_icon = self.load_image("password-icon.png", (17, 17))
        self.google_icon = self.load_image("google-icon.png", (17, 17))

        self.missed_attempts = 0
        self.is_logged_in = False
        self.name_str = "Example Name"
        self.email_str = ""
        self.passw_str = ""

        self.create_widgets()

    def load_image(self, filename: str, size: tuple) -> ctk.CTkImage:
        """Load and return a CTkImage object with the specified size."""
        image_data = Image.open(self.res_path + filename)
        return ctk.CTkImage(dark_image=image_data, light_image=image_data, size=size)

    def create_widgets(self) -> None:
        """Create and place all widgets in the window."""
        #ctk.CTkLabel(master=self.app, text="", image=self.side_img).pack(expand=True, side="left")

        frame = ctk.CTkFrame(master=self.app, width=300, height=480, fg_color="#1a1a1a")
        frame.pack_propagate(False)
        frame.pack(expand=True, fill="both")

        self.login_logo = self.load_image("secondary-logo-white.png", (42, 38))
        ctk.CTkLabel(master=frame, text="", image=self.login_logo).pack(anchor="nw", padx=(24,0), pady=(24, 0))

        # Welcome and instructions
        ctk.CTkLabel(master=frame, text="Welcome Back!", text_color="#ffffff", anchor="w",
                     justify="left", font=("Arial Bold", 24)).pack(anchor="w", pady=(8, 0), padx=(24, 0))
        ctk.CTkLabel(master=frame, text="Sign in to your account", text_color="#b3b3b3", anchor="w",
                     justify="left", font=("Arial Bold", 12)).pack(anchor="w", pady=(0,0), padx=(24, 0))

        # Email entry
        ctk.CTkLabel(master=frame, text="  Email", text_color="#ffffff", anchor="w", justify="left",
                     font=("Arial Bold", 12), image=self.email_icon, compound="left").pack(anchor="w", pady=(32, 0), padx=(24, 0))
        self.email_entry = ctk.CTkEntry(master=frame, width=225, fg_color="#EEEEEE", border_color="#601E88",
                                        border_width=1, text_color="#000000")
        self.email_entry.pack(anchor="w", padx=(24, 0))

        # Password entry
        ctk.CTkLabel(master=frame, text="  Password:", text_color="#ffffff", anchor="w", justify="left",
                     font=("Arial Bold", 12), image=self.password_icon, compound="left").pack(anchor="w", pady=(16, 0), padx=(24, 0))
        self.passw_entry = ctk.CTkEntry(master=frame, width=225, fg_color="#EEEEEE", border_color="#601E88",
                                        border_width=1, text_color="#000000", show="*")
        self.passw_entry.pack(anchor="w", padx=(24, 0))

        # Error message label
        self.error_label = ctk.CTkLabel(master=frame, text="Wrong email or password", text_color="#FF0000",
                                       anchor="w", justify="left", font=("Arial Bold", 12))
        self.error_label.pack(anchor="w", padx=(25, 0))
        self.error_label.pack_forget()  # Hide initially

        # Login button
        login_button = ctk.CTkButton(master=frame, text="Login", fg_color="#601E88", hover_color="#E44982",
                                     font=("Arial Bold", 12), text_color="#ffffff", width=225, command=self.check_credentials)
        login_button.pack(anchor="w", pady=(40, 0), padx=(25, 0))

        # Signup and Google buttons
        ctk.CTkButton(master=frame, text="Sign up", fg_color="#ffffff", hover_color="#E44982",
                      font=("Arial Bold", 12), text_color="#601E88", width=225).pack(anchor="w", pady=(20, 0), padx=(25, 0))
        ctk.CTkButton(master=frame, text="Continue With Google", fg_color="#EEEEEE", hover_color="#EEEEEE",
                      font=("Arial Bold", 9), text_color="#601E88", width=225, image=self.google_icon).pack(anchor="w", pady=(20, 0), padx=(25, 0))

    def check_credentials(self) -> None:
        """Check the credentials and display error if necessary."""
        self.email_str = self.email_entry.get()
        self.passw_str = self.passw_entry.get()

        # Replace the following line with actual authentication logic
        wrong_credentials = not self.authenticate_user(self.email_str, self.passw_str)

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
