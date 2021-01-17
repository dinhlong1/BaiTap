#Bài 124: Viết hàm kiểm tra trong mảng các số nguyên có tồn tại giá trị chẵn nhỏ hơn 2004 hay không

#HÀm kiểm tra đây có phải là số nguyên
def is_integer(value):
    try:
        int(value)
        return True
    except ValueError:
        return False


#Hàm tìm số chẵn nhỏ hơn 2004 trong mảng
def find_even_number_smaller_2004_in_list(list):

    count_even_number_smaller_2004 =0
    #Kiểm tra lần lượt các giá trị trong mảng
    for i in list:

        #Nếu giá trị chẵn nào nhỏ hơn 2004  thì số lần tăng thêm 1
        if int(i) < 2004 and int(i) % 2 ==0:
            count_even_number_smaller_2004 += 1

    return count_even_number_smaller_2004


if __name__ == '__main__':

    list_integet_number = []

    n = input("Tổng số giá trị muốn nhập là ")
    while not is_integer(n) and int(n) <=0 :
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
    result = find_even_number_smaller_2004_in_list(list_integet_number)
    print("Tổng số giá trị chẵn nhỏ hơn 2004 trong mảng là "+str(result))