# OBJECTIVES
# What IS CLASS
# HOW TO CREATE AN CLASS
# WHAT IS INIT METHOD,constructor
# WHAT ARE ATTRIBUTES INSTANCE VARIABLES
# HOW TO CREATE OUR OBJECT

class Person:
    def __init__(self,first_name,last_name,age):
        # instance variables
        print("Init method // constructor get called")
        self.first_name = first_name
        self.last_name = last_name
        self.age = age


p1 = Person("Rahul","Rai",19)
p2 = Person("Mansi","Rai",19)

print(p1.first_name)

