from collections import Counter, defaultdict, deque
def group_anagrams(words):
    anagrams=defaultdict(list)
    for i in words:
        key=''.join(sorted(i))
        anagrams[key].append(i)

    return anagrams.values()

print(group_anagrams(['eat','tea','tan','ate','nat','bat']))