
#
a = 1
while a < 100 :                 #while就是重複判斷的簡寫，若判斷為True，則跑縮排（該段落）的東西。
    print (a)                   #print後面加上 , end = ' ' ,可以避免換行。
    a = a + 2                   #左式等於 a += 2。
print ('end')

#

n = 100
iterate = 0
total = 0
while iterate != n :
    iterate = iterate + 1
    total = total + iterate     #從1+...+99+100的程式碼。
                                #print (total , end = ' ')如果放在這裡，會在每一次while加完就print一次。
print (total)                   #放在縮排以外，就是全部加完才會print。

#以下會印990出來

n = 0
ans = 0
while n < 1001 :
    if (n % 11 == 0) :
        ans = n                 #若n可以被11整除，就把n儲存在ans裡面，而每跑11次while，ans會被覆蓋一次。
    n = n + 1
print(ans)

#以下會印1000出來

n = 1000
flag = True
while n > 0 :
    if (n % 11 == 0) and flag : #True and True才會進入if的縮排，False and True則不會。
        print(n)
        flag = False            #進入後flag被覆蓋成False，從此之後if只能為False，就再也不會進入if的縮排。
        #break                  #print完之後，break可以中斷最接近的while。放這裡或放下面都可以。
    print(n)
    n = n - 1
    break

#

n = 10
while n > 0 :
    if n == 5 :
        n -= 2
        continue                #省略（跳過）迴圈在continue下方的區塊的程式碼，直接回到while第一行。
    print(n , end = ' ')
    n -= 1
print('End')

#Exercise
i = 1
j = 1
while i <= 5 :
    while j <= 5 :
        if i * j > 9 :
            break
        print ( '*' , end = ' ')
        j += 1
    print('')    
    j = 1
    i += 1        

#Exercise
#import random
#answer = random.randint(1,100)

#n = 0
#while n != answer :
    #x = input ("Enter a number : ")
    #x = int(x)
    #if x > answer :
        #print ('Too big !')
    #elif x < answer :
        #print ('Too small !')
    #else :
        #print ('Correct !')
        #break

#

total = 0
for i in range (101) :
    total = total + i
print (total)

#

for i in range (1,10) :
    for j in range (1,10) :
        print (i , '*' , j , '=' , i*j , sep = ' ')

#

n = 2 
table = []
for i in range (n) :
    table.append( [0] * 3 )
print (table)

#

def f(n) :
    for i in range (1, n+1) :
        for j in range (1, n+1) :
            print (i, '*', j, '=', i*j, end = ' , ')
        print ('')

f(3)

#

def g(a,b) :
    print ('(' , b , ',' , a , ')' )

g(3,1)      #在def裡面已經定義函數為print，後面直接打就好了。

#


def h(a,b) :
    if a > b :
        return 'a > b'  #這裡可以用print也可以用return，print is a function所以要加括弧
    elif a == b :       #return後面可以加所有的object，everything is object，然後在後面再print出來。
        return  'a = b'
    else :
        return 'a < b'

print(h(1, 5))          #等於宣告var = h(1, 5)....print(var)


#
def bmi(height, weight):
    calculate = weight / (height*height)
    if calculate < 18.5 :
        result = '過輕'
        return result   #也可以直接打成return'過輕'，因為'過輕'也是一個str。
    elif 18.5 < calculate :
        result = '正常'
        return result
    else :
        result = '過重'
        return result

#回去看inner function的應用跟比較好的解釋，但基本上是

def maker(N) :
    def action(X) :
        return N**X
    return action       #先看外圍（螺旋看法），action在這裡只是object，在縮排的def才被定義成function。

f = maker(9)
print(f(5))

#

def rate (x) :
    def km (y) :
        return x*y
    return km

bus = rate (0.03)
car = rate (0.24)
motor = rate (0.06)
print('carbon_foot_bus = ' , bus(100))
print('carbon_foot_car = ' , car(100))
print('carbon_foot_motor = ' , motor(100))

#

def f5(a, b, c=3, d=4): 
    print(a, b, c, d)
f5(1, *(5, 6))

#

def f4(a, **kargs): 
    print(a, kargs)
f4(a=1, c=3, b=2)

#

def y(n) :
    if n == 0 :
        return 0
    elif n == 1 :
        return 1
    elif n > 1 :
        return y(n - 1) + y(n - 2)
print ('total = ' , y(30))

