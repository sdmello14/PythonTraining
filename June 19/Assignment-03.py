#Date: 19 June 2019
#Author: Suchita Dmello


def bubble_sort(input_list):
	bubble_list = input_list.copy()
	for i in range(len(bubble_list)):
		for j in range(0, len(bubble_list)-i-1):
			if bubble_list[j] > bubble_list[j+1]:
				bubble_list[j], bubble_list[j+1] = bubble_list[j+1], bubble_list[j]
	return bubble_list

def partition(quick_list,low,high): 
    i = ( low-1 )      
    pivot = quick_list[high]     
    for j in range(low , high):  
        if   quick_list[j] <= pivot: 
            i = i+1 
            quick_list[i],quick_list[j] = quick_list[j],quick_list[i] 
    quick_list[i+1],quick_list[high] = quick_list[high],quick_list[i+1] 
    return ( i+1 )

def quick_sort(lst,low,high):
    if low < high: 
        pi = partition(quick_list,low,high) 
        quick_sort(quick_list, low, pi-1) 
        quick_sort(quick_list, pi+1, high)
    return quick_list 

def selection_sort(input_list):
	selection_list = input_list.copy()
	for i in range(len(selection_list)):  
		mid = i 
		for j in range(i+1, len(selection_list)): 
			if selection_list[mid] > selection_list[j]: 
				mid = j         
		selection_list[i], selection_list[mid] = selection_list[mid], selection_list[i]
	return selection_list

def merge_sort(merge_list):
    if len(merge_list) > 1:
        mid = len(merge_list) // 2
        left = merge_list[:mid]
        right = merge_list[mid:]

        merge_sort(left)
        merge_sort(right)
        i = 0
        j = 0
        k = 0
        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                merge_list[k]=left[i]
                i=i+1
            else:
                merge_list[k]=right[j]
                j=j+1
            k=k+1

        while i < len(left):
            merge_list[k]=left[i]
            i=i+1
            k=k+1

        while j < len(right):
            merge_list[k]=right[j]
            j=j+1
            k=k+1
    return merge_list
	
	
  
	
input_list = [34,56,21,2,4,90,43,23]
print("Bubble Sort ==> ",bubble_sort(input_list))
quick_list = input_list.copy()
print("Quick Sort ==> ",quick_sort(quick_list,0,len(input_list)-1))
print("Selection Sort ==> ",selection_sort(input_list))
merge_list = input_list.copy()
print("Merge Sort ==> ",merge_sort(merge_list))
			
		
			
		
#Question 1	

def string_sort(lst):
    if not lst:
	    return []
    return (string_sort([x for x in lst[1:] if x <  lst[0]])
            + [lst[0]] +
            string_sort([x for x in lst[1:] if x >= lst[0]]))

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
sorted_word_list = string_sort(words_list)
sorted_list = []
print("Output B) ==> ",sorted_word_list)
for word in sorted_word_list:
	sorted_list.append(''.join(string_sort(word)))
print("Output C) ==> ",sorted_list)
		
