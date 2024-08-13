import stego_tools
import read_tools
from argparse import ArgumentParser
from PIL import Image
from os.path import splitext, basename, dirname, isfile

def exit_program(msg='Embeded data successfully!', exit_code=0):
    print(msg)
    exit(exit_code)
STEGANOGRAPHY_MODE = ('lsb', 'dct')

parser = ArgumentParser(description="A description of your program.")
general_group = parser.add_argument_group('General options')
lsb_group = parser.add_argument_group('LSB exclusive options')

general_group.add_argument('-i', '--input-path', type=str, required=True, help='Input file path (e.g., image file)')
general_group.add_argument('-o', '--output-path', type=str, required=False, help='Output file path (e.g., image file)')
general_group.add_argument('-d', '--data', type=str, required=True, help='Data to embed in the image')
general_group.add_argument('-w', '--warning', action='store_true', help='Disable warning messages')
general_group.add_argument('-B', '--binary', action='store_true', help='Specify if the data is in binary format')
general_group.add_argument('-m', '--mode', type=str, default=STEGANOGRAPHY_MODE[0], choices=STEGANOGRAPHY_MODE, help='Mode of operation. Choose from: ' + ', '.join(STEGANOGRAPHY_MODE))
general_group.add_argument('-s', '--script', type=str, default='', help='Script can be used to define custom behavior for hiding data. In all honesty, if you can use this stupid API, love yourself and build your own steganography app :/')


args = parser.parse_args()

if not isfile(args.input_path): exit_program('File does not exist', 64)
image = Image.open(args.input_path)
if image.format not in ('JPEG', 'PNG', 'BMP', 'GIF', 'TIFF'): 
    exit_program('Invalid file format, make sure they are JPEG, PNG, BMP, GIF or TIFF', 64)
if image.size[0] * image.size[1] * (1 if image.mode == '1' or image.mode == 'L' else 3 if image.mode == 'RGB' or image.mode == 'YCbCr' else 4 if image.mode == 'RGBA' or image.mode == 'CMYK' else 0) < len(args.data) and not args.warning: 
    print('Data is too big to fit in the image. Make the image bigger or reduce the data size. Overflowed data will be cropped', 64)

if not args.binary: args.data = ''.join(format(ord(c), '08b') for c in args.data)
if args.output_path == None:
    file_path = dirname(args.input_path)
    filename, file_extension = splitext(basename(args.input_path))
    args.output_path = file_path + '/' + filename + '-modified' + file_extension
    if not args.warning: print(f"--output-path is empty; it is now set to {args.output_path}")

#print("\nArguments and their values:")
#for arg in vars(args):
#    print(f"{arg}: {getattr(args, arg)}")

image = stego_tools.execute(image, args.data, open(f'scripts/{args.script}', 'r').read())
print(f'Saved image to {args.output_path}')
image.save(args.output_path)
