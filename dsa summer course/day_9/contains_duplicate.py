def contain_duplicate(list):
    seen=set()
    duplicate=set()
    for i in list:
        if i in seen:
            duplicate.add(i)
        else:
            seen.add(i)

    return True if len(duplicate) else False

print(contain_duplicate([1,3,4,5,5]))