from product import Product
from product_manager import ProductManager


manager = ProductManager()

produs1 = Product("Laptop Lenovo", 4000, 4)
produs2 = Product("Telefon Samsung", 2500, 5)
produs3 = Product("Mouse Logitech", 150, 15)

manager.add_product(produs1)
manager.add_product(produs2)
manager.add_product(produs3)
produs1.update_quantity(10)
