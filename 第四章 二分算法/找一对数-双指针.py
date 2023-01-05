a = list(map(int, input().split()))
m = int(input())
n = len(a)
a.sort()
l, r = 0, n - 1
# 法一，只适用于同一个升序数组
while l < r:
    if a[l] + a[r] > m:
        r -= 1
    elif a[l] + a[r] < m:
        l += 1
    else:
        print(a[l], a[r])
        break
# 法二，适用于一个或两个升序数组
while l < n:
    while r >= 0 and a[l] + a[r] > m:
        r -= 1
    if a[l] + a[r] == m:
        print(a[l], a[r])
        break
    l += 1
