from collections import Counter, defaultdict, deque
def most_frequent(sentence):
    words=sentence.split()
    talley=Counter(words)
    return talley.most_common(3)


print(most_frequent('The cat sat on the mat. The cat ...'))