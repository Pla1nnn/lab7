def prog1():
    from PIL import Image
    a = "one.jpg"
    with Image.open(a) as img:
        img.load()
    img.show()
    width, height = img.size
    form = img.format
    mode = img.mode
    print("Ширина - ", width)
    print("Высота -", height)
    print("Формат-", form)
    print("Цветовая модель-",mode)
def prog2():
    from PIL import Image
    a = "one.jpg"
    with Image.open(a) as img:
        img.load()
    new = img.resize((img.width // 3, img.height // 3))
    new.save("newone.jpg")
    b = img.transpose(Image.FLIP_TOP_BOTTOM)
    b.save("saveone.jpg")
    b = img.transpose(Image.FLIP_LEFT_RIGHT)
    b.save("saveone_one.jpg")

def prog3():
    from PIL import Image, ImageFilter
    name = ["one.jpg","two.jpg","three.jpg","four.jpg","five.jpg",]
    for file in name:
        with Image.open(file) as img:
            img.load()
            new = img.filter(ImageFilter.CONTOUR)
            new.show()
def prog4():
    from PIL import Image, ImageDraw
    img = Image.open('one.jpg')
    width,height = img.size
    draw = ImageDraw.Draw(img)
    text= "text v pravom nijnei chasti"
    textwidth, textheight = draw.textsize(text)
    margin = 10
    x = width - textwidth - margin
    y = height -  textheight - margin
    draw.text((x,y),text)
    img.show()



prog4()