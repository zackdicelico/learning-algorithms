import random

def quicksort(lst):
	""" Implement the quicksort algorithm in python! 
	visualize at https://goo.gl/z8TDy7
	"""
		
	if len(lst) < 2:
		return lst
		
	pivot = random.choice(lst)
	
	less = [item for item in lst if item < pivot]
	greater = [item for item in lst if item > pivot]
	
	return [
		*quicksort(less),
		pivot,
		*quicksort(greater)
	]
					
my_list = ['3', '2', '5', '4', '1']
quicksort(my_list)
