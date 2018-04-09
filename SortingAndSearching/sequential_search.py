def sequential_search(a_list, target):
	found = False
	position = 0
	while position < len(a_list) and not found:
		if a_list[position] == target:
			found = True
		else:
			position += 1
	return found

# a_list = [1, 2, 32, 8, 17, 19, 42, 13, 0]
# search_target = 3
# print(sequential_search(a_list, search_target))
# print(sequential_search(a_list, 13))

# ordered list
def ordered_sequential_search(a_list, target):
	found = False
	stop = False
	position = 0
	while position < len(a_list) and not found and not stop:
		if a_list[position] == target:
			found = True
		elif a_list[position] > target:
			stop = True
		else:
			position += 1
	return found

a_list = [0, 1, 2, 8, 13, 17, 19, 32, 42, 1]
print(ordered_sequential_search(a_list, 13))
print(ordered_sequential_search(a_list, 12))