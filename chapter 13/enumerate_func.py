# We use enumerate function with for loop to track the position of item in iterable

# How we can do this without enumerate function

names = ["Rahul","Mansi","Satyam"]
pos = 0
for name in names:
    print(f"{pos} ------> {name}")
    pos += 1

# with enumerate function
for pos,name in enumerate(names):
    print(f"{pos} ------> {name}")

def find_pos(l,target):
    for index,name in enumerate(l):
        if name == target:
            return index
    return -1

print(find_pos(["rahul","mansi","satyam"],"mansi"))