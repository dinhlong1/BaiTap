#Bài 100: Viết chương trình giải phương trình bậc 2

import math

#Kiểm tra giá trị có phải là số thực hay ko
def is_real_number(value):
    return value.isalpha() == False

#Hàm giải phương trình bậc 2
def solve_quadratic_equations(a, b, c):

    # ax^2 + bx +c =0
    if a == 0:
        # bx+c=0
        if b != 0:
            return "Phương trình có 1 nghiệm là "+str(-c/b)
        else:
            #c=0
            if c != 0 :
                return "Phương trình vô nghiệm"
            else:
                return "Phương trình vô số nghiệm"
    else:
        #Tính delta
        delta = b ** 2 - 4*a*c

        # Nếu delta <0  thì vô nghiệm
        if delta < 0:
            return "Phương trình vô nghiệm"

        # Nếu delta = 0  thì nghiệm kép
        elif delta == 0:
            return "Phương trình có nghiệm kép là " + str(-b/2*a)

        # Nếu delta > 0  thì 2 nghiệm phân biệt
        else:
            return "Phương trình có 2 nghiệm phân biệt là "+ str(-b + math.sqrt(delta)/ 2*a)+"," +str((-b - math.sqrt(delta))/ 2*a)


if __name__ == '__main__':
    a = input("Nhập a ")
    while not is_real_number(a):
        a = input("Nhập lại a")

    b = input("Nhập b")
    while not is_real_number(b):
        b = input("Nhập lại b")

    c = input("Nhập c")
    while not is_real_number(c):
        c = input("Nhập lại c")

    #Tìm kết quả
    result =solve_quadratic_equations(float(a),float(b),float(c))
    print(result)



