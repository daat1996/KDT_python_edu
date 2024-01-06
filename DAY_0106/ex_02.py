
def get_sum_max_min(x):
    listNum = []
    for a in x:
        if a.lstrip('-').isdigit():
            listNum.append(int(a))
    s, mx, mn = 0, 0, 0
    if len(listNum):
        s += sum(listNum)
        mx += max(listNum)
        mn += min(listNum)
    return print(f'합계 : {s:<10} 최댓값 : {mx:<10} 최솟값 : {mn:<10}')

data = input("데이터 입력 : ").split()

get_sum_max_min(data)

