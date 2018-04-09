def bubble_sort(a_list):
	for pass_num in range(len(a_list) - 1):
		print(a_list)
		for i in range(len(a_list) - 1 - pass_num):
			if a_list[i] > a_list[i + 1]:
				a_list[i], a_list[i + 1] = a_list[i + 1], a_list[i]
	return a_list

# a_list = [5, 2, 8, 1, 0, 10]
# print(bubble_sort(a_list))

def short_bubble(a_list):
	for pass_num in range(len(a_list) - 1):
		print(a_list)
		exchange = 0
		for i in range(len(a_list) - 1 - pass_num):
			if a_list[i] > a_list[i + 1]:
				a_list[i], a_list[i + 1] = a_list[i + 1], a_list[i]
				exchange += 1
		if exchange == 0:
			break
	return a_list

a_list = [1, 2, 3, 4, 5, 6, 10, 8]
print(short_bubble(a_list))