def process(img, data):
    pixels = image.load()
    num_channel = len(pixels[x, y])
    i = 0
    for x in range(image.size[0]):
        for y in range(image.size[1]):
            pixel = list(pixels[x, y])
            for c in range(num_channel):
                pixel[c] = (pixel[c] & ~1) | int(data[i])
                i += 1
                if i == len(data): 
                    pixels[x,y] = tuple(pixel)
                    return
                pixels[x,y] = tuple(pixel)
    return image
output = process(img, data)