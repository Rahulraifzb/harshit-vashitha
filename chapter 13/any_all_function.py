number1 = [2,4,6,8,10]
number2 = [1,2,3,4,5]

# Step 1
evens = []
for num in number1:
    evens.append(num%2==0)

print(all(evens))


# Step 2

def find_evens(numbers):
    return all([number for number in numbers if number%2==0])

print(find_evens(number1))


all_evens = lambda numbers:all([number for number in numbers if number %2==0])
print(all_evens(number1))

any_evens = lambda numbers:any([number for number in numbers if number %2==0])
print(any_evens(number1))