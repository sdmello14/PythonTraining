#Part 1
print("Part 1")
print("Hello My name is Suchita. I love Coding")
print("This is 'my first program'.")
'''value1 = int(input("Enter first value: "))
value2 = int(input("Enter second value: "))
value3 = int(input("Enter third value: "))
print("Value1 ={}, Value2 ={}, Value3={}".format(value1,value2,value3))
print("Datatype of Value1 ={}, Value2 ={}, Value3={}".format(type(value1),type(value2),type(value3)))'''

#Part 2
print("\nPart 2")
print('Hello! My name is XYX') 
print("Hello I am a candidate")
print("234.56")
print("34")
print("a+3j")

#Part 3
print("\nPart 3")
x= 10+20*(45+67.0)
print("Datatype of x for 10+20*(45+67.0) is",type(x))
x= (True and False) or False
print("Datatype of x for (True and False) or False is",type(x))
x= (True or True) and (not False and True)
print("Datatype of x for (True or True) and (not False and True)is",type(x))
x= (3>89) or (34>32)
print("Datatype of x for (3>89) or (34>32) is",type(x))
x= not True and False
print("Datatype of x for not True and False is",type(x))

#Part 4
print("\nPart 4")
num = int(input("Enter the number= "))
if (num % 2 == 0) and (num % 5 == 0):
	print("Hurray it is what I am looking for")
else:
	print("wrong input")
	
#Part 5
print("\nPart 5")
num = int(input("Enter the number= "))
if (num in range(10,50)):
	print("Yes I am in the range")
else:
	print("Oops")