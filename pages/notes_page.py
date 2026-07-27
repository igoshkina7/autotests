from pages.base_page import BasePage
from pages.components.note_card import NoteCard
from pages.components.note_modal import NoteModal
from playwright.sync_api import expect
import re

class NotesPage(BasePage):

    def __init__(self, page):

        super().__init__(page)

        self.add_note_button = page.locator("[data-testid='add-new-note']")

        self.search_input = page.locator("[data-testid='search-input']")

        self.search_button = page.locator("#search-btn")

        self.progress_label = page.locator("[data-testid='progress-info']")

        self.notes = page.locator("[data-testid='note-card']")

    def get_notes(self):
        cards=[]

        for i in range(self.notes.count()):
            cards.append(
                NoteCard(
                    self.page,
                    self.notes.nth(i)
                )
            )
        
        return cards

    def get_note_by_title(self, title):
        for note in self.get_notes():
            if note.get_title() == title:
                return note
        
        return None

    def open_create_form(self):
        self.add_note_button.click()

        modal = self.page.locator("[class='modal-content']")

        expect(modal).to_be_visible()

        return NoteModal(modal)
    
    def search(self, text):
        self.search_input.fill(text)
        self.search_button.click()

    def filter_by_category(self, category):
        self.page.locator(f"[data-testid='category-{category}']").click()

    def get_notes_count(self):
        return self.notes.count()
    
    def wait_notes_loaded(self):
        expect(self.notes.first).to_be_visible(timeout=5000)

    def get_note_by_id(self, note_id):
        card = self.page.locator(
            f'[data-testid="note-view"][href="/notes/app/notes/{note_id}"]'
        ).locator("xpath=ancestor::div[@data-testid='note-card']")

        return NoteCard(self.page, card)
    
    def get_completed_count(self):
        text = self.progress_label.text_content()

        return int(re.search(r"(\d+)/", text).group(1))
    
    def create_note(self, data):
        modal = self.open_create_form()
        modal.fill_form(data)
        modal.submit()
        self.wait_notes_loaded()

    def reload(self):
        self.page.reload()
        self.wait_notes_loaded()