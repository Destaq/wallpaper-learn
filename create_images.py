import os
import sys
import csv
from PIL import Image, ImageFont, ImageDraw
import font_dictionary


def empty_directory():
    """clear directory of any previous images"""
    filelist = [f for f in os.listdir("images")]
    for f in filelist:
        os.remove(f"images/{f}")


def form_images(topic, subtopic, level=None):
    """populate image folder with wallpaper-appropiate images"""

    # create array to hold 'cards' for wallpaper
    data = []
    default_image = ""
    extension_ending = "jpg"
    # read vocabulary from csv
    # search for csv file in level
    try:
        # find default image for wallpaper
        listing = os.listdir(f"{topic}/{subtopic}")

        for i in range(len(listing)):
            if (
                'jpg' in listing[i]
                or 'png' in listing[i]
            ):  # is an image
                default_image = listing[i]
                extension_ending = listing[i][-3:]
                break

        try:
            default = Image.open(f"{topic}/{subtopic}/{default_image}")
            width, height = default.size  # get dimensions for centering text
        except:
            default = Image.open(f"{topic}/{default_image}")
            width, height = default.size  # get dimensions for centering text 

        try:
            with open(f"{topic}/{subtopic}/{level}/{level.lower()}.csv") as vocab:
                reader = csv.reader(vocab)
                for row in reader:
                    data.append(row)
        except:
            with open(f"{topic}/{subtopic}/{subtopic.lower()}.csv") as vocab:
                reader = csv.reader(vocab)
                for row in reader:
                    data.append(row)
    # if fail, search for in subtopic
    except:
        # find default image for wallpaper
        listing = os.listdir(f"{topic}")

        for i in range(len(listing)):

            if (
                'jpg' in listing[i]
                or 'png' in listing[i]
            ):  # is an image
                default_image = listing[i]
                extension_ending = listing[i][-3:]
                break


        try:
            with open(f"{topic}/{subtopic}/{level}/{level.lower()}.csv") as vocab:
                reader = csv.reader(vocab)
                for row in reader:
                    data.append(row)
        except:
            with open(f"{topic}/{subtopic}/{subtopic.lower()}.csv") as vocab:
                reader = csv.reader(vocab)
                for row in reader:
                    data.append(row)


    if subtopic in list(font_dictionary.fonts.keys()):
        values = ImageFont.truetype(
            font_dictionary.fonts[subtopic], 100
        )  # font used for main card

        small_definition = ImageFont.truetype(
            font_dictionary.fonts[subtopic], 60
        )  # font used for information about card

    elif topic in list(font_dictionary.fonts.keys()):
        values = ImageFont.truetype(
            font_dictionary.fonts[topic], 100
        )  # font used for main card

        small_definition = ImageFont.truetype(
            font_dictionary.fonts[topic], 60
        )  # font used for information about card

    else:
        values = ImageFont.truetype(
            font_dictionary.fonts["default"], 100
        )  # font used for main card

        small_definition = ImageFont.truetype(
            font_dictionary.fonts["default"], 60
        )  # font used for information about card

    for i in range(2, len(data)):
        # let user know the progress
        print(f"Writing image {i} of {len(data)-1} in this set.\r", end="")
        # create images for vocabulary
        try:
            default = Image.open(
                f"{topic}/{subtopic}/{default_image}"
            )  # reopen each time to prevent text from spilling over
        except:
            default = Image.open(f"{topic}/{default_image}")

        width, height = default.size  # get dimensions for centering text
        draw = ImageDraw.Draw(default)

        if len(data[1]) == 4:  # advanced CSV, key + key2 + value + category
            w, h = draw.textsize(
                f"{data[i][0]} - {data[i][1]}", font=values
            )  # find size of text if it would be drawn; used for centering

            # 'draw' text to sample image
            draw.text(
                ((width - w) / 2, ((height - h) / 2) - 100),
                f"{data[i][0]} - {data[i][1]}",
                (0, 0, 0),
                font=values,
            )  # characters + pinyin

            w, h = draw.textsize(f"{data[1][2]}: {data[i][2]}", font=small_definition)
            draw.text(
                ((width - w) / 2, ((height - h) / 2) + 50),
                f"{data[1][2]}: {data[i][2]}",
                (0, 0, 0),
                font=small_definition,
            )  # english definition

            w, other_h = draw.textsize(
                f"{data[1][3]}: {data[i][3]}", font=small_definition
            )
            draw.text(
                ((width - w) / 2, ((height - other_h) / 2) + 60 + h),
                f"{data[1][3]}: {data[i][3]}",
                (0, 0, 0),
                font=small_definition,
            )  # word category

        elif len(data[1]) == 3:  # intermediate CSV, key + value + category
            w, h = draw.textsize(
                data[i][0], font=values
            )  # find size of text if it would be drawn; used for centering

            # 'draw' text to sample image
            draw.text(
                ((width - w) / 2, ((height - h) / 2) - 100),
                data[i][0],
                (0, 0, 0),
                font=values,
            )  # characters + pinyin

            w, h = draw.textsize(f"{data[1][1]}: {data[i][1]}", font=small_definition)
            draw.text(
                ((width - w) / 2, ((height - h) / 2) + 50),
                f"{data[1][1]}: {data[i][1]}",
                (0, 0, 0),
                font=small_definition,
            )  # english definition

            w, other_h = draw.textsize(
                f"{data[1][2]}: {data[i][2]}", font=small_definition
            )
            draw.text(
                ((width - w) / 2, ((height - other_h) / 2) + 60 + h),
                f"{data[1][2]}: {data[i][2]}",
                (0, 0, 0),
                font=small_definition,
            )  # word category

        elif len(data[1]) == 2:  # simple CSV, key + value
            w, h = draw.textsize(
                data[i][0], font=values
            )  # find size of text if it would be drawn; used for centering

            # 'draw' text to sample image
            draw.text(
                ((width - w) / 2, ((height - h) / 2) - 100),
                data[i][0],
                (0, 0, 0),
                font=values,
            )  # characters + pinyin

            w, h = draw.textsize(f"{data[1][1]}: {data[i][1]}", font=small_definition)
            draw.text(
                ((width - w) / 2, ((height - h) / 2) + 50),
                f"{data[1][1]}: {data[i][1]}",
                (0, 0, 0),
                font=small_definition,
            )  # definition

        # save image to disk; based on topic + subtopic + option level
        if level is not None:
            default.save(
                f"images/{topic}-{subtopic}-{level}-{i-1}.{extension_ending}"
            )  # TODO: correct filetype (for non .png/.jpg)
        else:
            default.save(f"images/{topic}-{subtopic}-{i-1}.{extension_ending}")
