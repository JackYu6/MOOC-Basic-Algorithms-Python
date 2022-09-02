s = input().split()
idx = -1


def exp():
    global idx
    idx += 1
    if s[idx] == '+':
        return exp() + exp()
    elif s[idx] == '-':
        return exp() - exp()
    elif s[idx] == '*':
        return exp() * exp()
    elif s[idx] == '/':
        return exp() / exp()
    else:
        return float(s[idx])


print(exp())
