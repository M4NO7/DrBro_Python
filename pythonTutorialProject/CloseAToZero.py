"""# Python3 program to find Closest number in a list

def closest(lst, K):
    return lst[min(range(len(lst)), key=lambda i: abs(lst[i] - K))]


# Driver code
lst = [3.64, 5.2, 9.42, 9.35, 8.5, 8, 2, 1, 0.1]
K = 0
print(closest(lst, K))

import math

positive_infinity = -math.inf
print(positive_infinity)  # Output: inf

negative_infinity = -(-math.inf)
print(negative_infinity)  # Output: -inf"""

import math


def Solve(N, A):
    closest = math.inf
    greater_value = -math.inf

    for num in A:
        if abs(num) < abs(closest):
            closest = num
            greater_value = num
        elif abs(num) == abs(closest) and num > greater_value:
            greater_value = num

    return greater_value


N = int(input("Enter the size of the array: "))
A = list(map(int, input("Enter the array elements: ").split()))
out_ = Solve(N, A)
print("The number closest to zero with the greater value is:", out_)





