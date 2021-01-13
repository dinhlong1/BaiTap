a=int(input("Nhap thang="))
while a>12:
    a= int(input("nhap lai thang hop le"))
if a==12 or a==9 or a==6 or a==3:
    quy=a//3
else:
    quy=a//3+1
print("Quy cua thang do la", quy)