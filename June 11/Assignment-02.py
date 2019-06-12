#Date: 11 June 2019
#Author: Suchita Dmello

#Question 1
x=[1,2,3,4,[10,20,30,40,[100,200,300,400],"rishabh_",5+5j],4000]
print(x[4][0:2])
print(x[4][-1])
print(x[4][4][2:])
print(x[4][3:6])

#Question 2
x = list(range(1,21))
result = set()
for i in range(1,21):
	for j in range(2,21):
		if (i+j) % 2 == 0 and i!=j:
			pair = sorted([i,j])
			result.add(tuple(pair))
print("\nPair with sum as even from range 1 to 20 are:")			
print(result)

#Question 3
input_string = input("\nEnter string: ")
result = dict()
for ch in input_string:
	if not ch.isalnum():
		count = result.get(ch, 0)
		result[ch] = count + 1
print("Count of special character in string:")
print(result)
	
#Question 4
print("\nList of number from range 1 to 50 with cube as odd number are:")
print([x for x in range(1,50) if (x*x*x) % 2 != 0])

#Question 5
input_list = input("\nEnter a list element separated by space: ")
input_list = input_list.split(" ")
print(input_list)
result = []
for item in input_list:
	if item.isdigit() and int(item) % 3 == 0:
		result.append(item)
print(result)


#Question 6
input_string = input("\nEnter string: ")
input_string = input_string.split(" ")
result = dict()
for word in input_string:
	result[word] = len(word)
print(result)

#Question 7
input_list = input("\nEnter a list element separated by space: ")
input_list = input_list.split(" ")
print("List contains all the integer value:")
result = "True"
for item in input_list:
	if not item.isdigit():
		result = "False"
		break
print(result)


	