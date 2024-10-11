

def matchingStrings(stringList, queries):
    x = []
    for i in queries:
        k = 0
        for j in stringList:
            if i == j:
                k = k + 1
        x.append(k)
    return x


stringList = ["aba", "baba", "aba", "xzxb"]
queries = ["aba", "xzxb", "ab"]
print(matchingStrings(stringList, queries))