import os
from PIL import Image

for dir in os.listdir("../resources/images/"):
    if os.path.isfile(dir):
        continue
    for i, img in enumerate(os.listdir(dir)):

        if os.path.splitext(img)[0].isdigit():
            continue
        img_file = Image.open(os.path.join(dir, img))
        name, ext = os.path.splitext(img)
        img_file.save(os.path.join(dir, str(i) + ".png"), format="PNG")
        os.remove(os.path.join(dir, img))