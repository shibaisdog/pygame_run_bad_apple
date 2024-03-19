import cv2
from PIL import Image
ONLOAD = []
ASCII_CHARS = ['0','0','0','1','1','1','1','1','1','1','1']
ASCII_CHARS.reverse()
ASCII_CHARS = ASCII_CHARS[::-1]
WIDTH = 105
path = "./source/video.mp4"
vidObj = cv2.VideoCapture(path)
def resize(image, new_width=WIDTH):
    (old_width, old_height) = image.size
    aspect_ratio = float(old_height)/float(old_width)
    new_height = int((aspect_ratio * new_width))
    new_dim = (new_width, new_height)
    new_image = image.resize(new_dim)
    return new_image
def grayscalify(image):
    return image.convert('L')
def modify(image, buckets=25):
    initial_pixels = list(image.getdata())
    new_pixels = [ASCII_CHARS[pixel_value//buckets] for pixel_value in initial_pixels]
    return ''.join(new_pixels)
def do(image, new_width=WIDTH):
    image = resize(image)
    image = grayscalify(image)
    pixels = modify(image)
    len_pixels = len(pixels)
    new_image = [pixels[index:index+int(new_width)] for index in range(0, len_pixels, int(new_width))]
    return new_image
    #return '\n'.join(new_image)
def load(file:int):
    image = None
    try:
        success,image = vidObj.read()
        image = cv2.cvtColor(image,cv2.COLOR_RGB2BGR)
        image = Image.fromarray(image)
    except Exception:
        return [False]
    return [success,(do(image))]
def onload():
    i = 0
    while True:
        out = load(i)
        if out[0] == False:
            break
        else:
            ONLOAD.append(out[1])
        i += 1
    print("ONLOAD!")
def call(i:int):
    return ONLOAD[i]