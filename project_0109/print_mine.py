from random import randint, sample


def makeMine():
    matrix = []
    for sero in range(9):
        matseries = []
        for garo in range(9):
            num = randint(1, 8)
            if num%8 == 0:
                matseries.append('*')
            else:
                matseries.append('0')
        matrix.append(matseries)
    return matrix


for a in range(9):
    for b in range(9):
        if randint(1,8)%8 == 0:
            print('*', end=''if b<8 else '\n')
        else:
            print('0', end=''if b<8 else '\n')

print(makeMine())