import os
import shutil
from PIL import Image, ImageMath

extensions = ("", ".png")

shortcuts = (("happy",      "dh"),
             ("sad",        "ds"),
             ("laughing",   "nl"),
             ("smug",       "sg"),
             ("bruh",       "sn"),
             ("thinking",   "8n"),
             ("dizzy",      "wr"),
             ("asleep",     "uh"),
             ("happycry",   "hw"),
             ("ooh",        "dt"))

eyes, mouths = [], []

for file in os.listdir("./eyes"):
    im = Image.open("./eyes/" + file)
    if im.width > 67:
        eyes.append(( im.crop((0 , 0, 1*67, 70)),
                      im.crop((67, 0, 2*67, 70)),
                      os.path.splitext(file)[0] ))
    else:
        eyes.append(( Image.merge("RGBA", (im.split()[1], im.split()[1],
                                           im.split()[1], im.split()[3])),
                      im,
                      os.path.splitext(file)[0]                          ))
    
for file in os.listdir("./mouths"):
    mouths.append(( Image.open("./mouths/" + file),
                    os.path.splitext(file)[0]     ))

for e in eyes:
    print(e[-1])
    for m in mouths:
        for x in (0, 1):
            out = Image.alpha_composite(e[x], m[0])
            for ext in extensions:
                out.save("../" + e[-1] + m[-1] + "x"*x + ext, "PNG", option="optimize")

print("shortcuts")
for s in shortcuts:
    for x in (0, 1):
        for ext in extensions:
            shutil.copy("../" + s[1] + "x"*x + ext,
                        "../" + s[0] + "x"*x + ext)

print("DONE")
