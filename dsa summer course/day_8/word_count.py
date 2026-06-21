def char_freq(item):
    freq={}
    for i in range(len(item)):
        freq[item[i]]=freq.get(item[i],0)+1

    return freq

print(char_freq('hello world'))