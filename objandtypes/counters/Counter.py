from collections import Counter

lines = ["aaaa","bbb","cad","d","e", "f", "cad"]
counter = Counter(lines)

print(counter["cad"])