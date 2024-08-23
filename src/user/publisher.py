from user import User

class Publisher(User):
    def __init__(self, name: str, email: str, password: str,
                 publisher_name: str) -> None:
        super().__init__(name, email, password)
        self.name = publisher_name

    def get_publisher_name(self) -> str:
        return self.name
    
    def set_publisher_name(self, new_name: str) -> None:
        self.name = new_name