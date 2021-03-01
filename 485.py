#Bài 485: Viết chương trình nhập tọa độ 3 đỉnh của 1 tam giác trong mặt phẳng Oxy.
# Tính diện tích, chu vi và tọa độ trọng tâm của tam giác và xuất ra kết quả
import math
import mangsothuc as st

def distance_calculation( xa, ya, xb, yb):
    return math.sqrt((xa - xb) ** 2 + (ya - yb) ** 2)
class triangle():
    def __init__(self,xa,ya,xb,yb,xc,yc):
        self.xa = xa
        self.ya = ya
        self.xb = xb
        self.yb = yb
        self.xc = xc
        self.yc = yc

    def set_xa(self, xa):
        self.xa = xa

    def set_xb(self, xb):
        self.xb = xb

    def set_xc(self, xc):
        self.xc = xc

    def set_ya(self, ya):
        self.ya = ya

    def set_yb(self, yb):
        self.yb = yb

    def set_yc(self, yc):
        self.yc = yc

    def get_xa(self):
        return self.xa

    def get_xb(self):
        return self.xb

    def get_xc(self):
        return self.xc

    def get_ya(self):
        return self.ya

    def get_yb(self):
        return self.yb

    def get_yc(self):
        return self.yc

    def __str__(self):
        return "(({},{}),({},{}),({},{}))".format(self.xa,self.ya,self.xb,self.yb,self.xc,self.yc)

    def calculate_the_area_of_the_triangle(self):
        return 1/2*abs((self.xb-self.xa)*(self.yc -self.ya) - (self.xc - self.xa) *(self.yb -self.ya))

    def calculate_the_circumference_of_the_triangle(self):
        return distance_calculation(self.xa,self.ya,self.xb,self.yb) + distance_calculation(self.xc,self.yc,self.xb,self.yb) + distance_calculation(self.xa,self.ya,self.xc,self.yc)

    def find_the_coordinates_of_the_center_of_the_triangle(self):
        return "({},{})".format((self.xa+self.xb+self.xc)/3, (self.ya+self.yb+self.yc)/3)

def create_triangle_in_plane_Oxy():
    x1 = input("Nhập tọa độ xA")
    while st.is_float(x1) == False:
        x1 = input("Nhập lại tọa độ xA")

    y1 = input("Nhập tọa độ yA")
    while st.is_float(y1) == False:
        y1 = input("Nhập lại tọa độ yA")

    x2 = input("Nhập tọa độ xB")
    while st.is_float(x2) == False:
        x2 = input("Nhập lại tọa độ xB")

    y2 = input("Nhập tọa độ yB")
    while st.is_float(y2) == False:
        y2 = input("Nhập lại tọa độ yB")

    x3 = input("Nhập tọa độ xC")
    while st.is_float(x3) == False:
        x3 = input("Nhập lại tọa độ xC")

    y3 = input("Nhập tọa độ yC")
    while st.is_float(y3) == False:
        y3 = input("Nhập lại tọa độ yC")

    p = triangle(x1,y1,x2,y2,x3,y3)
    return p

a = create_triangle_in_plane_Oxy()
print(a.__str__())