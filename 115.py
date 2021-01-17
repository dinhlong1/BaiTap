# Bài 115: Viết chương trình nhập họ tên, điểm toán, điểm văn của 1 học sinh. Tính điểm trung bình và xuất ra kết quả

#Hàm kiểm tra điểm nhập vào
def is_score(value):
    return value.isdigit() and float(value).is_integer() and 10 >= int(value) >= 0

#Hàm tính điểm trung bình của 2 môn
def average_two_score(name, first_score, second_score):

    return "Điểm trung bình của " +str(name) +" là "+str((first_score + second_score)/2)

if __name__ == '__main__':

    #Nhập thông tin
    name = input("Nhập họ tên")

    #Nhập điểm Toán
    math_score = input("Nhập điểm Toán ")
    while not is_score(math_score):
        math_score = input("Nhập lại điểm Toán ")

    #Nhập điểm văn
    literature_score = input("Nhập điểm văn ")
    while not is_score(literature_score):
        literature_score= input("Nhập lại điểm Văn ")

    result = average_two_score(name , int(math_score),int(literature_score))
    print(result)


