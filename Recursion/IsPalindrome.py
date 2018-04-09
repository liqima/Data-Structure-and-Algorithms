def is_palindrome(a_str):
	if len(a_str) <= 1:
		return True
	else:
		if a_str[0] != a_str[-1]:
			return False
		else:
			return is_palindrome(a_str[1:len(a_str) - 1])

print(is_palindrome('radar radar'))