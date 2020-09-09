from PIL import Image, ImageDraw, ImageFont

def textImage(text, name):
    image_width = 1024
    image_height = 1024
    img = Image.new('RGB', (image_width, image_height), color=(0, 0, 0))
    # create the canvas
    canvas = ImageDraw.Draw(img)
    font = ImageFont.truetype('/Users/noah/Library/Fonts/Aleo-Light.ttf', size=48)
    text_width, text_height = canvas.textsize(text, font=font)
    print(f"Text width: {text_width}")
    print(f"Text height: {text_height}")
    x_pos = int((image_width - text_width) / 2)
    y_pos = int((image_height - text_height) / 2)
    canvas.text((x_pos, y_pos), text, font=font, fill='#FFFFFF')
    img.save('/Users/noah/Keynotes/countdown/image.png',optimize=True,quality=100)
    img.close()
    print('Closed image')
    bgImg = Image.open('/Users/noah/Keynotes/countdown/image.png')
    circleLogo = Image.open('/Users/noah/Keynotes/logo-text.png')
    
    bgImg.paste(circleLogo, (770,770), circleLogo)
    print('Pasted image')
    bgImg.save(f'/Users/noah/Keynotes/countdown/{name}.png',optimize=True,quality=100)
    print('Saved finalimage')


countdowns = ['One week until the Apple Event', 'Six days until the Apple Event', 'Five days until the Apple Event', 'Four days until the Apple Event', 'Three days until the Apple Event', 'Two days until the Apple Event', '24 hours until the Apple Event']

filename = 1

for entry in countdowns:
    textImage(text=entry, name=filename)
    filename = filename + 1