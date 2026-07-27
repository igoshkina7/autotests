from playwright.sync_api import expect
from data.notes_data import NoteData

class NoteModal:

    def __init__(self, locator):
        self.locator = locator 

        self.submit_button = locator.locator("[data-testid='note-submit']")

        self.delete_button = locator.locator("[data-testid='note-delete-confirm']")

        self.cancel_button = locator.locator("[class='btn btn-secondary']")

        self.description = locator.locator("[data-testid='note-description']")

        self.title = locator.locator("[data-testid='note-title']")

        self.category = locator.locator("[data-testid='note-category']")

        self.completed_checkbox = locator.locator("[data-testid='note-completed']")

    def fill_form(self, note: NoteData):
        self.category.select_option(note.category)

        if note.completed:
            self.completed_checkbox.check()
        else:
            self.completed_checkbox.uncheck()

        self.title.fill(note.title)
        self.description.fill(note.description)

    def submit(self):
        self.submit_button.click()

        expect(self.locator).not_to_be_visible()

    def cancel(self):
        self.cancel_button.click()

        expect(self.locator).not_to_be_visible()

    def delete(self):
        self.delete_button.click()

        expect(self.locator).not_to_be_visible()
    