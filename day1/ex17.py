import numpy as np
import nlp.ex15
import nlp.ex16

path = "./dataset/data.txt"
docs = []
with open(path, encoding = "utf-8") as f:
    while True:
        line = f.readline()
        if not line:
            break
        fruit_list = line.replace('\n','').split("と")
        docs.append(fruit_list)

terms = list(set(w for doc in docs for w in doc))
mtx = np.zeros((len(docs), len(docs)))
tf_idf_mtx = nlp.ex15.tf_idf(docs, terms)
for i in range(len(docs)):
    for j in range(len(docs)):
        mtx[i][j] = nlp.ex16.cosine_sim(tf_idf_mtx[i], tf_idf_mtx[j])

print(mtx)
