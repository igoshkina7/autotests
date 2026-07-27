from api.base_client import BaseClient
from api.endpoints import NOTES

class NotesClient(BaseClient):

    # def __init__(self, session):
    #     super().__init__(session)

    def create_note(self, data):
        response = self.post(
            NOTES,
            json = data
        )

        return response

    def get_note(self, note_id):
        response = self.get(
            f"{NOTES}/{note_id}"
        )

        return response

    def get_notes(self):
        response = self.get(
            NOTES
        )

        return response.json()["data"]

    def update_note(self, note_id, data):
        response = self.put(
            f"{NOTES}/{note_id}",
            json = data
        )

        return response

    def delete_note(self, note_id):
        response = self.delete(
            f"{NOTES}/{note_id}"
        )
        
        return response
    
    def completed_note(self, note_id, data):
        response = self.patch(
            f"{NOTES}/{note_id}",
            json = data
        )

        return response