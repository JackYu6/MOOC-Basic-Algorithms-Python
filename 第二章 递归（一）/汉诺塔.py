def hanoi(n, src, mid, des):
    if n == 1:
        print(src + '->' + des)
        return
    hanoi(n-1, src, des, mid)
    print(src + '->' + des)
    hanoi(n-1, mid, src, des)


n = int(input())
hanoi(n, 'A', 'B', 'C')
