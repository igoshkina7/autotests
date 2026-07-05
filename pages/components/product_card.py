class ProductCard:
    def __init__(self, root):
        self.root = root

    def name(self):
        return self.root.locator("[data-test='inventory-item-name']").inner_text()
    
    def price(self):
        return self.root.locator("[data-test='inventory-item-price']").inner_text()

    def add(self):
        self.root.locator("[data-test^='add-to-cart']").click()
    
    def remove(self):
        self.root.locator("[data-test^='remove']").click()