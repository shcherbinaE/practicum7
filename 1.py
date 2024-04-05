num = 0
for i in range(100,999):
    if i % 17 == 0:
        print(i, end = ' ')
        num += 1
print('\n', num)