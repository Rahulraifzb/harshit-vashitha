class Laptop:
    def __init__(self,brand,model_name,price):
        # instance variables

        self.brand = brand
        self.model_name = model_name
        self.price = price
        self.laptop_name = brand + " " + model_name


laptop1 = Laptop("Hp","au114tx",63000)
# laptop1.apply_discount(40)