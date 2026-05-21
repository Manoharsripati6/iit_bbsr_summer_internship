""" 
    Task 4 — Debugging
    ● Fix the provided buggy Python code.
    numbers = [1, 2, 3, 4, 5]
    for i in range(len(numbers)):
    numbers.remove(numbers[i])
    print(numbers)
    ● Explain why the bug occurs.
    ● Provide the corrected solution & Explain the time complexity of your approach.

"""
#the bug occures due to the modification of arr over iteration
""" 
    eg: if arr=[1,2,3]
    for i=0
    arr[0] will be removed
    then arr=[2,3]
    noe for i=1
    arr[1] will be removed
    then arr=[2]
    then for i=2
    it'll try to remove arr[2] which gives an error
    This happens because len(numbers) is calculated only once
"""

numbers = [1, 2, 3, 4, 5]
for num in numbers[:]:
    numbers.remove(num)

print(numbers)# time complexity : O(n^2)


numbers = [1, 2, 3, 4, 5]
numbers.clear()
print(numbers)# time complexity : O(n)

