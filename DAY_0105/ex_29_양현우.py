'''

def get_quotient_remainder(x,y):
    return x//y, x%y


x= 10
y =3

quotient, remainder = get_quotient_remainder(x,y)
print('몫: {0}, 나머지: {1}'.format(quotient,remainder))


def calc(x,y):
    return x+y, x-y, x*y, x/y

x,y = map(int, input().split())

a, s, m, d = calc(x,y)
print('덧셈: {0}, 뺄셈: {1}, 곱셈: {2}, 나눗셈: {3}'.format(a,s,m,d))

'''
#
# def hello():
#     print('Hello, world!')
#
# hello()

print(int('-13'))
print('13'.lstrip('-').isnumeric())