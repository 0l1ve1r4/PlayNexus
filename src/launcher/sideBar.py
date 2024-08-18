import customtkinter as ctk

from PIL import Image
from .pages import Pages

class SideBar(Pages):
    def __init__(self, app) -> None:
        """Create the sidebar for the launcher application"""
        super().__init__(app)

        self.app = app
        self.current_frame = None        
        self.res_path = "res/"
        self.pages = Pages(self.app)

    def show_frame(self, frame_method) -> None:
        if self.current_frame:
            self.current_frame.pack_forget()
        frame_method()
        self.current_frame = self.frames[frame_method.__name__]
        ctk.CTkLabel(master=self.sidebar_frame, text="", fg_color="#302c2c").pack(expand=True)

    def create_sidebar(self) -> None:
        """Create the sidebar frame with the logo and buttons"""
        self.sidebar_frame = ctk.CTkFrame(master=self.app, fg_color="#2a2a2a", width=240, height=650, corner_radius=0)
        self.sidebar_frame.pack_propagate(0)
        self.sidebar_frame.pack(fill="y", anchor="w", side="left")

        self.add_logo()
        self.add_buttons()

    def add_logo(self) -> None:
        """Add the logo image to the sidebar"""
        logo_img_data = Image.open(self.res_path + "primary-logo-white.png")
        logo_img = ctk.CTkImage(dark_image=logo_img_data, light_image=logo_img_data, size=(182, 34))
        ctk.CTkLabel(master=self.sidebar_frame, text="", image=logo_img).pack(fill="x",pady=(24, 0), anchor="center")

    def add_buttons(self) -> None:
        """Add the buttons to the sidebar"""
        button_data = [
            ("home-smile.png", "Store", super().home_page(), "transparent", "#4d4d4d", 60),
            ("backpack.png", "Library", super().home_page(), "transparent", "#4d4d4d", 16),
            ("download.png", "Downloads", super().home_page(), "transparent", "#4d4d4d", 16),
            ("settings_icon.png", "Settings", super().home_page(), "transparent", "#4d4d4d", 16),
            ("person_icon.png", "Account", super().home_page(), "transparent", "#4d4d4d", 160)
        ]

        for img_file, text, command, fg_color, hover_color, pady in button_data:
                img_data = Image.open(self.res_path + img_file)
                img = ctk.CTkImage(dark_image=img_data, light_image=img_data)
                ctk.CTkButton(master=self.sidebar_frame, image=img, text=text, command=lambda cmd=command: self.show_frame(cmd), fg_color=fg_color,
                            font=("Roboto Medium", 14), hover_color=hover_color, anchor="w").pack(anchor="center",fill="x", ipady=10, pady=(pady, 0), padx=10)