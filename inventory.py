from datetime import datetime

class Product:
    def __init__(self, product_id, name, quantity_in_stock):
        self.product_id = product_id
        self.name = name
        self.quantity_in_stock = quantity_in_stock
    
    def calculate_value(self):
        pass

class SimpleProduct(Product):
    def __init__(self, product_id, name, quantity_in_stock, unit_price):
        super().__init__(product_id, name, quantity_in_stock)
        self.unit_price = unit_price
    
    def calculate_value(self):
        return self.quantity_in_stock * self.unit_price

class PerishableProduct(Product):
    def __init__(self, product_id, name, quantity_in_stock, unit_price, expiry_date):
        super().__init__(product_id, name, quantity_in_stock)
        self.unit_price = unit_price
        self.expiry_date = expiry_date
    
    def calculate_value(self):
        remaining_shelf_life = (self.expiry_date - datetime.now()).days
        if remaining_shelf_life > 0:
            discount_factor = remaining_shelf_life / 365 
            return self.quantity_in_stock * self.unit_price * discount_factor
        else:
            return 0

class DigitalProduct(Product):
    def __init__(self, product_id, name, quantity_in_stock, price):
        super().__init__(product_id, name, quantity_in_stock)
        self.price = price
    
    def calculate_value(self):
        return self.quantity_in_stock * self.price

if __name__ == "__main__":
    simple_product = SimpleProduct(1, "Book", 10, 20)
    perishable_product = PerishableProduct(2, "Milk", 20, 2, datetime(2024, 3, 15))
    digital_product = DigitalProduct(3, "E-book", 100, 5)

    print("Total value of Simple Product:", simple_product.calculate_value())
    print("Total value of Perishable Product:", perishable_product.calculate_value())
    print("Total value of Digital Product:", digital_product.calculate_value())
