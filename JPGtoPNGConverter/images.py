from PIL import Image, ImageFilter

img = Image.open('./Pokedex/pikachu.jpg')
# filtered_img = img.convert('L')
# box = (100,100,400,400)
# resize = filtered_img.crop(box)
# resize.save("grey.png", 'png')

img.thumbnail((1500,1500))
img.save('thumbnail.jpg')

print(img.size)