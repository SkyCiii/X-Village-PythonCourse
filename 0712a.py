import random
a = random.randint(1,100+5)
print (a)

#

import math
b = math.sqrt (9)
print (b)

#

lis = [5, 6, 4, 9, 110, 47]
c = random.choice(lis)
print (c)

#

import zoo

zoo.duck()
zoo.cat()
zoo.tiger()

#找出50以下的所有質數

for i in range (1, 51) :
    for j in range (2, i) :
        if i % j == 0 :
            break
    else :
        print (i)

#

import datetime


def print_next_day() :
    x = int(input('Day of today = : '))     # input 的型別：str；int()的型別：int。
    y = int(input('Month of today = : '))   
    z = int(input('Year of today = : '))
    h = datetime.date(z, y, x)              # datetime module 底下的所有 function 都為 "date" 型別。
    x = (h + datetime.timedelta(1))
    print (x)                               # print()可以印出所有東西，如此例，x 型為" date"。

print_next_day()
