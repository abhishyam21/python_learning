# problem 51

def list_slice1(input, n):
    res = []
    for i in range(n):
        temp = []
        for j in range(i, len(input), n):
            temp.append(input[j])
        res.append(temp)
    return res


def list_slice2(input, n):
    return [input[i::n] for i in range(n)]


input = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n']
print(list_slice1(input, 3))
print(list_slice2(input, 3))

print("--------------Problem 51 End--------------------------")

# problem 52

color1 = ["red", "orange", "green", "blue", "white"]
color2 = ["black", "yellow", "green", "blue"]

print(set(color1) - set(color2))
print(set(color2) & set(color1))
print("--------------Problem 52 End--------------------------")

# problem 53

import itertools

c = itertools.count()
print(next(c))
print(next(c))
print(next(c))
print(next(c))
print(next(c))

print("--------------Problem 53 End--------------------------")

# problem 54
color = ['red', 'green', 'orange']
print("-".join(color))

print("--------------Problem 54 End--------------------------")

# problem 55

original_list = [{'key1': 'value1', 'key2': 'value2'}, {'key1': 'value3', 'key2': 'value4'}]
new_list = [{k: v for k, v in d.items() if k != 'key1'} for d in original_list]
print(new_list)

print("--------------Problem 55 End--------------------------")

# problem 56
import ast

color = "['Red', 'Green', '1']"
print(ast.literal_eval(color))
print("--------------Problem 56 End--------------------------")

# problem 57

color1 = ["green", "orange", "black", "white"]
color2 = ["green", "green", "green", "green"]

print(all(c =='green' for c in color2))
print(all(c =='blue' for c in color1))
print("--------------Problem 57 End--------------------------")

# problem 58

num1 = [1, 3, 5, 7, 9, 10]
num2 = [2, 4, 6, 8]

num1[-1:] = num2
print(num1)

print("--------------Problem 58 End--------------------------")

# problem 59

x = [1, 2, 3, 4, 5, 6]
print(x[-1])

print("--------------Problem 59 End--------------------------")

# problem 60

x = [(4, 1), (1, 2), (6, 0)]

def min_sec_index1(input):
    result = ()
    min_val = input[0][1]
    for i in input:
        if min_val > i[1]:
            min_val = i[1]
            result = i
    return result


def min_sec_index2(input):
    return min(x, key=lambda n: (n[1], -n[0]))


print(min_sec_index1(x))
print(min_sec_index2(x))
print("--------------Problem 60 End--------------------------")
