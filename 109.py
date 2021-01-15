#Bài 109: Viết chương trình in bảng cửu chương ra màn hình

#Hàm in ra bảng cửu chương
def multiplication_table():
    for i in range(1,10):
        for t in range(1,10):
            print(str(i) +" * "+str(t)+" = " +str(i*t))
        print("")

if __name__ == '__main__':

    #in ra bảng cửu chương
    multiplication_table()