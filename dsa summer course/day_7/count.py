word='Hello World'
words=word.split()
vovel=['a','e','i','o','u','A','E','I','O','U']
vovel_count=0
word_count=len(word)
for i in range(len(word)):
    if word[i] in vovel:
        vovel_count+=1
longest=max(words,key=len)
print(vovel_count)
print(word_count-vovel_count)
print(longest)