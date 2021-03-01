# Bài 479: Hãy khai báo kiểu dữ liệu biểu diễn khái niệm đơn thức P(x) = ax^n trong toán học và
# định nghĩa và định nghĩa hàm nhập, hàm xuất cho kiểu dữ liệu này

import mangsonguyen as sn

class monomial():
    def __init__(self,a,n):
        self.a = a
        self.n = n
    def set_a(self,a):
        self.a = a
    def set_n(self,n):
        self.n = n
    def get_a(self):
        return self.a
    def get_n(self):
        return self.n
    def __str__(self):
        return "{}x^{}".format(self.a,self.n)

# Bài 486: Tính tích 2 đơn thức
    def caculate_the_product_of_two_monomials(self,other):
        z = self.a * other.a
        x = self.n + other.n
        p = monomial(z,x)
        return p
# Bài 487: Tính đạo hàm cấp 1 đơn thức
    def calculate_the_derivative_of_the_unilateral_level(self):
        z = self.a * self.n
        x = self.n - 1
        p = monomial(z, x)
        return p
# Bài 488: Tính thương 2 đơn thức
    def calculate_the_quotient_of_two_monomials(self,other):
        z = self.a / other.a
        x = self.n - other.n
        p = monomial(z, x)
        return p
# Bài 489: Tính đạo hàm cấp k đơn thức
    def caculate_monomial_k_level_derivatives(self,k):
        p = monomial(self.a,self.n)
        while k > 0:
            p = p.calculate_the_derivative_of_the_unilateral_level()
            k -= 1
        return p
# Bài 490: Tính giá trị đơn thức tại vị trí x=x0
    def caculate_the_monomial_value_at_position_x(self,x):
        return self.a * (x ** self.n)
# Bài 491: Định nghĩa toán tử (operator *) cho 2 đơn thức
    def __mul__(self,other):
        z = self.a * other.a
        x = self.n + other.n
        p = monomial(z, x)
        return p
# Bài 492: Định nghĩa toán tử (operator /) cho 2 đơn thức
    def __truediv__(self,other):
        z = self.a / other.a
        x = self.n - other.n
        p = monomial(z, x)
        return p



#Hàm tạo đơn thức
def create_monomial():
    a = input("Nhập a")
    while sn.is_integer(a) == False:
        a = input("Nhập lại a")
    n = input("Nhập n")
    while sn.is_integer(n) == False:
        n = input("Nhập lại n")
    p = monomial(int(a),int(n))
    return p
def print_monomial(numerator,denominator):
    print("{}/{}".format(numerator,denominator))

a = create_monomial()
b = create_monomial()
print((a * b).__str__())




