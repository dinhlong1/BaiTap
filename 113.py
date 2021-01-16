#Bài 113: Lập chương trình tính sin(x) với độ chính xác 0.00001 theo công thức:
# Sin(x) = x – x^3/3! + x^5/5! + … + (-1)^n . x^2n + 1/(2n + 1)!

#Hàm kiểm tra giá trị có phải là số hay ko
def is_number(value):
    return value.isdigit()  and float(value).is_integer() and int(value) >= 0

# Giải hàm số Sin(x) = x – x^3/3! + x^5/5! + … + (-1)^n . x^2n + 1/(2n + 1)!
def solve_functions_sinx(x , n):
   result = x
   if n != 0:

       #giải lần lượt từ 1 - n
       for i in range(1,n + 1):
            giaithua = 1

            # Tính giai thừ
            for t in range(1,2*i+2):
                giaithua = giaithua * t

            #Giải hàm số (-1)^n . x^(2n + 1)/(2n + 1)!
            result = result + (((-1) ** i ) * (x **(2*i +1)) / int(giaithua))
   return result

if __name__ == '__main__':
    x = input("Nhập x = ")
    while not is_number(x):
        width  = input("Nhập lại x = ")


    n = input("Nhập n = ")
    while not is_number(n):
        n = input("Nhập lại n = ")

    result = solve_functions_sinx(int(x), int(n))
    print("Kết quả là " + str(result))