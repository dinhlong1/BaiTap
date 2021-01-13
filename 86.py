import math
n=int(input("Nhap N="))
tong=0
for i in range(1,n+1):
    tong= tong+math.pow(i,3)
print(tong)