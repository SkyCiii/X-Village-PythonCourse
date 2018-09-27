
#

def function() :
    x = 3           # function是要「動」的東西，所以如果我函數的內容物是靜態的（x = 3好比是初始衛生紙有 3 包），
                    # 那我就不會回傳東西，即回傳None。
#

class NewType :
    y = 3 # ( attribute , variable )    # class 可以理解成進階的 function，裡面可以儲存「靜」的東西，
    def Buy_z1(self) :                        # 也可以儲存「動」的東西（method）。
        for i in range (1, 10) :        # Class 裡：初始衛生紙有 3 包，也有另幾個函數是每天增加一包或每天增加兩包。
            y = y + 1
            print (y)
    def Buy_z2(self) :
        for j in range (1, 10) :
            y = y + 2
            print (y)

z1 = NewType()                          # 雖然 z1 和 z2 都被 assign 了 NewType 這個 class，
z2 = NewType()                          # 但是可以把 z1 和 z2 理解成兩家不同人，但他們家的初始衛生紙都是 3 包，
                                        # 又因為 class 可以儲存靜態的東西，所以需要一個儲存位址，即儲存instance object，
                                        # 在兩個不同的記憶體位置（兩家不同人），直到我再寫出 class.Buy1，才會開始增加衛生紙。

class Human :
    blood_color = 'red'
    eye_shape = 'circle'
    def cry(self) :
        print ('crying')
    def set_name(self, your_name) :
        self._name = your_name

p1 = Human ()
p2 = Human ()

p1.cry ()           #背後運作機制：Human.cry(p1)
p2.cry ()           #背後運作機制：Human.cry(p2)

print (p1.blood_color)

p1.blood_color = 'Blue'
print (p1.blood_color)

p1.my_name = 'SkyC'
print (p1.my_name)

#print (p2.my_name) # my_name 這個 attiburte(variable) 是在 p1 後來的 scope 底下，
                    # 不會更改原本的 class Human，所以 p2 找不到 my_name。

p1.set_name('SkyCiii')
print (p1._name)

#

class Shape :
    def set_edge(self, n) :
        self.edge = n
    def display(self) :
        for i in range (self.edge, 0, -1) :
            for j in range (1, self.edge+1) :
                if i + j > self.edge+1 :
                    break
                else :
                    print ('* ' ,end = '')
            print ('')
        

x = Shape()
x.set_edge(10)
x.display()