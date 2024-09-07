def all_variants(text):
    for i in range(len(text)):
        for q in range(len(text) - i):
            yield text[q:q + i + 1]


a = all_variants("abc")
for w in a:
    print(w)
