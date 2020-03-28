
#for target_list in range(1, 11):
#    print target_list

'''
def fibo(value_n):
    """Generador de Fibonacci"""
    left_a, right_b = 0, 1
    while left_a < value_n:
        print left_a
        left_a, right_b = right_b, left_a + right_b

fibo(1000)
'''

result = 0

def sub(val):
    global result
    result -= val
    return result

def sum_custom(val):
    global result
    result += val
    return result

print sub(10)
print sum_custom(10)
