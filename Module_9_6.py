

def all_variants(text):
    for ind in range(len(text) + 1):
        for j in range(len(text) - ind + 1):
            yield text[j:j + ind]


a = all_variants("abc")
for i in a:
    print(i)
