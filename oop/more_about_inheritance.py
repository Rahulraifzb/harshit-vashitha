# can we derive more than one class from base class
# multilevel inheritance
# method resolution order
# method overriding
# isinstance(),issubclass()

class Phone:
    discount_percentage = 10
    def __init__(self,brand,model_name,price):
        self.brand = brand
        self.model_name = model_name
        self._price = max(price,0)

    @property
    def complete_specification(self):
        return f"{self.brand} {self.model_name} and price {self._price}"

    def apply_discount(self):
        off_price = self._price * (self.discount_percentage / 100)
        return self._price - off_price

    def make_a_class(self,number):
        print(f"Calling {number}...")

    def full_name(self):
        return f"{self.brand} {self.model_name}"

    @property
    def price(self):
        return self._price 
    
    @price.setter
    def price(self,new_price):
        self._price = max(new_price,0)

class SmartPhone(Phone):
    def __init__(self,brand,model_name,price,ram,internal_memory,rear_camera):
        #two 
        # Phone.__init__(self,brand,model_name,price) #uncommon way
        super().__init__(brand,model_name,price)
        self.ram = ram
        self.internal_memory = internal_memory
        self.rear_camera = rear_camera

class FlagshipPhone(SmartPhone):
    def __init__(self,brand,model_name,price,ram,internal_memory,rear_camera,front_camera,refresh_rate):
        #three
        # SmartPhone.__init__(self,brand,model_name,price,ram,internal_memory,rear_camera) #uncommon way

        super().__init__(brand,model_name,price,ram,internal_memory,rear_camera)

        self.front_camera = front_camera
        self.refresh_rate = refresh_rate


phone1 = Phone("Nokia","1100",-1000)
oneplus5 = SmartPhone("OnePlus","6",30000,"6 GB","64 GB","20 MP")
oneplus5t = FlagshipPhone("Realme","narzo 30",38000,"8 GB","124 GB","56 MP","32 MP","120 HZ")
# print(help(FlagshipPhone))


# print(isinstance(oneplus5t,FlagshipPhone))

print(issubclass(FlagshipPhone, SmartPhone))

