#Bài 475: Hãy khai báo kiểu dữ liệu biểu diễn khái niệm phân số trong toán học và
# định nghĩa hàm nhập, hàm xuất cho kiểu dữ liệu này

import mangsonguyen as sn

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
        return "{}/{}".format(self.numerator,self.denominator)

def create_fraction():
    numerator = input("Nhập tử số")
    while sn.is_integer(numerator) == False:
        numerator = input("Nhập lại tử số")
    denominator = input("Nhập mẫu số")
    while sn.is_integer(denominator) == False or denominator ==0:
        denominator = input("Nhập lại mẫu số")
    p = Fraction(numerator,denominator)
    return p
def print_fraction(numerator,denominator):
    print("{}/{}".format(numerator,denominator))