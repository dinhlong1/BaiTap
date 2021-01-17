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

#Hàm sắp xếp lại giá trị tăng dần trong mảng
def sort_real_number_in_list(list):

    # .sort() là hàm sắp xếp mảng , reverse=False tăng dần ,reverse là giảm dần
    list.sort(reverse=False)

    return list

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
        list_float_numbers.append(float(real_number))

    #Lấy ra kết quả và in ra màn hình
    result = sort_real_number_in_list(list_float_numbers)
    print("Các giá trị tăng dần lân lượt trong mảng là "+str(result))