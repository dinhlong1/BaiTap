input = "D:\BaiTap\Bai.Tap\\7o7.py\nD:\BaiTap\iTap\\7i9.cpp\nC:\BaiTap\\78.qt\nD:\BaiTap\\69.bat"
print(input)

fileName = []   #List tên file sau khi tách

listPath = input.splitlines()    #Tách chuỗi ký tự từ \n
for i in listPath:
    indexLastDot = i.rfind('.')     #Tìm dấu chấm cuối cùng ở chuỗi
    indexLastBackSlash = i.rfind('\\') +1      #Tìm vị trí ký tự  sau dấu xẹt trái
    fileName.append(i[indexLastBackSlash:indexLastDot])        #Add Tên file vào List
print(fileName)

# for i in str:
#     if "." and "," in i:
#         num = i.split(".")
#         numfile.append(num[0])
# print(numfile)
