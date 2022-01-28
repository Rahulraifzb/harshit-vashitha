# In this video we will talk about
# Encapsulation
# Abstraction
# Some Special naming convention
# Name Mangling , __name (not a convention)

class Phone:
    def __init__(self,brand,model_name,price):
        self.brand = brand
        self.model_name = model_name
        self.__price = price

    def make_a_call(self,phone_number):
        print(f"Calling {phone_number} ...")

    def full_name(self):
        return f"{self.brand} {self.model_name}"

    def send_message(self):
        pass #twilio


# __name #convention of private name
# __name__ # dunder/magic methods

p1 = Phone("Real Me","Narzo 2022",8900)
# print(p1.__dict__)
print(phone1)