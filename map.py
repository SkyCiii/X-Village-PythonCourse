
#class HW1

class Life :

    def set_map(self, n) :
        self.set_map_lis1 = []
        self.set_map_lis2 = []

        for a in range (1, n+1) :
            for b in range (1, n+1) :
                self.set_map_lis1.append('*')
            self.set_map_lis2.append(self.set_map_lis1)
            self.set_map_lis1 = []

    def set_pattern(self, n, p) :
        if p == 1 :
            self.set_map_lis2[int((n-1)/2)-1][int((n-1)/2)-1] = '0'
            self.set_map_lis2[int((n-1)/2)-1][int((n-1)/2)] = '0'
            self.set_map_lis2[int((n-1)/2)-1][int((n-1)/2)+1] = '0'
            self.set_map_lis2[int((n-1)/2)][int((n-1)/2)-1] = '0'
            self.set_map_lis2[int((n-1)/2)+1][int((n-1)/2)] = '0'
        if p == 0 :
            pass
    
    def display(self) :

        for c in range (0, n) :
            print (self.set_map_lis2[c], end = ' ')
            print ('')
            print ('')

x = Life()
n = int(input ('n x n map = '))
p = int(input ('glider = '))
x.set_map(n)
x.set_pattern(n, p)
x.display()
