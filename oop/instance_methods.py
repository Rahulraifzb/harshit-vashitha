# instance methods

class Person:
    def __init__(self,first_name,last_name,age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def full_name(self):
        return f"{self.first_name} {self.last_name}"

    def is_above_18(self):
        return self.age > 18

p1 = Person("Rahul","Rai",19)
p2 = Person("Satyam","Rai",18)

# print(p1.full_name())
# print(p1.is_above_18())

l = [1,2,3,4,5,6]
# clear,pop
# l.clear()

# list.clear(l)
# l.append(12)
list.append(l,10)
print(l)