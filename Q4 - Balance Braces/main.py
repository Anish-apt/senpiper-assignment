def answer(s):
    d = {")":"(","]":"[","}":"{"}
    n = len(s)
    stack = []
    for i in range(n):
        if (s[i] == '(' or s[i] == '{' or s[i] == '['):
            stack.append(s[i])
        elif (s[i] == ')' or s[i] == '}' or s[i] == ']'):
            if (len(stack) == 0):
                return False
            if (stack[-1] != d[s[i]]):
                return False
            stack.pop()
    if (len(stack) == 0):
        return True
    else:
        return False

s = input() 
print (answer(s))