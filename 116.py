# Bài 116: Viết chương trình nhập n và tính tổng S = 1 + 2 + 3 + … + n

#Kiểm tra giá trị nhập vào có phải là số nguyên dương
def is_number(value):
    return value.isdigit() and float(value).is_integer() and int(value) > 0


# Hàm tính tổng S = 1 + 2 + 3 + … + n
def caculate_sum( target_number):
    #Gắn tống bằng biến sum
    Sum = 0

    #Dùng vòng lặp để tính tổng
    for i in range(1,target_number+1):
        Sum = Sum + i

    #Trả vể tổng sau khi thực hiện xong vòng lặp
    return Sum

if __name__ == '__main__':

    #Nhập giá trị
    n = input("Nhập n ")
    while not is_number(n):
        n = input("Nhập lại n ")

    #Dùng hàm để tính tổng
    result = caculate_sum(int(n))
    print("Kết quả là " +str(result))
