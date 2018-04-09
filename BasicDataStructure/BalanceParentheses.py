import Stack as st 

def par_checker(symbol_string):
	s = st.Stack()
	index = 0
	balance = True
	while index < len(symbol_string) and balance:
		symbol = symbol_string[index]
		if symbol == '(':
			s.push(symbol)
		else:
			if s.is_empty():
				balance = False
			else:
				s.pop()
		index += 1
	if balance and s.is_empty():
		return True
	else:
		return False

print(par_checker('((()))'))
print(par_checker('(())))'))