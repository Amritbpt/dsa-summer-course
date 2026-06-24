def find_duplicate(list):
    seen=set()
    duplicate=set()
    for i in list:
        if i in seen:
            duplicate.add(i)
        else:
            seen.add(i)

    return duplicate

print(find_duplicate([1,3,2,3,1,5,2,5,6,4,6,5]))