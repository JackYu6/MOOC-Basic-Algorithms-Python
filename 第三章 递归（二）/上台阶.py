def stairs(n):
    if n == 0 or n == 1:
        return 1
    return stairs(n - 1) + stairs(n - 2)


while True:
    n = input()
    if n.isdigit():
        print(stairs(int(n)))
    else:
        break
