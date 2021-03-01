#Bài 476: Hãy khai báo kiểu dữ liệu biểu diễn khái niệm hỗn số trong toán học và
# định nghĩa hàm nhập, hàm xuất cho kiểu dữ liệu này
import mangsonguyen as sn

class mixedNumbers():
    def __init__(self,integer,numerator,denominator):
        self.integer = integer
        self.numerator = numerator
        self.denominator = denominator
    def set_integer(self,integer):
        self.integer = integer
    def set_numerator(self,numerator):
        self.numerator = numerator
    def set_denominator(self,denominator):
        self.denominator = denominator
    def get_integer(self):
        return self.integer
    def get_numerator(self):
        return self.numerator
    def get_denominator(self):
        return self.denominator
    def __str__(self):
        return "{}({}/{})".format(self.integer,self.numerator,self.denominator)

def create_mixed_numbers():
    integer = input("Nhập phần nguyên")
    while sn.is_integer(integer) == False:
        integer = input("Nhập lại phần nguyên")
    numerator = input("Nhập tử số")
    while sn.is_integer(numerator):
        numerator = input("Nhập lại tử số")
    denominator = input("Nhập mẫu số")
    while sn.is_integer(denominator) == False or denominator == 0:
        denominator = input("Nhập lại mẫu số")
    p = mixedNumbers(integer,numerator,denominator)
    return p
def print_mixed_numbers(integer,numerator,denominator):
    print("{}({}/{})".format(integer,numerator,denominator))