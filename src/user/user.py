class User:
    def __init__(self, name: str, email: str, password: str) -> None:    
        self.name = name
        self.email = email
        self.password = password

    def get_user_name(self) -> str:
        return self.name

    def set_user_name(self, new_name: str) -> None:
        self.name = new_name

    def get_user_email(self) -> str:
        return self.email
    
    def set_user_email(self, new_email: str) -> None:
        self.email = new_email    

    def get_user_password(self) -> str:
        return self.password

    def set_user_password(self, new_password: str) -> None:
        self.password = new_password   