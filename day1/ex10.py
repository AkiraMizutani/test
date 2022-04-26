import sys

def n_gram (c_list, n):
    tango = []
    moji = []
    for i in range(len(c_list)-n+1):
        tango.append(c_list[i:i+n])

    str = "".join(c_list)
    for i in range(len(str)-n+1):
        moji.append(str[i:i+n])

    print("単語", n, "-gram:", tango)
    print("文字", n, "-gram:", moji)

value = sys.argv[1:]
n_gram(value, 2)