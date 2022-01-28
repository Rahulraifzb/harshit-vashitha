class Laptop:
    discount_price = 10
    def __init__(self,brand,model_name,price):
        self.brand = brand
        self.model_name = model_name
        self.price = price
        self.laptop_name = brand + " " + model_name

    def apply_discount(self):
        off_price = (self.discount_price/100)*self.price
        return self.price - off_price

laptop1 = Laptop("Hp","au114tx",63000)
laptop2 = Laptop("Apple","Macbook Pro",200000)
laptop2.discount_price = 30
print(laptop2.apply_discount())