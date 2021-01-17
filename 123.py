#Bài 123: Viết hàm tìm 1 vị trí mà giá trị tại vị trí đó là giá trị nhỏ nhất trong mảng 1 chiều các số nguyên

#HÀm kiểm tra đây có phải là số nguyên
def is_integer(value):
    try:
        int(value)
        return True
    except ValueError:
        return False


#Hàm lấy ra giá trị nhỏ nhất trong mảng
def smallest_number_in_list(list):

    #Gắn số nhỏ nhất cho giá trị đầu trong mảng
    smallest_number = list[0]

    #Kiểm tra lần lượt các giá trị trong mảng
    for i in list:

        #Nếu giá trị nào nhỏ hơn giá trí đang đc gán hiện tại
        #Thì chuyển qua gán giá trị đó là giá trị nhỏ nhất
        if i <smallest_number:
            smallest_number = i

    return smallest_number


if __name__ == '__main__':

    list_integet_number = []

    n = input("Tổng số giá trị muốn nhập là ")
    while not is_integer(n):
        print("Lỗi")
        n = input("Tổng số giá trị muốn nhập là ")

    #Dùng vòng lặp để nhập đối tượng vào mảng
    for i in range(int(n)):

        integer_number = input("Nhập phần tử số nguyên thứ "+str(i+1)+" là ")
        #Nếu ko phải là số nguyên thì nhập lại
        while not is_integer(integer_number):
            integer_number = input("Nhập lại phần tử số nguyên thứ " + str(i + 1) + " là ")
        list_integet_number.append(integer_number)

    #Lấy ra kết quả và in ra màn hình
    result = smallest_number_in_list(list_integet_number)
    print("Giá trị nhỏ nhất trong mảng là "+str(result))