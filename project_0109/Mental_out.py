print(' ',end='')
for a in range(21):
    print(f'{a:^3}',sep='',end='' if a<20 else '\n')
for a in range(1, 21):
    print(f' {a:2} ',' □ '*20,sep='')

