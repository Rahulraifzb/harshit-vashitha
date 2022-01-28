# any all function

def my_sum(*args):
    # args = ()

    if all([(type(arg) == int or type(arg) == float) for arg in args]):
        total = 0
        for arg in args:
            total += arg
        return total
    else:
        return "wrong input"

print(my_sum(1,2,3,4,6.8))
