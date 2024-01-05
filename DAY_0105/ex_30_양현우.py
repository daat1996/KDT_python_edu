print(*[1,2,3])

def personal_info(name='미공개',age=0):
    print('ok')
print(personal_info(**{'name':'홍길동', 'age':30}))

korean, english, mathematics, science = 100, 86, 81, 91


def get_max_score(*args):
    return max(args)

max_score = get_max_score(korean, english, mathematics, science)
print('높은 점수:', max_score)

max_score = get_max_score(english, science)
print('높은 점수:', max_score)


korean, english, mathematics, science = 76, 82, 89, 84
# korean, english, mathematics, science = map(int, input().split())


def get_min_max_score(*args):
    return min(args), max(args)

def get_average(**x):
    return sum(x.values())/len(x)



min_score, max_score = get_min_max_score(korean, english, mathematics, science)
average_score = get_average(korean=korean, english=english, mathematics=mathematics, science=science)
print(f'낮은 점수: {min_score:.2f}, 높은 점수: {max_score:.2f}, 평균 점수: {average_score:.2f}')

min_score, max_score = get_min_max_score(english, science)
average_score = get_average(english=english, science=science)
print(f'낮은 점수: {min_score:.2f}, 높은 점수: {max_score:.2f}, 평균 점수: {average_score:.2f}')
