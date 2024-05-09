class Account:

    def __init__(self, customer):
        self.name = customer
        self.balance = 0

    def get_customer(self):
        return self.name

    def get_balance(self):
        return self.balance

    def deposit(self, sum):
        self.balance += sum

    def withdraw(self, sum):
        if self.balance - sum >= 0 and self.balance > 0:
            self.balance -= sum
            return True
        return False

    def transfer_to(self, account, sum):
        return False
