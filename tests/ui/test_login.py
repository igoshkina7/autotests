from playwright.sync_api import expect
import pytest
from pages.login_page import LoginPage

def test_login(logged_in):
    page = logged_in

    expect(page).to_have_url("**/inventory.html")

@pytest.mark.parametrize(
        "username, password", 
    [
        ("123456789", "secret_sauce"),
        ("standard_user", "abracadabra"),
        ("", ""),
        ("         ", "          ")
    ]
)
def test_incorrect_login(page, username, password):
    login_page = LoginPage(page)

    login_page.open()
    login_page.login(username, password)

    error = page.locator("[data-test='error']")
    expect(error).to_be_visible()

    expect(error).to_contain_text(
        "Epic sadface"
    )

