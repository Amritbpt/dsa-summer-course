def arranged(report):
    students=sorted(report,key=lambda x:-x[1])
    return students

def grade(score):
    if score>=90: return 'A'
    if score>=80: return 'B'
    if score>=70: return 'C'
    if score<70: return 'D'
card=[('Alice',85),('Bob',92),('Carol',73)]
print(arranged(card))
for name, score in card:
    print(f'{name}:{score}:{grade(score)}')