def isZero(x):
    return abs(x) <= EPS


def count24(a, n):
    if n == 1:
        return isZero(a[0] - 24)
    b = [0] * 4
    for i in range(n-1):
        for j in range(i+1, n):
            m = 0
            for k in range(n):
                if k != i and k != j:
                    b[m] = a[k]
                    m += 1
            b[m] = a[i] + a[j]
            if count24(b, m+1):
                return True
            b[m] = a[i] - a[j]
            if count24(b, m+1):
                return True
            b[m] = a[j] - a[i]
            if count24(b, m+1):
                return True
            b[m] = a[i] * a[j]
            if count24(b, m+1):
                return True
            if not isZero(a[i]):
                b[m] = a[j] / a[i]
                if count24(b, m+1):
                    return True
            if not isZero(a[j]):
                b[m] = a[i] / a[j]
                if count24(b, m+1):
                    return True
    return False


EPS = 1e-6
while 1:
    lis = list(map(int, input().split()))
    if lis == [0, 0, 0, 0]:
        break
    if count24(lis, 4):
        print('YES')
    else:
        print('NO')
