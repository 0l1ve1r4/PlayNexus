import customtkinter as ctk
from PIL import Image

ctk.set_default_color_theme("res/themes/purple.json")

class Launcher:
    def __init__(self) -> None:
        """Main class for the launcher application"""
        self.app = ctk.CTk()
        self.frames = {}
        self.app.title("PlayNexus | Launcher")
        self.configure_app()
        self.create_sidebar()
        self.create_main_view()
        self.current_frame = None
        self.app.mainloop()


    def configure_app(self) -> None:
        """Configure the main application window"""
        self.app.geometry("856x645")
        self.app.resizable(0, 0)
        ctk.set_appearance_mode("dark")
        self.res_path = "res/"
        self.app.iconbitmap(self.res_path + 'secondary-logo-colored.ico')


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
            ("home-smile.png", "Store", self.home_page, "transparent", "#4d4d4d", 60),
            ("backpack.png", "Library", self.library_page, "transparent", "#4d4d4d", 16),
            ("download.png", "Downloads", self.home_page, "transparent", "#4d4d4d", 16),
            ("settings_icon.png", "Settings", self.home_page, "transparent", "#4d4d4d", 16),
            ("person_icon.png", "Account", self.home_page, "transparent", "#4d4d4d", 160)
        ]

        for img_file, text, command, fg_color, hover_color, pady in button_data:
                img_data = Image.open(self.res_path + img_file)
                img = ctk.CTkImage(dark_image=img_data, light_image=img_data)
                ctk.CTkButton(master=self.sidebar_frame, image=img, text=text, command=lambda cmd=command: self.show_frame(cmd), fg_color=fg_color,
                            font=("Roboto Medium", 14), hover_color=hover_color, anchor="w").pack(anchor="center",fill="x", ipady=10, pady=(pady, 0), padx=10)
                
    def show_frame(self, frame_method) -> None:
        if self.current_frame:
            self.current_frame.pack_forget()
        frame_method()
        self.current_frame = self.frames[frame_method.__name__]


        ctk.CTkLabel(master=self.sidebar_frame, text="", fg_color="#302c2c").pack(expand=True)

<<<<<<< Updated upstream
=======
    def create_search_bar(self, master: ctk.CTkFrame) -> None:
        """Create the first line of the main view with a search bar and a button."""
        self.first_line = ctk.CTkFrame(master=master, fg_color="transparent")
        self.first_line.pack(anchor="n", fill="x", pady=(0, 0))

        self.search_entry = ctk.CTkEntry(master=self.first_line, width=400, height=30, fg_color="#3c3c3c", bg_color=SIDE_BAR_COLOR,
                                        font=("Roboto", 12), placeholder_text="Search in store")
        self.search_entry.pack(side="left")

        search_button = ctk.CTkButton(master=self.first_line, height=30, text="Search",
                                    font=("Roboto Medium", 12), text_color="#ffffff", width=225, command=self.search_in_store)
        search_button.pack(anchor="w", padx=(10, 0))

    def create_labels_and_content(self, master):
        """Creates labels and content sections."""

        ctk.CTkLabel(master=master, text="Recently added", text_color="#ffffff", anchor="w",
                    justify="left", font=("Roboto Medium", 24)).pack(anchor="w", pady=(30, 10), padx=(0, 0))
        
        # Container frame for recently added games
        recently_added_frame = ctk.CTkFrame(master, fg_color="transparent")
        recently_added_frame.pack(fill="x", pady=(10, 0))
        self.show_games(recently_added_frame)

        # Adding a spacer label (transparent) to create space between sections
        ctk.CTkLabel(master=master, text_color=SIDE_BAR_COLOR,
                     text="__________________________________________________________________________________________", 
                     fg_color="transparent").pack(fill="x", pady=(20, 0))

        # Tabs:
        tabs =  ["Popular", "New", "Upcoming", "All"]

        tabs_frame = ctk.CTkFrame(master, fg_color="transparent")
        tabs_frame.pack(fill="x", pady=(10, 0))

        for _ in tabs:
            ctk.CTkButton(master=tabs_frame, text=_, fg_color="transparent", text_color="#ffffff", 
                          font=("Roboto", 24), hover_color=SIDE_BAR_COLOR).pack(side="left", padx=10, pady=(0, 0))
        

        self.show_games(tabs_frame)

    def show_games(self, master: ctk.CTkFrame) -> None:
        for _ in range(5):
            # Create a frame to hold each game's details side by side
            game_frame = ctk.CTkFrame(master, corner_radius=10, fg_color="#1a1a1a", width=150, height=200)
            game_frame.pack(side="left", padx=10, pady=10)

            game_img_data = Image.open(self.res_path + f"secondary-logo-colored.png")
            game_img = ctk.CTkImage(dark_image=game_img_data, light_image=game_img_data, size=(150, 150))
            ctk.CTkLabel(master=game_frame, image=game_img, text="").pack()

            ctk.CTkLabel(master=game_frame, text="Game Title", text_color="#ffffff", anchor="w",
                        justify="left", font=("Roboto Medium", 12)).pack(anchor="w", pady=(8, 0))

            ctk.CTkLabel(master=game_frame, text="Publisher Name", text_color="#b3b3b3", anchor="w",
                        justify="left", font=("Roboto Medium", 12)).pack(anchor="w", pady=(0, 0))

            ctk.CTkLabel(master=game_frame, text="Price", text_color="#ffffff", anchor="w",
                        justify="left", font=("Roboto Medium", 12)).pack(anchor="w", pady=(0, 0))

>>>>>>> Stashed changes
    def create_main_view(self) -> None:
        """Create the main view frame with the title and content"""
        self.main_view = ctk.CTkFrame(master=self.app, fg_color="#201c1c", width=680, height=650, corner_radius=0)
        self.main_view.pack_propagate(0)
        self.main_view.pack(side="left")

<<<<<<< Updated upstream
        self.title_frame = ctk.CTkFrame(master=self.main_view, fg_color="transparent")
        self.title_frame.pack(anchor="n", fill="x", padx=27, pady=(29, 0))

        ctk.CTkLabel(master=self.title_frame, text="there should be something here", font=("Arial Black", 25), text_color="#302c2c").pack(anchor="nw", side="left")
=======
        self.home_page()

    def search_in_store(self) -> None:
        """Search for a game in the store."""
        pass

    def home_page(self) -> None:
        """Return to the home page."""
        if "home_page" not in self.frames:
            self.home_frame = ctk.CTkFrame(master=self.main_view, fg_color="#1a1a1a")
            self.home_frame.pack(fill="both", expand=True)
            self.frames["home_page"] = self.home_frame

            self.title_frame = ctk.CTkFrame(master=self.home_frame, fg_color="transparent")
            self.title_frame.pack(anchor="n", fill="x", padx=27, pady=(29, 0))

            self.create_search_bar(self.title_frame)
            self.create_labels_and_content(self.title_frame)
        else:
            self.frames["home_page"].pack(fill="both", expand=True)

    def library_page(self) -> None:
        """Show the user's library."""
        if "library_page" not in self.frames:
            self.library_frame = ctk.CTkFrame(master=self.main_view, fg_color="transparent")
            self.library_frame.pack(fill="both", expand=True)
            self.frames["library_page"] = self.library_frame
        else:
            self.frames["library_page"].pack(fill="both", expand=True)
>>>>>>> Stashed changes
