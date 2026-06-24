from collections import Counter, defaultdict, deque
def inventory_manager(words):
    talley=defaultdict(int)
    for item,quantity in words:
        talley[item]+=quantity

    maximum_sold=max(talley,key=talley.get)
    
    return talley,maximum_sold

print(inventory_manager( [('apple',3),('banana',2),('apple',1),('cherry',5)]))
