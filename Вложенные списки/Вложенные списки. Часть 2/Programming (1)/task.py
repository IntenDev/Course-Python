# put your python code here
n = int(input())
list1 =[]
count = 1
for i in range(n):
    list1.append([])
    for j in range(count):
        list1[i].append(j+1)
    count += 1
    print(list1[i])