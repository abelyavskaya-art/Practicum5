height, weight = int(input()), int(input())
IMB = float(weight // float((height / 100)**2))
if IMB < 16:
    print('выраженный дефицит массы тела')
elif 16 <= IMB <= 18.49:
    print('недостаточная масса тела')
elif 18.5 <= IMB <= 24.99:
    print('норма')
elif 25 <= IMB <= 29.99:
    print('избыточная масса тела')
elif 30 <= IMB <= 34.99:
    print('ожирение первой степени')
elif 35 <= IMB <= 39.99:
    print('ожирение второй степени')
elif IMB >= 40:
    print('ожирение третьей степени')
print(IMB)


