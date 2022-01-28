class Laptop:
    def __init__(self,brand,model_name,price):
        print("Init method called")
        self.brand = brand
        self.model_name = model_name
        self.price = price
        self.laptop_name = brand + " " + model_name

l1 = Laptop("Hp","au114tx",63000)

print(l1.laptop_name)
