lis = input()
idx = -1


def expression_value():  # 求一个表达式的值
    result = term_value()  # 求第一项的值
    more = True
    while more:
        global idx
        if idx < len(lis) - 1:
            idx += 1
            op = lis[idx]
            if op == '+' or op == '-':
                value = term_value()
                if op == '+':
                    result += value
                else:
                    result -= value
            else:
                idx -= 1
                more = False
        else:
            break
    return result


def term_value():  # 求一个项的值
    result = factor_value()  # 求第一个因子的值
    while True:
        global idx
        if idx < len(lis) - 1:
            idx += 1
            op = lis[idx]
            if op == '*' or op == '/':
                value = factor_value()
                if op == '*':
                    result *= value
                else:
                    result /= value
            else:
                idx -= 1
                break
        else:
            break
    return result


def factor_value():  # 求一个因子的值
    result = 0
    global idx
    idx += 1
    c = lis[idx]
    if c == '(':
        result = expression_value()
        idx += 1
    else:
        while c.isdigit():
            result = 10 * result + int(c)
            if idx < len(lis) - 1:
                idx += 1
                c = lis[idx]
            else:
                break
        else:
            idx -= 1
    return result


print(int(expression_value()))
