from PIL import Image

abc = open("abc.txt", 'r')
abcdata = eval(abc.read())
print len(abcdata)
pixnum = 8986218
height = 569
width = 929
abcimg = Image.new('RGB', (int(width),int(height)))
abcimg.putdata(abcdata)
abcimg.save("abcimg.jpg")
