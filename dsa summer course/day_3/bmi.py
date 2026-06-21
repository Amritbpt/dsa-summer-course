def bmi(w,h):
    x=w/(h*h)
    if x<18.5:
        y='underweight'
    elif 18.5<=x<24.9:
        y='normal'
    elif 25<=x<29.9:
        y='overweight'
    else:
        y='obese'

    return x,y



print(bmi(70, 1.75))