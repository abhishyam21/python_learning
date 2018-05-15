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

d = {1: 10, 2: 20, 3: 30, 4: 40, 5: 50, 6: 60}


def is_key_present1(input):
    for i in d.items():
        if i[0] == input:
            print("Key already exists")
            return
    print("No Key exists")


def is_key_present2(input):
    if input in d:
        print("Key already exists")
    else:
        print("No Key exists")


is_key_present1(5)
is_key_present1(9)

is_key_present2(5)
is_key_present2(9)

print("--------------Problem 4 End--------------------------")

# problem 5

for key, val in d.items():
    print("{} --> {}".format(key, val))
print("-------------------------------")
for i in d.items():
    print("{} --> {}".format(i[0], i[1]))

print("--------------Problem 5 End--------------------------")

# problem 6

output = {}
for i in range(1, 10):
    output[i] = i ** 2
print(output)

print("--------------Problem 6 End--------------------------")

# problem 7


output = {}
for i in range(1, 16):
    output[i] = i * i
print(output)

print("--------------Problem 7 End--------------------------")

# problem 8
d1 = {'a': 100, 'b': 200}
d2 = {'x': 300, 'y': 200}
d3 = {}
d3.update(d1)
d3.update(d2)
print(d3)

print("--------------Problem 8 End--------------------------")

# problem 9

for key, val in d.items():
    print("{} --> {}".format(key, val))
print("-------------------------------")
for i in d.items():
    print("{} --> {}".format(i[0], i[1]))

print("--------------Problem 9 End--------------------------")

# problem 10

my_dict = {'data1': 100, 'data2': -54, 'data3': 247}


def sum_values1(input):
    result = 0
    for key, val in input.items():
        result += val
    return result


def sum_values2(input):
    return sum(input.values())


print(sum_values1(my_dict))
print(sum_values2(my_dict))

print("--------------Problem 10 End--------------------------")
