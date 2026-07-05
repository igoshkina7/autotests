from pages.base_page import BasePage
from pages.components.header import Header
from pages.components.product_card import ProductCard

class CartPage(BasePage):
    def __init__(self, page):

        super().__init__(page)

        self.header = Header(page)

        self.title = page.locator("[data-test='title']")
        self.cart_items = page.locator(".cart_item")

        self.checkout_button = page.locator("[data-test='checkout']")
        self.continue_shopping = page.locator("[data-test='continue-shopping']")

    def get_items_count(self):
        return int(self.cart_items.count())
    
    def product_by_name(self, name):
        return ProductCard(
            self.cart_items.filter(has_text=name)
        )

    def product(self, index):
        return ProductCard(
            self.cart_items.nth(index)
        )
    


    
    

    
