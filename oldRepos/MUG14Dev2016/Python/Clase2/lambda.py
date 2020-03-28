
arr = [1, 2, 3, 4, 5]

l = lambda x: x + 2

print map(l, arr)
print arr

print filter(lambda x: x >= 3, arr)

def get_lambda():
    return lambda x: x * 2

print get_lambda()(10)
