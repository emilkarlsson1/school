class Employee:
    BASE_BONUS = 200

    # The method initializes a new employee object
    # The name, id and starting salary of the employee
    # are given as parameters
    def __init__(self, name, employee_id, salary):
        self.__name = name
        self.__id = employee_id
        self.__salary = salary
        self.__bonus = 0

    # The method returns the name of the employee
    def get_name(self):
        return self.__name

    # The method returns the id of the employee
    def get_id(self):
        return self.__id

    # The method returns the salary of the employee
    def get_salary(self):
        return self.__salary

    # The method returns the bonus of the employee
    def get_bonus(self):
        return self.__bonus

    # The method changes the salary of the employee
    def change_salary(self, new_salary):
        kasi = 1.08 * self.__salary
        if self.__salary <= new_salary <= kasi:
            self.__salary = new_salary
        else:
            self.__salary = self.__salary

            # The method calculates and sets the bonus of the employee based on
    # The constant BASE_BONUS and the bonus coefficient given
    # as a parameter
    def calculate_and_set_bonus(self, bonus_coefficient):

        if self.__salary >= 3000:
            b = 0.1 * self.__salary
        else:
            b = 0.07 * self.__salary
        bonus = b * bonus_coefficient
        self.__bonus = bonus

    # The method returns a string representation of the information
    # of the employee
    def __str__(self):
        info = "{:s} (employee id: {:d})\n".format(self.__name, self.__id)
        info += "Salary: {:.2f}\n".format(self.__salary)
        info += "Bonus: {:.2f}\n".format(self.__bonus)
        return info

