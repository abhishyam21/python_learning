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

print("--------------Problem 55 End--------------------------")

# problem 56

print("--------------Problem 56 End--------------------------")

# problem 57

print("--------------Problem 57 End--------------------------")

# problem 58

print("--------------Problem 58 End--------------------------")

# problem 59

print("--------------Problem 59 End--------------------------")

# problem 60

print("--------------Problem 60 End--------------------------")
