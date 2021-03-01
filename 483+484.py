# Bài 483: Hãy khai báo kiểu dữ liệu biểu diễn khái niệm đường tròn trong mặt phẳng Oxy và
# định nghĩa hàm nhập, hàm xuất cho kiểu dữ liệu này
# Bài 484: Viết chương trình nhập tọa độ tâm và bán kính của 1 đường tròn trong mặt phẳng Oxy.
# Tính diện tích và chu vi của nó và xuất ra kết quả

import mangsothuc as st
class circle():
    def __init__(self,a,b,r):
        self.a = a
        self.b = b
        self.r = r

    def set_a(self, a):
        self.a = a

    def set_b(self, b):
        self.b = b

    def set_r(self, r):
        self.r = r

    def get_a(self):
        return self.a

    def get_b(self):
        return self.b

    def get_r(self):
        return self.r

    def __str__(self):
        return "(x - {})^2 + (y - {})^2 = {}^2".format(self.a, self.b, self.r)

    def calculate_the_area_of_the_circle(self):
        return self.r * self.r * 3.14

    def calculate_the_circumference_of_the_circle(self):
        return 2 * self.r * 3.14
def create_circle():
    a = input("Nhập a")
    while st.is_float(a) == False:
        a = input("Nhập lại a")
    b = input("Nhập b")
    while st.is_float(b) == False:
        b = input("Nhập lại b")
    r = input("Nhập bán kính")
    while st.is_float(r) == False or float(r) <=  0:
        r = input("Nhập lại bán kính")
    p = circle(a,b,r)
    return p

a= create_circle()
print(a.__str__())