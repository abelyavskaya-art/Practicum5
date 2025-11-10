pin = int(input())
a = pin // 1000
b = pin % 1000 // 100
c = pin % 100 // 10
d = pin % 10


if (len(str(pin)) == 4 and (pin < 1900 or pin > 2050)
        and (a != b and a != c and a != d and b != c and b != d and c != d)):
    print('ОК')
else:
    print('ERROR')
