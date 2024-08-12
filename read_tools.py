# This is only meant to check if stego_tools.py is working correctly, there's no guarantee it will crack other steganography image
def binary_to_string(b): return ''.join(chr(int(b[i:i+8], 2)) for i in range(0, len(b), 8))
def load_image(image): return image.size[0], image.size[1], image.load()
def LSB(image, data, output_path):
    width, height, pixels = load_image(image)
    data = string_to_binary(data) + '00000000'
    if width * height * 3 < len(data): raise ValueError("Data is too long to fit in the image. Please use a shorter string or a larger image.")
    i = 0
    for x in range(width):
        for y in range(height):
            if i == len(data):
                image.save(output_path)
                return
            r, g, b = pixels[x, y]

            r = (r & ~1) | int(data[i])
            i += 1
            if i == len(data):
                pixels[x, y] = (r, g, b)
                image.save(output_path)
                return
            
            g = (g & ~1) | int(data[i])
            i += 1
            if i == len(data):
                pixels[x, y] = (r, g, b)
                image.save(output_path)
                return
            
            b = (b & ~1) | int(data[i])
            i += 1
            pixels[x, y] = (r, g, b)
            
    image.save(output_path)