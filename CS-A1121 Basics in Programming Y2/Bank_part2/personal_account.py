from account import Account


class PersonalAccount(Account):

    def __init__(self, customer):
        super().__init__(customer)

    def transfer_to(self, account, sum):
        if self.withdraw(sum) is True:
            account.deposit(sum)
            return True
        return False
