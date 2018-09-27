x = 'World'
def func():
    x = 'Hello'
    print(x)
    
func()                          #因為函數的內容已經包含 print，所以可以直接呼叫 func()，就像直接呼叫 print()。
print(x)

#

y = 'Spam'
def fun():
    y = 'HI!'
    
print(y)                        #這裡的 print 放在 globl scope，且沒有呼叫fun()，所以 y 是 print 'Spam' 。

#

w = 22
def outer():
    w = 23
    def inner():
        w = 24
        print('first: ', w)     # first print
    inner()                     # inner() 要放在這裡因為 inner 在 local 被定義，local 以外的 scope 不認識 inner()。
    print('second: ', w)        # second print

outer()
print('third: ', w)             # third print

#

x = 88                          # 在 global scople 下把 88 assign 給 x。
def f(): 
    global x                    # 在 def 內部（local scope）先把 x 設定為可以影響 global 的狀態。
    x = 99                      # 這裡的 x 重新 assign 99 給他，會改變 global scope x 的值。

f()
print(x)

#

print ('a' , 'b' , end = '\t')  # print 是一個 built-in 的 function，所以我輸入 print 其實是呼叫已經存在在內部的函數。

#以下不要理他，會用就好。

def h(**kwargs):
    print(kwargs)
h(key=1, key2=2, key3=3)

#

def g(a):                       #3 #2即是把 88 也 assgin 給 a，此時 a = 88。
    a = 99                      #4 這個函式的內容是指，不論 a = 多少被input，輸出值都是 a = 99，即後來 99 又 re-assign 給 a。
b = 88                          #1 首先 88 assign 給 b。
g(b)                            #2 88 這個 object 丟入函數裡面。
print(b)                        #5 a 和 b 都是variable，彼此之間不能互相影響，只能修改與 object 之間的連結 (reference)。