#Bài 97: Viết chương trình nhập 3 cạnh của 1 tam giác, cho biết đó là tam giác gì

# Kiểm tra xem đây có phải là số nguyên dương hay ko
def is_number(value):
    return value.isdigit() and float(value).is_integer() and int(value) > 0

# Hàm kiểm tra tam giác
def identify_triangle(first_edge,second_edge,third_edge):

    #Điều kiện tam giác đều
    if first_edge == second_edge and second_edge == third_edge:
        return "Đây là tam giác đều"
    #Điều kiện tam giác cân
    elif first_edge == second_edge or first_edge == third_edge or second_edge == third_edge:
        return "Đây là tam giác cân"
    #Điều kiện tam giác vuông
    elif first_edge**2 == (second_edge **2 +third_edge**2) or second_edge**2 == (first_edge**2+third_edge**2) or third_edge**2 == (first_edge**2+second_edge**2):
        return "Đây là tam giác vuông"
    #Điều kiện tam giác vuông cân
    elif (first_edge**2 == (second_edge **2 +third_edge**2) and second_edge==third_edge) or (second_edge**2 == (first_edge**2+third_edge**2) and first_edge==third_edge) or (third_edge**2 == (first_edge**2+second_edge**2) and first_edge==second_edge):
        return "Đây là tam giác vuông cân"
    else:
        return "Đây là tam giác thường"

if __name__ == '__main__':

    #Nhập giá trị 3 cạnh
    first_edge = input("Nhập độ dài cạnh đầu tiên")
    while not is_number(first_edge):
        first_edge = input("Nhập lại độ dài cạnh đầu tiên")

    second_edge = input("Nhập độ dài cạnh thứ hai")
    while not is_number(second_edge):
        second_edge = input("Nhập độ dài cạnh thứ hai")

    third_edge = input("Nhập độ dài cạnh thứ ba")
    while not is_number(third_edge):
        third_edge = input("Nhập độ dài cạnh thứ ba")

    result = identify_triangle(int(first_edge),int(second_edge),int(third_edge))

    print(result)
