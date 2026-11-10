from product import Product
from product_manager import ProductManager


manager = ProductManager()

produs1 = Product("Laptop", 3500, 5)
produs2 = Product("Telefon", 2000, 3)
produs3 = Product("Mouse", 100, 20)

manager.add_product(produs1)
manager.add_product(produs2)
manager.add_product(produs3)
produs1.update_quantity(10)
print("LISTA PRODUSELOR:")
manager.display_all_products()

total = manager.calculate_total_value()

print(f"Valoarea totala a inventarului: {total} lei")