import customtkinter as ctk
from PIL import Image

class Launcher:
    def __init__(self) -> None:
        """Main class for the launcher application"""
        self.app = ctk.CTk()
        self.app.title("PlayNexus | Launcher")
        self.configure_app()
        self.create_sidebar()
        self.create_main_view()
        self.app.mainloop()

    def configure_app(self) -> None:
        """Configure the main application window"""
        self.app.geometry("856x645")
        self.app.resizable(0, 0)
        ctk.set_appearance_mode("light")
        self.res_path = "res/"

    def create_sidebar(self) -> None:
        """Create the sidebar frame with the logo and buttons"""
        self.sidebar_frame = ctk.CTkFrame(master=self.app, fg_color="#302c2c", width=240, height=650, corner_radius=0)
        self.sidebar_frame.pack_propagate(0)
        self.sidebar_frame.pack(fill="y", anchor="w", side="left")

        self.add_logo()
        self.add_buttons()

    def add_logo(self) -> None:
        """Add the logo image to the sidebar"""
        logo_img_data = Image.open(self.res_path + "primary-logo-white.png")
        logo_img = ctk.CTkImage(dark_image=logo_img_data, light_image=logo_img_data, size=(150, 50))
        ctk.CTkLabel(master=self.sidebar_frame, text="", image=logo_img).pack(fill="x",pady=(38, 0), anchor="center")

    def add_buttons(self) -> None:
        """Add the buttons to the sidebar"""
        button_data = [
            ("analytics_icon.png", "Store", "transparent", "#201c1c", 60),
            ("secondary-logo-colored.png", "Library", "transparent", "#201c1c", 16),
            ("list_icon.png", "Downloads", "transparent", "#201c1c", 16),
            ("settings_icon.png", "Settings", "transparent", "#201c1c", 16),
            ("person_icon.png", "Account", "transparent", "#201c1c", 160)
        ]

        for img_file, text, fg_color, hover_color, pady in button_data:
                img_data = Image.open(self.res_path + img_file)
                img = ctk.CTkImage(dark_image=img_data, light_image=img_data)
                ctk.CTkButton(master=self.sidebar_frame, image=img, text=text, fg_color=fg_color,
                            font=("Arial Bold", 14), hover_color=hover_color, anchor="w").pack(anchor="center",fill="x", ipady=10, pady=(pady, 0), padx=10)


        ctk.CTkLabel(master=self.sidebar_frame, text="", fg_color="#302c2c").pack(expand=True)

    def create_main_view(self) -> None:
        """Create the main view frame with the title and content"""
        self.main_view = ctk.CTkFrame(master=self.app, fg_color="#201c1c", width=680, height=650, corner_radius=0)
        self.main_view.pack_propagate(0)
        self.main_view.pack(side="left")

        self.title_frame = ctk.CTkFrame(master=self.main_view, fg_color="transparent")
        self.title_frame.pack(anchor="n", fill="x", padx=27, pady=(29, 0))

        ctk.CTkLabel(master=self.title_frame, text="there should be something here", font=("Arial Black", 25), text_color="#302c2c").pack(anchor="nw", side="left")