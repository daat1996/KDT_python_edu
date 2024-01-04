matrix = []

col = int(input("가로 길이: "))
row = int(input("세로 길이: "))

for i in range(row):
    matrix.append(list(input()))
    if len(matrix[i]) != col:
        print("가로 갯수와 다릅니다.")
        break
    else:
        matrix[i].insert(0,'.')
        matrix[i].append('.')
matrix.insert(0,['.']*(col+2))
matrix.append(['.']*(col+2))
print(matrix)

for x in range(1, col+1):
    for y in range(1, row+1):
        if matrix[x][y] != '*':
            matrix[x][y] = str(matrix[x-1][y-1:y+2].count('*')+matrix[x][y-1].count('*')+
                    matrix[x][y+1].count('*')+matrix[x+1][y-1:y+2].count('*'))
            print(matrix[x][y],end=''if y != row else '\n')
        else:
            print('*',end=''if y != row else '\n')








#            if x == y == 0 or (x == col and y == 0) or (x == 0 and y == row) or (x == col and y == row):