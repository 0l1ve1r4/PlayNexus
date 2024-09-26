import json
import customtkinter as ctk
from PIL import Image

RES_PATH = 'res/'
THEMES_PATH = RES_PATH + 'themes/'

def load_json(file_path: str) -> dict:
    """Load a JSON file and return it as a dictionary."""
    with open(file_path, 'r') as file:
        return json.load(file)
    
def load_image(file_path: str) -> Image:
    """Load an image file and return it as a PIL Image object."""
    return Image.open(RES_PATH + file_path)

def load_theme() -> dict:
    
    #"""Load the theme settings from the JSON file."""
    
    return load_json(THEMES_PATH + 'purple.json')

def show_frame(self, frame_name: str) -> None:
    
    #"""Show the selected frame and hide the current one."""
    
    if self.current_frame:
        self.current_frame.pack_forget()
    frame_method = self.frames.get(frame_name)
    if frame_method:
        frame_method()  # This should show the frame and pack it
        self.current_frame = frame_method
    ctk.CTkLabel(master=self.sidebar_frame, text="", fg_color="#302c2c").pack(expand=True)