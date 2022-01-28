# Filter Function

# Step 1
def is_even(num):
    return num % 2 == 0

numbers = [1,2,3,4,5,6,7,8,9]


l = []
for num in numbers:
    l.append(is_even(num))

print(l)

# Step 2
evens = tuple(filter(is_even,numbers))
print(evens)

# Step 3
evens = tuple(filter(lambda num:num%2==0,numbers))
print(evens)

# Step 4
evens = [num for num in numbers if num%2==0]
print(evens)
