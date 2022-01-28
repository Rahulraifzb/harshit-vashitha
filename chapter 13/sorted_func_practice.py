from django.urls import reverse


fruits1 = ["grapes","mango","apple"]

# sort() method

# fruits1.sort()
# print(fruits1)

fruits2 = ["grapes","pineapple","apple"]
print(sorted(fruits2))

print(sorted(fruits2,key=lambda fruit:len(fruit),reverse=True))


fruits3 = {"grapes","mango","apple"}
print(sorted(fruits3))


guitars = [
    {"model":"Yamaha f310","price":8400},
    {"model":"faith naptune","price":50000},
    {"model":"faith apollo venus","price":35000},
    {"model":"taylor 814ce","price":450000}
]

print(sorted(guitars,key=lambda guitar:guitar.get("price"),reverse=True))