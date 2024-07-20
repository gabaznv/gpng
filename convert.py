import lzma
from PIL import Image, ImageTk
import numpy as np
import tkinter as tk
from tkinter import Label

MAX_WIDTH = 1280
MAX_HEIGHT = 720

class GpngImage:
    def __init__(self, width, height, data):
        self.width = width
        self.height = height
        self.data = data

    def save(self, filename, memory_efficient=False):
        with open(filename, 'wb') as f:
            # Write header
            f.write(self.width.to_bytes(4, 'big'))
            f.write(self.height.to_bytes(4, 'big'))
            # Compress and write data
            if memory_efficient:
                compressed_data = lzma.compress(self.data, preset=9)
            else:
                inflated_data = self.data * 10  # Inflate data to 10x the original size
                compressed_data = lzma.compress(inflated_data, preset=0)
            f.write(compressed_data)

    @staticmethod
    def load(filename):
        with open(filename, 'rb') as f:
            # Read header
            width = int.from_bytes(f.read(4), 'big')
            height = int.from_bytes(f.read(4), 'big')
            # Read and decompress data
            compressed_data = f.read()
            try:
                data = lzma.decompress(compressed_data)
            except lzma.LZMAError as e:
                print(f"Decompression error: {e}")
                raise
            if len(data) == width * height * 4 * 10:
                data = data[:width * height * 4]  # Reduce data back to original size
            return GpngImage(width, height, data)

    def to_image(self):
        array = np.frombuffer(self.data, dtype=np.uint8).reshape((self.height, self.width, 4))
        return Image.fromarray(array, 'RGBA')

    @staticmethod
    def from_image(image):
        array = np.array(image)
        data = array.tobytes()
        return GpngImage(image.width, image.height, data)


def png_to_gpng(png_filename, gpng_filename, memory_efficient=False):
    image = Image.open(png_filename).convert('RGBA')
    gpng_image = GpngImage.from_image(image)
    gpng_image.save(gpng_filename, memory_efficient)


def gpng_to_png(gpng_filename, png_filename):
    gpng_image = GpngImage.load(gpng_filename)
    image = gpng_image.to_image()
    image.save(png_filename)


def resize_image(image, max_width, max_height):
    width, height = image.size
    if width > max_width or height > max_height:
        ratio = min(max_width / width, max_height / height)
        new_size = (int(width * ratio), int(height * ratio))
        return image.resize(new_size, Image.LANCZOS)
    return image


def view_gpng_image(gpng_filename):
    gpng_image = GpngImage.load(gpng_filename)
    image = gpng_image.to_image()

    image = resize_image(image, MAX_WIDTH, MAX_HEIGHT)

    root = tk.Tk()
    root.title(gpng_filename)

    img = ImageTk.PhotoImage(image)
    label = Label(root, image=img)
    label.pack()

    root.mainloop()


if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser(description="Convert PNG to GPNG and vice versa.")
    parser.add_argument('input', help="Input file (PNG or GPNG)")
    parser.add_argument('output', nargs='?', help="Output file (GPNG or PNG)")
    parser.add_argument('memory_efficient', nargs='?', default='false', help="Boolean for memory efficient compression (default: false)")

    args = parser.parse_args()

    memory_efficient = args.memory_efficient.lower() == 'true'

    if args.input.lower().endswith('.png') and args.output and args.output.lower().endswith('.gpng'):
        png_to_gpng(args.input, args.output, memory_efficient)
    elif args.input.lower().endswith('.gpng') and args.output and args.output.lower().endswith('.png'):
        gpng_to_png(args.input, args.output)
    elif args.input.lower().endswith('.gpng') and not args.output:
        view_gpng_image(args.input)
    else:
        print("Invalid file extensions or arguments. Provide a .png file to convert to .gpng, a .gpng file to convert to .png, or a .gpng file to view the image.")