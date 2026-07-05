from pages.inventory_page import InventoryPage
from playwright.sync_api import expect
import re
from pages.cart_page import CartPage

def test_cart_title(empty_cart):
    page = empty_cart
    cart_page = CartPage(page)

    expect(cart_page.title).to_have_text("Your Cart")

def test_cart_elements_visible(cart_with_one_item):
    page, item = cart_with_one_item

    cart_page = CartPage(page)

    assert cart_page.get_items_count() > 0

    expect(cart_page.continue_shopping).to_be_visible()
    expect(cart_page.checkout_button).to_be_visible()

    product = cart_page.product(0)

    assert product.name() == item["name"]
    assert product.price() == item["price"]

def test_continue_shopping(empty_cart):
    page = empty_cart
    cart_page = CartPage(page)

    cart_page.continue_shopping.click()

    cart_page.wait_url(re.compile(r".*/inventory\.html"))

def test_checkout_navigation(empty_cart):
    page = empty_cart
    cart_page = CartPage(page)

    cart_page.checkout_button.click()

    cart_page.wait_url(re.compile(r".*/checkout-step-one\.html"))

def test_remove_product_from_cart(cart_with_one_item):
    page, item = cart_with_one_item

    cart_page = CartPage(page)

    old_count = cart_page.header.get_cart_count()
    old_items = cart_page.get_items_count()

    product = cart_page.product_by_name(item["name"])

    product.remove()

    new_count = cart_page.header.get_cart_count()
    new_items = cart_page.get_items_count()

    assert new_count == old_count - 1
    assert new_items == old_items - 1

def test_added_product_data(cart_with_one_item):
    page, item = cart_with_one_item

    cart_page = CartPage(page)

    product = cart_page.product(0)

    assert product.name() == item["name"]
    assert product.price() == item["price"]

def test_removed_product(cart_with_two_items):
    page, items = cart_with_two_items

    cart_page = CartPage(page)

    old_count = cart_page.header.get_cart_count()
    old_items = cart_page.get_items_count()

    removed_product = cart_page.product_by_name(
        items[0]["name"]
    )

    removed_product.remove()

    new_count = cart_page.header.get_cart_count()
    new_items = cart_page.get_items_count()

    assert new_count == old_count - 1
    assert new_items == old_items - 1

    cart_page.continue_shopping.click()

    inventory_page = InventoryPage(page)

    inventory_page.wait_url(
        re.compile(r".*/inventory\.html")
    )

    product = inventory_page.product_by_name(
        items[0]["name"]
    )

    expect(product.root.locator(
        "[data-test^='add-to-cart']")
    ).to_be_visible()

def test_empty_cart(empty_cart):
    page = empty_cart
    cart_page = CartPage(page)

    cart_page.wait_url(re.compile(r".*/cart\.html"))

    assert cart_page.header.get_cart_count() == 0
    assert cart_page.get_items_count() == 0

    

