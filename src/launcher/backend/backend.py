import mysql.connector as mysql # Import the MySQL connector library for database operations.
import zlib # Import the zlib library for data compression.

class connect_db:
    """Connect to the database."""

    db_host = "localhost"
    db_user = "root"
    db_password = "bl4ckm1rr0r"
    db_name = "PlayNexus"

    def __init__(self):
        self.session = mysql.connect(host=self.db_host, user=self.db_user, password=self.db_password, database=self.db_name)
        self.cursor = self.database.cursor()

    def __exit__(self):
        self.cursor.close()
        self.session.close()

    def execute(self, sql: str, values: tuple):
        self.cursor.execute(sql, values)

    def result(self):
        return self.cursor.fetchone()
        
    def commit(self):
        self.session.commit()

######################################################################################################
# The following methods are used to interact with the USERS.                                         #
######################################################################################################

def authenticate_user(email: str, password: str) -> bool:
    """Check if the provided credentials are valid."""
    database = connect_db()
    database.execute("SELECT * FROM Account WHERE email = %s AND password = %s", (email, password))
    if database.result() is not None: return True
    return False

def create_user(email: str, password: str, user_type: str) -> bool:
    """Create a new user in the database."""
    if user_type not in ["Gamer", "Publisher"]: return False
    database = connect_db()
    database.execute("SELECT * FROM Account WHERE email = %s", (email,))
    if database.result() is not None: return False
    database.execute("INSERT INTO Account (email, password, type) VALUES (%s, %s, %s)", (email, password, user_type))
    database.commit()
    return True

def update_user_account_details(user_id: int, new_email: str, new_username: str) -> bool:
    """Update user account details."""
    pass

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

def create_gamer(email: str, username: str, birth_date: str, country: str) -> bool:
    """Create and set gamer details in the database."""
    database = connect_db()
    database.execute("SELECT * FROM Account WHERE email = %s AND type = 'Gamer'", (email,))
    if database.result() is None: return False
    database.execute("INSERT INTO Gamer (account, username, birth_date, country) VALUES (%s, %s, %s, %s)", (email, username, birth_date, country))
    return True

def create_publisher(email: str, name: str) -> bool:
    """Create and set publisher details in the database."""
    database = connect_db()
    database.execute("SELECT * FROM Account WHERE email = %s AND type = 'Publisher'", (email,))
    if database.result() is None: return False
    database.execute("INSERT INTO Publisher (account, name) VALUES (%s, %s)", (email, name))
    database.commit()
    return True

######################################################################################################
# The following methods are used to interact with the GAME STORE.                                    #
######################################################################################################

def publish_game(publisher: str, title: str, developer: str, genre: str, description: str, cover_path: str, installer_path: str, price: float) -> bool:
    """Publish a game in the store."""
    database = connect_db()
    database.execute("SELECT * FROM Publisher WHERE account = %s", (publisher,))
    if database.result() is None: return False
    database.execute("SELECT * FROM Game WHERE title = %s AND publisher = %s", (title, publisher))
    if database.result() is not None: return False
    cover = zlib.compress(open(cover_path, "rb").read())
    installer = zlib.compress(open(installer_path, "rb").read())
    database.execute("INSERT INTO Game (title, publisher, developer, genre, description, cover, installer, price) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)", (title, publisher, developer, genre, description, cover, installer, price))
    database.commit()
    return True

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

def get_all_games() -> list:
    """Fetch all games from the database."""
    pass

######################################################################################################
# The following methods are used to interact with the GAME LIBRARY.                                  #
######################################################################################################

def fetch_library(gamer: str) -> list:
    """Fetch all games in the user's library."""
    database = connect_db()
    database.execute("SELECT title FROM Purchase WHERE gamer = %s", (gamer,))
    result = database.result()
    if result is None: return list()
    return list(result)

def get_downloads(user_id: int) -> list:
    """Fetch download history for a user."""
    pass

def add_game_to_library(user_id: int, game_id: int) -> bool:
    """Add a game to the user's library."""
    pass

def remove_game_from_library(user_id: int, game_id: int) -> bool:
    """Remove a game from the user's library."""
    pass
