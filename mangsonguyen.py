#Bài 128 + 130: Viết hàm nhập, xuất mảng 1 chiều các số thực

import math

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

#Bài 132: Viết hàm liệt kê các giá trị chẵn trong mảng 1 chiều các số nguyên\
def find_integer_even_numbers(list):
    #Biến đếm thứ tự

    list_even_number= []

    for i in list:
        if i % 2 ==0:
            list_even_number.append(i)
    return list_even_number

#Bài 136: Tìm số chẵn cuối cùng trong mảng 1 chiều các số nguyên. Nếu mảng không có giá trị chẵn thì trả về -1
def find_last_integer_even_numbers_in_list(list):
    i = len(list) - 1
    while i > 0 :
        if int(list[i]) % 2 == 0:
            return i
        i = i -1
    return -1

#Bài 138: Tìm vị trí của giá trị chẵn đầu tiên trong mảng 1 chiều các số nguyên. Nếu mảng không có giá trị chẵn thì sẽ trả về -1

def find_first_integer_even_numbers_in_list(list):
    i = 0
    while i < len(list):
        if int(list[i]) % 2 == 0:
            return i
        i = i + 1
    return -1

#Bài 139: Tìm vị trí số hoàn thiện cuối cùng trong mảng 1 chiều các số nguyên. Nếu mảng không có số hoàn thiện thì trả về giá trị  -1

def is_perfect_number(target_number):
    Sum = 0
    for i in range(1,target_number):
        if target_number % i == 0:
            Sum = Sum + i
    if Sum == target_number:
        return True
    else:
        return False
def find_last_perfect_number_in_list(list):
    i = len(list)-1
    while i >0:
        if is_perfect_number(int(list[i])) == True:
            return i
    return -1

#Bài 143: Viết hàm tìm số chẵn đầu tiên trong mảng các số nguyên. Nếu mảng không có giá trị chẵn thì trả về  -1
def find_first_integer_even_numbers_in_list(list):
    i = 0
    while i < len(list) -1 :
        if int(list[i]) % 2 == 0:
            return i
        i = i + 1
    return -1

#Bài 144: Tìm số nguyên tố đầu tiên trong mảng 1 chiều các số nguyên. Nếu mảng không có số nguyên tố thì trả về  – 1

#Hàm tìm số nguyên tố
def is_prime_number(target_number):

    # 1, 2, 3 luôn là số nguyên tố
    if target_number== 1 or target_number== 2 or target_number== 3:
        return True
    else:
        for i in range(2,target_number,1):
            if target_number % i == 0:
                return False
        return True


def find_first_prime_number_in_list(list):
    i = 0
    while i < len(list) -1 :
        if is_prime_number(list[i]) == True:
            return list[i]
        i = i + 1
    return -1

#Bài 145: Tìm số hoàn thiện đầu tiên trong mảng 1 chiều số nguyên. Nếu mảng không có số hoàn thiện thì trả về  -1

def find_first_perfect_number_in_list(list):
    i = 0
    while i < len(list) -1 :
        if is_perfect_number(list[i]) == True:
            return list[i]
        i = i + 1
    return -1

#Bài 148: Tìm số nguyên tố cuối cùng trong mảng 1 chiều các số nguyên. Nếu mảng không có số nguyên tố thì trả về  -1

def find_last_prime_number_in_list(list):
    i = len(list) -1

    while i > 0 :
        if is_prime_number(list[i]) == True:
            return list[i]
        i = i -1
    return -1

#Bài 149: Tìm số hoàn thiện cuối cùng trong mảng 1 chiều các số nguyên. Nếu mảng không có số hoàn thiện thì trả về  -1

def find_last_perfect_number_in_list(list):

    i = len(list) -1

    while i > 0 :
        if is_perfect_number(list[i]) == True:
            return list[i]
        i = i -1
    return -1

#Bài 151: Hãy tìm số nguyên tố lớn nhất trong mảng 1 chiều các số nguyên. Nếu mảng không có số nguyên tố thì trả về -1

def find_biggest_prime_number_in_list(list):
    biggest_prime_number = -1

    for i in list:
        if is_prime_number(i) == True and biggest_prime_number < i:
            biggest_prime_number=i

    return biggest_prime_number

#Bài 152: Hãy tìm số hoàn thiện nhỏ nhất trong mảng 1 chiều các số nguyên. Nếu mảng không có số hoàn thiện thì trả về -1

def find_smallest_perfect_number_in_list(list):
    smallest_perfect_number = -1

    for i in list:
        if (is_perfect_number(i) == True and smallest_perfect_number<0) or smallest_perfect_number > i:
            smallest_perfect_number=i

    return smallest_perfect_number

#Bài 153: Hãy tìm giá trị chẵn nhỏ nhất trong mảng 1 chiều các số nguyên. Nếu mảng không có số chẵn thì trả về -1
def find_smallest_even_number_in_list(list):
    smallest_even_number = -1

    for i in list:
        if (i % 2 == 0 and smallest_even_number == -1) or (smallest_even_number > i and  i % 2 == 0):
            smallest_even_number = i

    return smallest_even_number

#Bài 161: Cho mảng 1 chiều các số nguyên, hãy tìm giá trị đầu tiên nằm trong khoảng [x, y] cho trước. Nếu mảng không có giá trị thỏa điều kiện trên thì trả về -1

def find_real_number_in_range(x,y,list):

    for i in list:
        if x > y:
            if i >=y and i <= x:
                return i
        else:
            if i <=y and i >= x:
                return i
    return -1

#Bài 163: Tìm số chính phương đầu tiên trong mảng 1 chiều các số nguyên

#Hàm kiểm tra số chính phương
def is_square_number(target_number):

    if target_number < 0:
        return False

    else:
        for i in range(1, target_number):
            if i * i == target_number:
                return True

        return False


def find_square_number_in_list_integer_number(list):
    for i in list:
        if is_square_number(i)== True:
            return i
    return -1
#Bài 164: Cho mảng 1 chiều các số nguyên. Hãy tìm giá trị đầu tiên thỏa mãn tính chất số gánh

#Hàm xác định số đảo ngược
def is_reversible_number(target_number):
    #Biến số thành chuôi
    str1 = str(target_number)
    #Đảo ngược chuôi
    str2 = str1[::-1]
    if (str1 == str2):
        return True
    else:
        return False

def find_first_reversible_number_in_list(list):
    for i in list:
        if is_reversible_number(i) == True:
            return i
    return  -1

#Bài 165: Cho mảng 1 chiều các số nguyên. Hãy tìm giá trị đầu tiên có chữ số đầu tiên là chữ số lẻ

def find_first_odd_number_in_list_integer_number(list):
    for i in list:
        if i % 2 != 0:
            return  i
    return  -1

#Bài 166: Cho mảng 1 chiều các số nguyên. Hãy viết hàm tìm giá trị đầu tiên trong mảng có dạng 2^k. Nếu mảng không có giá trị dạng 2k thì hàm sẽ trả về 0

def find_first_square_root_number_in_list_integer_number(list):
    for i in list:
        if math.sqrt(i).is_integer() == True:
            return i
    return 0

#Bài 167: Hãy tìm giá trị thỏa điều kiện toàn chữ số lẻ và là giá trị lớn nhất thỏa điều kiện ấy trong mảng 1 chiều các số nguyên.
# Nếu mảng không có giá trị thỏa điều kiện trên thì trả về 0

def is_is_number_by_all_negative(number):

    str_number = str(number)

    total_number = len(str_number) -1

    while total_number < 0:
        if int(str_number[total_number]) % 2 == 0:
            return False
        total_number = total_number - 1
    return True

def find_number_with_all_negative_number_in_list(list):

    target_number = 0
    for i in list:
        if (is_is_number_by_all_negative(i) == True and target_number ==0 ) or (is_is_number_by_all_negative(i) == True and i >target_number):
            target_number = i
    return target_number

#Bài 168: Cho mảng 1 chiều các số nguyên. Hãy viết hàm tìm giá trị lớn nhất trong mảng có dạng 5^k. Nếu mảng khong tồn tại giá trị 5^k thì hàm sẽ trả về 0


def is_number_square_root_of_five(number):
    while number != 1 :
        if number % 5 != 0:
            return False
        number = number// 5
    return True

def find_number_square_root_of_five_number_in_list_integer_number(list):

    biggeset_number_square_root_of_five = 0

    for i in list:
        if (is_number_square_root_of_five(i) == True and biggeset_number_square_root_of_five==0) or (is_number_square_root_of_five(i) == True and biggeset_number_square_root_of_five < i):
            biggeset_number_square_root_of_five = i
    return biggeset_number_square_root_of_five

#Bài 169 (*): Cho mảng 1 chiều các số nguyên. Hãy viết hàm tìm số chẵn nhỏ nhất lớn hơn mọi giá trị có trong mảng


def find_smallest_even_number_bigger_sum_numbers_in_list(list):
    sum_list = 0
    for i in list:
        sum_list = sum_list + i


    while sum_list != 0.1:
        sum_list = sum_list + 1
        if sum_list % 2 == 0:
           return sum_list




#Bài 170: Cho mảng 1 chiều các số nguyên. Hãy viết hàm tìm số nguyên tố nhỏ nhất lớn hơn mọi giá trị có trong mảng

def find_smallest_prime_number_bigger_sum_numbers_in_list(list):
    sum_list = 0
    for i in list:
        sum_list = sum_list + i

    while sum_list!=0.1:
        sum_list = sum_list + 1
        if is_prime_number(sum_list)==True:

           return sum_list

#Bài 171: Cho mảng 1 chiều các số nguyên. Hãy viết hàm tìm ước chung lớn nhất của tất cả các phần tử trong mảng

def is_number_common_divisor_in_list(x , list):
    for t in range(0, len(list)):
        if list[t] % x != 0:
            return False
    return True


def find_greatest_common_divisor_in_list(list):
    smallest_number = list[0]
    for i in list:
        if i <= 0:
            return -1
        if i < smallest_number and i >0:
            smallest_number = i
    for i in range(smallest_number, 0 , -1):
        if is_number_common_divisor_in_list(i,list) == True:
            return i

    return -1

#Bài 172: Cho mảng 1 chiều các số nguyên. Hãy viết hàm tìm bội chung nhỏ nhất của tất cả các phần tử trong mảng

def is_common_multiple_in_list(x, list):
    for i in  list:
        if x % i != 0:
            return False
    return True

def find_the_smallest_common_multiple_in_list(list):
    biggest_number = list[0]
    product_of_numbers = 1
    for i in list:
        if i <= 0:
            return -1
        else:
            product_of_numbers = product_of_numbers * i
            if i > biggest_number:
                biggest_number = i
    for i in range(biggest_number, product_of_numbers , 1):
        if is_common_multiple_in_list(i,list) == True:
            return i

    return -1

#Bài 173 (*): Cho mảng 1 chiều các số nguyên. Hãy  viết hàm tìm chữ số xuất hiện ít nhất trong mảng

def find_number_appears_least(list):
    count_number_appears_least = 0
    number_appears_least = [0]
    for i in range(1,10):
        count_number_appears = 0
        for t in list:
            count_number_appears = count_number_appears + int(str(t).count(str(i)))
        if count_number_appears < count_number_appears_least or count_number_appears_least==0:
            count_number_appears_least = count_number_appears
            number_appears_least = i
    return number_appears_least

#Bài 178: Hãy liệt kê các số chẵn trong mảng 1 chiều các số nguyên thuộc đoạn [x, y] cho trước (x, y là các số nguyên)

def find_all_number_in_space_in_list_number(x, y,list):
    list_number = []
    for i in list:
        if i <= y and i >= x and i % 2 == 0:
            list_number.append(i)
    return list_number

#Bài 179: Hãy liệt kê các giá trị trong mảng mà thỏa điều kiện lớn hơn giá trị tuyệt đối của giá trị đứng liền sau nó

def find_number_bigger_next_number_in_list(list):
    list_number =[]
    for i in range(1,len(list)-1):
        if list[i] > abs(list[i+1]):
            list_number.append(list[i])
    return list_number

#Bài 180: Hãy liệt kê các giá trị trong mảng mà thỏa điều kiện nhỏ hơn trị tuyệt đối của giá trị đứng liền sau nó
# và lớn hơn trị tuyệt đối của giá trị đứng liền trước nó

def find_number_bigger_previous_number_and_smaller_next_number_in_list(list):
    list_number =[]
    for i in range(1,len(list)-1):
        if list[i] < abs(list[i+1]) and list[i] > abs(list[i-1]) :
            list_number.append(list[i])
    return list_number
if __name__ == '__main__':

    #Dùng hàm nhập
    result = enter_array_of_integer_numbers()

    a = find_number_bigger_previous_number_and_smaller_next_number_in_list(result)
    print(a)




