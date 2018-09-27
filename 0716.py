# class Car :
#     def __init__(self, color, speed = 0) :
#         self.color = color
#         self.speed = speed

#     def boost(self, m) :
#         while self.speed < m :
#             self.speed += 1
#         return self.speed
        
#     def step_break (self, m, n) :
#         self.speed = m
#         while self.speed > n :
#             self.speed -= 1
#             return self.speed

#     def get_speed (self) :
#         return self.speed

#     def set_speed (self, newspeed) :
#         if newspeed < 0 or newspeed > 100 :
#             return 'Error'
#         else :
#             self.speed = newspeed

# x = Car('Blue')
# x.boost(10)
# print (x.speed)
# x.set_speed(80)
# print (x.speed)
# x.step_break(30, 25)

class Animal :
    def __init__(self) :
        self.feet_number = 4
    def shout (self) :
        print ('Hello! Im an animal')

class Dog(Animal) :
    pass

dog = Dog()
print (dog.feet_number)
dog.shout()

# class Car():
#     def shout(self):
#         print("I'm a Car!")

# class Bus(Car):
#     def shout(self):
#         print("I'm a Bus!")

# class Truck(Car):
#     def shout(self):
#         print("I'm a Truck!")

# # polymorphism 的意思就是 Car, Bus, Truck 分別呼叫了 function shout，但結果不一樣。
# # polymorphsim 也可以用加號舉例，3 + 4 和 '3' + '4' 是不一樣的，加號就是多型。

# def div(dividend, divisor):
#     print("The answer is {}".format(dividend/divisor))

# for i in range(5, -1, -1):
#     for j in range(5, 1, -1):
#         div(i, j)

# try :
#     print ('In try block')
# except Exception:
#     print ('In exception block')
# else :
#     print ('No exception')

# try :
#     print (int('a'))
# except ValueError :
#     print ('ValueError')
# else :
#     print ('No exception')

# try :
#     n = y
# except NameError as e :
#     print (e)
#     print (type(e))
#     print (e.args)

# a = [1, 2, 3]
# try:
#     num = y
#     print(a[100])
    
# except NameError as e:
#     print("I'm in NameError! ")
#     print(e)
# except IndexError as e:
#     print("I'm in IndexError!" )
#     print(e)
# else:
#     print("I'm in else!")

# def func () :
#     try:
#         print("hello!")
#         x = gggggg
#     except Exception as e:
#         print(e)
#         return

#     finally:
#         print("I'm in finally!")
# func()

# def f(a, b):
#     if b == 0:
#         raise IndexError("divisor cannot be zero!")
#     else: return a/b

# num = f(1,0)
# print(num)

def ex(a, b) :
    # if b == 5 :
    #     raise TypeError('int vs str')
    try :
        # a == b
        if True :
            raise TypeError
            print (int('a'), int('b'))
    except ValueError :
        print ('Error')
        return 123
    else :
        print ('No Error')
    finally :
        print ('Finally')

print (ex(3, 5))