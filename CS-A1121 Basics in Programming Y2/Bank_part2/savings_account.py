from account import Account


class SavingsAccount(Account):

    def __init__(self, customer):
        super().__init__(customer)

    def transfer_to(self, account, sum):
        if self.name == account.get_customer():
            if self.withdraw(sum) is True:
                account.deposit(sum)
                return True
            else:
                return False
        else:
            return False

