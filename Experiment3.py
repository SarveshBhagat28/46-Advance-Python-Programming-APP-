class PaymentStrategy:
    def pay(self, amount):
        pass


class CreditCard(PaymentStrategy):
    def pay(self, amount):
        print(f"Paid ₹{amount} using Credit Card")


class PayPal(PaymentStrategy):
    def pay(self, amount):
        print(f"Paid ₹{amount} using PayPal")


class UPI(PaymentStrategy):
    def pay(self, amount):
        print(f"Paid ₹{amount} using UPI")


class Payment:
    def __init__(self, strategy):
        self.strategy = strategy

    def make_payment(self, amount):
        self.strategy.pay(amount)


# Choose payment method dynamically
payment = Payment(UPI())
payment.make_payment(500)

payment = Payment(CreditCard())
payment.make_payment(1000)
