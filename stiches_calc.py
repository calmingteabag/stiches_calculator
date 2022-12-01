import webcolors
from PIL import Image


class StichesCalculator:
    def __init__(self, filepath, targetWidth, convertParam, outputFile):
        """
        filepath: Image to convert
        targetWidth: Size of canvas (etamine,etc)
        convertParam: rgb or cmyk
        """
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
        """
        There are several convert arguments for Pillow
        """

        img = self.resize()
        # new_img = img.convert(self.convertParam)
        new_img = img.convert(
            self.convertParam, palette=Image.WEB, colors=8)

        return new_img

    def test_data(self):
        img_data = list(self.converter().getdata())
        self.image.save('nuuuu.jpg')
        return img_data

    def get_data(self):
        """
        Returns a dictionary of a pixel frequency in a image.
        (255,255,255) : 1
        (255, 0, 0) : 2
        """
        img_data = list(self.converter().getdata())
        # print(img_data)
        """
        The idea is, read through img_data and return how many
        different colors exists in a image based on a set parameter.

        img_data reuurns pixel data as tuples of three values representing
        the rgb color (can be changed to CMYK which will return four).

        For that, the rough idea is iterate over those tuples and return
        the nearest color. For example, a certain pixel reads as
        (245, 250, 248) which is close to pure white (255,255,255) so
        the program should approximate those values to white somehow.

        After that it should seek (255,255,255) on some kind of dictionary
        color and return its name 'white'.

        I've tried setting the dictionary key as an interval of values, for
        example (240 < red < 255, 240 < green < 255, 240 < blue< 255) : 'white'
        but it didn't work because dicts only accepts fixed keys and not
        intervals.

        """
        color_dict = {}

        for pixel in img_data:
            # basically returning pixel frequency

            if (pixel[0], pixel[1], pixel[2]) not in color_dict:
                color_dict[(pixel[0], pixel[1], pixel[2])] = 1
            else:
                color_dict[(pixel[0], pixel[1], pixel[2])] += 1

        return color_dict

    def write_file(self):
        with open(self.outputFile, "w") as txt:

            for key in self.get_data():
                txt.write(str(key) + ' : ' + str(self.get_data()[key]))
                print(key, )

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


b = StichesCalculator('images/ganyu.jpg', 5, 'RGB', 'ascii_image.txt')
# b.process()
print(b.get_data())
# print(b.test_data())
# b.write_file()

# a = StichesCalculator('images/ganyu.jpg', 5, 'P', 'ascii_image.txt')
# print(a.test_data())
