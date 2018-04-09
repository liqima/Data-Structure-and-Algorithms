def to_str(n, base):
	convert_str = '0123456789ABCDEF'
	if n < base:
		return convert_str[n]
	else:
		return to_str(n // base, base) + convert_str[n % base]

print(to_str(10, 2))