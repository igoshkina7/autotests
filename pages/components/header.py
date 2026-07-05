class Header():
    def __init__(self, page):
        self.page = page

        self.cart_link = page.locator("[data-test='shopping-cart-link']")
        
        self.cart_badge = page.locator("[data-test='shopping-cart-badge']")

    def get_cart_count(self):
        if self.cart_badge.count() == 0:
            return 0

        return int(self.cart_badge.inner_text())
    
    def open_cart(self):
        self.cart_link.click()