#Bài 91: In tất cả các số nguyên dương lẻ nhỏ hơn 100

def ListOddPositiveIntegers():
    OddPositiveIntegers = []
    for i in range(1,100,2):
        OddPositiveIntegers.append(i)
    return OddPositiveIntegers

if __name__ == '__main__':

    print("Các số nguyên lẻ nhỏ hơn 100 là " + str(ListOddPositiveIntegers()))

