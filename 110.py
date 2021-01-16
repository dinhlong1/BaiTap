#Bài 110: Cần có tổng 200000 đồng từ 3 loại giấy bạc 1000 đồng, 2000 đồng, 5000 đồng. Lập chương trình để tìm ra tất cả các phương án có thể


def find_way_to_get_200000():

    #Tổng số cách
    total_way = 0

    # Tổng số tờ 1000 có thể lấy để đủ 200000 là 200 tờ nên giới hạn lấy ra tối đa là 200
    for i in  range(1,201):

        # Tổng số tờ 2000 có thể lấy để đủ 200000 là 100 tờ nên giới hạn lấy ra tối đa là 100
        for t in range(1,101):

            # Tổng số tờ 5000 có thể lấy để đủ 200000 là 40 tờ nên giới hạn lấy ra tối đa là 40
            for v in range(1,40):

                #Nếu tổng tiền của các tờ cộng lại với nhau mà bằng 200000 đồng thì in ra kết qua
                if (i * 1000) + (t * 2000) + (v * 5000) == 200000:
                    print( str(i) + " tờ 1000 đồng + " + str(t) +" tờ 2000 đồng + " + str(v) + " tờ 5000 đồng = 200000 đồng")
                    total_way = total_way +1

    print("Tổng số cách để lấy ra 200000 đồng từ 1000,2000,5000 là " + str(total_way) + " cách")


if __name__ == '__main__':

    #Chạy chương trình
    find_way_to_get_200000()