str = "パタトクカシーー"
a = ""
b = ""
for i in range(len(str)):
    if i % 2 == 0:
        a += str[i]
    else:
        b += str[i]

print(a)
print(b)