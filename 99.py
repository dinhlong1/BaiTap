#Bài 99: Viết chương trình nhập vào 3 số thực. Hãy in 3 số ấy ra màn hình theo thứ tự tang dần mà chỉ dùng tối đa 1 biến phụ

#Kiểm tra giá trị có phải là số thực hay ko
def is_real_number(value):
    return value.isalpha() == False

if __name__ == '__main__':
    list_float_number = []

    #Nhập 3 số thực
    first_number = input("Nhập số thực đầu tiên")
    while not is_real_number(first_number):
        first_number = input("Nhập lại số thực đầu tiên")

    second_number = input("Nhập số thực thứ hai")
    while not  is_real_number(second_number):
        second_number = input("Nhập lại số thực thứ hai")

    third_number = input("Nhập số thực thứ ba")
    while not  is_real_number(third_number):
        third_number = input("Nhập lại số thực thứ ba")

    #Add 3 số thực vaò mảng
    list_float_number.append(float(first_number))
    list_float_number.append(float(second_number))
    list_float_number.append(float(third_number))

    #Sắp xếp lại mảng theo thứ tự tăng dần
    result = list_float_number.sort(reverse=False)

    print(result)