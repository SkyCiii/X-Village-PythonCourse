
#A

Score = 91
if Score > 90 :
    Extra_pay = 8000
elif 70 <= Score <= 90 :
    Extra_pay = 6000
elif Score < 70 :
    Extra_pay = 4000

Extra_hour = 20

print ('A : Score = 91 ,' , 'Extra_hour = 20 ,' , 'Pay = ' , Extra_pay + Extra_hour*200 )

#B

Score = 75
if Score > 90 :
    Extra_pay = 8000
elif 70 <= Score <= 90 :
    Extra_pay = 6000
elif Score < 70 :
    Extra_pay = 4000

Extra_hour = 15

print ('B : Score = 75 ,' , 'Extra_hour = 15 ,' , 'Pay = ' , Extra_pay + Extra_hour*200 )

#C

Score = 60
if Score > 90 :
    Extra_pay = 8000
elif 70 <= Score <= 90 :
    Extra_pay = 6000
elif Score < 70 :
    Extra_pay = 4000

Extra_hour = 25

print ('C : Score = 60 ,' , 'Extra_hour = 25 ,' , 'Pay = ' , Extra_pay + Extra_hour*200 )

#D

Score = 75
if Score > 90 :
    Extra_pay = 8000
elif 70 <= Score <= 90 :
    Extra_pay = 6000
elif Score < 70 :
    Extra_pay = 4000

Extra_hour = 10

print ('D : Score = 75 ,' , 'Extra_hour = 10 ,' , 'Pay = ' , Extra_pay + Extra_hour*200 )

#E

Score = 80
if Score > 90 :
    Extra_pay = 8000
elif 70 <= Score <= 90 :
    Extra_pay = 6000
elif Score < 70 :
    Extra_pay = 4000

Extra_hour = 10

print ('E : Score = 80 ,' , 'Extra_hour = 10 ,' , 'Pay = ' , Extra_pay + Extra_hour*200 )

#F

Score = 90
if Score > 90 :
    Extra_pay = 8000
elif 70 <= Score <= 90 :
    Extra_pay = 6000
elif Score < 70 :
    Extra_pay = 4000

Extra_hour = 25

print ('F : Score = 90 ,' , 'Extra_hour = 25 ,' , 'Pay = ' , Extra_pay + Extra_hour*200 )

#G

Score = 45
if Score > 90 :
    Extra_pay = 8000
elif 70 <= Score <= 90 :
    Extra_pay = 6000
elif Score < 70 :
    Extra_pay = 4000

Extra_hour = 14

print ('G : Score = 45 ,' , 'Extra_hour = 14 ,' , 'Pay = ' , Extra_pay + Extra_hour*200 )

#H

Score = 95
if Score > 90 :
    Extra_pay = 8000
elif 70 <= Score <= 90 :
    Extra_pay = 6000
elif Score < 70 :
    Extra_pay = 4000

Extra_hour = 13

print ('H : Score = 95 ,' , 'Extra_hour = 13 ,' , 'Pay = ' , Extra_pay + Extra_hour*200 )

#I

Score = 88
if Score > 90 :
    Extra_pay = 8000
elif 70 <= Score <= 90 :
    Extra_pay = 6000
elif Score < 70 :
    Extra_pay = 4000

Extra_hour = 2

print ('I : Score = 88 ,' , 'Extra_hour = 2 ,' , 'Pay = ' , Extra_pay + Extra_hour*200 )

#Function

def f(Score) :
    if Score > 90 :
        return 8000
    elif 70 <= Score <= 90 :
        return 6000
    elif Score < 70 :
        return 4000

def g(Extra_hour) :
    return Extra_hour * 200

print ('A : Score = 91 ,' , 'Extra_hour = 20 ,' , 'Pay = ' , f(91) + g(20) )
print ('B : Score = 75 ,' , 'Extra_hour = 15 ,' , 'Pay = ' , f(75) + g(15) )
print ('C : Score = 60 ,' , 'Extra_hour = 25 ,' , 'Pay = ' , f(60) + g(25) )
print ('D : Score = 75 ,' , 'Extra_hour = 10 ,' , 'Pay = ' , f(75) + g(10) )
print ('E : Score = 80 ,' , 'Extra_hour = 10 ,' , 'Pay = ' , f(80) + g(10) )
print ('F : Score = 90 ,' , 'Extra_hour = 25 ,' , 'Pay = ' , f(90) + g(25) )
print ('G : Score = 45 ,' , 'Extra_hour = 14 ,' , 'Pay = ' , f(45) + g(14) )
print ('H : Score = 95 ,' , 'Extra_hour = 13 ,' , 'Pay = ' , f(95) + g(13) )
print ('I : Score = 88 ,' , 'Extra_hour = 2 ,' , 'Pay = ' , f(88) + g(2) )

#

def h(n) :
    row = [1]
    for i in range(n):
        print ('  ' * (n-i) , end = ' ')
        print (row)
        #print (row[:])
        p = row[:]      # row[:]和 row 基本上是同一個東西。
        for j in range(1, len(row)):
            row[j] = p[j] + p[j-1]
        row.append(1)

h(9)

