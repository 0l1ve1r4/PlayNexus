import mysql.connector as mysql # Import the MySQL connector library for database operations.
import string # Import the string library for string operations.
import zlib # Import the zlib library for data compression.
import os # Import the os library for file operations.

class ConnectDB:
    """Connect to the database."""

    db_host = "localhost"
    db_user = "root"
    db_password = "bl4ckm1rr0r"
    db_name = "PlayNexus"

    def __init__(self):
        self.session = mysql.connect(host=self.db_host, user=self.db_user, password=self.db_password, database=self.db_name)
        self.cursor = self.session.cursor()

    def __exit__(self):
        self.cursor.close()
        self.session.close()

    def execute(self, sql: str, values: tuple):
        self.cursor.execute(sql, values)

    def result(self):
        return self.cursor.fetchone()
    
    def results(self):
        return self.cursor.fetchall()
        
    def commit(self):
        self.session.commit()

def get_user_path(account: str) -> str:
    """Create a directory for the user and return the path."""
    if os.path.exists("users") is False: os.mkdir("users")
    user_path = f"users/{account.split("@")[0].translate(str.maketrans("", "", string.punctuation))}"
    if os.path.exists(user_path) is False: os.mkdir(user_path)
    return user_path

def get_games_path(account: str) -> str:
    """Create a directory for the game and return the path."""
    games_path = f"{get_user_path(account)}/games"
    if os.path.exists(games_path) is False: os.mkdir(games_path)
    return games_path

def get_game_path(account: str, game_title: str) -> str:
    """Return the path to the game."""
    game_path = f"{get_games_path(account)}/{game_title.replace(" ", "_")}.run"
    return game_path

######################################################################################################
# The following methods are used to interact with the USERS.                                         #
######################################################################################################

def authenticate_user(email: str, password: str) -> bool:
    """Check if the provided credentials are valid."""
    database = ConnectDB()
    database.execute("SELECT * FROM Account WHERE email = %s AND password = %s", (email, password))
    if database.result() is None: return False
    get_user_path(email)
    return True

def create_user(email: str, password: str, user_type: str) -> bool:
    """Create a new user in the database."""
    if user_type not in ["Gamer", "Publisher"]: return False
    database = ConnectDB()
    database.execute("SELECT * FROM Account WHERE email = %s", (email,))
    if database.result() is not None: return False
    database.execute("INSERT INTO Account (email, password, type) VALUES (%s, %s, %s)", (email, password, user_type))
    database.commit()
    return True

def log_failed_login_attempt(email: str) -> None:
    """Log a failed login attempt."""
    pass

def update_user_password(email: str, new_password: str) -> bool:
    """Update the user's password in the database."""
    pass

def fetch_user_details(email: str) -> dict:
    """Fetch user details from the database."""
    pass

def log_user_activity(user_id: int, activity: str) -> None:
    """Log user activity."""
    pass

def create_gamer(account: str, username: str, birth_date: str, country: str) -> bool:
    """Create and set gamer details in the database."""
    database = ConnectDB()
    database.execute("SELECT * FROM Account WHERE email = %s AND type = 'Gamer'", (account,))
    if database.result() is None: return False
    database.execute("INSERT INTO Gamer (account, username, birth_date, country) VALUES (%s, %s, %s, %s)", (account, username, birth_date, country))
    database.commit()
    return True

def count_gamers() -> int:
    """Count the number of gamers in the database."""
    database = ConnectDB()
    database.execute("SELECT * FROM Gamer")
    return len(database.results())

def create_publisher(account: str, name: str) -> bool:
    """Create and set publisher details in the database."""
    database = ConnectDB()
    database.execute("SELECT * FROM Account WHERE email = %s AND type = 'Publisher'", (account,))
    if database.result() is None: return False
    database.execute("INSERT INTO Publisher (account, name) VALUES (%s, %s)", (account, name))
    database.commit()
    return True

def count_publishers() -> int:
    """Count the number of publishers in the database."""
    database = ConnectDB()
    database.execute("SELECT * FROM Publisher")
    return len(database.results())

######################################################################################################
# The following methods are used to interact with the GAME STORE.                                    #
######################################################################################################

def publish_game(title: str, publisher: str, developer: str, genre: str, description: str, cover_path: str, installer_path: str, price: float) -> bool:
    """Publish a game in the store."""
    database = ConnectDB()
    database.execute("SELECT * FROM Publisher WHERE account = %s", (publisher,))
    if database.result() is None: return False
    database.execute("SELECT * FROM Game WHERE title = %s AND publisher = %s", (title, publisher))
    if database.result() is not None: return False
    if (os.path.exists(cover_path) and os.path.exists(installer_path)) is False: return False
    cover = zlib.compress(open(cover_path, "rb").read())
    installer = zlib.compress(open(installer_path, "rb").read())
    database.execute("INSERT INTO Game (title, publisher, developer, genre, description, cover, installer, price) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)", (title, publisher, developer, genre, description, cover, installer, price))
    database.commit()
    return True

def get_all_games() -> list:
    """Fetch all games from the database."""
    database = ConnectDB()
    database.execute("SELECT * FROM Game")
    return database.results()

def count_games_in_store() -> int:
    """Count the number of games in the store."""
    return len(get_all_games())

def search_in_store(query: str) -> dict:
    """Search for a game in the store."""
    pass

def get_recently_added_games(limit: int = 5) -> list:
    """Fetch recently added games from the database."""
    pass

def get_popular_games() -> list:
    """Fetch popular games from the database."""
    pass

def get_new_games() -> list:
    """Fetch new games from the database."""
    pass

def get_upcoming_games() -> list:
    """Fetch upcoming games from the database."""
    pass

######################################################################################################
# The following methods are used to interact with the GAME LIBRARY.                                  #
######################################################################################################

def get_library(gamer: str) -> list:
    """Fetch all games in the user's library."""
    database = ConnectDB()
    database.execute("SELECT * FROM Purchase WHERE gamer = %s", (gamer,))
    return database.results()

def count_games_in_library(gamer: str) -> int:
    """Count the number of games in the user's library."""
    return len(get_library(gamer))

def game_is_installed(gamer: str, game_title: str) -> bool:
    """Check if a game is installed in the system."""
    return os.path.exists(get_game_path(gamer, game_title))

def install_game(gamer: str, game_title: str, game_publisher: str) -> bool:
    """Install a game from the user's library."""
    if game_is_installed(gamer, game_title): return False
    database = ConnectDB()
    database.execute("SELECT installer FROM Game WHERE title = %s AND publisher = %s", (game_title, game_publisher))
    installer = zlib.decompress(database.result()[0])
    game_path = get_game_path(gamer, game_title)
    with open(game_path, "wb") as file: file.write(installer)
    return True

def uninstall_game(gamer: str, game_title: str) -> bool:
    """Uninstall a game from the user's library."""
    if game_is_installed(gamer, game_title) is False: return False
    os.remove(get_game_path(gamer, game_title))
    return True

def play_game(gamer: str, game_title: str) -> bool:
    """Play a game from the user's library."""
    if game_is_installed(gamer, game_title) is False: return False
    game_path = get_game_path(gamer, game_title)
    os.system(f"chmod +x {game_path}")
    os.system(f"./{game_path}")
    return True
