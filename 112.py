#Bài 111: Viết chương trình in ra tam giác cân có độ cao h


#Kiểm tra lựa chọn
def is_option(value):
    return value.isdigit() and float(value).is_integer() and 1 <= int(value) <= 2

#Kiểm tra cạnh
def is_edge(value):
    return value.isdigit() and float(value).is_integer() and 1<= int(value)

#Hình chữ nhật đặc
def solid_rectangle(width, length):

    for row in range(width):
        for col in range(length):
            print("*", end= " ")

        #Xuống dòng
        print()

#hình chữ nhật rỗng
def hollow_rectangle(width, length):
    #Thiết kế chiều rộng
    for row in range(width):
        #thiết kế chiều cao
        for col in range(length):

            #In ngôi sao ở hàng đầu tiên, hàng cuối cùng , dòng dầu tiên và dòng cuối cùng
            if col == 0 or col == length-1 or row==0 or row == width -1:
                print("*", end=" ")
            else:
                print(end= "  ")
        #Xuống dòng
        print()

if __name__ == '__main__':
    print("1.  Hình chữ nhật đặc\n"
          "2. Hình chữ nhật rỗng")
    option = input("Nhập lựa chọn")

    while not is_option(option):
        option = input("Nhập lựa chọn hợp lệ: ")

    width = input("Nhập chiều rộng: ")

    while not is_edge(width):
        width  = input("Nhập lại chiều rộng: ")


    length = input("Nhập chiều dài: ")
    while not is_edge(length):
        length = input("Nhập lại chiều dài: ")

    if int(option) == 1:
        solid_rectangle(int(width),int(length))
    else:
        hollow_rectangle(int(width),int(length))