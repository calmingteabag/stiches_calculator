from PIL import Image

# load
image = Image.open('ganyu.jpg')
img_width, img_height = image.size

# resize
aspect = img_width / img_height
new_height = 100 / aspect
resized_image = image.resize((100, (int(new_height))))
new_img = resized_image.convert('L')
pixels = list(new_img.getdata())
ascii_str = ""

ASCII_CHARS = ["@", "#", "$", "%", "?", "*", "+", ";", ":", ",", "."]

for pixel in pixels:
    ascii_str += ASCII_CHARS[pixel // 25]

str_result = ""

for i in range(0, len(ascii_str), 100):
    # start:stop:step. didn't knew this
    str_result += ascii_str[i:i+100] + "\n"

with open("ascii_image.txt", "w") as txt:
    txt.write(str_result)
