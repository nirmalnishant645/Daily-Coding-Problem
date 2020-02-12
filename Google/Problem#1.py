'''
Given a list of numbers and a number k, return whether any two numbers from the list add up to k.
For example, given [10, 15, 3, 7] and k of 17, return true since 10 + 7 is 17.
Bonus: Can you do this in one pass?
'''
def elements_sum(arr, target):
    dict = {}
    for i in range(len(arr)):
        temp = target - arr[i]
        if temp in dict:
            return True
        dict.update({arr[i] : i})
    return False
    
arr = arr = list(map(int, input().split()))
target = int(input())
print(elements_sum(arr, target))
