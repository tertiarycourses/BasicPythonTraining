# Python Essential Training
# Module 3: Control Structures
# Author: Dr. Alfred Ang
# Update: 19 Jan 2017

# a = 7
# b = 7

# if (a<b):
# 	print("a is smaller than b")
# elif (a>b):
# 	print("a is larger than b")
# else:
# 	print("a is same as b")

# order = 100
# discount = 25 if order > 200 else 0
# print(discount)

# grade = "D"
grade = input('What is your grade')

if (grade == 'A'):
	print("Excellent")
elif (grade == "B"):
	print("Well Done!")
elif (grade == 'C'):
	print("Work Harder")
else:
	print('I don\'t know your grade\n')
	print("the end")

# Loop

# a = 1
# while (a<10):
# 	print(a)
	#a += 1

# a = 1
# b = 1
# while (b<100):
# 	a,b = b,a+b
# 	print(a)

# For Loop

# a = (3,4,7,9)
# for i in a:
# 	print(i)

# for i in range(1,11):
	#if i==4:continue
	# if i==4:break
	# print(i)

# a = []
# for i in range(1,11):
# 	a.append(i*i)
# print(a)

# person = ['Ally','Belinda','Jane']
# height = [168,155,170]
# weight = [60,68,55]

# for index, name in enumerate(person):
# 	#print(index, name)
# 	print("{} height is {}cm and weight is {}kg".format(name,height[index],weight[index]))

# c = zip(person,height,weight)
#print(list(c))

# for name, h, w in c:
# 	print("{} height is {}cm and weight is {}kg".format(name,h,w))

# for i in range(1,11):
# 	if i==4:break
# 	print(i)
# else:
# 	print("no break")

# primes = []
# for n in range(1,101):
# 	for divisor in range(2, n):
# 		if n%divisor == 0:break
# 	else: 
# 		primes.append(n)

# print(primes)

