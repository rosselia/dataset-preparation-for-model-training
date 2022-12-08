import os

total_area = 0
num = 12899
max_area = 0
min_area = 16190.0
for i in range(1, num+1):

    path = "./labels/dt4_" + str(i) + ".txt"

    isExist = os.path.exists(path)
    if isExist == False:
        continue

    file_path = open("./labels/dt4_" + str(i) + ".txt", "r")
    data = file_path.read()
    file_path.close()

    width = float(data[22:24] + "." + data[24])
    height = float(data[31:33] + "." + data[33])

    area = ((1920*width)/100)*((1080*height)/100)
    rounded = '{:.2f}'.format(area)

    total_area = total_area + area
    
    if area > max_area:
        max_area = area

    if area < min_area:
        min_area = area


average_area = '{:.2f}'.format(total_area / num)
max_area = '{:.2f}'.format(max_area)
min_area = '{:.2f}'.format(min_area)


print("-----------------------------------")
print("avg area is: " + str(average_area))
print("-----------------------------------")
print("max area is: " + str(max_area))
print("-----------------------------------")
print("min area is: " + str(min_area))
print("-----------------------------------")
