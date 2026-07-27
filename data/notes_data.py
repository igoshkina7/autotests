from dataclasses import dataclass

@dataclass
class NoteData:
    category: str = "Home"
    completed: bool = False
    title: str = ""
    description: str = ""

