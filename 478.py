#Bài 478: Hãy khai báo kiểu dữ liệu biểu diễn khái niệm điểm trong không gian Oxyz và định nghĩa hàm nhập, hàm xuất cho kiểu dữ liệu này

import mangsothuc as st

class Coordinates():
    def __init__(self,x,y,z):
        self.x = x
        self.y = y
        self.z = z
    def set_x(self,x):
        self.x = x
    def set_y(self,y):
        self.y = y
    def set_z(self, z):
        self.z = z
    def get_x(self):
        return self.x
    def get_y(self):
        return self.y
    def get_z(self):
        return self.z
    def __str__(self):
        return "({},{},{})".format(self.x,self.y,self.z)

def create_coordinates():
    x = input("Nhập x")
    while st.is_float(x) == False:
        x = input("Nhập lại x")
    y = input("Nhập y")
    while st.is_float(y) == False :
        y = input("Nhập lại y")
    z = input("Nhập z")
    while st.is_float(z) == False:
        z = input("Nhập lại z")
    p = Coordinates(x,y,z)
    return p
def print_coordinates(x,y,z):
    print("({},{},{})".format(x,y,z))