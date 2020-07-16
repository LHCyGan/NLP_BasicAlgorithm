from collections import Counter



sentence = "Bob likes to play basketball, Jim likes too.".strip().replace('.','').replace(',','')
result = Counter(sentence)
print(result)
