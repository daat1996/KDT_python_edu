import random
print(' ',end='')
for a in range(21):
    print(f'{a:^3}',sep='',end='' if a<20 else '\n')
for a in range(1, 21):
    print(f' {a:2} ',' □ '*20,sep='')

print('rk'.isdigit())

list1 = ['**']*10 + ['  ']*2
print(list1)
print(random.shuffle(list1))
print(list1)
print('ㅇ')
print(ord('①'))
print(ord('⑳'))