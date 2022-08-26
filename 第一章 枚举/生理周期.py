cnt = 0
while 1:
    p, e, i, d = map(int, input().split())
    if p == -1:
        break
    cnt += 1
    day = p
    while 1:
        if (day - e) % 28 == 0 and day > d:
            break
        day += 23
    while 1:
        if (day - i) % 33 == 0:
            break
        day += 23 * 28
    print('Case {}: the next triple peak occurs in {} days.'.format(cnt, day - d))