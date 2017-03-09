import PIL
from PIL import Image


def crop_image(input_file, output_file, width=320, height=240):
    img = Image.open(input_file)
    wpercent = (width / float(img.size[0]))
    hsize = int((float(img.size[1]) * float(wpercent)))
    img = img.resize((width, hsize), PIL.Image.ANTIALIAS).crop((0,0,width,height))
    img.save(output_file)

