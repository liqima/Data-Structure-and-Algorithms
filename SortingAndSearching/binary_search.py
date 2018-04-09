def binary_search(a_list, target):
	first = 0
	last = len(a_list) - 1
	found = False
	while first <= last and not found:
		print(a_list[first:last+1])
		mid_position = (first + last) // 2
		if a_list[mid_position] == target:
			found = True
		elif a_list[mid_position] > target:
			last = mid_position - 1
		else:
			first = mid_position + 1
	return found

def binary_search_recursive(a_list, target):
	print(a_list)
	if len(a_list) == 0:
		return False
	else:
		mid_position = (len(a_list)) // 2
		if a_list[mid_position] == target:
			return True
		elif a_list[mid_position] > target:
			return binary_search_recursive(a_list[:mid_position], target)
		else:
			return binary_search_recursive(a_list[mid_position+1:], target)

a_list = [0, 1, 2, 8, 13, 17, 19, 32, 42]
# print(binary_search(a_list, 5))
print(binary_search_recursive(a_list, 42))