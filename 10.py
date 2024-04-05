temp = float(input())
num = 0
while temp != 0:
    temp1 = float(input())
    if temp > temp1:
        num += 1
    temp = temp1
print(num - 1)