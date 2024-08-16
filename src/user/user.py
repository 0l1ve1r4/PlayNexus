class User:
    def __init__(self, name: str, email: str) -> None:    
        self.name = name
        self.email = email

    def get_name(self):
        return self.name

    def get_email(self):
        return self.email

    def __str__(self):
        return f"Name: {self.name}, Email: {self.age}"