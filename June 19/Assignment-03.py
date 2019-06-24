#Date: 19 June 2019
#Author: Suchita Dmello


def bubble_sort(input_list):
	bubble_list = input_list
	temp = []
	for i in range(len(bubble_list)):
		for j in range(0, len(bubble_list)-i-1):
			if bubble_list[j] > bubble_list[j+1]:
				bubble_list[j], bubble_list[j+1] = bubble_list[j+1], bubble_list[j]
	return bubble_list

def quick_sort(lst):
	quick_list = lst
    if not quick_list:
		return []
    return (quick_sort([x for x in quick_list[1:] if x <  quick_list[0]])
            + [quick_list[0]] +
            quick_sort([x for x in quick_list[1:] if x >= quick_list[0]]))

def selection_sort(input_list):
	selection_list = input_list
	for i in range(len(selection_list)):  
		min_idx = i 
		for j in range(i+1, len(selection_list)): 
			if selection_list[min_idx] > selection_list[j]: 
				min_idx = j         
		selection_list[i], selection_list[min_idx] = selection_list[min_idx], selection_list[i]
	return selection_list
	
	
def merge_sort(arr):
	merge_list = arr
	mid = int(len(merge_list)/2)
	print(mid)
	left_list = merge_list[:mid]
	right_list = merge_list[mid:]
	print(left_list)
	print(right_list)
  
	
input_list = [34,56,21,2,4,90,43,23]
print("Bubble Sort ==> ",bubble_sort(input_list))
print("Quick Sort ==> ",quick_sort(input_list))
print("Selection Sort ==> ",selection_sort(input_list))
print("Merge Sort ==> ",merge_sort(input_list))
			
		
			
			
			
#Question 1			
input_string = input("\nEnter string: ")
words_list = []
word = ''
for index,ch in enumerate(input_string):
	if ch == ' ' and index != len(input_string)-1:
		words_list.append(word)
		word = ''
	else:
		word = word + ch
words_list.append(word)
print("Output A) ==> ",words_list)
sorted_word_list = quick_sort(words_list)
sorted_list = []
print("Output B) ==> ",sorted_word_list)
for word in sorted_word_list:
	sorted_list.append(''.join(quick_sort(word)))
print("Output C) ==> ",sorted_list)
		
