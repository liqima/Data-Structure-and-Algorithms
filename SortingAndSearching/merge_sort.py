def merge_sort(a_list):
	print('spliting: ', a_list)
	if len(a_list) > 1:
		mid = len(a_list) // 2
		left_half = a_list[:mid]
		right_half = a_list[mid:]
		merge_sort(left_half)
		merge_sort(right_half)
		i = j = k = 0
		while i < len(left_half) and j < len(right_half):
			if left_half[i] < right_half[j]:
				a_list[k] = left_half[i]
				i += 1
			else:
				a_list[k] = right_half[j]
				j += 1
			k += 1
		while i < len(left_half):
			a_list[k] = left_half[i]
			i += 1
			k += 1
		while j < len(right_half):
			a_list[k] = right_half[j]
			j += 1
			k += 1
	print('merging: ', a_list)

a_list = [1, 10, 2, 9, 3, 8, 4, 7]
merge_sort(a_list)