from PIL import Image, ImageDraw

newImg = Image.new('RGBA', (300,300), "#f0fff0")
drawObj = ImageDraw.Draw(newImg)
for i in range(100,200,5):
    for j in range(100,200,5):
        drawObj.point([j,i], fill="Black")
drawObj.line([(1,1),(1,298),(298,298),(298,1),(1,1)], fill='Black')
drawObj.line([(4,4),(4,295),(295,295),(295,4),(4,4)], fill='Black')
drawObj.line([(7,7),(7,292),(292,292),(292,7),(7,7)], fill='Black')

for x in range(150, 300, 10):
    drawObj.line([(x,0),(300,x-150)], fill="Black")
    drawObj.line([(x,300),(300,450-x)], fill="Black")
for y in range(0, 150, 10):
    drawObj.line([(y,300),(150-y,0)], fill="Black")
    drawObj.line([(0,y),(0,150+y)], fill="Black")


newImg.save("test.png")