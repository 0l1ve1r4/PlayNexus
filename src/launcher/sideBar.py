import customtkinter as ctk

from PIL import Image
from .pages import Pages
from functools import partial

class SideBar(Pages):
    def __init__(self, app) -> None:
        """Create the sidebar for the launcher application."""
        super().__init__(app)
        self.app = app
        self.current_frame = None        
        self.res_path = "res/"
        self.pages = Pages(self.app)
        self.frames = {}  

    def show_frame(self, frame_method: callable) -> None:
        """Show the selected frame and hide the current one."""
        if self.current_frame:
            self.current_frame.pack_forget()
        frame_method()  # This should show the frame and pack it
        self.current_frame = self.frames.get(frame_method.__name__)
        ctk.CTkLabel(master=self.sidebar_frame, text="", fg_color="#302c2c").pack(expand=True)

    def create_sidebar(self) -> None:
        """Create the sidebar frame with the logo and buttons."""
        self.sidebar_frame = ctk.CTkFrame(
            master=self.app, fg_color="#2a2a2a", width=240, height=650, corner_radius=0
        )
        self.sidebar_frame.pack_propagate(0)
        self.sidebar_frame.pack(fill="y", anchor="w", side="left")

        self.add_logo()
        self.add_buttons()

    def add_logo(self) -> None:
        """Add the logo image to the sidebar."""
        logo_img_data = Image.open(self.res_path + "primary-logo-white.png")
        logo_img = ctk.CTkImage(dark_image=logo_img_data, light_image=logo_img_data, size=(182, 34))
        ctk.CTkLabel(master=self.sidebar_frame, text="", image=logo_img).pack(
            fill="x", pady=(24, 0), anchor="center"
        )

    def add_buttons(self) -> None:
        """Add the buttons to the sidebar."""
        top_buttons_frame = ctk.CTkFrame(master=self.sidebar_frame, fg_color="transparent")
        bottom_buttons_frame = ctk.CTkFrame(master=self.sidebar_frame, fg_color="transparent")
        top_buttons_frame.pack(fill="x", pady=(24, 0), anchor="n", side="top")
        bottom_buttons_frame.pack(fill="x", pady=(0, 16), anchor="s", side="bottom")

        top_buttons_data = [
            ("home-smile.png", "Store", self.home_page, "transparent", "#4d4d4d", 0),
            ("backpack.png", "Library", self.library_page, "transparent", "#4d4d4d", 8),
        ]

        for img_file, text, command, fg_color, hover_color, pady in top_buttons_data:
            img_data = Image.open(self.res_path + img_file)
            img = ctk.CTkImage(dark_image=img_data, light_image=img_data)
            ctk.CTkButton(
                master=top_buttons_frame,
                image=img,
                text=text,
                command=partial(self.show_frame, command),
                fg_color=fg_color,
                font=("Roboto Bold", 16),
                hover_color=hover_color,
                anchor="w"
            ).pack(anchor="center", fill="x", ipady=16, pady=(pady, 0), padx=16)

        bottom_buttons_data = [
            ("download.png", "Downloads", self.home_page, "transparent", "#4d4d4d", 0),
            ("settings_icon.png", "Settings", self.home_page, "transparent", "#4d4d4d", 8),
            ("person_icon.png", "Account", self.home_page, "transparent", "#4d4d4d", 8)
        ]

        for img_file, text, command, fg_color, hover_color, pady in bottom_buttons_data:
            img_data = Image.open(self.res_path + img_file)
            img = ctk.CTkImage(dark_image=img_data, light_image=img_data)
            ctk.CTkButton(
                master=bottom_buttons_frame,
                image=img,
                text=text,
                command=partial(self.show_frame, command),
                fg_color=fg_color,
                font=("Roboto Bold", 16),
                hover_color=hover_color,
                anchor="w"
            ).pack(anchor="center", fill="x", ipady=16, pady=(pady, 0), padx=16)
