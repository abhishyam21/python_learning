# problem 41

obj = {}
for i in range(1, 21):
    obj[str(i)] = []

print(obj)

print("--------------Problem 41 End--------------------------")

# problem 42

list1 = ['a', 'b', 'c', 'd', 'e', 'f']
list2 = ['d', 'e', 'f', 'g', 'h']

print("Missing Values in List2 are: {}".format(set(list1) - set(list2)))
print("Missing Values in List1 are: {}".format(set(list2) - set(list1)))

print("--------------Problem 42 End--------------------------")

# problem 43

color = [("Black", "#000000", "rgb(0, 0, 0)"), ("Red", "#FF0000", "rgb(255, 0, 0)"),
         ("Yellow", "#FFFF00", "rgb(255, 255, 0)")]
a, b, c = color
print(a)
print(b)
print(c)

print("--------------Problem 43 End--------------------------")

# problem 44

print([[5 * x + j for j in range(1, 6)] for x in range(5)])

print("--------------Problem 44 End--------------------------")

# problem 45

input = [(1, 2), (3, 4), (1, 2), (5, 6), (7, 8), (1, 2), (3, 4), (3, 4),
         (7, 8), (9, 10)]
output = set()
for i in input:
    output.add(i[0])
    output.add(i[1])

print(output)
print(set().union(*input))

print("--------------Problem 45 End--------------------------")

# problem 46

x = [1, 2, 3, 4, 5, 6, 7, 8, 9]

print(x[::2])
print("--------------Problem 46 End--------------------------")

# problem 47

color = ['Red', 'Green', 'Black']
print([x for y in color for x in ['c', y]])

print("--------------Problem 47 End--------------------------")

# problem 48


colors = [['Red'], ['Green'], ['Black']]
print("\n".join([str(x) for x in colors]))

print("--------------Problem 48 End--------------------------")

# problem 49

color_name = ["Black", "Red", "Maroon", "Yellow"]
color_code = ["#000000", "#FF0000", "#800000", "#FFFF00"]

print([{'Color Name': n, 'and Color Code': c} for n, c in zip(color_name, color_code)])
print("--------------Problem 49 End--------------------------")

# problem 50

my_list = [{'key': {'subkey': 1}}, {'key': {'subkey': 10}}, {'key': {'subkey': 5}}]
print("Original List: ")
my_list.sort(key=lambda e: e['key']['subkey'], reverse=True)
print(my_list)
print("--------------Problem 50 End--------------------------")
