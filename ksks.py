from PIL import Image

ksks = Image.open('ksks.jpg')
kspix = ksks.load()
width, height = ksks.size
flag = ''
txt = ''
for i in range(0, height):
    for j in range (0, width):
        flag += str(kspix[j,i][0]%2) + str(kspix[j,i][1]%2) + str(kspix[j,i][2]%2)

zipped = zip(*[iter(flag)]*8)
#print zipped
for t in zipped:
    txt += chr(int(''.join(t), 2))
print txt
