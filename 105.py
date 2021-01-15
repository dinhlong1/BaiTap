#Bài 105: Viết chương trình nhập 1 số nguyên có 2 chữ số.  Hãy in ra cách đọc của số nguyên này

#Hàm kiểm tra giá trị nhập vào có phải là số có 2 chữ sô
def is_number(value):
    return value.isdigit() and float(value).is_integer() and 99 >= int(value) >= 10

def read_number(target_number):
    name_number= ""
    dozens_of_numbers = target_number//10
    un_of_numbers = target_number % 10

    #Cách đọc hàng chục
    if dozens_of_numbers == 1:
        name_number = name_number + "Mười"
    elif dozens_of_numbers == 2:
        name_number = name_number + "Hai Mươi"
    elif dozens_of_numbers == 3:
        name_number = name_number + "Ba Mười"
    elif dozens_of_numbers == 4:
        name_number = name_number + "Bốn Mươi"
    elif dozens_of_numbers == 5:
        name_number = name_number + "Năm Mươi"
    elif dozens_of_numbers == 6:
        name_number = name_number + "Sáu Mươi"
    elif dozens_of_numbers == 7:
        name_number = name_number + "Bảy Mươi"
    elif dozens_of_numbers == 8:
        name_number = name_number + "Tám Mươi"
    elif dozens_of_numbers == 9:
        name_number = name_number + "Chín Mươi"

    #Cách đọc hàng đơn vị
    if un_of_numbers == 1:
        name_number = name_number + "Mốt"
    elif un_of_numbers == 2:
        name_number = name_number + "Hai"
    elif un_of_numbers == 3:
        name_number = name_number + "Ba"
    elif un_of_numbers == 4:
        name_number = name_number + "Bốn"
    elif un_of_numbers == 5:
        name_number = name_number + "Năm"
    elif un_of_numbers == 6:
        name_number = name_number + "Sáu"
    elif un_of_numbers == 7:
        name_number = name_number + "Bảy"
    elif un_of_numbers == 8:
        name_number = name_number + "Tám"
    elif un_of_numbers == 9:
        name_number = name_number + "Chín"
    return name_number

if __name__ == '__main__':

    two_digit_number = input("Nhập số có 2 chữ số")

    while not is_number(two_digit_number):
        two_digit_number = input("Nhập lại số có 2 chữ số")

    result = read_number(int(two_digit_number))
    print("Cách đọc của số này là " +str(result))
