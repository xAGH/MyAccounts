from src.controllers.users.login_controller import LoginController

version = "/api/v01"

users: dict = {
   "index": "/", "index_controller": LoginController.as_view("index")
}
