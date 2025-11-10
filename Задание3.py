number = int(input())
a1 = number // 1000
a2 = number // 100 % 10
a3 = number // 10 % 10
a4 = number % 10
if a1 == a4 and a2 == a3:
    print('настоящее')
else:
    print('кривое')