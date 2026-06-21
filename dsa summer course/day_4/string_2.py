s='Welcome to the world'
words=s.split()
unique=set(words)
longest=max(words,key=len )
print(f"total words : {len(words)} , unique : {len(unique)} , longest : {longest}")