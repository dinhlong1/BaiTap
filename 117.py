# Bài 117: Viết chương trình nhập n và tính tổng S(n) = x + x^2 + x^3 + … + x^n

def is_number(value):
    return value.isdigit() and float(value).is_integer() and int(value) > 0


# Tính hàm S(n) = x + x^2 + x^3 + … + x^n
def caculate_sum( target_number , x):
    #Gắn tống bằng biến sum
    Sum = 0

    #Dùng vòng lặp để tính tổng
    for i in range(1,target_number+1):

        #Lần lượt lấy x^i để cộng vào tổng, i đi từ 1 đến n
        Sum = Sum + x**i

    #Trả vể tổng sau khi thực hiện xong vòng lặp
    return Sum


if __name__ == '__main__':

    #Nhập giá trị
    n = input("Nhập n ")
    while not is_number(n):
        n = input("Nhập lại n ")

    x = input("Nhập x ")
    while not is_number(x):
        x = input("Nhập lại x ")

    #Dùng hàm để tính tổng
    result = caculate_sum(int(n), int(x))
    print("Kết quả là " +str(result))