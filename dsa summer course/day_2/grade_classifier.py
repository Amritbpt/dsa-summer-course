score = 85
if score>90 and score<100:
    grade='A'
elif 80<score<89:
    grade='B'
elif 70<score<79:
    grade='C'
elif 60<score<69:
    grade='D'
else:
    grade='F'

print(f"score = {score} --> Grade = {grade}")