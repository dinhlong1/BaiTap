

#Kiểm tra giá tị nhập vào có phải là số nguyên dương
def is_number(value):
    return value.isalpha() == False

#Hàm kiểm tra số chính phương
def is_square_number(target_number):

    if target_number < 0:
        return False

    else:
        for i in range(1, target_number):
            if i * i == target_number:
                return True

        return False

if __name__ == '__main__':

    # Nhập giá trị
    n = input("Nhập n ")
    while not is_number(n):
        n = input("Nhập lại n ")

    list_square_number =[]
    for i in range(1,int(n)):

        if is_square_number(i) == True:
            list_square_number.append((i))

    print("Kết quả các số chính phương nhỏ hơn n là " +str(list_square_number))
