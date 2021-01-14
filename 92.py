#Bài 92: Tìm ước số chung lớn nhất của 2 số nguyên dương
def checkNumberInteger(Num):
    if Num.isdigit() == False or float(Num).is_integer() == False or int(Num) <= 0:
        return False
    else:
        return True
def greatestCommonDivisor(Num1 ,Num2):
    if Num1 > Num2:
        smallNumber = Num2
    else:
        smallNumber = Num1
    for i in range(smallNumber, 1, -1):
        if Num1 % i ==0 and Num2 % i ==0:
            return i
            break


if __name__ == '__main__':
    NumberFirst = (input("Nhập số thứ nhất "))
    while checkNumberInteger(NumberFirst) == False:
        NumberFirst = (input("Nhập lại số thứ nhất "))
    NumberSecond = (input("Nhập số thứ hai "))
    while checkNumberInteger(NumberFirst) == False:
        NumberFirst = (input("Nhập lại số thứ hai "))
    print("Ước chung lớn nhất của 2 số là " + str(greatestCommonDivisor(int(NumberFirst),int(NumberSecond))))

