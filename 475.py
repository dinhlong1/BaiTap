#Bài 475: Hãy khai báo kiểu dữ liệu biểu diễn khái niệm phân số trong toán học và
# định nghĩa hàm nhập, hàm xuất cho kiểu dữ liệu này

import mangsonguyen as sn


def find_the_greatest_common_divisor_of_two_numbers(a, b):
    if sn.is_integer(a) == False or sn.is_integer(b) == False:
        print("Lỗi")
        return
    target_number = abs(a)
    if a > b:
        target_number = abs(b)
    for i in range(target_number, 0,-1):
        if a % i == 0 and b % i == 0:
            return i
def find_the_least_common_multiple_of_two_numberss(a, b):
    if sn.is_integer(a) == False or sn.is_integer(b) == False or a <=0 or b <= 0:
        print("Lỗi")
        return
    target_number = b
    if a > b:
        target_number = a
    for i in range(target_number, a * b +1):
        if i % a == 0 and i % b == 0:
            return i
class Fraction():
    def __init__(self,numerator,denominator):
        self.numerator = numerator
        self.denominator = denominator
    def set_numerator(self,numerator):
        self.numerator = numerator
    def set_denominator(self,denominator):
        self.denominator = denominator
    def get_numerator(self):
        return self.numerator
    def get_denominator(self):
        return self.denominator
    def __str__(self):
        return "{}/{}".format(self.numerator, self.denominator)

    # Bài 506: rút gọn phân số
    def fraction_reduction(self):
        temp = find_the_greatest_common_divisor_of_two_numbers(self.numerator, self.denominator)
        self.denominator = self.denominator // temp
        self.numerator = self.numerator // temp
        p = Fraction(self.numerator, self.denominator)
        return p
    # Bài 507: Tính tổng 2 phân số
    def sum_two_fractions(self,other):
        numerator = self.numerator * other.denominator + self.denominator * other.numerator
        denominator = self.denominator * other.denominator
        a = Fraction(numerator,denominator)
        a.fraction_reduction()
        return a
    # Bài 508: Tính hiệu 2 phân số
    def subtract_two_fractions(self,other):
        numerator = self.numerator * other.denominator - self.denominator * other.numerator
        denominator = self.denominator * other.denominator
        a = Fraction(numerator,denominator)
        a.fraction_reduction()
        return a
    # Bài 509: Tính tích 2 phân số
    def divisor_two_fractions(self,other):
        numerator = self.numerator * other.numerator
        denominator = self.denominator * other.denominator
        a = Fraction(numerator, denominator)
        a.fraction_reduction()
        return a
    # Bài 510: Tính thương 2 phân số
    def divisor_two_fractions(self,other):
        numerator = self.numerator * other.denominator
        denominator = self.denominator * other.numerator
        a = Fraction(numerator, denominator)
        a.fraction_reduction()
        return a
    # Bài 511: Kiểm tra phân số tối giản
    def simple_fraction_test(self):
        if find_the_greatest_common_divisor_of_two_numbers(self.numerator,self.denominator) == 1:
            print("Phân  số đã tối giản")
        else:
            print("Phân số chưa tối giản")
    # Bài 512: Qui đồng phân số
    def the_least_common_multiple_of_the_denominators(self,other):
        temp = find_the_least_common_multiple_of_two_numberss(self.denominator,other.denominator)
        self.numerator = (temp // self.denominator) * self.numerator
        other.numerator = (temp // other.denominator) * other.numerator
        self.denominator = temp
        other.denominator = temp
        print("Hai phân số sau khi quy đồng là\n"
              "{}/{} và {}/{}".format(self.numerator,self.denominator,other.numerator,other.denominator))
    # Bài 513: Kiểm tra phân số dương
    def is_a_positive_fraction(self):
        if self.numerator / self.denominator >= 0:
            print("Đây là phân số dương")
        else:
            print("Đây không phải là phân số dương")

    # Bài 514: Kiểm tra phân số âm
    def is_a_negative_fraction(self):
        if self.numerator / self.denominator < 0:
            print("Đây là phân số âm")
        else:
            print("Đây không phải là phân số âm")

    # Bài 515: So sánh 2 phân số: hàm trả về 1 trong 3 giá trị: 0,-1,1
    def compare_two_fractions(self,other):
        if self.is_a_positive_fraction() and other.is_a_negative_fraction():
            return 1
        elif other.is_a_positive_fraction() and self.is_a_negative_fraction():
            return -1
        else:
            if self.is_a_positive_fraction():
                a = self.numerator * other.denominator
                b = self.denominator * other.numerator
                if a > b:
                    return 1
                elif a == b:
                    return 0
                else:
                    return -1
            else:
                a = self.numerator * other.denominator
                b = self.denominator * other.numerator
                if a > b:
                    return -1
                elif a == b:
                    return 0
                else:
                    return 1

    # Bài 516: Định nghĩa toán tử operator + cho 2 phân số
    def __add__(self, other):
        numerator = self.numerator * other.denominator + self.denominator * other.numerator
        denominator = self.denominator * other.denominator
        a = Fraction(numerator, denominator)
        a.fraction_reduction()
        return a
    # Bài 517: Định nghĩa toán tử operator – cho 2 phân số
    def __sub__(self, other):
        numerator = self.numerator * other.denominator - self.denominator * other.numerator
        denominator = self.denominator * other.denominator
        a = Fraction(numerator, denominator)
        a.fraction_reduction()
        return a
    # Bài 518: Định nghĩa toán tử operator * cho 2 phân số
    def __mul__(self, other):
        numerator = self.numerator * other.numerator
        denominator = self.denominator * other.denominator
        a = Fraction(numerator, denominator)
        a.fraction_reduction()
        return a
    # Bài 519: Định nghĩa toán tử operator / cho 2 phân số
    def __truediv__(self, other):
        numerator = self.numerator * other.denominator
        denominator = self.denominator * other.numerator
        a = Fraction(numerator, denominator)
        a.fraction_reduction()
        return a

    # Bài 520: Định nghĩa toán tử operator ++ cho 2 phân số

    # Bài 521: Định nghĩa toán tử operator —- cho 2 phân số
def create_fraction():
    numerator = input("Nhập tử số")
    while sn.is_integer(numerator) == False:
        numerator = input("Nhập lại tử số")
    denominator = input("Nhập mẫu số")
    while sn.is_integer(denominator) == False or denominator ==0:
        denominator = input("Nhập lại mẫu số")
    p = Fraction(int(numerator),int(denominator))
    return p
a = create_fraction()
b = create_fraction()
print((a.the_least_common_multiple_of_the_denominators(b)))











