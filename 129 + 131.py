#Bài 128 + 130: Viết hàm nhập, xuất mảng 1 chiều các số thực



#Hàm kiểm tra đây có phải là số thực
def is_float(value):
    try:
        float(value)
        return True
    except ValueError:
        return False
#Hàm kiểm tra đây có phải là số nguyên
def is_option(value):
    return value.isdigit() and float(value).is_integer() and int(value) >= 0

#Hàm nhập mảng số nguyên
def enter_array_of_integer_numbers():

    list_integer_numbers = []

    n = input("Tổng số giá trị muốn nhập là ")
    while not is_option(n):
        print("Lỗi")
        n = input("Tổng số giá trị muốn nhập là ")

    #Dùng vòng lặp để nhập đối tượng vào mảng số nguyên
    for i in range(int(n)):

        integer_number = input("Nhập phần tử số nguyên thứ "+str(i+1)+" là ")
        #Nếu ko phải là số thực thì nhập lại
        while not is_float(integer_number):
            integer_number = input("Nhập lại phần tử số nguyên thứ " + str(i + 1) + " là ")
        list_integer_numbers.append(int(integer_number))

    return list_integer_numbers

#Hàm in ra mảng số nguyên
def print_array_of_integer_numbers(list):
    print()
    #Biến đếm thứ tự
    ordinal =1

    for i in list:
        print("Phần tử số nguyên thứ " + str(ordinal) + " trong mảng là " + str(i))
        ordinal+=1


if __name__ == '__main__':

    #Dùng hàm nhập
    result = enter_array_of_integer_numbers()

    #Dùng hàm xuất
    print_array_of_integer_numbers(result)
