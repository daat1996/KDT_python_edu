"""
26 장 세트 연습
"""

a = set('apple')
print(a)

b = set(range(5))
print(b)

# set 연산
a = {1, 2, 3, 4}
b = {3, 4, 5, 6}

# 합집합
print(a|b)
print(set.union(a,b))

# 교집합
print(a&b)
print(set.intersection(a,b))

# 차집합
print(a-b)
print(set.difference(a,b))

# 대칭차집합
print(a^b)
print(set.symmetric_difference(a,b))

