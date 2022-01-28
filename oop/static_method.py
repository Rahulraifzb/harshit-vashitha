# class method as a constructor

class Person:
    count_instance = 0

    def __init__(self,first_name,last_name,age):
        print("Init method called")
        Person.count_instance += 1

        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    @classmethod
    def from_string(cls,string):
        first_name,last_name,age = string.split(",")
        return cls(first_name,last_name,age)

    @classmethod
    def count_instances(cls):
        return f"You have created {cls.count_instance} instances of {cls.__name__}"

    @staticmethod
    def hello():
        print("Hello,static method called")

    def full_name(self):
        return f"{self.first_name} {self.last_name}"

    def is_above_18(self):
        return self.age > 18

# p1 = Person("Harshit","vashitha",18)
# p2 = Person("Rahul","Rai",19)

p3 = Person.from_string("Rahul,Rai,18")
Person.hello()

