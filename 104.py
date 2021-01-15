#Bài 104: Viết chương trình nhập ngày, tháng, năm. Tính xem ngày đó là ngày thứ bao nhiêu trong năm


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

#Hàm đếm xem ngày đó là ngày bao nhiêu trong năm
def count_day_in_year(day, month, year):
    day_year = 0
    if year %4 == 0:
        day_year = 1
    if month == 1:
        day_year = day
    elif month == 2:
        day_year = 31 + day
    elif month == 3:
        day_year = day_year + 31 + 28 + day
    elif month == 4:
        day_year = day_year + 31 + 28 + 31 + day
    elif month == 5:
        day_year = day_year + 31 + 28 + 31 + 30 +day
    elif month == 6:
        day_year = day_year + 31 + 28 + 31 + 30 + 31 + day
    elif month == 7:
        day_year = day_year + 31 + 28 + 31 + 30 + 31 + 30 + day
    elif month == 8:
        day_year = day_year + 31 + 28 + 31 + 30 + 31 + 30 + 31 + day
    elif month == 9:
        day_year = day_year + 31 + 28 + 31 + 30 + 31 + 30 + 31 + 31 + day
    elif month == 10:
        day_year = day_year + 31 + 28 + 31 + 30 + 31 + 30 + 31 + 31 + 30 + day
    elif month == 11:
        day_year = day_year + 31 + 28 + 31 + 30 + 31 + 30 + 31 + 31 + 30 + 31 + day
    elif month == 12:
        day_year = day_year + 31 + 28 + 31 + 30 + 31 + 30 + 31 + 31 + 30 + 31 + 30 + day

    return day_year


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

    result = count_day_in_year(int(day), int(month),int(year))
    print("Đây là ngày thứ "+str(result)+" trong năm")


