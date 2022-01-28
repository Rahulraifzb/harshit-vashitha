
numbers = [1,2,3,4,5,6,7,8]

# Step 1
def square(a):
    return a ** 2

l = []
for num in numbers:
    l.append(square(num))

print(l)

# Step 2
print(list(map(lambda a:a ** 2,numbers)))

# Step 3
print([i ** 2 for i in numbers])

names = ["abc","abcd","abcde"]

length = list(map(len,names))
print(length)



