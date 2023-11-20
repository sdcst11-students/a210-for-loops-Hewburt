#! python3
"""
##### Task 3
Print all the numbers from 1 to 1000 that are divisible by 5.
"""

for num in range(1, 1001):
    if num % 5 == 0:
        print(num, end=" ")
