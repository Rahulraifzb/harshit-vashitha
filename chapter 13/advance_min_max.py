# advance min() and max()

numbers = [1,2,3,4,5]

# It will return the maximum value of the numbers list.
# print(max(numbers))

# It will return the minimum value of the numbers list.
# print(min(numbers))

names = ["abcd","efg","hi"]
print(max(names,key=lambda name:len(name)))
print(min(names,key=lambda name:len(name)))

students1 = [
    {"name":"harshit","score":90,"age":24},
    {"name":"rahul","score":85,"age":19},
    {"name":"mansi","score":83,"age":83},
]

# print(max(students1,key=lambda student:student.get("score")).get("name"))

students2 = {
    "harshit":{"score":87,"age":26},
    "rahul":{"score":85,"age":19},
    "mansi":{"score":83,"age":18},
}

print(max(students2,key=lambda student:students2[student]["score"]))