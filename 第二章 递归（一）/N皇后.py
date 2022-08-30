N = int(input())
queensPos = [-1] * N


def nQueens(k):
    if k == N:
        for i in range(N):
            sign = ' ' if i < N - 1 else ''
            print(queensPos[i] + 1, end=sign)
        print()
        return
    for i in range(N):
        for j in range(k):
            if queensPos[j] == i or abs(queensPos[j] - i) == abs(j - k):
                break
        else:
            queensPos[k] = i
            nQueens(k + 1)


nQueens(0)
