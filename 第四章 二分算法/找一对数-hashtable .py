a = list(map(int, input().split()))
m = int(input())
has = {}
for i in range(len(a)):
    if m - a[i] in has:
        print(m - a[i], a[i])
    has[a[i]] = i
