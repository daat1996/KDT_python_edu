import random

list1 = ['0','*']
for a in range(10):
    print(random.sample(list1,1), end=' ')

for b in range(9):
    for c in range(9):
        if random.randint(1,8)%8 == 0:
            print('*', end=''if c<8 else '\n')
        else:
            print('0', end=''if c<8 else '\n')