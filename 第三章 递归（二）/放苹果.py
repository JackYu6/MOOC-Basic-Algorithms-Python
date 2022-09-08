def f(m, n):  # m个苹果放在n个盘子里的放法总数
    if m == 0:
        return 1
    if n == 0:
        return 0
    if m < n:
        return f(m, m)
    elif m >= n:
        return f(m, n - 1) + f(m - n, n)


T = int(input())
for t in range(T):
    M, N = map(int, input().split())
    print(f(M, N))
