import customtkinter as ctk
from PIL import Image, ImageTk
from .utils import *
from .backend.backend import *
import tkinter as tk
from launcher import sideBar

from launcher.backend import backend

SIDE_BAR_COLOR = "#2a2a2a"

class Pages:
    def __init__(self, main_view: ctk.CTkFrame, email: str) -> None:
        """Initialize Pages with a main view and frame management."""
        self.main_view = main_view
        self.email = email  # Armazena o email do usuário
        self.name = self.getUsername(self.email) #gets the username from the database
        self.frames = {}
        self.Admin = self.getAdmin(self.email)
        
        

        #Fonts
        
        self.h1 = ctk.CTkFont(family="Roboto", size=24, weight="bold")
        self.body = ctk.CTkFont(family="Roboto", size=16)
        self.body_bold = ctk.CTkFont(family="Roboto", size=16, weight="bold")
        self.small = ctk.CTkFont(family="Roboto", size=12)

        self.game_in_library = False
        self.editing = False
        self.window_open = False
        self.count = False
    
        self.bio = "Welcome to your admin page! Here you can manage your games and account settings."
    
    def home_page(self) -> None:
        """Return to the home page."""
        
        if "home_page" not in self.frames:
            print("Home page not found")
            home_frame = ctk.CTkScrollableFrame(master=self.main_view)
            home_frame.pack(fill="both", expand=True)

            self.home_frame = home_frame
            self.frames["home_page"] = home_frame
            print(f"Admin status: {self.Admin}")

            if self.Admin:
                self.admin_page(home_frame)
            else:
                self.store_page(home_frame)
        else:
            self.count = not self.count
            try:
                # Destroy existing widgets and home frame
                
                for widget in self.main_view.winfo_children():
                    widget.destroy()
                
                # Remove the home page frame from frames dictionary
                frames_to_remove = list(self.frames.keys())
                for frame in frames_to_remove:
                    self.frames.pop(frame)
                home_frame = ctk.CTkScrollableFrame(master=self.main_view)
                home_frame.pack(fill="both", expand=True)
                self.home_frame = home_frame
                self.frames["home_page"] = home_frame
                self.store_page(home_frame, None)

            except Exception as e:
                print(f"Error while resetting home page: {e}")
                self.home_page()



    def store_page(self, master, games = None) -> None:
        print("Store page loaded")
        for widget in self.home_frame.winfo_children():
            widget.destroy()

        search_frame = ctk.CTkFrame(master=master)
        search_frame.pack(anchor="n", fill="both", padx=24, pady=24)

        self.create_search_bar(search_frame, " Search in store")

        if self.count:
            self.home_page()

        if games == None:
            self.create_labels_and_content(master,"Recently added", games)

        else:
            self.create_labels_and_content(master,"Search Result", games)


        

    def admin_page(self,master) -> None:
        print("Admin page loaded")
        content_frame = ctk.CTkFrame(master=master, fg_color="transparent")
        content_frame.pack(anchor="n", fill="both", padx=24, pady=24)

        ctk.CTkLabel(master=content_frame, text="Hi, " + self.name + "!", anchor="w", font=self.h1).pack(fill="x")
        ctk.CTkLabel(master=content_frame, text="What would you like to do today?", anchor="w", font=self.body).pack(fill="x")

        plus_icon= ctk.CTkImage(dark_image=load_image("plus.png"), light_image=load_image("plus.png"), size=(16, 16))
        list_icon = ctk.CTkImage(dark_image=load_image("list_icon.png"), light_image=load_image("list_icon.png"), size=(16, 16))

        buttons_frame = ctk.CTkFrame(master=content_frame, fg_color="transparent")
        buttons_frame.pack(fill="x", pady=(24, 0))

        add_button = ctk.CTkButton(master=buttons_frame, text="Publish new game", fg_color="transparent", hover_color="#4d4d4d",
                                        border_width=2, border_color="#b3b3b3", width=260, command=lambda: self.show_frame(self.new_game_page), image=plus_icon)
        add_button.pack(anchor="w", side="left", padx=(0, 8))
        list_button = ctk.CTkButton(master=buttons_frame, text="View published games", fg_color="transparent", hover_color="#4d4d4d",
                                        border_width=2, border_color="#b3b3b3", width=260, image=list_icon)
        list_button.pack(anchor="w", side="right")

    def library_page(self) -> None:
        #"""Show the user's library."""
        if "library_page" not in self.frames:


            library_frame = ctk.CTkScrollableFrame(master=self.main_view, fg_color="transparent")
            library_frame.pack(fill="both", expand=True)
            self.frames["library_page"] = library_frame

            content_frame = ctk.CTkFrame(master=library_frame, fg_color="transparent")
            content_frame.pack(anchor="n", fill="x", padx=24, pady=24)
            header_frame = ctk.CTkFrame(master=content_frame, fg_color="transparent")
            header_frame.pack(fill="x")

            #Search bar
            
            first_line = ctk.CTkFrame(master=header_frame, fg_color="transparent")
            first_line.pack(anchor="n", fill="x", side="left")

            search_entry = ctk.CTkEntry(master=first_line, height=30,
                                        font=("Roboto", 12), placeholder_text="Search in library")
            search_entry.pack(side="left", fill="x", expand=True)

            icon = load_image("search-md.png")
            icon = ctk.CTkImage(dark_image=icon, light_image=icon, size=(16, 16))

            search_button = ctk.CTkButton(
                master=first_line, height=30, text="Search", text_color="#ffffff",
                width=112, command=lambda: self.execute_search(search_entry.get()), compound="left", image=icon)
            search_button.pack(anchor="w", padx=(0, 0), side="left")

            #Add external game button
            
            img=ctk.CTkImage(dark_image=load_image("plus.png"), light_image=load_image("plus.png"), size=(16, 16))
            ctk.CTkButton(master=header_frame, text="Add game", fg_color="transparent", hover_color="#4d4d4d",
                          border_width=2, border_color="#b3b3b3", image=img).pack(anchor="w", side="right")
            
            self.create_labels_and_content(library_frame,"Last played")
        else:
            self.frames["library_page"].pack(fill="both", expand=True)

    def settings_page(self) -> None:
        """Show the settings page."""
        if "settings_page" not in self.frames:
            settings_frame = ctk.CTkScrollableFrame(master=self.main_view, fg_color="transparent")
            settings_frame.pack(fill="both", expand=True)
            self.frames["settings_page"] = settings_frame

            content_frame = ctk.CTkFrame(master=settings_frame, fg_color="transparent")
            content_frame.pack(anchor="w", fill="both", padx=24, pady=24, expand=True)

            # Cabeçalho da página de Configurações
            
            ctk.CTkLabel(
                master=content_frame,
                text="Settings",
                anchor="w",
                justify="left",
                font=self.h1
            ).pack(anchor="w", fill="y", expand=True)

            # SEÇÃO DE CONFIGURAÇÕES DE CONTA
            
            account_frame = ctk.CTkFrame(master=content_frame, fg_color="transparent")
            account_frame.pack(fill="x", anchor="w", pady=(24, 0))
            ctk.CTkLabel(
                master=account_frame,
                text="Account settings",
                anchor="w",
                font=self.body_bold
            ).pack(fill="x")

            ## Exibição do Email do Usuário
            
            change_email_frame = ctk.CTkFrame(master=account_frame, fg_color="transparent")
            change_email_frame.pack(fill="x", anchor="w", pady=(16, 0))
            headline = ctk.CTkFrame(master=change_email_frame, fg_color="transparent")
            headline.pack(fill="x", side="left", anchor="w")

            # Título e Subtítulo
            
            ctk.CTkLabel(
                master=headline,
                text="Email",
                anchor="w",
                font=self.body
            ).pack(anchor="w")
            ctk.CTkLabel(
                master=headline,
                text="Your registered email address",
                anchor="w",
                font=self.small,
                text_color="#b3b3b3"
            ).pack()

            # Exibição do Email como Rótulo (Não Editável)
            
            email_label = ctk.CTkLabel(
                master=change_email_frame,
                text=self.email,
                font=self.body,
                anchor="w"
            )
            email_label.pack(side="right", padx=(0, 8))

            ## Botões de Configuração Adicionais
            
            
            self.add_setting_btn(account_frame, "Change password", self.change_password, "link_external.png")
            self.add_setting_btn(account_frame, "Manage accounts", self.go_to_manage, "right_arrow.png")

            # SEÇÃO DE CONFIGURAÇÕES DO APLICATIVO
            
            app_settings_frame = ctk.CTkFrame(master=content_frame, fg_color="transparent")
            app_settings_frame.pack(fill="x", anchor="w", pady=(24, 0))
            self.add_separator(app_settings_frame)
            ctk.CTkLabel(
                master=app_settings_frame,
                text="App settings",
                anchor="w",
                font=self.body_bold
            ).pack(fill="x", pady=(16, 0))

            ## Alterar Tema
            
            change_theme = ctk.CTkFrame(master=app_settings_frame, fg_color="transparent")
            change_theme.pack(fill="x", anchor="w", pady=(24, 0))
            headline = ctk.CTkFrame(master=change_theme, fg_color="transparent")
            headline.pack(fill="x", side="left", anchor="w")

            ctk.CTkLabel(
                master=headline,
                text="Theme Color",
                anchor="w",
                font=self.body
            ).pack(anchor="w")

            ## Opções de Tema
            
            change_color_btn = ctk.CTkFrame(master=change_theme, height=32, width=310, fg_color="#4d4d4d")
            change_color_btn.pack(side="right") 

            ctk.CTkButton(
                master=change_color_btn,
                text="Dark",
                height=22,
                width=100,
                corner_radius=4,
                fg_color="transparent",
                command=self.dark_theme
            ).pack(fill="both", side="left", padx=5, pady=5)
            ctk.CTkButton(
                master=change_color_btn,
                text="White",
                height=22,
                width=100,
                corner_radius=4,
                fg_color="transparent",
                command=self.white_theme
            ).pack(fill="both", side="left", padx=5, pady=5)
            ctk.CTkButton(
                master=change_color_btn,
                text="System",
                height=22,
                width=100,
                corner_radius=4,
                fg_color="transparent",
                command=self.system_theme
            ).pack(fill="both", side="left", padx=5, pady=5)

        else:
            self.frames["settings_page"].pack(fill="both", expand=True)

    def getAdmin(self, mail):
        user = backend.fetch_user_details(mail)
        print(f"User details fetched: {user}")  # depuracao
        if user["type"] == 'Gamer':
            return False
        elif user["type"] == 'Publisher':
            return True
        else:
            print(f"Unknown user type: {user['type']}")
            return False


    def dark_theme(self) -> None:
        """Change the theme to dark."""
        ctk.set_appearance_mode("dark")
        ctk.set_default_color_theme(THEMES_PATH + "purple.json")

    def white_theme(self) -> None:
        """"Change the theme to white."""
        ctk.set_appearance_mode("light")
        ctk.set_default_color_theme(THEMES_PATH + "white.json")

    def game_page(self, game_title: str = "Game title", publisher: str = "Publisher", game_description: str = "Lorem ipsum dolor sit amet, consectetur adipiscing elit.",
                  game_tags: list = ["NULL, NULL"]
                  ) -> None:
        """Show the game page."""

        for widget in self.main_view.winfo_children():
            widget.destroy()
        
        if "game_page" not in self.frames:
            
            game_frame = ctk.CTkScrollableFrame(master=self.main_view, fg_color="transparent")
            game_frame.pack(fill="both", expand=True)
            self.frames["game_page"] = game_frame

            content_frame = ctk.CTkFrame(master=game_frame, fg_color="transparent")
            content_frame.pack(anchor="w", fill="x", padx=24, pady=24)

            self.add_game_header(content_frame, game_title, publisher, self.library_page)

            # Game image
            
            #imagem do jogo
            
            game_img_data = load_image("secondary-logo-colored.png")
            game_img = ctk.CTkImage(dark_image=game_img_data, light_image=game_img_data, size=(200, 168))
            ctk.CTkLabel(master=content_frame, image=game_img, text="", fg_color="#4d4d4d").pack(anchor="w", fill="x", pady=24,padx=0)

            # Buttons
            ### botoes
            btns_frame = ctk.CTkFrame(master=content_frame, fg_color="transparent", height=32)
            btns_frame.pack(fill="x", pady=(0, 24))

            ##Play/Dowload button (depending wether its in library or not
            # botao de download

            ##Button to add to library/In library button
            ## botao de adiciona a biblioteca
            
            bookmark = ctk.CTkImage(dark_image=load_image("bookmark.png"), light_image=load_image("bookmark.png"), size=(16, 16))
            bookmarked = ctk.CTkImage(dark_image=load_image("bookmark_check.png"), light_image=load_image("bookmark_check.png"), size=(16, 16))
            play = ctk.CTkImage(dark_image=load_image("play.png"), light_image=load_image("play.png"), size=(16, 16))

            if self.game_in_library:
                play_btn = ctk.CTkButton(master=btns_frame, image=play, text="Play", command=self.library_page)
                play_btn.pack(anchor="w", side="left", padx=(0, 8), fill="y")
                in_library = ctk.CTkButton(master=btns_frame, image=bookmarked, text="In library", command=self.remove_game_from_library, fg_color="#4d4d4d", hover_color="#3c3c3c")
                in_library.pack(anchor="w", side="left", padx=(0, 8), fill="y")
            else:
                add_button = ctk.CTkButton(master=btns_frame,image=bookmark, text="Add to library", command=self.add_game_to_library)
                add_button.pack(anchor="w", side="left", padx=(0, 8), fill="y")
            
            ##Favorite button
            #botao de favorito
            
            favorite = ctk.CTkImage(dark_image=load_image("heart.png"), light_image=load_image("heart.png"), size=(16, 16))
            favorite_button = ctk.CTkButton(master=btns_frame, image=favorite, text="", command=self.library_page, fg_color="transparent", border_color="#b3b3b3",
                                            hover_color="#4d4d4d", border_width=2, width=32)
            favorite_button.pack(anchor="w", side="right", fill="y")
            
            #About section
            #Seção sobre
            about_frame = ctk.CTkFrame(master=content_frame, fg_color="transparent")
            about_frame.pack(fill="x")
            description = ctk.CTkFrame(master=about_frame, fg_color="transparent", width=431)
            description.pack(side="left")
            ctk.CTkLabel(master=description, text="Game description", anchor="w", font=("Roboto",24,"bold")).pack(anchor="w")
            ctk.CTkLabel(master=description,font=("Roboto",12), text=game_description,
                         anchor="w", wraplength=431).pack(anchor="w")
            
            tags = ctk.CTkFrame(master=about_frame, fg_color="transparent", width=200)
            tags.pack(side="right", anchor="nw")
            ctk.CTkLabel(master=tags, text="Tags: ", anchor="w", font=("Roboto",12,"bold"), text_color="#b3b3b3").pack(anchor="w")
            
            for tag in game_tags:
                self.add_tag(tags, tag)
        
            self.add_separator(content_frame)

            ##Requirements section
            ctk.CTkLabel(master=content_frame, text="System requirements", anchor="w", font=self.h1).pack(fill="x", pady=(24,0))
            tabview = ctk.CTkTabview(master=content_frame, fg_color="#2a2a2a")
            tabview.pack(fill="x", pady=(16,24))

            tabview.add("Minimum")
            tabview.add("Recommended")
            tabview.add("Maximum")

            min_req_frame = ctk.CTkFrame(master=tabview.tab("Minimum"), fg_color="transparent")
            min_req_frame.pack(fill="x", anchor="w")
            rec_req_frame = ctk.CTkFrame(master=tabview.tab("Recommended"), fg_color="transparent")
            rec_req_frame.pack(fill="x", anchor="w")
            max_req_frame = ctk.CTkFrame(master=tabview.tab("Maximum"), fg_color="transparent")
            max_req_frame.pack(fill="x", anchor="w")

            min_requirements = {
                "OS": "Windows 7",
                "Processor": "Intel Core i5-3470 / AMD FX-6300",
                "Memory": "4 GB RAM",
                "Graphics card": "NVIDIA GeForce GTX 660 / AMD Radeon HD 7870",
                "Storage": "30 GB available space"
            }

            for key, value in min_requirements.items():
                ctk.CTkLabel(master=min_req_frame, text=key + ": " + value, anchor="w").pack(fill="x")

            rec_requirements = {
                "OS": "Windows 8",
                "Processor": "Intel Core i5-3470 / AMD FX-6300",
                "Memory": "8 GB RAM",
                "Graphics card": "NVIDIA GeForce GTX 660 / AMD Radeon HD 7870",
                "Storage": "40 GB available space"
            }

            for key, value in rec_requirements.items():
                ctk.CTkLabel(master=rec_req_frame, text=key + ": " + value, anchor="w").pack(fill="x")

            max_requirements = {
                "OS": "Windows 10",
                "Processor": "Intel Core i5-3470 / AMD FX-6300",
                "Memory": "8 GB RAM",
                "Graphics card": "NVIDIA GeForce GTX 660 / AMD Radeon HD 7870",
                "Storage": "50 GB available space"
            }

            for key, value in max_requirements.items():
                ctk.CTkLabel(master=max_req_frame, text=key + ": " + value, anchor="w").pack(fill="x")

            self.add_separator(content_frame)

            ##Reviews section

        else:
            self.frames["game_page"].pack(fill="both", expand=True)

    def add_game_to_library(self) -> None:
        """Add the game to the library."""
        self.game_in_library = True

    def remove_game_from_library(self) -> None:
        """Remove the game from the library."""
        pass

    def getUsername(self,mail):
        user = backend.fetch_account_details(mail)
        return (user["name"])

    def add_tag(self, master: ctk.CTkFrame, category: str) -> None:
        """Add a tag to the provided frame."""
        width = len(category)
        ctk.CTkButton(master=master, text=category, fg_color="#4d4d4d", hover_color="#3c3c3c", width=width).pack(anchor="w", pady=3)

    def new_game_page(self) -> None:
        """Show the page to add a new game."""
        if "new_game_page" not in self.frames:
            new_game_frame = ctk.CTkScrollableFrame(master=self.main_view, fg_color="transparent")
            new_game_frame.pack(fill="both", expand=True)
            self.frames["new_game_page"] = new_game_frame

            header_frame = ctk.CTkFrame(master=new_game_frame, fg_color="transparent")
            header_frame.pack(fill="x", padx=24, pady=(24,16))
            self.add_header(header_frame, "Add new game", self.home_page)

            #Frame where all the content will be placed
            content_frame = ctk.CTkFrame(master=new_game_frame, fg_color="#2a2a2a")
            content_frame.pack(anchor="w", fill="x", padx=24, pady=24)

            ##Frame where the form will be placed
            general_info = ctk.CTkFrame(master=content_frame, fg_color="transparent")
            general_info.pack(fill="x", padx=16, pady=16)
            ctk.CTkLabel(master=general_info, text="General info", anchor="w", justify="left",
                        font=("Roboto", 20, "bold")).pack(fill="x")
            ctk.CTkLabel(master=general_info, text="Title", anchor="w", justify="left").pack(fill="x")
            ctk.CTkEntry(master=general_info, border_width=2, placeholder_text="Game title").pack(fill="x")

            ctk.CTkLabel(master=general_info, text="Developer", anchor="w", justify="left").pack(fill="x")
            ctk.CTkEntry(master=general_info, border_width=2, placeholder_text="Game developer").pack(fill="x")

            ctk.CTkLabel(master=general_info, text="Game description", anchor="w", justify="left").pack(fill="x")
            ctk.CTkEntry(master=general_info, border_width=2, placeholder_text="Tell the users more about this game",
                         height=68).pack(fill="x")
            
            ###Price frame
            price = ctk.CTkFrame(master=general_info, fg_color="transparent")
            price.pack(fill="x")

            sale_price= ctk.CTkFrame(master=price, fg_color="transparent")
            sale_price.pack(side="left", anchor="w")
            ctk.CTkLabel(master=sale_price, text="Price", anchor="w", justify="left", width=250).pack()
            ctk.CTkEntry(master=sale_price, border_width=2, placeholder_text="R$1000", width=250).pack(anchor="nw")

            discount = ctk.CTkFrame(master=price, fg_color="transparent")
            discount.pack(side="right")
            ctk.CTkLabel(master=discount, text="Discount", anchor="w", justify="left", width=250).pack()
            ctk.CTkEntry(master=discount, border_width=2, placeholder_text="R$0", width=250).pack()

            ctk.CTkLabel(master=general_info, text="Publish date", anchor="w", justify="left").pack(fill="x")
            ctk.CTkEntry(master=general_info, border_width=2, placeholder_text="DD/MM/YY").pack(fill="x")

            ##Requirements frame
            requirements = ctk.CTkFrame(master=content_frame, fg_color="transparent")
            requirements.pack(fill="x", padx=16, pady=16)
            ctk.CTkLabel(master=requirements, text="Requirements", anchor="w", justify="left", font=("Roboto",20,"bold")).pack(fill="x")

            ctk.CTkLabel(master=requirements, text="Minimum", anchor="w", justify="left").pack(fill="x")
            ctk.CTkEntry(master=requirements, border_width=2, placeholder_text="OS, Processor, Memory, Graphics, Storage",
                         height=68).pack(fill="x")
            ctk.CTkLabel(master=requirements, text="Recommended", anchor="w", justify="left").pack(fill="x")
            ctk.CTkEntry(master=requirements, border_width=2, placeholder_text="OS, Processor, Memory, Graphics, Storage",
                         height=68).pack(fill="x")
            ctk.CTkLabel(master=requirements, text="Maximum", anchor="w", justify="left").pack(fill="x")
            ctk.CTkEntry(master=requirements, border_width=2, placeholder_text="OS, Processor, Memory, Graphics, Storage",
                         height=68).pack(fill="x")
            
            ##Tags frame and complementary info
            frame = ctk.CTkFrame(master=content_frame, fg_color="transparent")
            frame.pack(fill="x", padx=16, pady=16)
            ctk.CTkLabel(master=frame, text="Tags", anchor="w", justify="left").pack(fill="x")
            ctk.CTkCheckBox(master=frame, text="Action", fg_color="#4d4d4d").pack(anchor="w", side="left")


            ##Buttons frame
            buttons_frame = ctk.CTkFrame(master=content_frame, fg_color="transparent")
            buttons_frame.pack(fill="x", pady=16, padx=16)
            ctk.CTkButton(master=buttons_frame, text="Publish", command=self.new_game_page_warning, fg_color="#7C439E").pack(side="right")
            ctk.CTkButton(master=buttons_frame, text="Cancel", command=self.cancel_add_game,fg_color="transparent", hover_color="#4d4d4d",
                          border_width=2, border_color="#b3b3b3").pack(side="right", padx=(0,8))            

        else:
            self.frames["home_page"].pack_forget()
            self.frames["new_game_page"].pack(fill="both", expand=True)
    
    def cancel_add_game(self) -> None:
        """Cancel the addition of a new game."""
        self.frames["new_game_page"].pack_forget()
        self.frames["home_page"].pack(fill="both", expand=True)


    def new_game_page_warning(self) -> None:
        """Show a warning window before publishing a new game."""
        self.window = ctk.CTkToplevel()
        self.window.title("Confirm Changes")
        self.window.geometry("300x150")

        window_label = ctk.CTkLabel(master=self.window, text="Publish new game?", font=("Roboto", 16), width = len("Publish new game"))
        window_label.pack(pady=16)

        window_btn_confirm = ctk.CTkButton(master=self.window, text="Confirm", fg_color="purple", hover_color="#4d4d4d",border_width=2, border_color="#b3b3b3", width=len("Confirm"))
        window_btn_confirm.pack(side="left", anchor="s", padx=(50, 0), pady=(0, 16))

        window_btn_cancel = ctk.CTkButton(master=self.window, text="Cancel", command=self.window.destroy,fg_color="transparent", hover_color="#4d4d4d",border_width=2, border_color="#b3b3b3", width=len("Cancel"))
        window_btn_cancel.pack(side="right", anchor="s", padx=(0, 50), pady=(0, 16))

    def profile_page(self) -> None:
        """Show the user's profile page."""
        if "profile_page" not in self.frames:
            global name_Label, bio_Label, user_info, profile_info, ed

            profile_frame = ctk.CTkScrollableFrame(master=self.main_view, fg_color="transparent")
            profile_frame.pack(fill="both", expand=True)
            self.frames["profile_page"] = profile_frame

            content_frame = ctk.CTkFrame(master=profile_frame, fg_color="transparent")
            content_frame.pack(anchor="w", fill="x", padx=24, pady=24)

            profile_info = ctk.CTkFrame(master=content_frame, fg_color="transparent")
            profile_info.pack(fill="x")

            profile_img = ctk.CTkImage(dark_image=load_image("secondary-logo-colored.png"), light_image=load_image("secondary-logo-colored.png"), size=(100, 100))
            ctk.CTkLabel(master=profile_info, image=profile_img, text="", fg_color="#4d4d4d").pack(side="left")

            user_info = ctk.CTkFrame(master=profile_info, fg_color="transparent")
            user_info.pack(padx=(16, 0), side="left", anchor="nw")

            name_Label = ctk.CTkLabel(master=user_info, text=self.name, anchor="nw", justify="left", font=("Roboto", 24))
            name_Label.pack(fill="x")

            bio_Label = ctk.CTkLabel(master=user_info, text=self.bio, anchor="nw", justify="left", font=("Roboto", 16), text_color="#b3b3b3", wraplength=250)
            bio_Label.pack()

            ed = ctk.CTkButton(master=profile_info, text="Edit profile", command=self.edit_profile, fg_color="transparent", hover_color="#4d4d4d",border_width=2, border_color="#b3b3b3", width=len("Edit profile"))
            ed.pack(side="right", anchor="s")

            ##Account insights
            insights_frame = ctk.CTkFrame(master=content_frame, fg_color="transparent")
            insights_frame.pack(fill="x", pady=24, ipady=16, side="left")

            clock=ctk.CTkImage(dark_image=load_image("clock.png"), light_image=load_image("clock.png"), size=(64,64))
            reviews_icon=ctk.CTkImage(dark_image=load_image("review.png"), light_image=load_image("review.png"), size=(64,64))
            gaming_pad=ctk.CTkImage(dark_image=load_image("gaming_pad.png"), light_image=load_image("gaming_pad.png"), size=(64,64))

            inlibrary = ctk.CTkFrame(master=insights_frame, fg_color="#2a2a2a", width=200)
            inlibrary.pack(side="left", anchor="w", padx=(0,16), ipadx=36)
            ctk.CTkLabel(master=inlibrary, text="Games in library").pack(fill="x", pady=16)
            ctk.CTkLabel(master=inlibrary, text="", image=gaming_pad).pack(fill="x")
            ctk.CTkLabel(master=inlibrary, text="0", font=self.h1).pack(fill="x", pady=16)

            hrsplayed = ctk.CTkFrame(master=insights_frame, fg_color="#2a2a2a", width=200)
            hrsplayed.pack(side="left", anchor="e", padx=(16,16), ipadx=38)
            ctk.CTkLabel(master=hrsplayed, text="Hours played").pack(pady=16)
            ctk.CTkLabel(master=hrsplayed, text="", image=clock).pack()
            ctk.CTkLabel(master=hrsplayed, text="0",font=self.h1).pack(pady=16)

            reviews = ctk.CTkFrame(master=insights_frame, fg_color="#2a2a2a", width=200)
            reviews.pack(side="right", anchor="e",padx=(16,16), pady=16, ipadx=42)
            ctk.CTkLabel(master=reviews, text="Reviews").pack(pady=16)
            ctk.CTkLabel(master=reviews, text="", image=reviews_icon).pack()
            ctk.CTkLabel(master=reviews, text="0", font=self.h1).pack( pady=16)

            
        else:
            self.frames["profile_page"].pack(fill="both", expand=True)

    def edit_profile(self) -> None:
        """Edit the user's profile."""
        if not self.editing:

            self.set_alterations = ctk.CTkButton(master=profile_info, text="Ok", command=self.warning_window, fg_color="transparent", hover_color="#4d4d4d",border_width=2, border_color="#b3b3b3", width=len("Ok"))
            self.set_alterations.pack(side="left", anchor="s", pady=10, padx=10)

            ed.pack_forget()

            name_Label.pack_forget()
            self.name_entry = ctk.CTkEntry(master=user_info, border_width=2, placeholder_text=self.name, width=250)
            self.name_entry.insert(0, self.name)
            self.name_entry.pack()

            bio_Label.pack_forget()
            self.bio_entry = ctk.CTkEntry(master=user_info, border_width=2, height=50, placeholder_text=self.bio, width=250)
            self.bio_entry.insert(0, self.bio)
            self.bio_entry.pack(pady=10)

            self.editing = True

    def warning_window(self):
        """Confirm the alterations made to the user's profile."""
        self.window = ctk.CTkToplevel()
        self.window.title("Confirm Changes")
        self.window.geometry("300x150")

        window_label = ctk.CTkLabel(master=self.window, text="Save changes?", font=("Roboto", 16), width = len("Save changes"))
        window_label.pack(pady=16)

        window_btn_confirm = ctk.CTkButton(master=self.window, text="Confirm", command=self.confirm_changes, fg_color="#7C439E", hover_color="#4d4d4d",border_width=2, border_color="#b3b3b3", width=len("Confirm"))
        window_btn_confirm.pack(side="left", anchor="s", padx=(50, 0), pady=(0, 16))

        window_btn_cancel = ctk.CTkButton(master=self.window, text="Cancel", command=self.discard_changes, fg_color="transparent", hover_color="#4d4d4d",border_width=2, border_color="#b3b3b3", width=len("Cancel"))
        window_btn_cancel.pack(side="right", anchor="s", padx=(0, 50), pady=(0, 16))

    def confirm_changes(self) -> None:
        """Save alterations made to the user's profile."""
        new_name = self.name_entry.get()
        new_bio = self.bio_entry.get()
       
        update_username(new_name, self.name, self.email)
        self.name = new_name
        name_Label.configure(text=self.name)
        self.name_entry.pack_forget()
        name_Label.pack(fill="x")

        self.bio = new_bio
        bio_Label.configure(text=self.bio)
        self.bio_entry.pack_forget()
        bio_Label.pack(fill="x")

        ed.pack(side="right", anchor="s")

        self.set_alterations.pack_forget()

        self.window.destroy()

    def discard_changes(self) -> None:
        """Discard the alterations made to the user's profile."""
        self.name_entry.pack_forget()
        name_Label.pack(fill="x")

        self.bio_entry.pack_forget()
        bio_Label.pack(fill="x")

        ed.pack(side="right", anchor="s")

        self.set_alterations.pack_forget()

        self.editing = False
        self.window.destroy()

    def manage_accounts_page(self) -> None:
        """Show the page to manage accounts."""
        if "manage_accounts_page" not in self.frames:
            manage_accounts_frame = ctk.CTkScrollableFrame(master=self.main_view, fg_color="transparent")
            manage_accounts_frame.pack(fill="both", expand=True)
            self.frames["manage_accounts_page"] = manage_accounts_frame

            content_frame = ctk.CTkFrame(master=manage_accounts_frame, fg_color="transparent")
            content_frame.pack(anchor="w", fill="x", padx=24, pady=24)

            header = ctk.CTkFrame(master=content_frame, fg_color="transparent")
            header.pack(fill="x")

            self.add_header(header, "Manage accounts", self.settings_page)
            ctk.CTkButton(master=header, text="Add account", fg_color="#4d4d4d", hover_color="#3c3c3c").place(rely=0.5, x=475, anchor="center")

            # Account list
            account_list_frame = ctk.CTkFrame(master=content_frame, fg_color="transparent")
            account_list_frame.pack(fill="x", pady=(16, 0))

            self.account_frame(account_list_frame, "Name", "Email")

        else:
            self.frames["manage_accounts_page"].pack(fill="both", expand=True)

    def account_frame(self, master: ctk.CTkFrame, name: str, email: str) -> None:
        """Add an account to the account list."""
        account_frame = ctk.CTkFrame(master=master, fg_color="transparent")
        account_frame.pack(fill="x", pady=(8, 0))

        label = ctk.CTkFrame(master=account_frame, fg_color="transparent")
        label.pack(fill="x", side="left")

        ctk.CTkLabel(master=label, text=name, anchor="w", justify="left",
                    font=("Roboto", 16)).pack(anchor="w", side="top")

        ctk.CTkLabel(master=label, text=email, anchor="w", justify="left",
                    font=("Roboto", 12), text_color="#b3b3b3").pack(anchor="w", side="bottom")
        
        login_icon = ctk.CTkImage(dark_image=load_image("login.png"), light_image=load_image("login.png"), size=(16, 16))
        ctk.CTkButton(master=account_frame, text="Remove",width=78, fg_color="transparent",height=32, hover_color="#4d4d4d", border_color="#b3b3b3",
                      border_width=2).pack(anchor="w", side="right")
        ctk.CTkButton(master=account_frame, text="Login", width=91, image=login_icon,height=32).pack(anchor="w", side="right",padx=(0,8))

    def create_search_bar(self, master: ctk.CTkFrame, placeholder) -> None:
        """Create the first line of the main view with a search bar and a button."""
        first_line = ctk.CTkFrame(master=master, fg_color="transparent")
        first_line.pack(anchor="n", fill="x")

        # Entry field for the search query
        search_entry = ctk.CTkEntry(master=first_line, height=30,
                                    font=("Roboto", 12), placeholder_text=placeholder)
        search_entry.pack(side="left", fill="x", expand=True)

        icon = load_image("search-md.png")
        icon = ctk.CTkImage(dark_image=icon, light_image=icon, size=(16, 16))

        # Button com lambda para capturar o valor de search_entry e passar para execute_search
        search_button = ctk.CTkButton(
            master=first_line, height=30, text="Search", text_color="#ffffff",
            width=112, command=lambda: self.execute_search(search_entry.get()), compound="left", image=icon
        )
        search_button.pack(anchor="w", padx=(8, 0), side="right")


    def execute_search(self, query: str) -> None:
        """Handle the search action by querying the store and displaying results."""
        
        print(f"Buscando por: {query}")
        
        if query:
            try:
                results = search_in_store(query)  # Chama a função de busca com o termo fornecido
                self.display_search_results(results)
            except Exception as e:
                print(f"Erro ao buscar jogos: {e}")
                # Opcional: exibir uma mensagem de erro na interface
        else:
            print("Por favor, insira um termo de pesquisa.")
            # Opcional: exibir uma mensagem na interface solicitando o termo de pesquisa

    def display_search_results(self, results: list) -> None:
        """Display the search results in the interface."""
        # Primeiro, criar um novo frame ou limpar o existente para exibir os resultados
        
        print(f"Exibindo resultados: {results}")
        self.store_page(self.home_frame, results)

        
    
    # Opcional: Adicionar botões ou outras funcionalidades para cada resultado


    def create_labels_and_content(self, master: ctk.CTkFrame, header, games=None) -> None:
        """Create labels and content sections."""
        ctk.CTkLabel(master=master, text=header, anchor="w", justify="left",
                     font=("Roboto Bold", 24)).pack(anchor="w", pady=(8, 16), padx=24)

        recently_added_frame = ctk.CTkFrame(master, fg_color="transparent")
        recently_added_frame.pack(fill="x", pady=(10, 0),padx=(24,0))
        
        is_search = False

        

        if games is not None:
            games = [list(game.values()) for game in games]
            is_search = True
        
        else:
            games = get_all_games()

        print("GAMES: {}".format(games))
        for i in range(min(5, len(games))):  # Ensure i does not exceed the length of games
            try:
                # Ensure the game list has enough elements
                title = games[i][0] if len(games[i]) > 0 else None
                developer = games[i][2] if len(games[i]) > 2 else None
                description = games[i][4] if len(games[i]) > 4 else None  # Or use an appropriate default value
                genre = games[i][3] if len(games[i]) > 3 else None
                
                self.game_card(recently_added_frame, title, developer, description, genre).pack(side="left", padx=(0, 8), pady=8)

            except IndexError:
                pass  # If there's an index error, skip this game

        self.add_separator(master)                

        games = get_all_games()

        # Tabs:
        tabs = ["All"]

        games_frame = ctk.CTkFrame(master, fg_color="transparent")
        games_frame.pack(fill="x", pady=24, padx=24)

        menu = ctk.CTkFrame(master=games_frame, fg_color="transparent")
        menu.pack(fill="x", side="top")

        for tab in tabs:
            btn = ctk.CTkButton(master=menu, text=tab, fg_color="transparent", text_color="#ffffff",
                                font=("Roboto", 24), hover_color=SIDE_BAR_COLOR, width=len(tab))
            btn.pack(side="left", padx=(0, 8), pady=(0, 16))

        cards_frame = ctk.CTkFrame(master=games_frame, fg_color="transparent")
        cards_frame.pack(fill="both", expand=True)

        num_columns = 3


        minus_index = 5
        if is_search:
            minus_index = 0 

        for i in range(len(games) - minus_index):
            row = i // num_columns
            column = i % num_columns
            self.game_card(cards_frame, games[i+minus_index][0], games[i+minus_index][2], games[i+minus_index][5], games[i+minus_index][3]).grid(row=row, column=column, padx=8, pady=8, sticky="nsew")

        for col in range(num_columns):
            cards_frame.grid_columnconfigure(col, weight=1)
        cards_frame.grid_rowconfigure(0, weight=1)

    def _on_mouse_wheel_horizontal(self, event):
        """Scroll the frame horizontally."""
        event.widget.xview("scroll", int(-1*(event.delta/120)), "units")

    def game_card(self, master, game_title="Game Title", publisher="Publisher", description="NULL", tags="STR") -> ctk.CTkFrame:
        """Create and return a game card frame."""
        game_frame = ctk.CTkFrame(master, corner_radius=8, fg_color="transparent", width=150, height=200)
        
        try:
            image = load_image("secondary-logo-colored.png")
            image = image.resize((150, 200), Image.LANCZOS)  # Resize the image to fit the frame
            ctk_image = ctk.CTkImage(light_image=image, dark_image=image, size=(134, 134))
        except Exception as e:
            print(f"Error loading image: {e}")
            ctk_image = None

        if ctk_image:
            image_label = ctk.CTkLabel(master=game_frame, image=ctk_image, text="")
            image_label.grid(row=0, column=0, padx=16, pady=16, sticky="nsew")


        ctk.CTkLabel(master=game_frame, text=game_title, text_color="#ffffff", anchor="w", justify="left",
                     font=("Roboto Bold", 12)).grid(row=1, column=0, sticky="w", padx=16, pady=(16, 0))
        ctk.CTkLabel(master=game_frame, text=publisher, text_color="#ffffff", anchor="w", justify="left",
                     font=("Roboto Bold", 12)).grid(row=2, column=0, sticky="w", padx=16, pady=(0, 16))

        def on_enter(event):
            event.widget.config(cursor="hand2")
            game_frame.configure(fg_color="#4d4d4d")

        def on_leave(event):
            event.widget.config(cursor="")
            game_frame.configure(fg_color="transparent")

        tags = tags.split(", ")

        game_frame.bind("<Button-1>", lambda e: self.show_frame(self.game_page(game_title, publisher, description, tags)))
        game_frame.bind("<Enter>", on_enter)
        game_frame.bind("<Leave>", on_leave)

        for widget in game_frame.winfo_children():
            widget.bind("<Button-1>", lambda e: self.show_frame(self.game_page(game_title, publisher, description, tags)))
            widget.bind("<Enter>", on_enter)
            widget.bind("<Leave>", on_leave)

        return game_frame



    def add_header(self, master: ctk.CTkFrame, title: str, return_frame: str) -> None:
        """Add the header to the main view."""
        header = ctk.CTkFrame(master=master, fg_color="transparent")
        header.pack(anchor="w")

        arrow_left = load_image("arrow-left.png")
        left_arrow = ctk.CTkImage(dark_image=arrow_left, light_image=arrow_left, size=(29, 29))
        ctk.CTkButton(master=header, image=left_arrow, fg_color="transparent", hover_color=SIDE_BAR_COLOR,
                      command=lambda: self.show_frame(return_frame), text='', width=29, height=29).pack(anchor="w", side="left", padx=(0, 32), fill="y")

        title_label = ctk.CTkLabel(master=header, text=title, anchor="w", justify="left",
                                  font=self.h1)
        title_label.pack(anchor="w", fill="y", expand=True)

    def add_game_header(self, master: ctk.CTkFrame, title: str, publisher: str, return_frame: str) -> None:
        """Add the header to the main view."""
        header = ctk.CTkFrame(master=master, fg_color="transparent")
        header.pack(fill="x")

        arrow_left = load_image("arrow-left.png")
        left_arrow = ctk.CTkImage(dark_image=arrow_left, light_image=arrow_left, size=(29, 29))
        ctk.CTkButton(
            master=header,
            image=left_arrow,
            fg_color="transparent",
            hover_color=SIDE_BAR_COLOR,
            command=lambda: [self.home_page()], 
            text='',
            width=29,
            height=29
        ).pack(anchor="w", side="left", padx=(0, 32), fill="y")

        text_frame = ctk.CTkFrame(master=header, fg_color="transparent")
        text_frame.pack(fill="x", expand=True, side="left")

        title_label = ctk.CTkLabel(master=text_frame, text=title, anchor="w", justify="left", font=self.h1)
        title_label.pack(anchor="w", expand=True)
        
        publisher_label = ctk.CTkLabel(master=text_frame, text=publisher, anchor="w", justify="left",
                                    font=self.body, text_color="#b3b3b3")
        publisher_label.pack(anchor="w", expand=True)

    def add_separator(self, master) -> None:
        """Add a separator to the main view."""
        ctk.CTkLabel(master=master, text_color=SIDE_BAR_COLOR,
                     text="__________________________________________________________________________________________",
                     fg_color="transparent").pack(fill="x", pady=(0, 0))
        
    def add_setting_btn(self, master, text, command, icon) -> None:
        btn_frame = ctk.CTkFrame(master=master, fg_color="transparent", corner_radius=0)
        btn_frame.pack(fill="x", anchor="w", pady=(8, 0))
        icon = ctk.CTkImage(dark_image=load_image(icon), light_image=load_image(icon), size=(24, 24))

        ctk.CTkLabel(master=btn_frame, text=text, anchor="w", font=self.body, pady=16).pack(anchor="w", side="left")
        ctk.CTkLabel(master=btn_frame, text="", anchor="w", image=icon).pack(side="right")

        btn_frame.bind("<Button-1>", lambda e: command())
        btn_frame.bind("<Enter>", lambda event: event.widget.config(cursor="hand2"))
        btn_frame.bind("<Leave>", lambda event: event.widget.config(cursor=""))
        btn_frame.bind("<Enter>", lambda event: btn_frame.configure(fg_color="#4d4d4d"))
        btn_frame.bind("<Leave>", lambda event: btn_frame.configure(fg_color="transparent"))

        for widget in btn_frame.winfo_children():
            widget.bind("<Button-1>", lambda e: command())
            widget.bind("<Enter>", lambda event: event.widget.config(cursor="hand2"))
            widget.bind("<Enter>", lambda event: btn_frame.configure(fg_color="#4d4d4d"))
            widget.bind("<Leave>", lambda event: event.widget.config(cursor=""))
            widget.bind("<Leave>", lambda event: btn_frame.configure(fg_color="transparent"))

    def go_to_manage(self) -> None:
        self.show_frame(self.manage_accounts_page)
    
    def change_password(self) -> None:
        print("Change password")

    def create_main_view(self) -> None:
        """Create the main view frame with the title and content."""
        self.main_view = ctk.CTkFrame(master=self.app, width=680, height=650, corner_radius=0)
        self.main_view.pack_propagate(0)
        self.main_view.pack(side="left")

        self.show_frame(self.home_page)