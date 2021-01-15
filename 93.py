#Bài 93: Viết chương trình kiểm tra 1 số có phải là số nguyên tố hay không
def is_number(value):
    return value.isdigit() and float(value).is_integer() and int(value) > 0

def checkPrimeNumber(Number):
    if float(Number).is_integer() == False or int(Number) <= 0:
        return "Đây không phải là số nguyên tố"
    else:
        for i in range(2,Number):
            if Number % i == 0:
                return "Đây không phải là số nguyên tố"
        return "Đây là số nguyên tố"

if __name__ == '__main__':
    number = input("Nhập N ")

    while not is_number(number):
        number = input("Nhập lại N ")

    print(str(checkPrimeNumber(int(number))))