n, k, r = map(int, input().split())
i = 2
while n * (1 + k / 100) <= r:
    n *= 1 + k / 100
    i += 1
print(i)