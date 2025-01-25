# a = 30
# b = 20

# print(10 + 20)
# print(10 - 20)
# print(10 * 20)

# print(a + b)
# print(a - b)
# print(a * b)

# a = 01

# print(a)
# print(type(a))

# print(6 & 3)

# a = 'Bangladesh'
# b = str(20)
# b = '20'
# b = 20

# print(a + str(b))

# print(type(a))

# a = int(input('Enter A Number :'))
# b = int(input('Enter 2nd Number :'))

# a = input('Enter A Number :')
# b = input('Enter 2nd Number :')

# # print(int(a) + int(b))
# print(int(a) + float(b))


# a = 'I Love Bangladesh'
# a = 'i love bangladesh'

# print(a[-17:])

# print(a[::-1])

# print(a.upper())
# print(a.lower())
# print(a.capitalize())
# print(a.title())
# print(a.find('e'))
# print(a.replace('bangladesh','india'))
# print(a.swapcase())

# print(len(a))

# print(a[:-11:-1])

# print(a.index('B'))
# print(a.strip('.'))
# print(a.split())

# b = a.split()

# b.insert(2, 'very Much')

# c = ' '.join(b)

# print(c)

# b = a.strip()
# c = ''.join(b.split())

# print(len(c))
# c = a.split()
# b = ''.join(c)
# print(b)




# b = input('Insert a User Name : ')
# c = input('Insert a User Age : ')
# d = input('Insert a Subject : ')

# b= 20
# c = 45
# d = 79

# # print(a.format(b,c,d))
# a = f''' Username : {b}
#         Age : {c}
        # Subject :  {d} '''
# print(a)

# print(f'I {d} love Bangladesh {b} {b + c}')

# a = 'I Love Bangladesh'

# print(a[::-1])

# print(a[:])

# + - * / % ** //

# a = 10
# b = 6

# print(a // b)

# =

# a = 10
# b = 20
# c = 30
# a = 12
# a = a + 3
# a += 3
# a **= 3
# a = 3

# print(a)

# == != > < >= <=

# print(a <= b)

# and or not

# print(not(a <= b and b > c))
# a = 'I love BangLadesh'
# print(' ' in a)

    
# 0 = 0 0 0 0 
# 1 = 0 0 0 1
# 2 = 0 0 1 0
# 3 = 0 0 1 1
# 4 = 0 1 0 0
# 5 = 0 1 0 1
# 6 = 0 1 1 0
# 7 = 0 1 1 1

# & | ^ ~ << >>

# a = 6
# b = 3
# c = 4
 
# d = a ^ b ^ c


# 0 1 1 0
# 0 0 1 1
# 0 1 0 0

#   0  0 0 1

# print(d)

# a = 30

# b = 30

# if a > b:
#     print('a is bgger than b')
# elif a < b:
#     print('a is less than b')
# else:
#     print('Invalid')

# == != < > <= >= 

# if a > b or a * b == 900:
#     print('a is bgger than b')
# elif a < b:
#     print('a is less than b')
# else:
#     print('Invalid')

# score = int(input('Enter A Score :'))

# if score <= 100 and score >= 0:
#     if score >=80 or score >78:
#         if score == 79:
#             score += 1
#             print(f'A+ {score}')
#     elif score >=70:
#         print('A')
#     elif score >=60:
#         print('A-')
# else:
#     print('Invalid Score')

# while for

# a = 1
# while a == 10:
#     print('Bangladesh')

# print(a==10)

# while True:
#     print('Bangladesh')

# while a <= 10:
#     print(a)
#     # a = a + 1
#     if a == 9:
#         break
#     a+=1

# while a < 10:
#     a += 1
#     if a == 6 or a == 8:
#         continue
#     print(a)

# while a <= 10:
#     print(a)
#     # a = a + 1
#     if a == 6:
#         continue
#     a+=1

# a = 'I Love Bangladesh'

# for i in a:
#     print(i)



# for i in range(1,11,2):
#     print(i)


# for j in a:
#     print(j,end="")

# for i in a:
#     if i == 'B':
#         continue
#     print(i,end="")



# a = int(input('Enter A Number : '))

# b = 1
# while b <= 10:
#     print(f'{a} X {b}= {a * b}')
#     b+= 1

# a = [12,12.4,'Bangladesh',True,3434]
# a = 'Bangladesh'
# print(a[1])
# print(type(a))
# print(a)

# a.append('India')

# print(a.index(12))
# a.insert(2,'India')

# b = a.copy()
# print(a)
# b.insert(2,'India')
# print(b)
# print(a.count(12))
# a.remove('Bangladesh')
# a.pop()
# print(a)

# a = [12.23,4.34,3,23.45,45,4,8,2]
# a.sort(reverse=True)
# print(a)
# a.reverse()
# print(a)
# a.clear()
# print(a)

# a = []

# for i in range(1,11):
# 	a.append(i)

# print(a)
# Result = []
# while True:
# 	print('Type "A" or "a" for Add')
# 	print('Type "B" or "b" for Sub')
# 	print('Type "C" or "c" for Mult')
# 	print('Type "D" or "d" for Div')
# 	print('Type "E" or "e" for Exit')
# 	print('===========================')
# 	operator = input('Enter A Operator : ').lower()
	
# 	if operator == 'a':
# 		num1 = int(input('Enter First Number : '))
# 		num2 = int(input('Enter 2nd Number : '))
# 		cal = num1+num2
# 		print(f'{num1} + {num2} = {cal}')
# 		Result.append(cal)
# 		print('===========================')
# 	elif operator == 'b':
# 		num1 = int(input('Enter First Number : '))
# 		num2 = int(input('Enter 2nd Number : '))
# 		cal = num1-num2
# 		print(f'{num1} - {num2} = {cal}')
# 		Result.append(cal)
# 		print('===========================')
# 	elif operator == 'e':
# 		break
# 	else:
# 		print('Invalid Input')
		# print('===========================')

# print(Result)

# a = 'Bangladesh'

# print(a.lower())

# a = (12,34,'Bangladesh')
# a = (12, 34, 'Bangladesh', 'India')

# print(type(a))

# print(a.count(12))
# print(a.index(34))

# b = list(a)
# b.append('India')
# a = tuple(b)
# print(b)
# print(a)

# a = [12, 34, 'Bangladesh', 'India']

# for i in a:
# 	if i == 'Bangladesh':
# 		# print(a.index(i))
# 		b = a.index(i)
# 		# c = a[b]
# 		# print(c.upper())
# 		a.insert(b,i.upper())
# 		a.pop(b+1)
	# print(i)

# print(a.index('Bangladesh'))
# print(a)


# a = {'name':'Rahim','age':34,'Salary':12350}

# print(a.keys())

# for i, j in a.items():
# 	print(i,j)
	# print(i)
	# for j in i:
	# 	print(j)

# a.clear()
# b = a.copy()
# b.pop('Salary')

# b.popitem()
# b.setdefault('Salary')
# b.update({'Salary': 12121})

# c = {}

# c.setdefault()

# b.setdefault('Salary','565656')
# print(c)
# print(b)

# a = {'asdjh',234,4545,234}
# b = {234,'Bangladesh',565,'asdjh',4545}
# print(a)
# print(type(a))
# a.add('hjhj')
# a.clear()
# b= a.copy()
# b.pop()
# b.remove(234)
# b.discard(234)
# print(b)

# for i in a:
# 	print(i)

# c = a.difference(b)
# c = a.intersection(b)
# c = a.union(b)
# print(c)
# c = a.issubset(b)

# print(c)


# a = ['bangladesh',34,67,56.45,'bangladesh',34,67,56.45,'bangladesh',56.45]

# b = []
# for i in a:
# 	if i in b:
# 		continue
# 	else:
# 		b.append(i)

# print(b)

# b = set(a)
# a = list(b)
# print(a)

# def rahim():
# 	print('Hello Python')


# rahim()

# def my_func(num1,num2):
# 	x = num1 + num2
# 	return x

# a = int(input('Enter A Number : '))
# b = int(input('Enter A Number : '))

# print(my_func(a,b))

# y = my_func(a,b)

# print(y)

# def my_func(*name):
# 	# print(f'Hello Mr {name[2]}')
# 	a = ''
# 	for i in name:
# 		a += i
# 	print(a)


# a = input('Enter Your First Name : ')
# b = input('Enter Your Middile Name : ')
# c = input('Enter Your Last Name : ')
# a = input('Enter A Number : ')
# b = input('Enter A Number : ')
# c = input('Enter A Number : ')
# d = int(input('Enter A Number : '))
# e = int(input('Enter A Number : '))
# f = int(input('Enter A Number : '))


# my_func(a,b,c)

# a = 12
# b = 23

# if a > b:
# 	print('a is bigger than b')
# else:
# 	print('a is smaller than b')

# c = 'a is bigger than b' if a > b else 'a is smaller than b' 

# print(c)

# a = {i for i in range(1,11)}
# print(a)

# a = lambda num1,num2: num1 + num2

# print(a(12,12))

# def factorial(n):
# 	if n == 0 or n == 1:
# 		return 1
# 	return n * factorial(n-1)


# print(factorial(3))

# def coutdown(n):
# 	if n == 0:
# 		# pass
# 		print('!Done')
# 	else:
# 		print(n)
# 		coutdown(n-1)

# coutdown(10)

# a = open('E:\\Universal IT\\my file.txt', 'r')
# a = open('../my file.txt', 'r')
# print(a.read())
# print(a.readline())
# print(a.readline())

# for i in a:
# 	print(i)

# a = open('../my file.txt', 'a')
# a.write('Everythings is new - 2')
# a.close()


# a = open('../my file.txt', 'r')
# print(a.read())

# try:
# 	a = open('../my file.txt', 'x')
# 	a.write('Everythings is new - 2')
# 	a.close()

# 	a = open('../my file.txt', 'r')
# 	print(a.read())
# # except:
# # 	print('This File is Already Exist.')
# except Exception as e:
# 	print(e)

# while True:
# 	try:
# 		a = float(input('Enter A Number : '))
		
# 		if a == 1:
# 			break
# 		else:
# 			b = float(input('Enter A Number : '))
# 			c = a + b
# 			print(c)
# 	except:
# 		print('Invalid Input ! Try Again')
# 	else:
# 		print(f'Successfully Done! Outut is {c}')

# while True:
# 	a = int(input('Enter A Number : '))
# 	b = int(input('Enter A Number : '))
# 	if a == 10:
# 		break
# 	else:
# 		print(a + b)


# import my_moudle

# from my_moudle import my_var, my_var_3,my_var_6,my_func


# print(my_var)
# print(my_var_3)
# print(my_var_6)

# import datetime

# a = datetime.datetime.now()
# print(a.strftime("%c"))

# my_moudle.my_func(12,34)

# import turtle

# screen = turtle.Screen()
# screen.bgcolor("lightblue")
# screen.title('Default Module Check')

# my_var = turtle.Turtle()

# shapes = ["arrow", "turtle", "circle","square", 'triangle', "classic"]

# for shape in shapes:
#     my_var.shape(shape)
#     my_var.penup()
#     my_var.forward(100)
#     my_var.stamp()
#     my_var.backward(100)
    
# screen.mainloop()

# screen = turtle.Screen()
# screen.bgcolor('white')
# screen.title('My Title')

# my_var = turtle.Turtle()

# my_var.shape('square')
# my_var.color('red')
# my_var.speed(1)

# for _ in range(4):
#     my_var.forward(100)
#     my_var.left(90)

# # my_var.penup()
# my_var.goto(-100,100)
# # my_var.pendown()

# my_var.color('green')
# my_var.circle(100)

# screen.mainloop()

# import os

# os.mkdir('My_folder')

# class my_class:
# 	a = 10
# 	# def my_fun(self,c,d):
# 	# 	print(c + d)
# 	def __init__(self):
# 		print('I Love Bangladesh')

# x = my_class()

# class Father:
# 	a = 10
# 	b = 20

# class Child(Father):
# 	c = 30
# 	d = 40

# x = Child()

# print(x.b)

# class car:
# 	def move(self):
# 		print('Drive')
# class Boat:
# 	def move(self):
# 		print('Sail')
# class Plane:
# 	def move(self):
# 		print('Fly')

# a = car()
# b = Boat()
# c = Plane()



# def add(*args):
# 	return sum(args)

# print(add(2,3,5))
# print(add(2,3))
# print(add(2,3,6,7,8))

# class A:
# 	def add(self,*args):
# 		return sum(args)

# class B:
# 	def add(self,*args):
# 		return args

# class C:
# 	def add(self,*args):
# 		self.num = []
# 		for i in range(1,11):
# 			self.num.append(i)
# 		return self.num


# x = A()
# y = B()
# z = C()

# s = int(input('Enter A Number : '))
# t = int(input('Enter A Number : '))
# g = input('Enter A Number : ')
# # print(x.add(1,2))
# print(x.add(s,t))
# print(y.add(g))
# print(z.add(23,5))



class Father:
	a = 10
	b = 20
# class Mother:
# 	s = 30
# 	t = 50

# class Child(Father,Mother):
# 	c = 30
# 	d = 40

# x = Child()

# print(x.b)

# class fileHandler:
# 	def __init__(self,file_name,mode):
# 		self.file = open(file_name,mode)
# 		print(f"{file_name} {mode}")
	
# 	def write_data(self,data):
# 		self.file.write(data)
# 		print(f"Data Write Successfully")
	
# 	def __del__(self):
# 		self.file.close()
# 		print("File Closed")
	

# file_handel = fileHandler('My_file.txt','w')
# file_handel.write_data("I Love Bangladesh")
# del file_handel


# print(Father.a)