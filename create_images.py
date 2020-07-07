import os
import csv
from PIL import Image, ImageFont, ImageDraw
import font_dictionary # different fonts for different types of csv files, to support various languages and give it a nice feel


def empty_directory():
    """clear directory of any previous images or create directory"""
    try:
        filelist = [f for f in os.listdir("images")]
        for f in filelist:
            os.remove(f"images/{f}")
    except:
        os.mkdir('images')


def form_images(topic, subtopic, level=None):
    """populate image folder with wallpaper-appropiate images"""

    # create array to hold 'cards' for wallpaper
    data = []
    default_image = ""
    extension_ending = "jpg"

    # read vocabulary from csv
    # search for csv file in level
    try:
        # find default image for wallpaper background
        listing = os.listdir(f"content/{topic}/{subtopic}")

        for i in range(len(listing)):
            if (
                'jpg' in listing[i]
                or 'png' in listing[i]
            ):  # is an image
                default_image = listing[i]
                extension_ending = listing[i][-3:]
                break

        # search for it in topic and subtopic
        try:
            default = Image.open(f"content/{topic}/{subtopic}/{default_image}")
            width, height = default.size  # get dimensions for centering text
        except:
            default = Image.open(f"content/{topic}/{default_image}")
            width, height = default.size  # get dimensions for centering text 

        # search for csv in topic and subtopic folders
        try:
            with open(f"content/{topic}/{subtopic}/{level}/{level.lower()}.csv") as vocab:
                reader = csv.reader(vocab)
                for row in reader:
                    data.append(row)
        except:
            with open(f"content/{topic}/{subtopic}/{subtopic.lower()}.csv") as vocab:
                reader = csv.reader(vocab)
                for row in reader:
                    data.append(row)

    # if fail, search for default image in subtopic
    except:
        # find default image for wallpaper
        listing = os.listdir(f"content/{topic}")

        for i in range(len(listing)):

            if (
                'jpg' in listing[i]
                or 'png' in listing[i]
            ):  # is an image
                default_image = listing[i]
                extension_ending = listing[i][-3:]
                break


        # if successful, search for default iamge as well
        try:
            with open(f"content/{topic}/{subtopic}/{level}/{level.lower()}.csv") as vocab:
                reader = csv.reader(vocab)
                for row in reader:
                    data.append(row)
        except:
            with open(f"content/{topic}/{subtopic}/{subtopic.lower()}.csv") as vocab:
                reader = csv.reader(vocab)
                for row in reader:
                    data.append(row)


    # search for the font, may be associated with either the subtopic or the topic
    if subtopic in list(font_dictionary.fonts.keys()):
        values = ImageFont.truetype(
            font_dictionary.fonts[subtopic], 100
        )  # font used for main card, (e.g. foreign language, event, etc.)

        small_definition = ImageFont.truetype(
            font_dictionary.fonts[subtopic], 60
        )  # font used for information about card at the bottom

    elif topic in list(font_dictionary.fonts.keys()):
        values = ImageFont.truetype(
            font_dictionary.fonts[topic], 100
        )  # font used for main card

        small_definition = ImageFont.truetype(
            font_dictionary.fonts[topic], 60
        )  # font used for information about card

    # if it cannot be found, use the default font
    else:
        values = ImageFont.truetype(
            font_dictionary.fonts["default"], 100
        )  # font used for main card

        small_definition = ImageFont.truetype(
            font_dictionary.fonts["default"], 60
        )  # font used for information about card

    # start at two to ignore first two rows in csv
    for i in range(2, len(data)):
        # let user know the progress
        print(f"Writing image {i} of {len(data)-1} in this set.\r", end="")
        # create images for vocabulary
        try:
            default = Image.open(
                f"content/{topic}/{subtopic}/{default_image}"
            )  # reopen each time to prevent text from spilling over
        except:
            default = Image.open(f"content/{topic}/{default_image}")

        width, height = default.size  # get dimensions for centering text
        draw = ImageDraw.Draw(default)


        # writing the image when used for advanced CSV with 4 columns | key + key2 + value + category
        if len(data[1]) == 4:
            w, h = draw.textsize(
                f"{data[i][0]} - {data[i][1]}", font=values
            )  # find size of text if it would be drawn; used for centering

            # 'draw' text to sample image
            draw.text(
                ((width - w) / 2, ((height - h) / 2) - 100),
                f"{data[i][0]} - {data[i][1]}",
                (0, 0, 0),
                font=values,
            )  # the question, what is in the larger font at the top

            # center it
            w, h = draw.textsize(f"{data[1][2]}: {data[i][2]}", font=small_definition)
            draw.text(
                ((width - w) / 2, ((height - h) / 2) + 50),
                f"{data[1][2]}: {data[i][2]}",
                (0, 0, 0),
                font=small_definition,
            )  # the definition, such as categories or translation

            w, other_h = draw.textsize(
                f"{data[1][3]}: {data[i][3]}", font=small_definition
            )
            draw.text(
                ((width - w) / 2, ((height - other_h) / 2) + 60 + h),
                f"{data[1][3]}: {data[i][3]}",
                (0, 0, 0),
                font=small_definition,
            )  # word category


        # used for intermediate level CSVs with a key + value + category
        elif len(data[1]) == 3:
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


        # used for simple CSVs with just a key + value pair
        elif len(data[1]) == 2:
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
        if level is not None: # try to save based on level
            default.save(
                f"images/{topic}-{subtopic}-{level}-{i-1}.{extension_ending}"
            )  # TODO: correct filetype (for non .png/.jpg)
        else: # level not applicable
            default.save(f"images/{topic}-{subtopic}-{i-1}.{extension_ending}")
