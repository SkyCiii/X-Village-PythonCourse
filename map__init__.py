
#class HW2

class Life :

    def __init__ (self, n, p) :
        self.set_map_lis1 = []
        self.set_map_lis2 = []

        for a in range (1, n+1) :
            for b in range (1, n+1) :
                self.set_map_lis1.append('*')
            self.set_map_lis2.append(self.set_map_lis1)
            self.set_map_lis1 = []

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

n = int(input ('n x n map = '))
p = int(input ('glider = '))
x = Life(n, p)
x.display()
