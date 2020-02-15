'''
Implement the function fib(n), which returns the nth number in the Fibonacci sequence, using only O(1) space
'''
def fib(n):
    if n <= 1:
        return n
    a, b = 0, 1
    for i in range(2, n):
        a, b = b, a + b
    return b
