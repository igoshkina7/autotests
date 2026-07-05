from pages.base_page import BasePage

class LoginPage(BasePage):
    def __init__(self, page):
        super().__init__(page)

        self.username = page.locator("[data-test='username']")

        self.password = page.locator("[data-test='password']")

        self.login_button = page.locator("[data-test='login-button']")

    def open(self):
       self.page.goto("https://www.saucedemo.com/")

    def login(self, username, password):
        self.username.fill(username)
        self.password.fill(password)

        self.login_button.click()
