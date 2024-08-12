def LSB(image, data, width, height, pixels, x, y, is_rgb):
    if width * height * 3 < len(data): raise ValueError("Data is too long to fit in the image. Please use a shorter string or a larger image.")
    i = 0
    for x in range(width):
        for y in range(height):
            if i == len(data): return
            r, g, b, a = pixels[x, y]
            
            r, i = (r & ~1) | int(data[i]), i + 1
            if i == len(data):
                pixels[x, y] = (r, g, b, a)
                return
            
            g, i = (g & ~1) | int(data[i]), i + 1
            if i == len(data):
                pixels[x, y] = (r, g, b, a)
                return
            
            b, i = (b & ~1) | int(data[i]), i + 1
            if i == len(data):
                pixels[x, y] = (r, g, b, a)
                return
            
            a, i = (a & ~1) | int(data[i]), i + 1
            pixels[x, y] = (r, g, b, a)
            
def DCT(image):
    pass
