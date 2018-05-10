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

print("--------------Problem 36 End--------------------------")

# problem 37


# problem 38

print("--------------Problem 38 End--------------------------")

# problem 39


print("--------------Problem 39 End--------------------------")

# problem 40

print("--------------Problem 40 End--------------------------")