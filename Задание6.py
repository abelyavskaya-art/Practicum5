day1, day2, day3 = int(input()), int(input()), int(input())
if day1 == day2 == day3:
    print('3')
elif day1 == day2 != day3 or day2 == day3 != day1 or day3 == day1 != day2:
    print('2')
else:
    print('0')