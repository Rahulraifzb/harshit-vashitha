l1 = [1,3,5,7]
l2 = [2,4,6,8]

l = [(1,2),(3,4),(5,6),(7,8)]

l1,l2=list(zip(*l))
print(l1)
print(l2)

d = {1:2,3:4,5:6,7:8}
l1,l2 = list(zip(*d.items()))
print(l1)
print(l2)