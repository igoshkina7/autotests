from api.base_client import BaseClient
from api.endpoints import LOGIN, REGISTER, LOGOUT, FORGOT_PASSWORD, RESET_PASSWORD, VERIFY_RESET_PASSWORD, CHANGE_PASSWORD

class AuthClient(BaseClient):

    # def __init__(self, api_session):
    #     super().__init__(api_session)

    def login(self, email, password):
        response = self.post(
            LOGIN,
            json = {
                "email": email, #string
                "password": password #stirng
            }                 
            )
        
        response.raise_for_status()

        token = response.json()["data"]["token"]

        self.session.headers.update(
            {
                "x-auth-token": token
            }
        )

        return token

    def register(self, name, email, password):
        response = self.post(
            REGISTER,
            json = {
                "name": name, #sting
                "email": email, #string
                "password": password #stirng
            }                 
        )

        return response
    
    def logout(self):
        response = self.delete(
            LOGOUT           
        )

        self.session.headers.pop(
                "x-auth-token",
                None
            )

        return response

    def forgot_password(self, email):
        response = self.post(
            FORGOT_PASSWORD,
            json = {
                "email": email #string
            }                 
        )

        return response
        
    def reset_password(self, token, new_password):
        response = self.post(
            RESET_PASSWORD,
            json = {
                "token": token, #string
                "newPassword": new_password #string
            }                 
        )

        return response

    def verify_reset_password_token(self, token):
        response = self.post(
            VERIFY_RESET_PASSWORD,
            json = {
                "token": token #string
            }                 
        )

        return response


    def change_password(self, current_password, new_password):
        response = self.post(
            CHANGE_PASSWORD,
            json = {
                "currentPassword": current_password, #stirng
                "newPassword": new_password #string
            }                 
        )

        return response