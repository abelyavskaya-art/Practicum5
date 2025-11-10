count = int(input())
if count % 10 == 1:
    print(f'{count} попугай')
elif 1 < count % 10 <= 4 :
    print(f'{count} попугая')
else:
    print(f'{count} попугаев')
