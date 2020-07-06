import os
import csv
from PIL import Image, ImageFont, ImageDraw


def empty_directory():
    """clear directory of any previous images"""
    filelist = [f for f in os.listdir("images")]
    for f in filelist:
        os.remove(f'images/{f}')


def form_images(topic, subtopic, level=None):
    """populate image folder with wallpaper-appropiate images"""
    empty_directory()

    # find default image for wallpaper
    listing = os.listdir(f"{topic}/{subtopic}")
    default_image = ""
    extension_ending = ".jpg"

    for i in range(len(listing)):
        if (
            listing[i].endswith("jpg")
            or listing[i].endswith("png")
            or listing[i].endswith("jpeg")
        ):  # is an image
            default_image = listing[i]
            extension_ending = listing[i][-3:]
            break

    default = Image.open(f"{topic}/{subtopic}/{default_image}")
    width, height = default.size  # get dimensions for centering text

    # create array to hold 'cards' for wallpaper
    data = []

    # read vocabulary from csv
    try:
        with open(f"{topic}/{subtopic}/{level}/{level.lower()}.csv") as vocab:
            reader = csv.reader(vocab)
            for row in reader:
                data.append(row)
    # if there are no levels for the current subtopic
    except FileNotFoundError:
        with open(f"{topic}/{subtopic}/{subtopic.lower()}.csv") as vocab:
            reader = csv.reader(vocab)
            for row in reader:
                data.append(row)

    values = ImageFont.truetype(
        "fonts/Noto_Serif_SC/NotoSerifSC-Medium.otf", 100
    )  # font used for main card

    small_definition = ImageFont.truetype(
        "fonts/Noto_Serif_SC/NotoSerifSC-Medium.otf", 60
    )  # font used for information about card

    for i in range(2, len(data)):
        # create images for vocabulary
        default = Image.open(
            f"{topic}/{subtopic}/{default_image}"
        )  # reopen each time to prevent text from spilling over
        draw = ImageDraw.Draw(default)

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

        w, h = draw.textsize(f"Definition: {data[i][2]}", font=small_definition)
        draw.text(
            ((width - w) / 2, ((height - h) / 2) + 50),
            f"Definition: {data[i][2]}",
            (0, 0, 0),
            font=small_definition,
        )  # english definition

        w, other_h = draw.textsize(f"Category: {data[i][3]}", font=small_definition)
        draw.text(
            ((width - w) / 2, ((height - other_h) / 2) + 60 + h),
            f"Category: {data[i][3]}",
            (0, 0, 0),
            font=small_definition,
        )  # word category

        # save image to disk; based on topic + subtopic + option level
        if level is not None:
            default.save(
                f"images/{topic}-{subtopic}-{level}-{i-1}.{extension_ending}"
            )  # TODO: correct filetype (for non .png/.jpg)
        else:
            default.save(f"images/{topic}-{subtopic}-{i-1}/{extension_ending}")