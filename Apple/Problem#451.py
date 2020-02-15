'''
Implement the function fib(n), which returns the nth number in the Fibonacci sequence, using only O(1) space
'''
def fib(n):
    a = 0
    b = 1
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        for i in range(2, n):
            c = a + b
            a, b = b, c
        return b
