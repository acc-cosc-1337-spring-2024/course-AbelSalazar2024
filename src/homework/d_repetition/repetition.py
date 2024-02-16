#HW3 for range while loops

def get_factorial(num):
    factorial = 1
    for i in range(1, num + 1):
        factorial = factorial * i
    return factorial

def sum_odd_number(num):
    total = 0
    i = 1
    while i <= num:
        total = total + i
        i = i + 2
    return total
    