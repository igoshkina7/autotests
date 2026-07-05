from playwright.sync_api import expect
import re
from pages.inventory_page import InventoryPage
import random

def test_inventory_title(logged_in):
    page = logged_in
    inventory_page = InventoryPage(page)

    inventory_page.wait_url(re.compile(r".*/inventory\.html"))
   
    expect(inventory_page.title).to_have_text("Products")

def test_add_products(logged_in):
    page = logged_in
    inventory_page = InventoryPage(page)

    inventory_page.wait_url(
        re.compile(r".*/inventory\.html")
    )

    old_count = inventory_page.header.get_cart_count()

    products = []

    count = random.randint(1, 6)
    print(f"Products count: {count}")

    for i in range(count):
        product = inventory_page.product(i)

        products.append({
            "name": product.name(),
            "price": product.price()
        })

        product.add()

    new_count = inventory_page.header.get_cart_count()

    assert new_count == old_count + count

def test_remove_product(logged_in):
    page = logged_in
    inventory_page = InventoryPage(page)

    inventory_page.wait_url(
        re.compile(r".*/inventory\.html")
    )

    product = inventory_page.product_by_name(
        "Sauce Labs Backpack"
    )

    product.add()

    assert inventory_page.header.get_cart_count() == 1

    product.remove()

    assert inventory_page.header.get_cart_count() == 0
