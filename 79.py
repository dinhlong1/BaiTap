n=int(input("Nhap N="))
a=1
sumN=0
while n>0:

    if n // a == 0:
        break
    sumN = sumN + 1
    a=a*10
print(sumN)