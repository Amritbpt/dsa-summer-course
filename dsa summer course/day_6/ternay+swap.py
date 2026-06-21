def classify_number(n):
    if n > 0:
        return "positive"
    elif n < 0:
        return "negative"
    else:
        return "zero"
    
def swap(a, b):
    return b, a


print(classify_number(-5))
print(swap(6,7))