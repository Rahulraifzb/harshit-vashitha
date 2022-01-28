# special magic methods / dunder methods

# operator overloading

# polymorphism

class Phone:
    def __init__(self,brand,model_name,price):
        self.brand = brand
        self.model_name = model_name
        self.price = price

    def phone_name(self):
        return f"{self.brand} {self.model_name}"

    # str , repr
    def __str__(self):
        return f"{self.brand} {self.model_name} and price is {self.price}"

    def __repr__(self):
        return f"phone(\'{self.brand}\',\'{self.model_name}\',{self.price})"

    def __len__(self):
        return len(self.phone_name())

    def __add__(self,other):
        return self.price + other.price

phone1 = Phone('Nokia',"1100",1000)
phone2 = Phone('Samsung',"Guru",900)

# print(repr(phone1))
# print(len(phone1))
# print(phone1.__repr__())
print(phone1 + phone2)