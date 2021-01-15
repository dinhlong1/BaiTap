#Bài 94: Viết chương trình in ra tất cả các số lẻ nhỏ hơn 100 trừ các số 5, 7, 93

def odd_integer_less_than_100():
    list_odd_integer=[]
    for i in range(1,100,2):
        if i == 5 or i==7 or i==93:
            continue
        list_odd_integer.append(i)
    return list_odd_integer
if __name__ == '__main__':
    print(odd_integer_less_than_100())

