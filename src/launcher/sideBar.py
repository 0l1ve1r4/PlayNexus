import customtkinter as ctk

from PIL import Image, ImageDraw
from .pages import Pages
from functools import partial
import tkinter as tk

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
            ("home-smile.png", "Home", self.home_page, "transparent", "#4d4d4d", 0),
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
                font=ctk.CTkFont(family='Helvetica', size=16, weight='bold'),
                hover_color=hover_color,
                anchor="w"
            ).pack(anchor="center", fill="x", ipady=16, pady=(pady, 0), padx=16)

        bottom_buttons_data = [
            ("download.png", "Downloads", self.home_page, "transparent", "#4d4d4d", 0),
            ("settings_icon.png", "Settings", self.settings_page, "transparent", "#4d4d4d", 0),
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
                font=ctk.CTkFont(family='Helvetica', size=16, weight='bold'),
                hover_color=hover_color,
                anchor="w"
            ).pack(anchor="center", fill="x", ipady=16, pady=(pady, 0), padx=16)
        
        # Add the profile button
        profile_img= ctk.CTkImage(Image.open(self.res_path + "secondary-logo-colored.png"), size=(48, 48))

        pbtn = ctk.CTkFrame(master=bottom_buttons_frame, fg_color="transparent", height=41,width=110)
        pbtn.pack(fill="x", expand=False, padx=16, pady=(16,0))

        name1 = "Admin"
        email1 = "admin@gmail.com"

        profile_btn = ctk.CTkButton(master=pbtn, text="", fg_color="transparent",image=profile_img,hover_color="#4d4d4d",
                                      border_width=2, border_color="#4d4d4d", anchor="w", command=partial(self.show_frame, self.profile_page))
        profile_btn.pack(fill="x", expand=True)
        email = ctk.CTkLabel(master=profile_btn, text="admin@gmail.com", text_color="#b3b3b3",
                             font=ctk.CTkFont(family='Helvetica', size=12), fg_color="transparent")
        email.place(x=117,y=40, anchor="center")
        name = ctk.CTkLabel(master=profile_btn, text="Admin", fg_color="transparent", 
                            font=ctk.CTkFont(family='Helvetica', size=16), justify="center")
        name.place(x=90,y=20, anchor="center")

        email.bind("<Enter>", lambda event: event.widget.config(cursor="hand2"))
        email.bind("<Leave>", lambda event: event.widget.config(cursor=""))
        email.bind("<Button-1>", lambda event: self.show_frame(self.profile_page))

        name.bind("<Enter>", lambda event: event.widget.config(cursor="hand2"))
        name.bind("<Leave>", lambda event: event.widget.config(cursor=""))
        name.bind("<Button-1>", lambda event: self.show_frame(self.profile_page))

        def on_enter(event):
            event.widget.config(cursor="hand2")
            email.configure(fg_color="#4d4d4d")
            name.configure(fg_color="#4d4d4d")

        def on_leave(event):
            event.widget.config(cursor="")
            email.configure(fg_color="transparent")
            name.configure(fg_color="transparent")
        
        profile_btn.bind("<Enter>", on_enter)
        profile_btn.bind("<Leave>", on_leave)


        


    def add_corners(self, im, rad):
        circle = Image.new('L', (rad * 2, rad * 2), 0)
        draw = ImageDraw.Draw(circle)
        draw.ellipse((0, 0, rad * 2 - 1, rad * 2 - 1), fill=255)
        alpha = Image.new('L', im.size, 255)
        w, h = im.size
        alpha.paste(circle.crop((0, 0, rad, rad)), (0, 0))
        alpha.paste(circle.crop((0, rad, rad, rad * 2)), (0, h - rad))
        alpha.paste(circle.crop((rad, 0, rad * 2, rad)), (w - rad, 0))
        alpha.paste(circle.crop((rad, rad, rad * 2, rad * 2)), (w - rad, h - rad))
        im.putalpha(alpha)
        return im