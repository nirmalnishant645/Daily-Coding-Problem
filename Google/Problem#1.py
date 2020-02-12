'''
Given a list of numbers and a number k, return whether any two numbers from the list add up to k.
For example, given [10, 15, 3, 7] and k of 17, return true since 10 + 7 is 17.
Bonus: Can you do this in one pass?
'''
def elements_sum(arr, target):
    res = set()
    for i in arr:
        temp = target - i
        if temp in res:
            return True
        res.add(i)
    return False
    
arr = list(map(int, input().split()))
target = int(input())
print(elements_sum(arr, target))
