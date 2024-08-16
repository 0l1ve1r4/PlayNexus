import login
import user
import launcher

if __name__ == "__main__":
    login = login.Login()
    login.app.mainloop()
    
    user = user.User(name=login.name_str, email=login.email_str)

    launcher = launcher.Launcher()