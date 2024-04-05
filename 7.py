n = int(input())
i = 1
ans = ''
while i < n:
    i = i * 2
    if i == n:
        ans = 'верно'
    else:
        ans = 'неверно'
print(ans)