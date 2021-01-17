#Bài 128 + 130: Viết hàm nhập, xuất mảng 1 chiều các số thực

import numpy as np

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
def enter_array_of_real_numbers():

    list_float_numbers = []

    n = input("Tổng số giá trị muốn nhập là ")
    while not is_option(n):
        print("Lỗi")
        n = input("Tổng số giá trị muốn nhập là ")

    #Dùng vòng lặp để nhập đối tượng vào mảng số thực
    for i in range(int(n)):

        real_number = input("Nhập phần tử số thực thứ "+str(i+1)+" là ")
        #Nếu ko phải là số thực thì nhập lại
        while not is_float(real_number):
            real_number = input("Nhập lại phần tử số thực thứ " + str(i + 1) + " là ")
        list_float_numbers.append(float(real_number))

    return list_float_numbers

#Hàm in ra mảng số thực
def print_array_of_real_numbers(list):
    print()
    #Biến đếm thứ tự
    ordinal =1

    for i in list:
        print("Phần tử số thực thứ " + str(ordinal) + " trong mảng là " + str(i))
        ordinal+=1


# Bài 133: Viết hàm liệt kê các vị trí mà giá trị tại đó là giá trị âm trong mảng 1 chiều các số thực
def find_locate_negative_number(list):
    # Biến đếm thứ tự
    ordinal = 0

    list_locate=[]

    for i in list:

        if i < 0:
            #Nếu phần tự nhỏ hơn 0 thì cho vị trí vào list
            list_locate.append(ordinal)
        ordinal += 1

    return list_locate

#Bài 134: Viết hàm tìm giá trị lớn nhất trong mảng 1 chiều các số thực
def find_biggest_real_number(list):
    biggest_number = list[0]

    for i in list:
        if biggest_number<i:
            biggest_number=i
    return biggest_number

#Bài 135: Viết hàm tìm giá trị dương đầu tiên trong mảng 1 chiều các số thực. Nếu mảng không có giá trị dương thì trả về -1
def find_first_positive_numbers_in_list_real_number(list):

    for i in list:
        if i > 0:
            return i
    return -1

#Bài 137: Tìm 1 vị trí mà giá trị tại vị trí đó là giá trị nhỏ nhất trong mảng 1 chiều các số thực
def find_locate_smallest_numbers_in_list_real_number(list):
    i = 1

    ordinal = 0
    smallest_number= list[0]

    while i < len(list) :
        if float(list[i]) < smallest_number:
            smallest_number = float(list[i])
            ordinal = i
        i = i+1
    return ordinal

#Bài 140: Hãy tìm giá trị dương nhỏ nhất trong mảng 1 chiều các số thực. Nếu mảng không có giá trị dương thì sẽ trả về -1
def find_smallest_positive_numbers_in_list_real_number(list):
    smallest_positive_number = -1

    for i in list:
        if (i > 0 and smallest_positive_number <0) or (i < smallest_positive_number and i >0):
            smallest_positive_number=i

    return smallest_positive_number

#Bài 141: Hãy tìm vị trí giá trị dương nhỏ nhất trong mảng 1 chiều các số thực. Nếu mảng không có giá trị dương thì trả về  -1
def find_locate_smallest_positive_numbers_in_list_real_number(list):

    ordinal = -1
    smallest_positive_number = -1
    for i in range(0,len(list)):
        if (list[i] > 0 and smallest_positive_number <0) or (list[i] < smallest_positive_number and list[i] > 0):
            smallest_positive_number = list[i]
            ordinal =i

    return ordinal

#Bài 142: Tìm giá trị nhỏ nhất trong mảng 1 chiều số thực
def find_smallest_numbers_in_list_real_number(list):
    i = 1

    smallest_number= list[0]

    while i < len(list) :
        if list[i] < smallest_number:
            smallest_number = list[i]

        i = i+1
    return smallest_number

#Bài 146: Tìm giá trị âm đầu tiên trong mảng 1 chiều các số thực. Nếu mảng không có giá trị âm thì trả về -1
def find_first_negative_number_in_list_real_number(list):
    i = 0
    while i < len(list) -1 :
        if list[i]<0:
            return list[i]
        i = i + 1
    return -1

#Bài 147: Tìm số dương cuối cùng trong mảng số thực. Nếu mảng không có giá trị dương thì trả về  -1

def find_last_positive_number_in_list_real_number(list):
    i = len(list)-1
    while i >0:
        if list[i] >0:
            return i
        i = i-1
    return -1


#Bài 150: Hãy tìm giá trị âm lớn nhất trong mảng 1 chiều các số thực. Nếu mảng không có giá trị âm thì trả về  -1

def find_smallest_negative_numbers_in_list_real_number(list):
    smallest_negative_numbers = 1
    for i in list:
        if (i < 0 and smallest_negative_numbers> 0) or (i > smallest_negative_numbers and i < 0):
            smallest_negative_numbers = i

    if smallest_negative_numbers == 1:
        smallest_negative_numbers= -1
    return smallest_negative_numbers
#Bài 154: Hãy tìm vị trí giá trị âm nhỏ nhất trong mảng các số thực. Nếu mảng không có số âm thì trả về -1

def find_locate_smallest_negative_numbers_in_list_real_number(list):
    locate = 1
    i = 0
    while i < len(list) - 1:
        if (list[i] < 0 and locate > 0) or (list[i] < smallest_negative_numbers and list[i] < 0):
            smallest_negative_numbers=list[i]
            locate = i
        i = i + 1
    if locate == 1:
        locate = -1
    return locate



if __name__ == '__main__':

    #Dùng hàm nhập
    result = enter_array_of_real_numbers()
    a = find_locate_smallest_negative_numbers_in_list_real_number(result)

    print(a)
