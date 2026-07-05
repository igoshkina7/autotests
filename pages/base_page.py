from playwright.sync_api import expect

class BasePage:
    def __init__(self, page):
        self.page = page

    def wait_url(self, pattern):
        expect(self.page).to_have_url(pattern)

    