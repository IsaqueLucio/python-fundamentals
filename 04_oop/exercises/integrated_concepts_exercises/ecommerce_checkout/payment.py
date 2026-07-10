from abc import ABC, abstractmethod
from typing import override

class PaymentMethod(ABC):

    @abstractmethod
    def process_payment(self, amount: float) -> bool:
        pass

class CreditCard(PaymentMethod):

    @override
    def process_payment(self, amount: float) -> bool:
        print(f"Charging ${amount} to Credit Card...")
        return True
    
class Pix(PaymentMethod):

    @override
    def process_payment(self, amount):
        print(f"Generating Pix QR Code for ${amount}...")
        return True