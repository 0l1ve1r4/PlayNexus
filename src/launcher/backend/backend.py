import mysql.connector as mysql # Import the MySQL connector library for database operations.
import string # Import the string library for string operations.
import zlib # Import the zlib library for data compression.
import os # Import the os library for file operations.
import platform # Import the platform library for platform information.

class ConnectDB:
   # """Connect to the database."""

    db_host = "localhost"
    db_user = "root"
    db_password = "12345"
    db_name = "PlayNexus"

    def __init__(self):
        ## connects to the database
        
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

######################################################################################################
# The following methods are used to interact with the FILE SYSTEM.                                   #
######################################################################################################
def get_home_path() -> str:
    
    #"""Create a directory for PlayNexus in the user's home directory and return the path."""
    
    home_path = os.path.join(os.path.expanduser('~'), ".PlayNexus")
    if not os.path.exists(home_path):
        os.mkdir(home_path)
    return home_path

def get_user_path(account: str) -> str:
    
    #"""Create a directory for the user and return the path."""
    
    user_path = os.path.join(get_home_path(), account.split("@")[0].translate(str.maketrans("", "", string.punctuation)))
    if not os.path.exists(user_path):
        os.mkdir(user_path)
    return user_path

def get_games_path(account: str) -> str:
    
    #"""Create a directory for the game and return the path."""
    
    games_path = os.path.join(get_user_path(account), "games")
    if not os.path.exists(games_path):
        os.mkdir(games_path)
    return games_path

def get_game_path(account: str, game_title: str) -> str:
    
    #"""Return the path to the game."""
    
    game_path = ""
    if platform.system() == "Linux":
        extension = ".run"
    elif platform.system() == "Windows":
        extension = ".exe"
    else:
        return None
    game_path = os.path.join(get_games_path(account), f"{game_title.replace(' ', '_')}{extension}")
    return game_path

######################################################################################################
# The following methods are used to interact with the USERS.                                         #
######################################################################################################

def authenticate_user(email: str, password: str) -> dict:
    #verifica as credenciais do usuario
    #"""Check if the provided credentials are valid."""
    database = ConnectDB()
    database.execute("SELECT email, type FROM Account WHERE email = %s AND password = %s", (email, password))
    result = database.result()
    if result is None:
        return {'success': False, 'account': {'email': None, 'type': None}}
    get_user_path(email)
    return {'success': True, 'account': {'email': result[0], 'type': result[1]}}

def log_failed_login_attempt(email: str) -> None:
    
    #tentativa de login falha
    """Log a failed login attempt."""
    pass

def update_user_password(email: str, new_password: str) -> bool:
    #altera a senha do usuario
    """Update the user's password in the database."""
    pass

def fetch_user_details(email: str) -> dict:
    #retorna o tipo do usuario
    """Fetch user details from the database."""
    database = ConnectDB()
    database.execute("SELECT email, type FROM Account WHERE email = %s", (email,))
    result = database.result()
    if result is None: return None
    return {"email": result[0], "type": result[1]}


def update_username(new_username:str, username: str, email: str) -> bool:
    
    #atualiza o nome do usuario
    
    #"""Update the user's username in the database."""
    database = ConnectDB()
    database.execute("UPDATE Gamer SET username = %s WHERE username = %s AND email = %s", (new_username, username, email))
    database.commit()
    return True

def create_user(email: str, password: str, user_type: str) -> bool:
    
    #cria um novo usuario
    
    #"""Create a user in the Account table."""
    database = ConnectDB()
    # Verificar se o email já existe
    database.execute("SELECT email FROM Account WHERE email = %s", (email,))
    if database.result():
        # Email já existe
        print("Email já existe no banco de dados.")
        return False
    # Inserir nova conta
    try:
        database.execute("INSERT INTO Account (email, password, type) VALUES (%s, %s, %s)", (email, password, user_type))
        database.commit()
        print("Conta criada com sucesso.")
        return True
    except Exception as e:
        print(f"Erro ao inserir na tabela Account: {e}")
        return False

def create_gamer(account: str, username: str, birth_date: str, country: str) -> bool:
    """Create and set gamer details in the database."""
    database = ConnectDB()
    # Verifica se a conta existe e é do tipo Gamer
    database.execute("SELECT * FROM Account WHERE email = %s AND type = 'Gamer'", (account,))
    if database.result() is None:
        print("Conta não encontrada ou não é do tipo Gamer.")
        return False
    # Verifica se o username já está em uso
    database.execute("SELECT * FROM Gamer WHERE username = %s", (username,))
    if database.result():
        print("Username já está em uso.")
        return False
    # Insere os detalhes do Gamer
    try:
        database.execute(
            "INSERT INTO Gamer (account, username, birth_date, country) VALUES (%s, %s, %s, %s)",
            (account, username, birth_date, country)
        )
        database.commit()
        print("Gamer criado com sucesso.")
        return True
    except Exception as e:
        print(f"Erro ao inserir na tabela Gamer: {e}")
        return False

def fetch_account_details(account: str) -> dict:
    """Fetch account details based on account type (Gamer or Publisher) from the database."""
    database = ConnectDB()
    # verifica o tipo de usuario no banco
    # Check the account type from the Account table
    database.execute("SELECT type FROM Account WHERE email = %s", (account,))
    account_type = database.result()
    
    if account_type is None: 
        return None
    
    # retorna os detalhes baseado no tipo // details based on account type
    if account_type[0] == 'Gamer':
        return fetch_gamer_details(account)
    
    elif account_type[0] == 'Publisher':
        return fetch_publisher_details(account)
        
    return None

def fetch_gamer_details(account: str) -> dict:
    #"""Fetch gamer details from the database."""
    database = ConnectDB()
    database.execute("SELECT * FROM Gamer WHERE account = %s", (account,))
    result = database.result()
    if result is None: return None
    return {"account": result[0], "name": result[1], "birth_date": result[2], "country": result[3], "bio": result[4]}

def count_gamers() -> int:
    #"""Count the number of gamers in the database."""
    database = ConnectDB()
    database.execute("SELECT * FROM Gamer")
    return len(database.results())

def create_publisher(account: str, name: str) -> bool:
    #"""Create and set publisher details in the database."""
    database = ConnectDB()
    # Verificar se a conta existe e é do tipo Publisher
    database.execute("SELECT * FROM Account WHERE email = %s AND type = 'Publisher'", (account,))
    if database.result() is None:
        print("Conta não encontrada ou não é do tipo Publisher.")
        return False
    # Inserir os detalhes do Publisher
    try:
        database.execute("INSERT INTO Publisher (account, name) VALUES (%s, %s)", (account, name))
        database.commit()
        print("Publisher criado com sucesso.")
        return True
    except Exception as e:
        print(f"Erro ao inserir na tabela Publisher: {e}")
        return False

def fetch_publisher_details(account: str) -> dict:
    
    #"""Fetch publisher details from the database."""
    
    database = ConnectDB()
    database.execute("SELECT * FROM Publisher WHERE account = %s", (account,))
    result = database.result()
    if result is None: return None
    return {"account": result[0], "name": result[1]}

def count_publishers() -> int:
   
    #"""Count the number of publishers in the database."""
    
    database = ConnectDB()
    database.execute("SELECT * FROM Publisher")
    return len(database.results())

def getAdmin(self, email: str) -> bool:
        """Check if the user is an admin (publisher)."""
        sql = "SELECT type FROM Account WHERE email = %s"
        self.execute(sql, (email,))
        result = self.result()
        if result and result[0] == 'Publisher':
            return True
        return False

######################################################################################################
# The following methods are used to interact with the GAME STORE.                                    #
######################################################################################################

def publish_game(title: str, publisher: str, developer: str, genre: str, description: str, cover_path: str, linux_installer_path: str, windows_installer_path: str, price: float) -> bool:
    """Publish a game in the store."""
    database = ConnectDB()
    database.execute("SELECT * FROM Publisher WHERE account = %s", (publisher,))
    if database.result() is None: return False
    database.execute("SELECT * FROM Game WHERE title = %s AND publisher = %s", (title, publisher))
    if database.result() is not None: return False
    if os.path.exists(cover_path) is False: return False
    cover = zlib.compress(open(cover_path, "rb").read())
    if linux_installer_path is not None:
        if os.path.exists(linux_installer_path) is False: return False
        linux_installer = zlib.compress(open(linux_installer_path, "rb").read())
    else: linux_installer = None
    if windows_installer_path is not None:
        if os.path.exists(windows_installer_path) is False: return False
        windows_installer = zlib.compress(open(windows_installer_path, "rb").read())
    else: windows_installer = None
    database.execute("INSERT INTO Game (title, publisher, developer, genre, description, cover, linux_installer, windows_installer, price) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)", (title, publisher, developer, genre, description, cover, linux_installer, windows_installer, price))
    database.commit()
    return True

def get_all_games() -> list:
    
    
    #"""Fetch all games from the database."""
    
    database = ConnectDB()
    database.execute("SELECT * FROM Game", ())  # Pass an empty tuple for the values argument
    return database.results()


def count_games_in_store() -> int:
    """Count the number of games in the store."""
    return len(get_all_games())


def search_in_store(query: str) -> dict:
    """Search for a game in the store by title or description."""
    database = ConnectDB()
    
    # Usamos %query% para buscar termos parciais no título ou descrição
    
    sql = """
    SELECT title, publisher, developer, genre, price 
    FROM Game 
    WHERE title LIKE %s OR description LIKE %s
    """
    search_term = f"%{query}%"
    database.execute(sql, (search_term, search_term))
    
    # Pega todos os resultados da consulta
    results = database.results()

    # Transformamos os resultados em uma lista de dicionários
    games = []
    for result in results:
        game = {
            "title": result[0],
            "publisher": result[1],
            "developer": result[2],
            "genre": result[3],
            "price": result[4]
        }
        games.append(game)

    return games


#def get_recently_added_games(limit: int = 5) -> list:
#    """Fetch recently added games from the database."""
#    pass

#def get_popular_games() -> list:
#    """Fetch popular games from the database."""
 #   pass

#def get_new_games() -> list:
 #   """Fetch new games from the database."""
#    pass

#def get_upcoming_games() -> list:
#    """Fetch upcoming games from the database."""
#    pass

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
    if platform.system() == "Linux": attribute = "linux_installer"
    elif platform.system() == "Windows": attribute = "windows_installer"
    else: return False
    database = ConnectDB()
    database.execute(f"SELECT {attribute} FROM Game WHERE title = %s AND publisher = %s", (game_title, game_publisher))
    result = database.result()
    if result is None: return False
    if result[0] is None: return False
    installer = zlib.decompress(result[0])
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
    if platform.system() == "Linux":
        print("oi")
        os.system(f"chmod +x {game_path}")
        os.system(f"{game_path}")
    elif platform.system() == "Windows": os.system(game_path)
    else: return False
    return True