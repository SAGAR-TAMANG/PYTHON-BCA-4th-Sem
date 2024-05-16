class Inventory:
    def __init__(self):
        self.items = {}

    def add_item(self, item_name, quantity):
        if item_name in self.items:
            self.items[item_name] += quantity
        else:
            self.items[item_name] = quantity

    def remove_item(self, item_name):
        if item_name in self.items:
            del self.items[item_name]
        else:
            print(f"{item_name} is not in the inventory.")

    def display_items(self):
        print("Inventory:")
        for item, quantity in self.items.items():
            print(f"{item}: {quantity}")

    def search_item(self, item_name):
        if item_name in self.items:
            print(f"{item_name} found in inventory.")
        else:
            print(f"{item_name} not found in inventory.")

    def update_quantity(self, item_name, new_quantity):
        if item_name in self.items:
            self.items[item_name] = new_quantity
        else:
            print(f"{item_name} is not in the inventory.")

# Example Usage
inventory = Inventory()

# Add items
inventory.add_item("Apple", 10)
inventory.add_item("Banana", 5)
inventory.add_item("Orange", 8)

# Remove an item
inventory.remove_item("Banana")

# Display items
inventory.display_items()

# Search for an item
inventory.search_item("Apple")

# Update quantity of an item
inventory.update_quantity("Orange", 15)

# Display updated items
inventory.display_items()
