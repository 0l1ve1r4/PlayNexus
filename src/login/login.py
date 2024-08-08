from customtkinter import *
from PIL import Image

class Login():

    def __init__(self) -> None:
        self.res_path = 'res/'
        self.app = CTk()
        self.app.geometry("600x480")
        self.app.resizable(0,0)
        self.app.title("PlayNexus | Login")

        side_img_data = Image.open(self.res_path + "side-img.png")
        email_icon_data = Image.open(self.res_path + "email-icon.png")
        password_icon_data = Image.open(self.res_path + "password-icon.png")
        google_icon_data = Image.open(self.res_path + "google-icon.png")

        self.side_img = CTkImage(dark_image=side_img_data, light_image=side_img_data, size=(300, 480))
        self.email_icon = CTkImage(dark_image=email_icon_data, light_image=email_icon_data, size=(20,20))
        self.password_icon = CTkImage(dark_image=password_icon_data, light_image=password_icon_data, size=(17,17))
        self.google_icon = CTkImage(dark_image=google_icon_data, light_image=google_icon_data, size=(17,17))

        pass

    def run(self):
        CTkLabel(master=self.app, text="", image=self.side_img).pack(expand=True, side="left")

        frame = CTkFrame(master=self.app, width=300, height=480, fg_color="#ffffff")
        frame.pack_propagate(0)
        frame.pack(expand=True, side="right")

        CTkLabel(master=frame, text="Welcome Back!", text_color="#601E88", anchor="w", justify="left", font=("Arial Bold", 24)).pack(anchor="w", pady=(50, 5), padx=(25, 0))
        CTkLabel(master=frame, text="Sign in to your account", text_color="#7E7E7E", anchor="w", justify="left", font=("Arial Bold", 12)).pack(anchor="w", padx=(25, 0))

        CTkLabel(master=frame, text="  Email:", text_color="#601E88", anchor="w", justify="left", font=("Arial Bold", 14), image=self.email_icon, compound="left").pack(anchor="w", pady=(38, 0), padx=(25, 0))
        self.email_entry = CTkEntry(master=frame, width=225, fg_color="#EEEEEE", border_color="#601E88", border_width=1, text_color="#000000")
        self.email_entry.pack(anchor="w", padx=(25, 0))

        CTkLabel(master=frame, text="  Password:", text_color="#601E88", anchor="w", justify="left", font=("Arial Bold", 14), image=self.password_icon, compound="left").pack(anchor="w", pady=(21, 0), padx=(25, 0))
        self.passw_entry = CTkEntry(master=frame, width=225, fg_color="#EEEEEE", border_color="#601E88", border_width=1, text_color="#000000", show="*")
        self.passw_entry.pack(anchor="w", padx=(25, 0))

        login_button = CTkButton(master=frame, text="Login", fg_color="#601E88", hover_color="#E44982", font=("Arial Bold", 12), text_color="#ffffff", width=225, command=self.check_credentials)
        login_button.pack(anchor="w", pady=(40, 0), padx=(25, 0))
        CTkButton(master=frame, text="Continue With Google", fg_color="#EEEEEE", hover_color="#EEEEEE", font=("Arial Bold", 9), text_color="#601E88", width=225, image=self.google_icon).pack(anchor="w", pady=(20, 0), padx=(25, 0))

        self.app.mainloop()

    # Check the frames in the database
    def check_credentials(self) -> None:
        email_str = self.email_entry.get()
        passw_str = self.passw_entry.get()

        print(f"Email: {email_str}, passw: {passw_str}")

        pass
