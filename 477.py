##Bài 477: Hãy khai báo kiểu dữ liệu biểu diễn khái niệm điểm trong mặt phẳng Oxy và
# định nghĩa hàm nhập, hàm xuất cho kiểu dữ liệu này
import mangsothuc as st

class Coordinates():
    def __init__(self,x,y):
        self.x = x
        self.y = y
    def set_x(self,x):
        self.x = x
    def set_y(self,y):
        self.y = y
    def get_x(self):
        return self.x
    def get_y(self):
        return self.y
    def __str__(self):
        return "({},{})".format(self.x,self.y)

def create_coordinates():
    x = input("Nhập x")
    while st.is_float(x) == False:
        x = input("Nhập lại x")
    y = input("Nhập y")
    while st.is_float(y) == False :
        y = input("Nhập lại y")
    p = Coordinates(x,y)
    return p
def print_coordinates(x,y):
    print("({},{})".format(x,y))