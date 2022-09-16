# put your python code here
num = input()
if len(num) > 5:
    print((num[:len(num) - 5]) + (''.join(reversed(num[len(num)-5:]))))
else:
    print(int(''.join(reversed(num))))