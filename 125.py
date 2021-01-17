#Bài 124: Viết hàm kiểm tra trong mảng các số nguyên có tồn tại giá trị chẵn nhỏ hơn 2004 hay không

#HÀm kiểm tra đây có phải là số nguyên
def is_integer(value):
    try:
        int(value)
        return True
    except ValueError:
        return False


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


#Hàm lấy ra giá trị nhỏ nhất trong mảng
def count_prime_number_in_list(list):

    #Biến đếm số nguyên tố
    count_prime_number = 0

    #Kiểm tra lần lượt các giá trị trong mảng
    for i in list:
        if int(i) <= 0:
            continue
        else:
            if is_prime_number(int(i))!=False:
                count_prime_number+=1
    return count_prime_number


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
    result = count_prime_number_in_list(list_integet_number)
    print("Tổng số giá trị là số nguyên tố  trong mảng là "+str(result))