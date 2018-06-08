def sum(*args):
    total = 0
    for arg in args:
        total += arg
    return total

print(sum(1,3,5,7,9))