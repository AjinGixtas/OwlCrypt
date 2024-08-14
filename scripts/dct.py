from math import cos, pi
def process(image, data):
    def a(uv): return (1 / (8 if uv == 0 else 4)) ** .5
    l_image = image.convert('L')
    pixels = l_image.load()
    C = [[0 for _ in range(image.size[0])] for _ in range(image.size[1])]
    
    for X in range(0, image.size[0], 8):
        for Y in range(0, image.size[1], 8):
            for x in range(8):
                for y in range(8):
                    C[X+x][Y+y] = 0.25 * a(x) * a(y) * sum(pixels[X+i, Y+j] * cos((2*i + 1) * x * pi / 16) * cos((2*j + 1) * y * pi / 16) for i in range(8) for j in range(8))
    
    return image
output = process(image, data)