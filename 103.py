#Bài 103: Viết chương trình nhập vào 1 ngày ( ngày, tháng, năm). Tìm ngày trước ngày vừa nhập (ngày, tháng, năm)

#Kiểm tra ngày hợp lệ
def is_day_in_month(day, month, year):
    if month == 4 or month == 6 or month == 9 or month == 11:
        return day.isdigit() and 1 <= int(day) and  int(day)<= 30
    elif month == 2 and year % 4 == 0:
         return day.isdigit() and 1 <= int(day) and int(day) <= 29
    elif month == 2 and year % 4 != 0:
        return day.isdigit() and 1 <= int(day) and int(day) <= 28
    else:
        return day.isdigit() and 1 <= int(day) and int(day) <= 31

#Hàm kiểm tra tháng hợp lệ
def is_month(value):
    return value.isdigit() and 1 <= int(value) <= 12

#Hàm kiểm tra năm hợp lệ
def is_year(value):
    return  value.isdigit() and 1<= int(value)

#Hàm tính ngày kế tiếp của ngày vừa nhập
def find_day_before(day, month, year):

    if day == 1 and (month==5 or month==7 or month==10 or month==12):
        return "Ngày trước đó là ngày 31/"+ str(month - 1) + "/" +str(year)

    elif day == 1 and month == 1:
        return "Ngày trước đó là ngày 31/12/"+ str(year-1)

    elif day == 1 and month==3 and year % 4 == 0:
        return "Ngày trước đó là ngày 29/2/" + str(year)

    elif day == 1 and month==3 and year % 4 != 0:
        return "Ngày trước đó là ngày 28/2/" + str(year)

    elif day==1 and (month==2 or month==4 or month==6 or month==8 or month==9 or month==11):
        return "Ngày trước đó là ngày 31/" + str(month - 1) + "/" + str(year)
    else:
        return "Ngày trước đó là ngày " + str(day-1)+"/" +str(month) + "/" +str(year)

if __name__ == '__main__':


    # Nhập ngày tháng năm
    day = input("Nhập ngày ")

    month = input("Nhập tháng ")
    while not is_month(month):
        month = input("Nhập lại tháng ")

    year = input("Nhập năm ")
    while not is_year(year):
        year = input("Nhập lại năm ")

    while not is_day_in_month(day, month, year):
        day = input("Nhập lại ngày hợp lệ")

    result = find_day_before(int(day), int(month),int(year))
    print(result)