class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price

class Cart:
    def __init__(self):
        self.items = []

    def add(self, product):
        self.items.append(product)

    def total(self):
        return sum(item.price for item in self.items)  

# Creating Object
cart = Cart()
cart.add(Product("Phone", 500))
cart.add(Product("Charger", 50))
print("Total:", cart.total())
