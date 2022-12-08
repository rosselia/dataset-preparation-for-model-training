import os
a=0
for i in range(1, 13268):
    
    path = "C:\\Users\\terzi\\OneDrive\\Masaüstü\\framing\\labels\\dt4_" + str(i) + ".txt"
    isExist = os.path.exists(path)
    if isExist==False:
        a=a+1
        print (str(i) + ". txt dosyası yok")


print(str(a)+" tane txt dosyası yok")

    