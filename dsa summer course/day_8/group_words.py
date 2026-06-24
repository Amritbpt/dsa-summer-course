def grouping(list):
    new_list={}
    for i in list:
        new_list[i[0]]= new_list.get(i[0],[])+ [i]

    return new_list

print(grouping(['apple','ant','bat','bee','cat']))