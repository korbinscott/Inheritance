class Person:
    def __init__(self, name, address, phone):
        self.name = name
        self.address = address
        self.phone = phone

    def get_name(self):
        return self.name

    def get_address(self):
        return self.address

    def get_phone_number(self):
        return self.phone

    def print_person(self):
        print("Name:", self.name)
        print("Addr:", self.address)
        print("Phone:", self.phone)


class Customer(Person):
    def __init__(self, name, address, phone, cust_number, on_list):
        Person.__init__(self, name, address, phone)

        self.cust_number = cust_number
        self.on_list = on_list

    def print_person(self):
        print("Name:", self.name)
        print("Addr:", self.address)
        print("Phone:", self.phone)
        print("Customer Number:", self.cust_number)
        if self.on_list:
            print("On Mailing List: Yes")
        else:
            print("On Mailing List: No")
