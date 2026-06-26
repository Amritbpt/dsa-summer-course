def sort_by(items):
    return sorted(items,key=lambda x:(x[1],-x[2]))

print(sort_by([
    ('apple', 1.50, 50),
    ('banana', 0.30, 100),
    ('cherry', 2.00, 50),
    ('date', 1.50, 80),
]))