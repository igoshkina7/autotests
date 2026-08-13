import pytest
from core.api_client import APIClient
from config.config import BASE_API_URL, BASE_URL
from playwright.sync_api import sync_playwright
import requests
from api.clients.auth_client import AuthClient
from api.clients.notes_client import NotesClient
from pages.notes_page import NotesPage
import os
from data.factories.user_factory import UserFactory

@pytest.fixture
def test_user(auth_client):
    user = UserFactory.create()

    response = auth_client.register(**user)
    assert response.status_code == 201

    yield user

    auth_client.login(
        user["email"],
        user["password"]
    )

@pytest.fixture()
def api_session():
    return requests.Session()

@pytest.fixture
def auth_client(api_session):
    return AuthClient(api_session)

@pytest.fixture
def notes_client(api_session):
    return NotesClient(api_session)

@pytest.fixture
def authorized_page(page, auth_client, test_user):
    token = auth_client.login(
        test_user["email"],
        test_user["password"]
    )

    page.add_init_script(
        f"""
        localStorage.setItem(
            "token",
            "{token}"
        )
        """
    )

    page.goto(BASE_URL, wait_until="domcontentloaded")

    return page

@pytest.fixture
def notes(authorized_page):
    return NotesPage(authorized_page)

@pytest.fixture(scope="session")
def api():
    return APIClient(BASE_API_URL)

@pytest.fixture
def page(request):
    with sync_playwright() as p:

        headless = os.getenv("HEADLESS", "false").lower() == "true"

        browser = p.chromium.launch(
            headless=headless
        )

        context = browser.new_context()

        context.tracing.start(
            screenshots=True,
            snapshots=True,
            sources=True
        )

        page = context.new_page()

        yield page

        report = getattr(request.node, "rep_call", None)
        
        if report and report.failed:
            context.tracing.stop(
                path=f"artifacts/traces/{request.node.name}.zip"
            )
        else:
            context.tracing.stop()

        browser.close()

# @pytest.fixture
# def logged_in(page):
#     login_page = LoginPage(page)

#     login_page.open()
#     login_page.login("standard_user", "secret_sauce")

#     login_page.wait_url(re.compile(r".*/inventory\.html"))
    
#     return page

# @pytest.fixture
# def cart_with_one_item(logged_in):
#     page = logged_in
#     inventory_page = InventoryPage(page)

#     old_count = inventory_page.header.get_cart_count()

#     product = inventory_page.product_by_name("Sauce Labs Backpack")

#     name = product.name()
#     price = product.price()

#     product.add()

#     new_count = inventory_page.header.get_cart_count()

#     assert new_count == old_count + 1

#     inventory_page.open_cart()

#     inventory_page.wait_url(re.compile(r".*/cart\.html"))

#     return page, {
#         "name": name,
#         "price": price
#     }

# @pytest.fixture
# def empty_cart(logged_in):
#     page = logged_in
#     inventory_page = InventoryPage(page)

#     inventory_page.open_cart()
    
#     inventory_page.wait_url(re.compile(r".*/cart\.html"))

#     return page

# @pytest.fixture
# def cart_with_two_items(logged_in):
#     page = logged_in
#     inventory_page = InventoryPage(page)

#     old_count = inventory_page.header.get_cart_count()

#     products = []

#     for i in range(2):
#         product = inventory_page.product(i)

#         products.append({
#             "name": product.name(),
#             "price": product.price()
#         })

#         product.add()

#     new_count = inventory_page.header.get_cart_count()

#     assert new_count == old_count + 2

#     inventory_page.open_cart()
#     inventory_page.wait_url(
#         re.compile(r".*/cart\.html")
#     )

#     return page, products

@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
        
    outcome = yield

    report = outcome.get_result()

    if report.when == "call":
        setattr(item, "rep_call", report)



