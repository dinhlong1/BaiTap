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


#Bài 155: Hãy tìm giá trị trong mảng các số thực xa giá trị x nhất

def find_farthest_real_number(x, list):


    #Biến khoảng cách xa nhất
    farthest_range = 0

    #Gắn giá trị đầu tiên trong mảng là giá trị xa nhất
    real_number_farthest = list[0]

    if x < 0:
        for i in list:
            # Tính khoảng cách
            range_x_vs_element = abs(x-i)
            if range_x_vs_element > farthest_range or farthest_range == 0:
                farthest_range = range_x_vs_element
                real_number_farthest = i

    return real_number_farthest

#Bài 156: Hãy tìm giá trị trong mảng các số thực gần giá trị x nhất

def find_nearest_real_number(x, list):


    #Biến khoảng cách xa nhất
    nearest_range = 0

    #Gắn giá trị đầu tiên trong mảng là giá trị xa nhất
    real_number_nearest = list[0]

    if x < 0:
        for i in list:
            range_x_vs_element = abs(i - x)

            #So sánh khoảng cách vừa đo với khoảng cách hiện tại
            if range_x_vs_element < nearest_range or nearest_range == 0:
                nearest_range = range_x_vs_element
                real_number_nearest = i

    return real_number_nearest

#Bài 157: Cho mảng 1 chiều các số thực, hãy tìm đoạn [a, b] sao cho đoạn này chứa tất cả các giá trị trong mảng

def find_range_min_real_number_max_real_number(list):
    min_number = list[0]
    max_number = list[0]
    for i in list:
        if min_number > i:
            min_number = i
        if max_number <i :
            max_number = i

    return "["+str(min_number)+","+str(max_number)+"]"

#Bài 158: Cho mảng 1 chiều các số thực, hãy tìm giá trị x sao cho đoạn [-x, x] chứa tất cả các giá trị trong mảng

def find_space_contain_all_value_in_list(list):

    highest_number = abs(list[0])

    for i in list:
        if abs(i) > highest_number:
            highest_number = abs(i)

    return "[-" + str(highest_number) + "," + str(highest_number) + "]"


#Bài 159: Cho mảng 1 chiều các số thực, hãy tìm giá trị đầu tiên lớn hơn giá trị 2003. Nếu mảng không có giá trị thỏa điều kiện trên thì trả về  -1

def find_first_real_number_bigger_2003(list):
    for i in list:
        if i >2003:
            return i
    return -1

#Bài 160: Cho mảng 1 chiều các số thực, hãy tìm giá trị âm cuối cùng lớn hơn giá trị -1. Nếu mảng không có giá trị thỏa điều kiện trên thì trả về -1

def find_last_real_number_smaller(list):

    for i in range(len(list)-1,-1,-1):
        if list[i] < 0 and list[i] > -1:
            return list[i]
    return -1

#Bài 162: Cho mảng 1 chiều các số thực. Hãy viết hàm tìm một vị trí trong mảng thỏa 2 điều kiện: có 2 giá trị lân cận và giá trị tại đó bằng tích 2 giá trị lân cận.
# Nếu mảng không tồn tại giá trị như vậy thì trả về giá trị -1

def find_real_number_by_product(list):

    for i in range(1, len(list)-1):
        if list[i] == (list[i - 1] * list[i + 1]):
            return list[i]
    return -1



if __name__ == '__main__':

    #Dùng hàm nhập
    result = enter_array_of_real_numbers()
    a = find_real_number_by_product(result)

    print(a)

