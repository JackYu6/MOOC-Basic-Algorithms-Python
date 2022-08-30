columns = set()
diagonal1 = set()  # 沿主对角线方向的斜线
diagonal2 = set()  # 沿副对角线方向的斜线
N = int(input())
queensPos = [-1] * N


def backtrack(row):
    if row == N:
        for i in range(N):
            sign = ' ' if i < N - 1 else ''
            print(queensPos[i] + 1, end=sign)
        print()
        return
    for i in range(N):
        if i in columns or row - i in diagonal1 or row + i in diagonal2:
            continue
        queensPos[row] = i
        columns.add(i)
        diagonal1.add(row - i)
        diagonal2.add(row + i)
        backtrack(row + 1)
        # queensPos[row] = -1
        columns.remove(i)
        diagonal1.remove(row - i)
        diagonal2.remove(row + i)


backtrack(0)
