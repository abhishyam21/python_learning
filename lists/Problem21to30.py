# problem 21

s = ['a', 'b', 'c', 'd']
print("".join(s))

print("--------------Problem 21 End--------------------------")

# problem 22

num = [10, 30, 4, -6]
print(num.index(30))
print(num.index(-6))

print("--------------Problem 22 End--------------------------")

# problem 23
import itertools


def flat_list(input):
    return list(itertools.chain(*input))


original_list = [[2, 4, 3], [1, 5, 6], [9], [7, 9, 0]]
print(flat_list(original_list))

print("--------------Problem 23 End--------------------------")

# problem 24

list1 = [1, 2, 3, 0]
list2 = ['Red', 'Green', 'Black']

print(list1 + list2)
print("--------------Problem 24 End--------------------------")

# problem 25

import random

color_list = ['Red', 'Blue', 'Green', 'White', 'Black']
print(random.choice(color_list))

print("--------------Problem 25 End--------------------------")

# problem 26


print("--------------Problem 26 End--------------------------")


# problem 27

def second_smallest(input):
    a = b = float("inf")
    for i in input:
        if i <= a:
            b, a = a, i
        elif i < b:
            b = i
    return b


print(second_smallest([1, 2, -8, -2, 0]))

print("--------------Problem 27 End--------------------------")


# problem 28

def second_largest(input):
    a = b = float("-inf")
    for i in input:
        if a < i:
            b, a = a, i
        elif b < i:
            b = i
    return b


print(second_largest([1, 2, -8, -2, 0]))

print("--------------Problem 28 End--------------------------")

# problem 29


input = [10, 20, 30, 40, 20, 50, 60, 40]


def remove_duplicates(input):
    return list(set(input))


print(remove_duplicates(input))
print("--------------Problem 29 End--------------------------")

# problem 30
import collections

my_list = {10, 10, 10, 10, 20, 20, 20, 20, 40, 40, 50, 50, 30}
print(collections.Counter(my_list))
print("--------------Problem 30 End--------------------------")
