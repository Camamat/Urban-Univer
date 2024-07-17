from itertools import combinations

def all_variants(text):
    for i in range(1, len(text)+1):
        lis = []
        b = combinations(text, i)
        lis.extend(b)
        for j in lis:
            yield (''.join(j))


a = all_variants("abc")
for i in a:
    print(i)