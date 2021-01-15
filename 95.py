#Bài 95: Viết chương trình nhập 3 số thực. Hãy thay tất cả các số âm bằng trị tuyệt đối của nó

#Kiểm tra xem đây là số thực hay ko
def is_real_number(value):
    return value.isalpha() == False

#Kiểm tra xem số này có phải là số âm
def is_negative_number(target_number):
    return target_number < 0

def absolute_value_number(target_number):

    # Hàm trả abs trả về giá trị tuyệt đố của một số
    return abs(target_number)

if __name__ == '__main__':
    list_real_number= []

    #Nhập vào một số thực nếu giá trị nhập vào ko phải là số thì nhập lại
    first_number = input("Nhập số thực đầu tiên")
    while not is_real_number(first_number):
        first_number = input("Nhập lại số thực đầu tiên")

    second_number = input("Nhập số thực thứ 2")
    while not is_real_number(second_number):
        second_number = input("Nhập lại số thực thứ 2")

    third_number = input("Nhập số thực thứ 3")
    while not is_real_number(third_number):
        third_number = input("Nhập lại số thực thứ 3")

    #Gom các số thực vào một mảng
    list_real_number.append(float(first_number))
    list_real_number.append(float(second_number))
    list_real_number.append(float(third_number))


    for i in range(0,len(list_real_number)):

        # Nếu giá trị của phần tử trong mảng nhỏ hơn 0 thì chuyển đổi giá trị đó thành giá trị tuyệt đối
        if is_negative_number(list_real_number[i]):
             list_real_number[i] = absolute_value_number(list_real_number[i])

    print(list_real_number)


