money = int(input())
sickles = money // 29
gallions = sickles // 17
knut = money - (sickles * 29)
if gallions > 0:
    print(gallions, 'галлеонов')
if sickles > 0 and sickles % 17 > 0:
    print(sickles - (gallions * 17), 'сиклей')
if knut > 0:
    print(knut, 'кнатов')