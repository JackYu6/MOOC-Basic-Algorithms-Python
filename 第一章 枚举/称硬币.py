def isFake(c, light):
    for i in range(3):
        if light:
            left = l[i][0]
            right = l[i][1]
        else:
            left = l[i][1]
            right = l[i][0]
        if l[i][2][0] == 'u':
            if c not in right:
                return False
        elif l[i][2][0] == 'e':
            if (c in left) or (c in right):
                return False
        elif l[i][2][0] == 'd':
            if c not in left:
                return False
    return True


T = int(input())
for t in range(T):
    l = [input().split() for i in range(3)]
    for c in ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L']:
        if isFake(c, True):
            print('{} is the counterfeit coin and it is light.'.format(c))
            break
        elif isFake(c, False):
            print('{} is the counterfeit coin and it is heavy.'.format(c))
            break
