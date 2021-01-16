#Bài 111: Viết chương trình in ra tam giác cân có độ cao h


#Kiểm tra lựa chọn
def is_option(value):
    return value.isdigit() and float(value).is_integer() and 1 <= int(value) <= 4

#Kiểm tra chiều cao
def is_height(value):
    return value.isdigit() and float(value).is_integer() and 1<= int(value)

#Hàm vẽ tam giác cân đặc
def triangle_solid(height):

    #Tạo chiều cao của tam giác
    for row in  range(0, height):

        # Tạo khoảng trống ở trước nếu số đầu tiên có height - row - 2 ô trống
        # Nếu row càng nhiều thì sẽ có ít " "
        # - 2 để chỗ cho dòng "*" và " "
        for i in range(0,height - row - 1):
            print(end=" ")

        #In ra số * bằng đúng với row đang nhận ở từng dòng
        # Nếu row bằng 1 thì in ra 1 ngôi sao, nếu == 2 thì in ra 2 ngôi sao
        for i in range(0, row +1 ):
            print("*" ,end=" ")

        #Xuống dòng
        print()

#Hàm vẽ tam giác cân rỗng
def triangle_hollow(height):

    #Tạo chiều cao của tam giác
    for row in  range(1, height+1):

        # Tạo khoảng trống ở trước nếu số đầu tiên có height - row - 2 ô trống
        # Nếu row càng nhiều thì sẽ có ít " "
        # - 2 để chỗ cho dòng "*" và " "
        for i in range(1,height*2):

            # 3 điều kiển để in ra "*"
            # 1. Luôn Luôn in ra ngôi sao ở dòng cuối cùng(Cạnh đáy)
            # 2. Tổng dòng và cột để in ra "*"  luôn bằng tổng số hàng cộng với 1(Cạnh trước)
            # Ví dụ nếu có 4 hàng thì vị trí in đầu tiên sẽ là vị trí 4 và dòng đâu tiên
            # còn dòng thứ 2 sẽ là vị trí thứ 3
            # 3. Đây là điều kiện để vẽ cạnh đối diện (cạnh sau)
            # Cạnh sau có vị trí đối diện cạnh trước
            # nên vị cạnh sau trừ cho dòng hiện tại sẽ luôn bằng tổng số dòng trừ đi một
            # bởi đỉnh ko có cạnh đối diện
            if row == height or row + i == height + 1 or i - row == height -1:
                print( "*",end="")
            else:
                print(end=" ")

        #Xuống dòng
        print()

#Hàm vẽ tam giác vuông cân rỗng
def triangle_right_angle_hollow(height):

    #Xác định số ra dòng
    for row in range(height):
        # in ra độ dài cạnh dưới bằng cạnh ngang
        for col in range(height):

            # Luôn in ra ngôi sao ở hàng đầu tiên
            # Luôn in ra ở hàng cuối cùng
            # Cạnh cuối luôn có vị trí cột và hàng bằng nha
            if col == 0 or row == (height - 1) or row == col:
                print("*", end="  ")

            #Nếu ko thì in ra khoảng trắng
            else:
                print(end="   ")

        #Xuống dòng
        print()

#Hàm vẽ tam giác vuông cân đặc
def triangle_right_angle_solid(height):

    # Xác định số dòng
    for row in range(height):

        #Xác định sô cột bằng dòng để vuông cân tam giác
        for col in range(row):

            #Dòng thứ bao nhiêu thì in ra bấy nhiêu ngôi sao
            print("* ",end= " ")
        print()

if __name__ == '__main__':
    print("1. Vẽ hình tam giác cân đặc\n"
          "2. Vẽ hình tam giác cân rỗng\n"
          "3. Vẽ Tam giác  vuông cân đặc\n"
          "4. Vẽ Tam giác  vuông cân rỗng")

    option = input("Nhập lựa chọn")

    while not is_option(option):
        option = input("Nhập lựa chọn hợp lệ: ")

    height = input("Nhập chiều cao")

    while not is_height(height):
        height = input("Nhập lại chiều cao: ")
    if int(option) == 1:
        triangle_solid(int(height))
    elif int(option) == 2:
        triangle_hollow(int(height))
    elif int(option) == 3:
        triangle_right_angle_solid(int(height))
    else:
        triangle_right_angle_hollow(int(height))