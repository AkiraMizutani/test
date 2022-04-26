text = "Hi He Lead Because Boron Could Not Oxidize Flourine. New Nations Might Also Sign Peace Security Clause. Arthur King Can."
table = (1, 5, 6, 7, 8, 9, 15, 16, 19)

list =text.replace('.', '').split(' ')
key = []
for i, str in enumerate(list):
    if i+1 in table:
        key.append(str[0])
    else:
        key.append(str[:2])

dict = dict(zip(key, range(1, len(key)+1)))
print(dict)