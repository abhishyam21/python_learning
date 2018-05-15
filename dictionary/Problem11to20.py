# problem 11

def common_data(input1, input2):
    for i in input1:
        if i in input2: return True
    return False


print(common_data([1, 2, 3, 4, 5], [5, 6, 7, 8, 9]))
print(common_data([1, 2, 3, 4, 5], [6, 7, 8, 9]))

print("--------------Problem 11 End--------------------------")

# problem 12

remove_pos = (0, 4, 5)


def remove_elements1(input):
    print(list(enumerate(input)))
    return [x for (i, x) in enumerate(input) if i not in remove_pos]


print(remove_elements1(['Red', 'Green', 'White', 'Black', 'Pink', 'Yellow']))

print("--------------Problem 12 End--------------------------")

# problem 13

array = [[['*' for col in range(6)] for col in range(4)] for col in range(3)]
print(array)

print("--------------Problem 13 End--------------------------")

# problem 14

num = [7, 8, 120, 25, 44, 20, 27]
print([x for x in num if x % 2 != 0])

print("--------------Problem 14 End--------------------------")

# problem 15
import random

color = ['Red', 'Green', 'White', 'Black', 'Pink', 'Yellow']
random.shuffle(color)
print(color)

print("--------------Problem 15 End--------------------------")


# problem 16

def printSqares():
    l = list()
    for i in range(21):
        l.append(i * i)
    print(l[:5])
    print(l[-5:])


printSqares()

print("--------------Problem 16 End--------------------------")


# problem 17

def printValues():
    l = list()
    for i in range(21):
        l.append(i * i)
    print(l[6:])


printValues()

print("--------------Problem 17 End--------------------------")

# problem 18

import itertools

print(list(itertools.permutations([1, 2, 3])))
print(list(itertools.permutations([1, 2, 3, 4])))

print("--------------Problem 18 End--------------------------")

# problem 19
list1 = [1, 2, 3, 4]
list2 = [1, 2]
print(list(set(list1) - set(list2)))

print("--------------Problem 19 End--------------------------")

# problem 20
nums = [5, 15, 35, 8, 98]

for (index, value) in enumerate(nums):
    print(index, value)

print("--------------Problem 20 End--------------------------")
