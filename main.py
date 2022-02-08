import PIL
from io import BytesIO
import urllib.request
from PIL import Image, ImageDraw, ImageFont
import json
import requests

rq = requests.get("https://fortnite-api.com/v2/cosmetics/br")
data=rq.json()['data']


print("Generating Images... This May Take A While!")
for item in data:
  if "CID_" in item['id']:
    rarity = item['rarity']['value']
    background = Image.open(f"raritys/{rarity}.png")

    url=f"https://fortnite-api.com/images/cosmetics/br/{item['id']}/icon.png"
    response = urllib.request.urlopen(url)
    skinimg = Image.open(response)

    background.paste(skinimg, (0, 0), skinimg)
    background.save(f"skins/{item['id']}.png")
print("Done Generating Images!")
