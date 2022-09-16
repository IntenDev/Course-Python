# put your python code here
weight, height = float(input()), float(input())

bmi = weight / (height * height)
if 18.5 <= bmi <= 25:
    print('Оптимальная масса')
elif bmi < 18.5:
    print('Недостаточная масса')
else:
    print('Избыточная масса')