import Stack

def divide_by_2(dec_num):
	s = Stack.Stack()
	binary_string = ''
	while dec_num > 0:
		s.push(dec_num % 2)
		dec_num //= 2
	while not s.is_empty():
		binary_string += str(s.pop())
	return binary_string

# print(divide_by_2(10))

def base_converter(dec_num, base):
	s = Stack.Stack()
	new_str = ''
	my_list = '0123456789ABCDEF'
	while dec_num > 0:
		s.push(my_list[dec_num % base])
		dec_num = dec_num // base
	while not s.is_empty():
		new_str += s.pop()
	return new_str
print(base_converter(1000, 16))