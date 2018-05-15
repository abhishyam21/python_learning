# problem1
import operator

d = {1: 2, 3: 4, 4: 1, 2: 1, 5: 1}
print("Original dictionary:", d)
sorted_dict = sorted(d.items(), key=operator.itemgetter(0))
print("Sorted dictionary:", sorted_dict)

print("--------------Problem 1 End--------------------------")

# problem2

d = {0: 10, 1: 20}
d[2] = 30
d.update({3: 30})
print(d)

print("--------------Problem 2 End--------------------------")

# problem 3

dic1 = {1: 10, 2: 20}
dic2 = {3: 30, 4: 40}
dic3 = {5: 50, 6: 60}
dic4 = {}
for d in (dic1, dic2, dic3):
    dic4.update(d)
print(dic4)

print("--------------Problem 3 End--------------------------")

# problem 4

print("--------------Problem 4 End--------------------------")

# problem 5

print("--------------Problem 5 End--------------------------")

# problem 6

print("--------------Problem 6 End--------------------------")

# problem 7

print("--------------Problem 7 End--------------------------")

# problem 8

print("--------------Problem 8 End--------------------------")

# problem 9

print("--------------Problem 9 End--------------------------")

# problem 10

print("--------------Problem 10 End--------------------------")
