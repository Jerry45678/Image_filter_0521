from PIL import Image
from PIL import ImageFilter


img1 = Image.open("images.jpg")
img2 = img1.filter(ImageFilter.SHARPEN)
img3 = img2.filter(ImageFilter.DETAIL)
img4 = img3.filter(ImageFilter.DETAIL)
img5 = img4.filter(ImageFilter.EDGE_ENHANCE)

img5.save("out01.jpg")