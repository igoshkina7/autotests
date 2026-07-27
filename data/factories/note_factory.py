from uuid import uuid4
from data.notes_data import NoteData
from faker import Faker

fake = Faker()


class NoteFactory:

    @staticmethod
    def create(**kwargs):
        return NoteData(
            category=kwargs.get("category", "Home"),
            completed=kwargs.get("completed", False),
            title=kwargs.get("title", f"Test note {fake.word()}"),
            description=kwargs.get(
                "description",
                f"Description {fake.sentence(nb_words=6)}"
            )
        )
    
    
