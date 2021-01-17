#Bài 126: Viết hàm tính tổng các giá trị âm trong mảng 1 chiều các số thực


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

#Hàm tính tổng giá trị âm trong mảng
def caculate_sum_negative_number_in_list(list):

    #Gắn tổng các giá trị âm bằng 1 biến
    sum_negative_number = 0

    #Kiểm tra lần lượt các giá trị trong mảng
    for i in list:

        #Nếu giá trị nào nhỏ hơn 0 thì cộng nó với biến tổng
        if float(i) < 0:
            sum_negative_number = sum_negative_number + float(i)

    return sum_negative_number

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
    result = caculate_sum_negative_number_in_list(list_float_numbers)
    print("Tổng các giá trị âm trong mảng là "+str(result))