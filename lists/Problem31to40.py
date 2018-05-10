# problem 31


def count_range_in_list(list, x, y):
    result = []
    for i in list:
        if x <= i <= y:
            result.append(i)
    return len(result)


list1 = [10, 20, 30, 40, 40, 40, 70, 80, 99]
list2 = ['a', 'b', 'c', 'd', 'e', 'f']
print(count_range_in_list(list1, 40, 100))

print(count_range_in_list(list2, 'a', 'e'))
print("--------------Problem 31 End--------------------------")


# problem 32

def is_Sublist(list, sublist):
    i = counter = 0
    while i <= (len(list) - (len(sublist) - 1)):
        if counter == (len(sublist)):
            return True
        elif sublist[counter] == list[i]:
            counter += 1
        else:
            counter = 0
        i += 1
    return counter == len(sublist)


a = [2, 4, 3, 5, 7]
b = [4, 3]
c = [3, 7]
print(is_Sublist(a, b))
print(is_Sublist(a, c))

print("--------------Problem 32 End--------------------------")

# problem 33

l1 = [10, 20, 30, 40]
l2 = ['X', 'Y', 'Z']


def sub_lists(list):
    result = [[]]
    i = j = 0
    while i <= len(list):
        while j < i:
            result.append(list[j:i])
            j += 1
        j = 0
        i += 1
    return result


print(sub_lists(l1))
print(sub_lists(l2))

print("--------------Problem 33 End--------------------------")

# problem 34
# TODO

print("--------------Problem 34 End--------------------------")


# problem 35

def concat_list1(list, n):
    result = []
    for i in range(1, n + 1):
        for j in list:
            result.append(j + str(i))
    return result


print(concat_list1(['p', 'q'], 4))


def concat_list2(list, n):
    return ['{}{}'.format(x, y) for y in range(1, n + 1) for x in list]


print(concat_list2(['p', 'q'], 4))
print("--------------Problem 35 End--------------------------")

# problem 36

x = 100
print(format(id(x), 'x'))
s = 'w3resource'
print(format(id(s), 'x'))

print("--------------Problem 36 End--------------------------")

# problem 37

color1 = "Red", "Green", "Orange", "White"
color2 = "Black", "Green", "White", "Pink"
print(color2 and color1)  # if 1st one is true then returns 2nd one
print(color2 or color1)
print(set(color1) & set(color2))
print(set(color1) | set(color2))

print("--------------Problem 37 End--------------------------")


# problem 38
# TODO
def replace2copy(list):
    for i in range(0, len(list), 2):
        temp = list[i + 1]
        list.insert(i + 1, list[i])
        list.insert(i, temp)
    return list


list = [0, 1, 2, 3, 4, 5]
print(replace2copy(list))
print("--------------Problem 38 End--------------------------")

# problem 39

list = [11, 33, 50]
print(''.join(map(str, list)))
print(map(str, list))
print("--------------Problem 39 End--------------------------")

# problem 40
# TODO
print("--------------Problem 40 End--------------------------")
