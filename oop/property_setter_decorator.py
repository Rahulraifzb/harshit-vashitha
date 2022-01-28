# will discuss three probles in existing
# then we eill solve them using getter,setter decorator

class Phone:
    def __init__(self,brand,model_name,price):
        self.brand = brand
        self.model_name = model_name
        self._price = max(price,0)

    @property
    def complete_specification(self):
        return f"{self.brand} {self.model_name} and price {self._price}" 

    @property
    def price(self):
        return self._price

    @price.setter
    def price(self,new_price):
        self._price = max(new_price,0)

    def make_a_call(self,phone_number):
        print(f"calling {phone_number} ...")

    def full_name(self):
        return f"{self.brand} {self.model_name}"

phone1 = Phone("Nokia","1100",-1000)
print(phone1.brand)
print(phone1.model_name)
phone1.price = -1300
print(phone1.__dict__)

print(phone1.complete_specification)