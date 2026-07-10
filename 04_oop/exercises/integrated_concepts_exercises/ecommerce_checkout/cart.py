from payment import PaymentMethod

class ShoppingCart:

    def __init__(self):
        self.items = []
        self.total = 0.0
        self.purchase_history = []


    def add_item(self, name: str, price: float):
        new_item = {}
        new_item[name] = price
        self.total += price
        self.items.append(new_item)

    def checkout(self, payment_method: PaymentMethod) -> bool:
        payment_method.process_payment(self.total)
        self.purchase_history.append(self.items.copy())
        self.items.clear()
        print("Checkout complete!")
        return True
        
    def get_cart(self):
        if not self.items:
            return "The cart is empty; add items to it and try again."
        else:
            print("\n--- Your Cart ---")
            result = []
            for item in self.items:
                for name, price in item.items():
                    result.append(f"{name}: ${price:.2f}")
            return "\n".join(result) + f"\n-----------------\nTotal: ${
                self.total:.2f}\n-----------------\n"
            
    
    def get_history(self):
        if not self.purchase_history:
            return "The purchase history is empty; buy some items and try again."
        result = []
        print("\n--- Your Purchase History ---")
        for i, purchase in enumerate(self.purchase_history, start=1):
            result.append(f"\nPurchase {i}:")
            for item in purchase:
                for name, price in item.items():
                    result.append(f"  {name}: ${price:.2f}")
            result.append("")
        return "\n".join(result) + "\n----------------------------"