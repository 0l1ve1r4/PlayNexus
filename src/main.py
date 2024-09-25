# main.py

from login.login import Login  # Importando a classe Login
import user
import launcher

if __name__ == "__main__":
    login_instance = Login()  # Renomeei a variável para evitar conflito
    login_instance.app.mainloop()
