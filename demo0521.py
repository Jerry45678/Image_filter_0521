from PIL import Image
from PIL import ImageFilter

img1 = Image.open("Patrick-Star.jpg")
img01 = Image.open("Forest.jpg")

img2 = img1.filter(ImageFilter.BLUR)
img2.save("out1.jpg")

img3 = img1.filter(ImageFilter.CONTOUR)
img3.save("out2.jpg")

img4 = img1.filter(ImageFilter.DETAIL)
img4.save("out3.jpg")

img5 = img2.filter(ImageFilter.EDGE_ENHANCE_MORE)
img5.save("out4.jpg")

img6 = img1.filter(ImageFilter.EMBOSS)
img6.save("out5.jpg")

img7 = img1.filter(ImageFilter.FIND_EDGES)
img7.save("out6.jpg")

img8 = img1.filter(ImageFilter.SMOOTH)
img8.save("out7.jpg")

img9 = img1.filter(ImageFilter.SHARPEN)
img9.save("out8.jpg")