n=int(input("Nhap N="))
list=[]
for i in range(2,n):
    if n%i == 0:
        list.append(i)
print(list)