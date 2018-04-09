def reverse_str(a_str):
	if len(a_str) == 1:
		return a_str[0]
	else:
		return reverse_str(a_str[1:]) + a_str[0]

print(reverse_str('abcd'))