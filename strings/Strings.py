s = "kiran rao"
print(s)
# ------Characters at even positions
i = 0
while i < len(s):
    print(s[i])
    i = i + 2
# -------Convert String B4A1D3 TO ABD134
s = 'B4A1D3'
i = 0
even = odd = output = ''
while i < len(s):
    if i % 2 == 0:
        even += s[i]
    else:
        odd += s[i]
    i = i + 1

for x in sorted(even):
    output += x
for x in sorted(odd):
    output += x
print(output)

