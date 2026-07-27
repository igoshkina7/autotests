from api.base_client import BaseClient
from api.endpoints import PROFILE, DELETE_ACCOUNT

class UsersClient(BaseClient):

    def get_profile(self):
        return self.get(PROFILE)
    
    def update_profile(self, data):
        return self.patch(
            PROFILE,
            json = data
        )
    
    def delete_account(self):
        return self.delete(DELETE_ACCOUNT)
