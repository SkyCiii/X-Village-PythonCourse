f = open ( 'workfile', 'w' )
print (f.write)
print (f.closed)
f.close()
print (f.closed)

# """
# <hello>

# hello world
# hello python
# """

# f = open('hello', 'r')      # 所以可以把 open 理解成一個 Class，且包含 def __init__ ()
# print(f.read())             # open 底下有 method 'read' , 'close' , ...
# f.close()

# with open('hello') as g :
#     print(f.read())
      # f.close()             # 使用 with 的話就不用特別打 close

#csv json HW1

# g = open ('note.txt', 'w+')     # 寫 w 的話，開啟這個檔案的同時只賦予了'寫'的權限，但不能讀，所以後面g.read()沒有權限，要用 w+ 開。
# date = input ('輸入日期')
# event = input ('輸入事件')
# description = input ('輸入心得')
# g.write (date)
# g.write (event)
# g.write (description)
# g.seek(0)                       # 當我寫入幾個字串之後，read 會從結尾的地方開始讀，所以還要再seek(0)回到第 0 個位置。
# print (g.read())
# g.close()

# csv json HW2

import csv
with open ('AQI_20180717100923.csv', 'r', encoding = 'utf-8-sig') as f :
    reader = csv.reader(f)
    min_AQI = []
    for row in reader :
        try :
            int(row[2])
        except ValueError :
            continue
        else :
            min_AQI.append(int(row[2]))
    print ('AQI = ', min(min_AQI))
    f.seek(0)
    reader = csv.reader(f)
    for row in reader :
        try :
            int(row[2])
        except ValueError :
            continue
        else :
            if int(row[2]) == min(min_AQI) :
                print(row [1], row[0])

import json
with open ('05c834d071ad5b62eaf85658de4d2e6f_export.json', 'r+') as g :
    HW3 = json.load(g)
print (json.dumps(HW3, ensure_ascii = False, indent = 4))

#format HW1

# for i in range (1, 10) :
#     for j in range (1, 10) :
#         print ('{0:2}'.format(i), '*', '{0:2}'.format(j), '=', '{0:2}'.format(i * j), end = ' ')
#     print('')

# print (complex(3, 4))
# print (complex(0, -1.2))
# print (abs(5))
# print (abs(-10))
# print (abs(3 + 4j))
# print (pow(2,0))
# print (max('a', 'b', 'c'))
# print (len((0, 0, 0)))

def eight_queens (a, A, b, B, c, C, d, D, e, E, f, F, g, G, h, H) :
    answer_lis = [[a, A], [b, B], [c, C], [d, D], [e, E], [f, F], [g, G], [h, H]]
    for i in range (0, 2) :
        for j in range (0, 8) :
            for k in range (0, j) :
                if answer_lis[j][i] == answer_lis[k][i] :
                    return False
                else :
                    i = 0
                    answer_min = min(answer_lis[j][i], answer_lis[j][i+1])
                    answer_max = max(answer_lis[j][i], answer_lis[j][i+1])
                    for l in range (-answer_min, 8 - answer_max) :
                        if answer_lis[j][i] + l == answer_lis[k][i] and answer_lis[j][i+1] + l == answer_lis[k][i+1] :
                            return False
                    for m in range (answer_min - 7, 8 - answer_max) :
                        if answer_lis[j][i] + m == answer_lis[k][i] and answer_lis[j][i+1] - m == answer_lis[k][i+1] :
                            return False

            for k in range (j+1, 8) :
                if answer_lis[j][i] == answer_lis[k][i] :
                    return False
                else :
                    i = 0
                    
                    answer_min = min(answer_lis[j][i], answer_lis[j][i+1])
                    answer_max = max(answer_lis[j][i], answer_lis[j][i+1])
                    for l in range (-answer_min, 9 - answer_max) :
                        if answer_lis[j][i] + l == answer_lis[k][i] and answer_lis[j][i+1] + l == answer_lis[k][i+1] :
                            return False
                    for m in range (answer_min - 7, 8 - answer_max) :
                        if answer_lis[j][i] + m == answer_lis[k][i] and answer_lis[j][i+1] - m == answer_lis[k][i+1] :
                            return False
        return True

print (eight_queens(0, 4, 1, 0, 2, 3, 3, 5, 4, 7, 5, 1, 6, 6, 7, 2))

# import timeit

# my_code_0 = "my_array_0 = [x for x in range(1000)]"
# my_code_1 = "my_array_1 = list(range(1000))"

# print (timeit.timeit(stmt = my_code_0, number=100000), "\n")
# print (timeit.timeit(stmt = my_code_1, number=100000), "\n")


# import timeit

# my_code_0 = "my_array_0 = [x for x in range(1000)]"
# my_code_1 = "my_array_1 = list(range(1000))"

# print (timeit.repeat(stmt = my_code_0, repeat= 5, number = 100000), "\n")
# print (timeit.repeat(stmt = my_code_1, repeat= 5, number = 100000), "\n")

# import time

# print("休息 10 分鐘~ \n")
# time.sleep(6)
# print("上課啦！上課啦！上課啦！上課啦！上課啦！上課啦！")

# E = [chr(i) for i in range (97, 123)]
# for j in range (0, 26) :
#     E.append(E[j])

# def caesar_cipher(a, b) :
#     caesar_lis = []
#     for k in range (0, len(a)) :
#         for l in range (0, 26) :
#             if a[k] == E[l] :
#                 caesar_lis.append(E[l+3])
#     print('\'', end ='')
#     for m in range (0, len(caesar_lis)) :
#         print (caesar_lis[m], end = '')
#     print('\'')

# caesar_cipher('xvillage', 3)