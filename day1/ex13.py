docs = [["リンゴ", "リンゴ"], ["リンゴ", "レモン"], ["レモン", "ミカン"]]
terms = ["リンゴ", "レモン", "ミカン"]

def tf(term, doc):
    return doc.count(term)/len(doc)


for doc in docs:
    for term in terms:
        print(f"tf({term}, {doc}) = {tf(term, doc)}  ", end = '')
    print()