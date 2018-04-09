import Stack as st

def par_checker(symbol_string):
	balance = True
	s = st.Stack()
	index = 0
	my_dict = {'}':'{', ']':'[', ')':'('}
	while index < len(symbol_string) and balance:
		symbol = symbol_string[index]
		if symbol_string[index] in '([{':
			s.push(symbol)
		else:
			if s.is_empty():
				balance = False
			else:
				current = s.pop()
				if current != my_dict[symbol]:
					balance = False
		index += 1
	if s.is_empty() and balance:
		return True
	else:
		return False

print(par_checker('(())'))
print(par_checker('([{'))