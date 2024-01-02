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

a, b, c = [1,2,3]
print(a,b,c)

a,b,c = (1,2,3)
print(a,b,c)

print(type(a))

# 딕셔너리 사용

lux = {'health': 490, 'mana':334, 'melee':550, 'armor':18.72}

print(lux)

lux = {'health': 490, 'health': 800, 'mana':334, 'melee':550, 'armor':18.72}
print(lux)  # 키가 중복되면 가장 마지막에 있는 값 사용..

lux1 = dict(health=490, mana=334, melee=550, armor=18.72)
print(lux1)

# (키, 값) 형식의 튜플로 딕셔너리를 만듦

print('health'in lux1)
print('attack' in lux1)

x = dict({'a':10, 'b':20})
print(x)
print(type({'a':10, 'b':20}))

# 12.4 연습문제
camille = { 'health' : 575.6,
            'health_regen' : 1.7,
            'mana': 338.8,
            'mana_regen':1.63,
            'melee': 125,
            'attack_damage': 60,
            'attack_speed': 0.625,
            'armor': 26,
            'magic_resistance':32.1,
            'movement_speed': 340}
print(camille['health'])
print(camille['movement_speed'])

#12.5 심사문제

key = input().split()
value = input().split()
print(dict(zip(key,value)))     # zip 써야하나..

