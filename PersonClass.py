class Person:
    def __init__(self, name, address, phone):
        self.__name = name
        self.__address = address
        self.__phone = phone

    def print_person(self):
        print()


class Customer(Person):
    def __init__(self):
        Person.__init__(self, "Customer")
        Person.__init__
