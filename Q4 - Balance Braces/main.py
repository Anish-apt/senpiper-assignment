open_brace = ["[","{","("]
close_brace = ["]","}",")"]

# Function to check parentheses
def check_braces(string):
	stack = []
	for i in string:
		if i in open_brace:
			stack.append(i)
		elif i in close_brace:
			pos = close_brace.index(i)
			if ((len(stack) > 0) and (open_brace[pos] == stack[len(stack)-1])):
				stack.pop()
			else:
				return "False"
	if len(stack) == 0:
		return "True"
	else:
		return "False"

string = input()
print(check_braces(string))