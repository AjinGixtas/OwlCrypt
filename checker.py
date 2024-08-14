from PIL import Image
image0, image1 = Image.open('misc/4.1.01.tiff'), Image.open('misc/4.1.01-modified.tiff')
pixels0, pixels1 = image0.load(), image1.load()
string = ''
for x in range(image0.size[0]):
    for y in range(image0.size[1]):
        for c in range(3):
            string += str(pixels1[x,y][c] & 1)
print(string)
