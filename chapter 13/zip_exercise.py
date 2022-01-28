# This Is challenge

# define a function take any no of lists containing number

# [1,2,4],[4,5,6],[7,8,9]

# return average

# (1+4+7)/3,(2,5,8)/3,(3,6,9)/3

# try to make this anonymous function in one line using lambda

average = lambda l:[sum(unpack)//len(unpack) for unpack in zip(*l)]
print(average([[1,2,3],[4,5,6],[7,8,9]]))



average = lambda *l:[sum(pair)/len(pair) for pair in zip(*l)]
print(average([1,2,3],[4,5,6],[7,8,9]))

d = {1:2,3:4,5:6,7:8}
print(list(zip(*d.items())))

print(d.keys())
print(d.values())


