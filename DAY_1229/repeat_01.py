tim = input("년, 월, 일, 시, 분, 초 를 입력하시오: ")

year, month, day, hour, minute, second = tim.split()

print(f'{year}-{month}-{day}',end="T")
print(hour, minute, second, sep=':')