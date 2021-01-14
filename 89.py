#Bài 89: Viết chương trình tính tổng các giá trị lẻ nguyên dương nhỏ hơn N
def SumOldIntegers(Num):
    Sum = 0
    for i in range(1,Num,2):
        Sum += i
    return Sum
if __name__ == '__main__':
    n = int(input("Nhập N "))
    print("Tổng các số lẻ nguyên dương nhỏ hơn N là " + str(SumOldIntegers(n)))
