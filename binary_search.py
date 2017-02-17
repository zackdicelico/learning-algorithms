def binary_search(lst, choice):
		low = 0             # lists are 0 indexed!
		high = len(lst) - 1 # calculate the last element index
		                    # (what's the index of lst[-1] ?)
		print('Searching for {0} in {1}'.format(choice, lst))
		while low <= high:
			mid = round((low + high) / 2) # calculate the index of the middle element
			print('mid is {0}'.format(mid))
			guess = lst[mid]             # pick the middle item to start
			print('guess is {0}'.format(guess))
			
			# ['a', 'b', 'c', 'd', 'e'] <-- list
			#   ^    ^    ^    ^    ^   <-- element
			#   0    1    2    3    4   <-- index
			# A list is an ordered collection of items.
			# Order is maintained/accessed via indices.
			
			if guess == choice:
				print('Found your choice {0} at index {1}'.format(choice, mid))
				return mid # if the guess is the item at index list[mid], return it!
				
			if guess > choice:
				high = mid - 1 # decrement the high if the is guess to the "left" of the user's choice
				print('your choice is to the left of my guess! searching...')
			else:
				low = mid + 1 # increment the low if the guess is to the "right" of the user's choice
				print('your choice is to the right of my guess! searching...')

		return None
		
my_list = ['bear', 'cat', 'dog', 'lion', 'panda', 'snail']
my_choice = 'panda'
binary_search(my_list, my_choice)


