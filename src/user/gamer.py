from user import User

class Gamer(User):
    def __init__(self, name: str, email: str, password: str, 
                 username: str, birthday: str, nationality: str) -> None:
        super().__init__(name, email, password)
        self._username = username
        self._birthday = birthday
        self._nationality = nationality

    def get_username(self) -> str:
        return self._username

    def set_username(self, username: str) -> None:
        self._username = username

    def get_birthday(self) -> str:
        return self._birthday

    def set_birthday(self, birthday: str) -> None:
        self._birthday = birthday

    def get_nationality(self) -> str:
        return self._nationality

    def set_nationality(self, nationality: str) -> None:
        self._nationality = nationality