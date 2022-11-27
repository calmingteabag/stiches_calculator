from PIL import Image
import os.path
from os import path
import random


class AsciiGenerator:
    def __init__(self, filepath, targetWidth, convertParam, outputFile):
        self.filepath = filepath
        self.targetWidth = targetWidth
        self.convertParam = convertParam
        self.outputFile = outputFile
        self.image = Image.open(self.filepath)

    def resize(self):
        width, height = self.image.size
        aspect = width / height

        resized_image = self.image.resize(
            (self.targetWidth, int(self.targetWidth / aspect)))

        return resized_image

    def converter(self):
        img = self.resize()
        new_img = img.convert(self.convertParam)
        return new_img

    def generate_filename(self, prefix):
        num_suffix = '0' * 5
        """ 
        What I want to do is set every filename with
        prefix_00000.txt up to self.filerange

        the '00000' part depens on the number range 
        set in self.filerange. If its set to 10000, filenames
        goes up to 10000 names, so the '00000' part should have 
        four 'zeroes' (range 0 to 10000)

        So I need a way to return the number of zeroes a
        certain range has. Example: 20000 has 5 zeroes (0 up to 19999),
        10000 has 4 zeroes(0 up to 10000), 100000 has 5 zeroes(0 to 99999),
        etc.
        """

        filename = prefix + '_' + str(num_suffix) + '.txt'

        return filename

    def process(self):
        ascii_chars = ["@", "#", "$", "%", "?", "*", "+", ";", ":", ",", "."]
        ascii_str = ""
        str_result = ""

        pixels = list(self.converter().getdata())

        for pixel in pixels:
            ascii_str += ascii_chars[pixel//25]

        for i in range(0, len(ascii_str), self.targetWidth):
            str_result += ascii_str[i:i+self.targetWidth] + "\n"

        # output = self.gen_random_filename('ascii')
        with open(self.outputFile, "w") as txt:
            txt.write(str_result)


b = AsciiGenerator('ganyu.jpg', 150, 'L', 'ascii_image.txt')
b.process()
print(os.listdir())

x = os.listdir()
if 'ganyu.jpg' in x:
    print('exists')

a = 0
b = 1

for i in range(0, 10):
    print(a)
    a = b
    b = a + b
