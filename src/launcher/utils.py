import json

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
    """Load the theme settings from the JSON file."""
    return load_json(THEMES_PATH + 'purple.json')