import sys
a = list(map(int, input().split()))
m = int(input())
n = len(a)
for i in range(n-1):
    for j in range(i+1, n):
        if a[i] + a[j] == m:
            print(a[i], a[j])
            sys.exit(0)
