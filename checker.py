from PIL import Image
image0, image1 = Image.open('misc/4.1.01.tiff'), Image.open('misc/4.1.01-modified.tiff')
pixels0, pixels1 = image0.load(), image1.load()
total_pixel_modified = 0
for x in range(image0.size[0]):
    for y in range(image1.size[1]):
        if pixels0[x,y] != pixels1[x,y]:
            print(x,y)
            total_pixel_modified+=1
print(total_pixel_modified)