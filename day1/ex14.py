import math

docs = [["リンゴ", "リンゴ"], ["リンゴ", "レモン"], ["レモン", "ミカン"]]
terms = ["リンゴ", "レモン", "ミカン"]

def idf(term, docs):
    count = 0
    for doc in docs:
        if term in doc:
            count += 1
    return math.log10(len(docs) / count) + 1

for term in terms:
    print(f"idf({term}) = {idf(term, docs)}")