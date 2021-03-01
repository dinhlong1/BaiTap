#Bài 481: Hãy khai báo kiểu dữ liệu biểu diễn ngày trong thế giới thực và
# định nghĩa hàm nhập, hàm xuất cho kiểu dữ liệu này

import mangsonguyen as sn
def is_month(month):
    if 1 <= month <= 12:
        return True
    else:
        return False
def is_day_in_month(day,month,year):
    if year % 4 == 0 and month == 2:
        if 0 <= day <= 29:
            return True
        else:
            return False
    elif year % 4 != 0 and month == 2:
        if 0 <= day <= 28:
            return True
        else:
            return False
    elif month in [1,3,5,7,8,10,12]:
        if 0 <= day <= 31:
            return True
        else:
            return False
    else:
        if 0 <= day <= 30:
            return True
        else:
            return False

class Date():
    def __init__(self,day,month,year):
        self.day = day
        self.month = month
        self.year = year

    def set_day(self,day):
        self.day = day
    def set_month(self,month):
        self.month = month
    def set_year(self,year):
        self.year = year
    def get_day(self):
        return self.day
    def get_month(self):
        return self.month
    def get_year(self):
        return self.year
    def __str__(self):
        return "Ngày {} Tháng {} Năm {}".format(self.day,self.month,self.year)

def input_date():
    day = input("Nhập vào ngày")
    month = input("Nhập vào tháng")
    while sn.is_integer(month) == False or is_month(int(month)) == False:
        day = input("Nhập lại tháng")
    year = input("Nhập vào năm")
    while sn.is_integer(year) == False or int(year) < 0:
        year = input("Nhập lại năm")
    while is_day_in_month(int(day), int(month), int(year)) == False or sn.is_integer(day) == False:
        day = input("Nhập lại ngày")
    p = Date(day,month,year)
    return p
a = input_date()
print(a.__str__())