a = list(map(int, input().split()))
m = int(input())
n = len(a)
a.sort()
for i in range(n):
    l, r = 0, n - 1  # 边界一定要在数组下标范围内
    while l < r:
        mid = l+r >> 1
        if a[mid] >= m - a[i]:
            r = mid
        else:
            l = mid + 1
    if a[l] == m - a[i]:
        print(a[i], a[l])
        break
