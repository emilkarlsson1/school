class Customer:
    id_counter = 0

    def __init__(self, name):
        self.name = name
        self.__id = Customer.id_counter
        Customer.id_counter += 1

    def get_id(self):
        return self.__id


