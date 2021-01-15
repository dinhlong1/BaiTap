#Bài 96: Viết chương trình nhập giá trị x sau tính giá trị của hàm số
import math

#Hàm kiểm tra giá trị có phải là số hay ko
def is_number(value):
    return value.isdigit() and float(value).is_integer() and int(value) > 0

#Hàm giải hàm số
def solve_number_funtion(x, a, b ,c ):
    if a != 0:
        if b!=0:
            # ax^2+ bx +c
            Sum = a * math.pow(x,2) + x * b +c
        else:
            # ax^2+ c
            Sum = a * math.pow(x, 2) + c
    else:
        if b != 0:
            # bx +c
            Sum = x * b +c
        else:
            # c
            Sum = c
    return Sum

if __name__ == '__main__':

    #Hàm số bất kỳ
    print("f(x) = 3x^2 +7*x +4")


    x = (input("Nhập x = "))
    while not is_number(x):
        x = (input("Nhập lại x = "))

    result = solve_number_funtion(int(x), 3, 7, 4)
    print("Kết quả là "+ str(result))