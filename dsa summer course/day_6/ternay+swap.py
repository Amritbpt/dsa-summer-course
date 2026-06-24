def classify_number(n):
    
    return "positive" if n>0 else "negative" if n<0 else "zero"


def swap(a, b):

    return b, a


print(classify_number(5))
print(swap(6,7))