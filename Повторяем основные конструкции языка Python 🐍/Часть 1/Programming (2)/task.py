# put your python code here
from math import *
str_1 = input()
price = len(str_1) * 0.60
b = price - floor(price)
a = b * 100
print(str(floor(price)) + ' р. ' + str(ceil(a)) + ' коп.')