#Bài 119: Liệt kê tất cả các số nguyên tố nhỏ hơn n


#Kiểm tra giá tị nhập vào có phải là số nguyên dương
def is_number(value):
    return value.isdigit() and float(value).is_integer() and int(value) > 0

#Hàm tìm số nguyên tố
def is_prime_number(target_number):

    if target_number== 1 or target_number== 2 or target_number== 3:
        return True
    else:
        for i in range(2,target_number,1):
            if target_number % i == 0:
                return False

if __name__ == '__main__':

    # Nhập giá trị
    n = input("Nhập n ")
    while not is_number(n):
        n = input("Nhập lại n ")

    #Mảng chứ số nguyên tố
    list_prime_number = []

    for i in range(1,int(n)):
        if is_prime_number(i) != False :
            list_prime_number.append(i)

    print("Các số nguyên tố nhỏ hơn n lần lượt là " + str(list_prime_number))
