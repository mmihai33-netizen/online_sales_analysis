from cart import Cart
import random
from product import Product
from product_manager import ProductManager


manager = ProductManager()

produs1 = Product("Laptop", 3500, 5)
produs2 = Product("Telefon", 2000, 3)
produs3 = Product("Mouse", 100, 20)

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

print("LISTA PRODUSELOR:")
manager.display_all_products()

total = manager.calculate_total_value()

print(f"Valoarea totala a inventarului: {total} lei")