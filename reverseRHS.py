#Extra Exercise，key point：印完空白再印星星，印完之後換行。
for i in range (1, 6, 1) :
    print ('  ' * (i-1) , end = ' ')    #在每一次run到i的時候根據 i 的值空多少格，不能放在for j 底下，否則會跟著 j 走。
    for j in range (5, 0, -1) :
        if i*j > 9 :                    #這兩行可以不用寫，只判斷有寫if的地方，其他不管。
            continue
        if i * j <= 9 :
            print ('*', end = ' ')
    print ('')