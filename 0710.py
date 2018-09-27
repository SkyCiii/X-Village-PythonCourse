#Exercise
print ( "Hello World!" )

a = 2
a = 1 
#1 = 2
print ( a )

name0 = "Mary"
print ( name0 )

#for = "Cindy"
#1name  = "Mike"
#+name  = "James"（+ 為運算子）
#name.1 = "Kate"

print ( 354896504 // 123 )
print ( 10 / 3 )                #其值不為3.33333....，而是3.3333...35，是因為二進位能精確表示浮點數。
print ( round(2.5) )            #若小數點後尾數恰為5，則看進位後的整數是否為偶數，若是則進位，若為奇數則捨去。
print ( round(1.5) )
print ( round(2.51) )           #小數點後尾數>5，直接進位。

print ( 1 << 3 )                #把1用二進位表示（即2^0欄位為1），然後把1往左移三個欄位，變成2^3的欄位為1，等於8。

#a = 1
#b = 3
print ( 1 < 3 )

a = 2
a **= 5
print (a)

#Excercise : known x**2 + 2x - 63 = 0
a = 1
b = 2
c = -63
x1 = ( -b + ( b**2 - 4*a*c )**( 1 / 2 ) ) / ( 2 * a )
x2 = ( -b - ( b**2 - 4*a*c )**( 1 / 2 ) ) / ( 2 * a )
print ( x1 )
print ( x2 )

a = 1
print ( 1 + 1 << 2 )
print ( 1 + 1 << 2 >= 3 ) or ( a >= 1 )

numbers = [ 100 , 200 , 300 , 400 , [ 1 , 2 ] ]
            #0    1     2     3     4
            #-5   -4    -3    -2    -1
print ( numbers [ 0 ] )
print ( numbers [ -2 ] )
print ( numbers [ 4 ] )
print ( numbers [ 1 : 4 ] )     #從list的第i個開始，遇到j結束，並列出j-1的值。
print ( numbers [ 0 : 5 : 2] )  #每間隔2抓一次，遇到j結束，並列出j-2的值。
del [ numbers [ 1 : 4 ] ]       #刪除list中第 i ~ j-1 項。
print ( numbers )

a = [ 2 , 4 , 6 ]
b = [ 1 , 3 , 5 , 7 ,9 ]
print ( a + b )
print ( [ 2 , 1, 2 ] + b )

fruit = ( 'apple' , 'banana' , 'grape' , 'watermelon' )
fruit = fruit + ( 'guava' , )   #tuple必須和tuple相加，不能和string相加，所以要加逗號。
print ( fruit )

number = ( 1 , 2 , 3 )
                                #number [ 0 ] = 5（tuple裡面的數值不能分別被修改）
number = ( 4 , 5 , 6 )          #但tuple可以整串被重新assign
print ( number )
number = [ 1 , 2 , 3 ]
number [ 0 ] = 4
number [ 1 ] = 5
number [ 2 ] = 6
print ( number )                #但list裡面的數值可以被更改。

dictionary = {                  #dictionary用大括號表示
    'Chinese' : 98 ,            #裡面由subject list和score list組成
    'English' : 65 ,
    'Math' : 87 ,
    'History' : 77 ,
    'Physics' : 50 ,
    'Chemistry' : 88
}
print ( dictionary )
print ( "Physics score = " , dictionary [ 'Physics' ] )
dictionary [ 'PE' ] = 95        #新增一項數據到dictinoary裡面
dictionary [ 'Physics'] = 100   #修改dictionary裡面的一項數據
print ( "Physics score = " , dictionary [ 'Physics' ] )

#a = input ( "Enter a sentence: " )
#print ( a )
#a = input ( "Enter a number: " )
## print(2 + a)，但a在這裡自動會被視為string，string和int不能相加。

print ( 1 , 2.0 , 3 , '4' , sep = '///' , end = '' )
print ( 1 )                     #end = ''代表最後不要換行，不然print(1)應該會在下一行。
print ( 1 , 2.0 , 3 , '4' , sep = '//' , end = '!!!' )
print ()

#weather = input("Enter the weather: ")
#if weather == 'rainy':      #用==是因為這裡不再assign東西給weather，而是要判斷string是否相等。
#    print("Bring umbrella")
#print("Go out.")

score = 58
if score >= 60:
    print("Yeah! I pass.")
else:
    print("Oh no! I fail.")

score = 68
if score >= 80 :
    if score >= 90 :
        print ( "A" )
    else :
        print ( "B" )
if score >= 60 :
    if score >= 70 :
        print ( "C" )
    else :
        print ( "D" )
print ( 'End' ) 

print ( 0.1*3 )                 #0.1*3因為小數是由二進位組成，並不一定確確實實是0.1，可能是0.99999....。

#Exercise：input一個座標，回傳他所在的象限。
x = input ( "x = " )
x = int ( x )
y = input ( "y = " )
y = int ( y )
if x > 0 :
    if y > 0 :
        print ( "the point is at first quadrant " )
    elif y < 0 :
        print ( "the point is at fourth quadrant " )
elif x < 0 :
    if y > 0 :
        print ( "the point is at second quadrant " )
    elif y < 0 :
        print ( "the point is at third quadrant " )
else :
    print ( "the point is at origin  " )
print ( 'End' )
             