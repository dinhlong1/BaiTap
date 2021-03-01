#Bài 480: Hãy khai báo kiểu dữ liệu để biểu diễn khái niệm đa thức 1 biến trong toán học:
#P(x) = a.n.X^n + a.n-1.X^n-1 + … + a.1.X + a.0 và định nghĩa hàm nhập và hàm xuất cho kiểu dữ liệu này
import mangsonguyen as sn

class polynomial():

    def __init__(self, coefficient, index_number):
        self.coefficient = coefficient
        self.index_number = index_number

    def set_coefficient(self, coefficient):
        self.coefficient = coefficient

    def set_index_number(self, index_number):
        self.index_number = index_number

    def get_coefficient(self):
        return self.coefficient

    def get_index_number(self):
        return self.index_number

    def __str__(self):
        p = ""
        for i in range(self.index_number, -1, -1):
            if self.coefficient[i] != 0:
                if self.coefficient[i] > 0:
                    if i == self.index_number:
                        p += "{}*X^{}".format(self.coefficient[i], i)
                    elif i == 0:
                        p += " + {}".format(self.coefficient[i])
                    elif i == 1:
                        p += " + {}*X".format(self.coefficient[i])
                    else:
                        p += " + {}*X^{}".format(self.coefficient[i], i)
                else:
                    if i == self.index_number:
                        p += "(-{})*X^{}".format(abs(self.coefficient[i]), i)
                    elif i == 0:
                        p += " - {}".format(abs(self.coefficient[i]))
                    elif i == 1:
                        p += " - {}*X".format(abs(self.coefficient[i]))
                    else:
                        p += " - {}*X^{}".format(abs(self.coefficient[i]), i)
        return p

# Bài 493: Tính hiệu 2 đa thức
    def subtract_two_polynomials(self, other):
        if self.index_number > other.index_number:
            index = self.index_number
            temp = self.coefficient
            n = other.index_number
        else:
            index = other.index_number
            temp = other.coefficient
            n = self.index_number
        for i in range(n + 1):
            if self.index_number >= other.index_number:
                temp[i] = self.coefficient[i] - other.coefficient[i]
            else:
                temp[i] = other.coefficient[i] - self.coefficient[i]
        p = polynomial(temp, index)
        return p
# Bài 494: Tính tổng 2 đa thức
    def sum_two_polynomials(self,other):
        if self.index_number > other.index_number:
            index = self.index_number
            temp = self.coefficient
            n = other.index_number
        else:
            index = other.index_number
            temp = other.coefficient
            n = self.index_number
        for i in range(n + 1):
            temp[i] = other.coefficient[i] + self.coefficient[i]
        p = polynomial(temp, index)
        return p
# Bài 495: Tính tích 2 đa thức
    def product_two_polynomials(self,other):
        temp = self.coefficient + other.coefficient
        index = self.index_number + other.index_number
        for i in range(self.index_number + 1):
            for j in range(other.index_number + 1):
                temp[i + j] = self.coefficient[i] + other.coefficient[j]
        p = polynomial(temp, index)
        return p

# Bài 496: Tính thương 2 đa thức
    def quotient_two_polynomials(self,other):
        temp = self.coefficient + other.coefficient
        index = self.index_number + other.index_number
        for i in range(self.index_number + 1):
            for j in range(other.index_number + 1):
                temp[i + j] = self.coefficient[i] + other.coefficient[j]
        p = polynomial(temp, index)
        return p

def create_polynomial():
    index_number = input("Nhập số mũ")
    while sn.is_integer(index_number) == False or int(index_number) < 1:
        index_number = input("Nhập lại số mũ")
    coefficient = []
    for i in range(0,int(index_number) + 1):
        a = input("Nhập hệ số vị trí mũ {}".format(i))
        while sn.is_integer(a) == False:
            a = input("Nhập hệ số vị trí mũ {}".format(i))
        coefficient.append(int(a))
    p = polynomial(coefficient, int(index_number))
    return p


a = create_polynomial()
b = create_polynomial()
print((a.product_two_polynomials(b)).__str__())





# Bài 497: Tính đa thức dư của phép chia đa thức thứ nhất cho đa thức thứ hai
# Bài 498: Tính đạo hàm cấp 1 của đa thức
# Bài 499: Tính đạo hàm cấp k của đa thức
# Bài 500: Tính giá trị của đa thức tại vị trí x = x0
# Bài 501: Định nghĩa toán tử cộng (operator +) cho hai đa thức
# Bài 502: Định nghĩa toán tử trừ (operator -) cho hai đa thức
# Bài 503: Định nghĩa toán tử nhân (operator *) cho hai đa thức
# Bài 504: Định nghĩa toán tử thương (operator /) cho hai đa thức
# Bài 505: Tìm nghiệm của đa thức trong đoạn [a, b] cho trước
#Hàm tạo đa thức
# def create_polynomial():
#     a = input("Nhập a")
#     while sn.is_integer(a) == False:
#         a = input("Nhập lại a")
#     n = input("Nhập n")
#     while sn.is_integer(n) == False:
#         n = input("Nhập lại n")
#     p = polynomial(a,n)
#     return p
#
# a= create_polynomial()
# print(a.__str__())