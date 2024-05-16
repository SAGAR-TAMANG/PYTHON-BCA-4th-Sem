class ShoppingCart:
    def __init__(self, is_member, total_amount):
        self.is_member = is_member
        self.total_amount = total_amount

    def apply_discount(self):
        if self.is_member:
            return self.total_amount * 0.1  # 10% discount for members
        else:
            return self.total_amount * 0.05  # 5% discount for non-members

    def calculate_shipping(self):
        if self.total_amount > 66:
            return 0  # Free shipping for orders above Rs 66
        else:
            # Assuming a basic shipping charge of Rs 10 for orders below Rs 66
            return 10

    def checkout(self):
        discount_amount = self.apply_discount()
        shipping_charge = self.calculate_shipping()
        final_amount = self.total_amount - discount_amount + shipping_charge
        return final_amount


# Example usage
is_member = True  # Set to True for member, False for non-member
total_amount = 80  # Total purchase amount

cart = ShoppingCart(is_member, total_amount)
final_amount = cart.checkout()

print("Final amount to pay:", final_amount)
