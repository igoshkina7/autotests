from pages.components.note_modal import NoteModal
from playwright.sync_api import expect

class NoteCard:

    def __init__(self, page, locator):
        self.page = page
        self.locator = locator

        self.title = locator.locator("[data-testid='note-card-title']")
        self.description = locator.locator("[data-testid='note-card-description']")

        self.edit_button = locator.locator("[data-testid='note-edit']")
        self.delete_button = locator.locator("[data-testid='note-delete']")
        self.view_button = locator.locator("[data-testid='note-view']")

        self.completed_checkbox = locator.locator("[data-testid='toggle-note-switch']")

    def open(self):
        self.view_button.click()

    def edit(self):
        self.edit_button.click()

        return self.get_modal()

    def delete(self):
        self.delete_button.click()

        return self.get_modal()
    
    def get_modal(self):
        modal = self.page.locator("[class='modal-content']")

        expect(modal).to_be_visible()

        return NoteModal(modal)

    def check_completed(self):
        self.completed_checkbox.check()

    def uncheck_completed(self):
        self.completed_checkbox.uncheck()

    def get_title(self):
        return self.title.text_content().strip()

    def get_description(self):
        return self.description.text_content()
    
    def is_completed(self):
        return self.completed_checkbox.is_checked()
    
    def get_title_background_color(self):
        return self.title.evaluate(
            "el => getComputedStyle(el).backgroundColor"
        )

    def get_id(self):
        href = self.view_button.get_attribute("href")
        return href.rsplit("/", 1)[-1]
        
