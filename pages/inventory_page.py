from pages.base_page import BasePage
from pages.components.product_card import ProductCard
from pages.components.header import Header

class InventoryPage(BasePage):
    def __init__(self, page):
        super().__init__(page)

        self.header = Header(page)

        self.title = page.locator("[data-test='title']")
        self.products = page.locator(".inventory_item")

       
    def open_cart(self):
        self.header.open_cart()

    def product_by_name(self, name):
        return ProductCard(
            self.products
            .filter(has_text=name)
        )
    
    def product(self, index):
        return ProductCard(
            self.products.nth(index)
        )

    



    

    