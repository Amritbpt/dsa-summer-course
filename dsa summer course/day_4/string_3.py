apl="abcdefghijklmnopqrstuvwxyzabc"
s="helloz"
u=""
for i in range(len(s)):
    k=s[i]
    l= apl.find(k)
    m=apl[l+3]
    u+=m

print(u)