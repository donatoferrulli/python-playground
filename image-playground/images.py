from PIL import Image, ImageFilter

img = Image.open('./Pokedex/pikachu.jpg')
filtered_image = img.filter(ImageFilter.BLUR)
filtered_image.save('blur.png', 'png')

converted_image = img.convert('L')
converted_image.save('grey.png', 'png')


rotated_image = img.rotate(90)
rotated_image.save('rotated.png', 'png')

resized_image = img.resize((300,300))
resized_image.save('resized.png', 'png')

box = (100,100,400,400)
cropped_image = img.crop(box)
cropped_image.save('cropped.png', 'png')

