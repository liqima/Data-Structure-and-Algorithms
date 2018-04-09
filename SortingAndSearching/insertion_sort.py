def insertion_sort(a_list):
	for index in range(1, len(a_list)):
		print(a_list)
		current_value = a_list[index]
		position = index
		while position > 0 and a_list[position - 1] > current_value:
			a_list[position] = a_list[position - 1]
			position -= 1
		a_list[position] = current_value
	return a_list

a_list = [1, 7, 2, 66, 3, 5, 4]
print(insertion_sort(a_list))

