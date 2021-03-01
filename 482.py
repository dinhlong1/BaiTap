#Bài 482: Hãy khai báo kiểu dữ liệu biểu diễn khái niệm đường thẳng ax + by + c = 0 trong mặt phẳng Oxy
# và định nghĩa hàm nhập, hàm xuất cho kiểu dữ liệu này
import mangsothuc as st

class straightLine():
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c
    def set_a(self, a):
        self.a = a

    def set_b(self, b):
        self.b = b

    def set_c(self, c):
        self.c = c

    def get_a(self):
        return self.a

    def get_b(self):
        return self.b

    def get_c(self):
        return self.c

    def __str__(self):
        return "{}x + {}y + {} = 0".format(self.a, self.b, self.c)

def create_straight_line():
    a = input("Nhập a")
    while st.is_float(a) == False:
        a = input("Nhập lại a")
    b = input("Nhập b")
    while st.is_float(b) == False:
        b = input("Nhập lại b")
    c = input("Nhập c")
    while st.is_float(c) == False:
        c = input("Nhập lại c")
    p = straightLine(a,b,c)
    return p
a = create_straight_line()
print(a.__str__())