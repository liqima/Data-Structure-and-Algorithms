def selection_sort(a_list):
	for pass_num in range(len(a_list) - 1):
		print(a_list)
		max_position = 0
		for i in range(len(a_list)- pass_num):
			if a_list[i] > a_list[max_position]:
				max_position = i
		position = len(a_list) - 1 - pass_num
		a_list[max_position], a_list[position] = a_list[position], a_list[max_position]
	return a_list		

a_list = [5, 2, 10, 6, 2, 9]
print(selection_sort(a_list))