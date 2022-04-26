import math
import numpy as np
docs = [["リンゴ", "リンゴ"], ["リンゴ", "レモン"], ["レモン", "ミカン"]]
terms = ["リンゴ", "レモン", "ミカン"]

def tf(term, doc):
    return doc.count(term)/len(doc)

def idf(term, docs):
    count = 0
    for doc in docs:
        if term in doc:
            count += 1
    return math.log10(len(docs) / count) + 1
def tf_idf(docs, terms):
    mtx = np.zeros((len(docs), len(terms)))
    for i in range(len(docs)):
        for j in range(len(terms)):
            mtx[i][j] = tf(terms[j], docs[i]) * idf(terms[j], docs)
    return mtx

if __name__ == '__main__':
    print(tf_idf(docs, terms))