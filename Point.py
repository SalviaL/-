'''l0,b0：最小经纬度
   l1,b1：最大经纬度'''
l0, b0 = 113.1935119628906250, 29.7338104248046875
l1, b1 = 113.4880828857421875, 29.9631500244140625
file = open("F:\\图像\\批量下载索引.txt", 'wt')
countR = 0
while (b1 > b0):
    l = l0
    countC = 0
    while (l < l1):
        countC += 1
        line = "{}{}|{},{}|{},{}|19"
        file.writelines(
            line.format('%03d' % countR, '%03d' % countC, l, b1 - 0.02, l +
                        0.02, b1) + "\r\n")
        l += 0.019
    b1 -= 0.019
    countR += 1
print("索引生成完毕")
file.close()
