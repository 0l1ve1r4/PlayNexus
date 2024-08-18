from .sideBar import SideBar

import customtkinter as ctk
import os as os

class Launcher:
    def __init__(self) -> None:
        """Main class for the launcher application"""
        ctk.set_default_color_theme("res/themes/purple.json")
        self.app = ctk.CTk()
        self.side_bar =  SideBar(self.app)
        self.res_path = "res/"          
        self.configure_app()
        self.side_bar.create_sidebar()
        self.side_bar.create_main_view()
        self.app.mainloop()

    def configure_app(self) -> None:
        """Configure the main application window"""
        self.app.title("PlayNexus | Launcher")
        self.app.geometry("856x645")
        self.app.resizable(0, 0)
        ctk.set_appearance_mode("dark")

        if (os.name == "nt"):
            self.app.iconbitmap(self.res_path + 'secondary-logo-colored.ico')