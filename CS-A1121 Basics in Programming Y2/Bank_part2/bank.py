from personal_account import PersonalAccount
from savings_account import SavingsAccount
from account import Account


class Bank:
    def __init__(self, name):
        self.name = name
        self.customerList = []
        self.accountList = []

    def get_name(self):
        return self.name

    def get_customers(self):
        return self.customerList

    def get_customers_by_name(self, name):
        lista = []
        for x in self.customerList:
            if x.name == name:
                lista.append(x)
        return lista

    def add_customer(self, customer):
        if customer not in self.customerList:
            self.customerList.append(customer)
    """
    def add_account(self, customer):
        if customer in self.customerList:
            cc = Account(customer)
            self.accountList.append(cc)
            return cc
        return None
    """
    def get_customer_by_id(self, id):
        for cus in self.customerList:
            if cus.get_id() == id:
                return cus
        return None

    def remove_customer(self, customer):
        for cus in self.customerList:
            if cus == customer:
                self.customerList.remove(cus)

    def get_accounts(self, customer):
        lista = []
        for x in self.accountList:
            if x.get_customer() == customer:
                lista.append(x)
        return lista

    def add_savings_account(self, customer):
        if customer in self.customerList:
            cc = SavingsAccount(customer)
            self.accountList.append(cc)
            return cc
        return None

    def add_personal_account(self, customer):
        if customer in self.customerList:
            cc = PersonalAccount(customer)
            self.accountList.append(cc)
            return cc
        return None
