# put your python code here
num = [int(i) for i in input().split(' ')]
num[0], num[len(num)-1] = num[len(num)-1], num[0]
print(*num)



