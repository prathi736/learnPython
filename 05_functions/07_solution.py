# Multiple variables sum
def sum_all(*args):
    print(*args)
    print(args)
    return sum(args)


print(sum_all(1,2,4,5,6))
print(sum_all(1,2,3,6,7,8))