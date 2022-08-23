import copy
oriLights = []
lights = []
result = [0] * 5


def getBit(c, i):  # 获取c的第j位（从0开始）二进制位的数值
    return (c >> i) & 1


def outputResult(t, result):
    print('PUZZLE #{}'.format(t))
    for i in range(5):
        for j in range(6):
            sign = ' ' if j < 5 else ''
            print(getBit(result[i], j), end=sign)
        print()  # 换行


T = int(input())
for t in range(1, T+1):
    for i in range(5):  # 读入数据
        temp = list(map(int, input().split()))
        c = 0
        for j in range(6):
            s = temp[j]
            if s:
                c |= (1 << j)  # 将c的第j位设为1
            else:
                c &= ~(1 << j)  # 将c的第j位设为0
        oriLights.append(c)

    for n in range(64):  # 使用二进制枚举第一行开关的情况
        switches = n  # 保存开关的状态
        lights = copy.deepcopy(oriLights)  # 深复制初始灯的状态
        for i in range(5):
            result[i] = switches
            for j in range(6):
                if getBit(switches, j):  # 如果按第j个开关
                    lights[i] ^= (1 << j)  # 翻转第j个灯的状态
                    if j > 0:
                        lights[i] ^= (1 << (j - 1))
                    if j < 5:
                        lights[i] ^= (1 << (j + 1))
            if i < 4:
                lights[i+1] ^= switches  # 翻转第i+1列灯的状态
            switches = lights[i]  # 利用第i行灯的状态更新第i+1行的开关的状态
        if lights[4] == 0:
            outputResult(t, result)
            break
