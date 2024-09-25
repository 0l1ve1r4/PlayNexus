# src/launcher/launcher.py

import customtkinter as ctk
from .sideBar import SideBar
from .utils import THEMES_PATH
import os

class Launcher:
    def __init__(self, email: str = "") -> None:
        """Main class for the launcher application."""
        ctk.set_default_color_theme(os.path.join(THEMES_PATH, "purple.json"))
        self.app = ctk.CTk()
        self.Admin = False
        self.side_bar = SideBar(self.app, admin=self.Admin, email=email)
        self.res_path = "res/"
        
        self.configure_app()
        self.side_bar.create_sidebar()
        self.side_bar.create_main_view()
        self.app.mainloop()

    def configure_app(self) -> None:
        """Configure the main application window."""
        self.app.title("PlayNexus | Launcher")
        self.app.geometry("856x645")
        self.app.resizable(False, False)
        ctk.set_appearance_mode("dark")

        # Set the window icon if running on Windows
        if os.name == "nt":
            icon_path = os.path.join(self.res_path, 'secondary-logo-colored.ico')
            if os.path.exists(icon_path):
                self.app.iconbitmap(icon_path)
            else:
                print(f"Icon file not found at {icon_path}")
