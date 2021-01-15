#Bài 107: Viết hàm tính S = CanBacN(x)

#Kiểm tra xem giá trị đó có phải số nguyên
def is_number(value):
    return value.isdigit() and  float(value).is_integer()

#HÀm tính căn mũ N
def square_root_n(x,n):
    return float(x ** (1/n))

if __name__ == '__main__':

    # Nhập số mũ
    n = input("Nhập số mũ N ")
    while not is_number(n):
        n = input("Nhập lại số mũ")

    #Nhập x
    x = input("Nhập x ")
    while not is_number(x):
        x = input("Nhập lại x")

    result = square_root_n(int(x), int(n))
    print("Kết quả hàm căn x mũ n là " +str(result))

