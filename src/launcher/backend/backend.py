import mysql.connector as mysql # Import the MySQL connector library.

db_host = "localhost"
db_user = "root"
db_password = "password"
db_name = "PalyNexus"

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

def authenticate_user(email: str, password: str) -> bool:
    """Check if the provided credentials are valid."""
    database = mysql.connect(host=db_host, user=db_user, password=db_password, database=db_name)
    cursor = database.cursor()
    cursor.execute("SELECT * FROM Account WHERE email = %s AND password = %s", (email, password))
    if cursor.fetchone() is not None:
        cursor.close()
        database.close()
        return True
    cursor.close()
    database.close()
    return False
    

def create_user(email: str, password: str, type: str) -> bool:
    """Create a new user in the database."""
    if type not in ["Gamer", "Publisher"]: return False
    database = mysql.connect(host=db_host, user=db_user, password=db_password, database=db_name)
    cursor = database.cursor()
    cursor.execute("SELECT * FROM Account WHERE email = %s", (email,))
    if cursor.fetchone() is not None:
        cursor.close()
        database.close()
        return False
    cursor.execute("INSERT INTO Account (email, password, type) VALUES (%s, %s, %s)", (email, password, type))
    database.commit()
    cursor.close()
    database.close()
    return True

def set_gamer(email: str, username: str, birth_date: str, country: str) -> bool:
    """Create and set gamer details in the database."""
    database = mysql.connect(host=db_host, user=db_user, password=db_password, database=db_name)
    cursor = database.cursor()
    cursor.execute("SELECT * FROM Account WHERE email = %s AND type = 'Gamer'", (email,))
    if cursor.fetchone() is None:
        cursor.close()
        database.close()
        return False
    cursor.execute("INSERT INTO Gamer (account, username, birth_date, country) VALUES (%s, %s, %s, %s)", (email, username, birth_date, country))
    database.commit()
    cursor.close()
    database.close()
    return True

def set_publisher(email: str, name: str) -> bool:
    """Create and set publisher details in the database."""
    database = mysql.connect(host=db_host, user=db_user, password=db_password, database=db_name)
    cursor = database.cursor()
    cursor.execute("SELECT * FROM Account WHERE email = %s AND type = 'Publisher'", (email,))
    if cursor.fetchone() is None:
        cursor.close()
        database.close()
        return False
    cursor.execute("INSERT INTO Publisher (account, company_name) VALUES (%s, %s)", (email, name))
    database.commit()
    cursor.close()
    database.close()
    return True

def update_user_password(email: str, new_password: str) -> bool:
    """Update the user's password in the database."""
    pass

def fetch_user_details(email: str) -> dict:
    """Fetch user details from the database."""
    pass

def log_user_activity(user_id: int, activity: str) -> None:
    """Log user activity."""
    pass

def get_downloads(user_id: int) -> list:
    """Fetch download history for a user."""
    pass

def add_game_to_library(user_id: int, game_id: int) -> bool:
    """Add a game to the user's library."""
    pass

def remove_game_from_library(user_id: int, game_id: int) -> bool:
    """Remove a game from the user's library."""
    pass

def fetch_library(user_id: int) -> list:
    """Fetch all games in the user's library."""
    pass

def update_user_account_details(user_id: int, new_email: str, new_username: str) -> bool:
    """Update user account details."""
    pass

def log_failed_login_attempt(email: str) -> None:
    """Log a failed login attempt."""
    pass