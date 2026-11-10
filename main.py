import random
from product import Product
from product_manager import ProductManager
from cart import Cart

manager = ProductManager()

produs1 = Product("Laptop Lenovo", 4000, 4)
produs2 = Product("Telefon Samsung", 2500, 5)
produs3 = Product("Mouse Logitech", 150, 15)

manager.add_product(produs1)
manager.add_product(produs2)
manager.add_product(produs3)

cart = Cart()

selected_products = random.sample(manager.products, 3)

for product in selected_products:
    cart.add_to_cart(product)

print("\nCONTINUTUL COSULUI:")
cart.display_cart()

print(f"Total de plata: {cart.calculate_total()} lei")