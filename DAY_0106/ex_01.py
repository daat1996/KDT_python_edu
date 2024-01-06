msg = ['Good', 'child','Zoo','apple','Flower','zero']

def cord(x):
    print(f'정렬 결과 : {sorted(x, reverse=True)}')
    print(f'가장 높은 문자열 : {max(x)}, 가장 낮은 문자열 : {min(msg)}')

cord(msg)

