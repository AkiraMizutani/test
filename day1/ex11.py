path = "./dataset/data.txt"
with open(path, encoding = "utf-8") as f:
    while True:
        line = f.readline()
        if not line:
            break
        print(line, end = '')
