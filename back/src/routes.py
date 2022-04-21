from src.controllers.users.login_controller import LoginUserController
from src.controllers.users.register_controller import RegisterUserController

api_version = "/api/v01"

users: dict = {
   "login": f"{api_version}/login", "login_controller": LoginUserController.as_view("login"),
   "register": f"{api_version}/register", "register_controller": RegisterUserController.as_view("register"),
}
