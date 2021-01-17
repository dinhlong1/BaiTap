#Bài 122: Viết hàm tìm giá trị lớn nhất trong mảng 1 chiều các số thực


#Hàm kiểm tra đây có phải là số thực
def is_float(value):
    try:
        float(value)
        return True
    except ValueError:
        return False
#Hàm kiểm tra đây có phải là số nguyên
def is_option(value):
    try:
        int(value)
        return True
    except ValueError:
        return False

#Hàm lấy ra số lớn nhất trong mảng
def biggest_number_in_list(list):

    #Gắn số lớn nhất cho giá trị đầu trong mảng
    biggest_number = list[0]

    #Kiểm tra lần lượt các giá trị trong mảng
    for i in list:

        #Nếu giá trị nào lớn hơn giá trí đang đc gán hiện tại
        #Thì chuyển qua gán giá trị đó là giá trị lớn nhất
        if i >biggest_number:
            biggest_number = i

    return biggest_number

if __name__ == '__main__':

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
        list_float_numbers.append(real_number)

    #Lấy ra kết quả và in ra màn hình
    result = biggest_number_in_list(list_float_numbers)
    print("Giá trị lớn nhất trong mảng là "+str(result))

