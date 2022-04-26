path = "./dataset/data.txt"
docs = []
with open(path, encoding = "utf-8") as f:
    while True:
        line = f.readline()
        if not line:
            break
        fruit_list = line.replace('\n','').split("と")
        docs.append(fruit_list)

print("docs:", docs)
print("terms:", list(set(w for doc in docs for w in doc)))
        

