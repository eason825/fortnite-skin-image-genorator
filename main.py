import PIL
from PIL import Image
from io import BytesIO
import urllib.request

from PIL import Image, ImageDraw, ImageFont

import json
import requests
import io


strip_width, strip_height = 468, 650

def center_text(img, font, text, color=(255, 255, 255)):
    draw = ImageDraw.Draw(img)
    text_width, text_height = draw.textsize(text, font)
    position = ((strip_width-text_width)/2,(strip_height-text_height)/2)
    draw.text(position, text, color, font=font)
    return img


strip_widthh, strip_heightt = 468, 750

def center_desc(img, font, text, color=(255, 255, 255)):
    draw = ImageDraw.Draw(img)
    text_width, text_height = draw.textsize(text, font)
    position = ((strip_widthh-text_width)/2,(strip_heightt-text_height)/2)
    draw.text(position, text, color, font=font)
    return img

rq = requests.get("https://fortnite-api.com/v2/cosmetics/br")
data=rq.json()['data']

print("generating images... please wait")
for item in data:
  if "CID_" in item['id']:
    rarity = item['rarity']['value']
    background = Image.open(f"raritys/{rarity}.png")
    border = Image.open(f"raritys/border.png")
    url=f"https://fortnite-api.com/images/cosmetics/br/{item['id']}/icon.png"
    response = urllib.request.urlopen(url)
    foreground = Image.open(response)

    background.paste(foreground, (0, 0), foreground)
    background.paste(border, (0, 0), border)

    text = item['name']

    
    font = ImageFont.truetype("fortnite.otf", 50)
    center_text(background, font, text)

    description = item['description']
    
    font = ImageFont.truetype("fortnite.otf", 30)
    center_desc(background, font, description)

    background.save(f"skins/{item['id']}.png")
print("done! check your skins folder!")
