#Bài 96: Viết chương trình nhập giá trị x sau tính giá trị của hàm số
# f(x) = 2x^2 + 5x + 9 khi x >= 5, f(x) = -2x^2 + 4x – 9 khi x < 5
import math

#Hàm kiểm tra giá trị có phải là số hay ko
def is_number(value):
    return value.isalpha()== False
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

    x = input("Nhập x = ")
    while not is_number(x):
        x = input("Nhập lại x = ")

        # Xét điều kiện
    if float(x) >=5 :
        #f(x) = 2x^2 + 5x + 9
        result = solve_number_funtion(float(x), 2, 5, 9)
    else:
        #f(x) = -2x^2 + 4x – 9
        result = solve_number_funtion(float(x), -2, 4, -9)

    print("Kết quả là" , result)