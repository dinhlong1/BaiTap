#Bài 89: Viết chương trình tính tổng các giá trị lẻ nguyên dương nhỏ hơn N
def SumOldIntegers(Num):
    Sum = 0
    for i in range(1,Num,2):
        Sum += i
    return Sum
if __name__ == '__main__':
    n = input("Nhập N ")
    print(float(n).is_integer())
    while n.isdigit() == False or float(n).is_integer() == False or int(n) < 0:
        n = input("Nhập lại N ")

    print("Tổng các số lẻ nguyên dương nhỏ hơn N là " + str(SumOldIntegers(int(n))))
