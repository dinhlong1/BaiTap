import math
n=int(input("Nhap N"))
m=int(input("Nhap X"))
sum=0
for i in range(1,n+1):
    sum = sum + math.pow(m, i)
    if i > 1:
        for t in range(2, i + 1):
            sum = sum + t
print(sum)