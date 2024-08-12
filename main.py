import stego_tools
import read_tools
from argparse import ArgumentParser
from PIL import Image
from os.path import splitext, basename, dirname, isfile


STEGANOGRAPHY_MODE = ['lsb']

parser = ArgumentParser(description="A description of your program.")
parser.add_argument('-i', '--input-path', type=str, help='Input file path')
parser.add_argument('-o', '--output-path', type=str, help='Output file path')
parser.add_argument('-d', '--data', type=str, help='Output file path')
parser.add_argument('-w', '--warning', action='store_true', help='Disable warning')
parser.add_argument('-b', '--binary', action='store_true', help='Data is in binary format')
parser.add_argument('-m', '--mode', type=str, default=STEGANOGRAPHY_MODE[0], choices=STEGANOGRAPHY_MODE, help='Mode of operation. Choose from: ' + ', '.join(STEGANOGRAPHY_MODE))
parser.add_argument('-px', '--pos-x', type=int, default=0, help='Starting value for x when looping. Default value is 0. Value range is [0, width)')
parser.add_argument('-py', '--pos-y', type=int, default=0, help='Starting value for y when looping. Default value is 0. Value range is [0, height)')
args = parser.parse_args()

if not isfile(args.input_path): exit_program('File does not exist', 64)
image = Image.open(args.input_path)
if image.format not in ('JPEG', 'PNG', 'BMP', 'GIF', 'TIFF'): exit_program('Invalid file format, make sure they are JPEG, PNG, BMP, GIF or TIFF', 64)
print(image.mode)
image = image.convert('RGBA')

if not 0 <= args.pos_x < image.size[0]: exit_program('x must in range [0, width)', 64)
if not 0 <= args.pos_y < image.size[1]: exit_program('y must in range [0, height)', 64)
if not args.binary: args.data = ''.join(format(ord(c), '08b') for c in args.data)
if image.size[0] * image.size[1] * 4 < len(args.data): exit_program('Data is too big to fit in the image. Make the image bigger or reduce the data size', 64)

if args.output_path == None:
    file_path = dirname(args.input_path)
    filename, file_extension = splitext(basename(args.input_path))
    args.output_path = file_path + '/' + filename + '-modified' + file_extension
    if not args.warning: print(f"--output-path is empty; it is now set to {args.output_path}")
print("\nArguments and their values:")
for arg in vars(args):
    print(f"{arg}: {getattr(args, arg)}")

if args.mode == 'lsb': stego_tools.LSB(image, args.data, image.size[0], image.size[1], image.load(), args.pos_x, args.pos_y, image.mode == 'rgb')
image.save(args.output_path)
def exit_program(msg='Embeded data successfully!', exit_code=0):
    print(msg)
    exit(exit_code)