def quick_sort(a_list):
	quick_sort_helper(a_list, 0, len(a_list) - 1)

def quick_sort_helper(a_list, first, last):
	print(a_list)
	if first < last:
		split_point = partition(a_list, first, last)
		quick_sort_helper(a_list, first, split_point - 1)
		quick_sort_helper(a_list, split_point + 1, last)

def partition(a_list, first, last):
	pivot_value = a_list[first]
	left_mark = first + 1
	right_mark = last
	done = False
	while not done:
		while left_mark <= right_mark and a_list[left_mark] <= pivot_value:
			left_mark += 1
		while right_mark >= left_mark and a_list[right_mark] >= pivot_value:
			right_mark -= 1
		if left_mark > right_mark:
			done = True
		else:
			a_list[left_mark], a_list[right_mark] = a_list[right_mark], a_list[left_mark]
	a_list[first], a_list[right_mark] = a_list[right_mark], a_list[first]
	return right_mark		

a_list = [9, 8, 7, 6, 5, 4, 3, 2, 1]
quick_sort(a_list)
print(a_list)