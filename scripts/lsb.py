# It's recommended to put your process code inside a function so you can control it better
def process(image, data):
    # It's recommended to load your data into variable if possible 
    # instead of passing it in arg to minimize error surface
    pixels = image.load()
    num_channel = len(pixels[0, 0])
    i = 0
    for x in range(image.size[0]):
        for y in range(image.size[1]):
            pixel = list(pixels[x, y])
            for c in range(num_channel):
                pixel[c] = (pixel[c] & ~1) | int(data[i]) # How does this modify the LSB? Dunno :)
                i += 1
                if i == len(data): 
                    pixels[x,y] = tuple(pixel)
                    return image # exit() is not an option because it throw away variable value from memory
                pixels[x,y] = tuple(pixel)
    return image
# output are the variable the api will read from.
output = process(image, data)
