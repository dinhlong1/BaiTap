#Bài 101: Viết chương trình nhập tháng, năm. Hãy cho biết tháng đó có bao nhiêu ngày

#Hàm kiểm tra tháng hợp lệ
def is_month(value):
    return value.isdigit() and 1<=int(value)<=12

#Hàm kiểm tra năm hợp lệ
def is_year(value):
    return  value.isdigit() and 1<= int(value)

def days_of_month(month,year):

    #Tháng 2 năm nhuận có 29 ngày
    if month==2 and year %4==0:
        return 29

    #Tháng 2 năm ko nhuận có 28 ngày
    elif month==2 and year %4 != 0:
        return 28

    #Tháng 4,6,9,11 có 30 ngày
    elif month==4 or month==6 or month==9 or month==11:
        return 30

    #Các tháng còn lại có 31 ngày
    else:
        return 31
if __name__ == '__main__':

    #Nhập tháng năm
    month = input("Nhập tháng ")
    while not is_month(month):
        month= input("Nhập lại tháng ")

    year = input("Nhập năm ")
    while not is_year(year):
        year = input("Nhập lại năm ")


    #Tìm kết quả
    result = days_of_month(int(month),int(year))
    print("Số ngày trong tháng đó là " + str(result))
