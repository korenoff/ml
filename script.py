import os
import json
from PIL import Image

with open('markup.json') as f:
    templates = json.load(f)

i = 0

try:
    os.mkdir(f"meyy")
    dataset_new = {}
except FileExistsError:
    dataset_new = {}

print(f"Image: {len(list(templates.keys()))}")
for image in templates:
    x1 = templates[image]["regions"][list(templates[image]["regions"].keys())[0]]["shape_attributes"]["all_points_x"][0]
    x2 = templates[image]["regions"][list(templates[image]["regions"].keys())[0]]["shape_attributes"]["all_points_x"][2]
    y1 = templates[image]["regions"][list(templates[image]["regions"].keys())[0]]["shape_attributes"]["all_points_y"][0]
    y2 = templates[image]["regions"][list(templates[image]["regions"].keys())[0]]["shape_attributes"]["all_points_y"][2]
    im = Image.open(image)
    area = (x1, y1, x2, y2)
    #print(image)
    try:
        label = list(templates[image]["regions"].keys())[0]
        try:
            os.mkdir(f"meyy/{label}")
            im.crop(area).save(f"meyy/{label}/im{i}.png")
            dataset_new[f"im{i}.png"] = {}
            dataset_new[f"im{i}.png"] = {"sign": label}
        except FileExistsError:
            im.crop(area).save(f"meyy/{label}/im{i}.png")
            dataset_new[f"im{i}.png"] = {}
            dataset_new[f"im{i}.png"] = {"sign" : label}
    except SystemError:
        continue
    i += 1

print(f"Correct image : {i}")

data = json.dumps(dataset_new)

with open("meyy/data.json", "w") as f:
    f.writelines(data)

