from src.controllers.users.auth_controller import RegisterUserController, LoginUserController

api_version = "/api/v01"

users: dict = {
   "login": f"{api_version}/login", "login_controller": LoginUserController.as_view("login"),
   "register": f"{api_version}/register", "register_controller": RegisterUserController.as_view("register"),
}
