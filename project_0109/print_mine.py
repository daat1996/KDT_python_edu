from random import randint, sample

list1 = ['*','0']
for a in range(9):
    for b in range(9):
        print(sample(list1,1),end=''if b<8 else '\n')

