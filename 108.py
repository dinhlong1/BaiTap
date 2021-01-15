#Bài 108:  Viết hàm tính S = x^y

def is_number(value):
    return value.isdigit() and float(value).is_integer()

#Hàm x^y
def function_solving(x,y):
    return x ** y

if __name__ == '__main__':

    #Nhập vào x và y
    x= input("Nhập x ")
    while not is_number(x):
        x = input("Nhập x ")

    y = input("Nhập y ")
    while not is_number(y):
        y = input("Nhập y ")

    #Giải Hàm và đưa ra kết quả
    result = function_solving(int(x),int(y))

    print("Kết quả của hàm số " +str(x)+"^"+str(y) +" là " +str(result))