# 10.1
a = [38, 21, 53, 62, 19]
print(a)
# 10.1.1
person = ['james', 17, 175.3, True]
print(person)

#10.1.2
a = []
print(a)
b = list()
print(b)

# 10.1.3
print(range(10))

a = list(range(10))
print(a)

b = list(range(5, 12))
print(b)

c=list(range(-4, 10,2))
print(c)

d = list(range(10,0,-1))
print(d)

# 10.2

a = (38, 21, 53, 62, 19)    # 튜플
print(a)

a = 38, 21, 53, 62, 19      # ()없이 , 으로도 튜플
print(a)

person = ('james', 17, 186.5, False)    # 여러 자료형 저장 가능
print(person)

b = (38)
c = 38,

print(type(b), type(c)) # 값에 , 붙여야함

# 10.2.2
print(tuple(range(5,12)))

# 10.2.3
a = [1,2,3]
print(tuple(a))

b = (4,5,6)
print(list(b))