# 1~10
for a in range(20):
    print(a+1)

nums = [1,2,3,4,5,6,7,8,9,10]

for n in nums:
    print(n, end=" " if n != 5 else '\n')

print("END")


print("*")
print("**")
print("***")
print("****")

print("*")
print("*"*2)
print("*"*3)
print("*"*4)

for a in range(1,6):
    print("*"*a)
for a in range(6,0,-1):
    print("*"*a)


for a in range(1,12):
    if a<=6:
        print("*" * a)
    else:
        print("*" * (12-a))


# 입력받은 수가 최대 가로 길이가 되도록하는 마르모 만들기

num = int(input("홀수를 입력하시오: "))
for a in range(1,num+1):
    if a <= (num+1)/2:
        print(f'{(2*a-1) * "*":^101}')
    else:
        print(f'{(2*(num-a)+1)*"*":^101}')

