# problem 61

print([{} for i in range(5)])

print("--------------Problem 61 End--------------------------")

# problem 62

num = [1, 2, 3, 4, 5]
# TODO

print("--------------Problem 62 End--------------------------")

# problem 63

num = [1, 2, 3, 4]
print(['stu' + str(x) for x in num])
print("--------------Problem 63 End--------------------------")

# problem 64

num = [1, 2, 3]
color = ['red', 'while', 'black']

print([(x, y) for x, y in zip(num, color)])
print("--------------Problem 64 End--------------------------")

# problem 65

num = {'physics': 80, 'math': 90, 'chemistry': 86}
print(list(num)[0])

print("--------------Problem 65 End--------------------------")

# problem 66

num = [[1, 2, 3], [4, 5, 6], [10, 11, 12], [7, 8, 9]]
print(max(num, key=sum))

print("--------------Problem 66 End--------------------------")

# problem 67

list1 = [220, 330, 500]
list2 = [12, 17, 21]

print(all(x >= 200 for x in list1))
print(all(x >= 25 for x in list2))
print("--------------Problem 67 End--------------------------")

# problem 68
x = [10, 20, 30]
y = [40, 50, 60]
x[:0] = y
print(x)

print("--------------Problem 68 End--------------------------")

# problem 69
import itertools

num = [[10, 20], [40], [30, 56, 25], [10, 20], [33], [40]]
new_list = list(num for num, _ in itertools.groupby(num))
print(new_list)

print("--------------Problem 69 End--------------------------")


# problem 70


def dict_depth(input):
    if isinstance(input, dict):
        return 1 + (max(map(dict_depth, input.values())) if input else 0)
    return 0


dic = {'a': 1, 'b': {'c': {'d': {}}}}
print(dict_depth(dic))

print("--------------Problem 70 End--------------------------")

# problem 71

my_list = [{}, {}, {}]
my_list1 = [{1, 2}, {}, {}]

print(all(not d for d in my_list))
print(all(not d for d in my_list1))
print("--------------Problem 71 End--------------------------")
