from PIL import Image
x = 186
y = 138
flag = []
def searchflag(size, offset, cx, cy, point, flag):
    if size == 0:
        return flag
    cx = point[1] + offset
    cy = point[2] + offset
    flag.append(chr(point[0]))
    size -=1
    point = spipix[cx,cy]
    print (cx, cy, flag)
    searchflag(size, offset, cx, cy, point, flag)

spidey = Image.open('spidey.png')
spipix = spidey.load()
tam = spidey.size
for i in range(0, tam[0]):
    for j in range(0, tam[1]):
        if spipix[i,j][0] == 51:
            if i-x == j-y and j-y < tam[1]-255:
                offset = j-y
                print (offset)
                last = searchflag(23, offset, i + offset, j + offset, spipix[i,j], flag)
print (last)

