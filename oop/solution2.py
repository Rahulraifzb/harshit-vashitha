class Laptop:
    def __init__(self,brand,model_name,price):
        self.brand = brand
        self.model_name = model_name
        self.price = price
        self.laptop_name = brand + " " + model_name

    def apply_discount(self,percentage):
        off_price = self.price * (percentage/100)
        return self.price - off_price

l1 = Laptop("Hp","au114tx",63000)
l2 = Laptop("Apple","maxbook pro",1000)
print(l2.apply_discount(30))