#Bài 90: Viết chương trình tìm số nguyên dương m lớn nhất sao cho 1 + 2 + … + m < N

def FindLargestInteger(Number):
    Sum = 0
    integerNumber = 0

    while Sum<Number:
        integerNumber = integerNumber + 1
        Sum = Sum + integerNumber
    return integerNumber

if __name__ == '__main__':
    n = input("Nhập N ")

    while n.isdigit() == False or float(n).is_integer() == False or int(n) <=0:
        n = input("Nhập lại N ")

    print("Số nguyên dương lớn nhất trong tổng các số nhỏ hơn N là " + str(FindLargestInteger(int(n))))