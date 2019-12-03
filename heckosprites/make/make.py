import os
import shutil
from PIL import Image, ImageMath

extensions = ("", ".png")

shortcuts = (("happy",          "dh"),
             ("sad",            "ds"),
             ("laughing",       "nl"),
             ("smug",           "sg"),
             ("bruh",           "sn"),
             ("thinking",       "8n"),
             ("dizzy",          "wr"),
             ("asleep",         "zt"),
             ("crying",         "cs"),
             ("happycry",       "ch"),
             ("innocent",       "9k"),
             ("really",         "in"),
             ("winking",        "kg"),
             ("ooh",            "dt"),
             ("nervous",       "2ns"),
             ("flushed",       "ttb"),
             ("blushing",      "2hb"),
             ("happyblush",    "2ns"),
             ("nervouslaugh",  "nls"),
             ("blank",          "bb"),
                                     )

size = (67, 70)

eyes, mouths, overlays = [], [], []

base = Image.open("base.png")

for file in os.listdir("./eyes"):
    im = Image.open("./eyes/" + file)
    eyes.append(( Image.merge("RGBA", (im.split()[1], im.split()[1],    # 0ff -> fff, 00f -> 000
                                       im.split()[1], im.split()[3])),  # (black and white)
                  Image.merge("RGBA", (im.split()[0], im.split()[2],    # 0ff -> 0ff, 00f -> 0ff
                                       im.split()[2], im.split()[3])),  # (sans eye)
                  os.path.splitext(file)[0]                          ))
    
for file in os.listdir("./mouths"):
    mouths.append(( Image.open("./mouths/" + file),
                    os.path.splitext(file)[0]     ))

for file in os.listdir("./overlays"):
    overlays.append(( Image.open("./overlays/" + file),
                      os.path.splitext(file)[0]       ))

overlays.sort(key = lambda x: x[1]) # the docs for listdir said the order is arbitrary so juuust in case

def imgsuperset(images):
    if len(images) <= 1:
        return [(Image.new("RGBA", size), ""), images[0]]
    else:
        currentimg = images[-1]
        return list(imgsuperset(images[:-1])) + [(Image.alpha_composite(i[0], currentimg[0]), i[1] + currentimg[1]) for i in imgsuperset(images[:-1])]

overlaysmerged = imgsuperset(overlays)

for e in eyes:
    print(e[-1])
    for x in (0, 1):
        eyed = Image.alpha_composite(base, e[x])
        for m in mouths:
            mouthed = Image.alpha_composite(eyed, m[0])
            for o in overlaysmerged:
                out = Image.alpha_composite(mouthed, o[0])
                for ext in extensions:
                    out.save("../" + e[-1] + m[-1] + o[1] + "x"*x + ext, "PNG", option="optimize")

print("shortcuts")
for s in shortcuts:
    for x in (0, 1):
        for ext in extensions:
            shutil.copy("../" + s[1] + "x"*x + ext,
                        "../" + s[0] + "x"*x + ext)

print("oneoffs")
for file in os.listdir("./oneoffs"):
    for ext in extensions:
        shutil.copy("./oneoffs/" + file,
                    "../" + os.path.splitext(file)[0] + ext)

print("DONE")
