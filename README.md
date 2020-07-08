# wallpaper-learn

> *Let your wallpaper become your teacher!*

With `wallpaper-learn`, you can effortlessly learn new phrases, countries and capitals, or really anything you want... straight from your wallpaper!

Curated phrases and educational material are available for a wide range of subjects and languages, and all you have to do is create a new folder and type one command before being able to have a cycling, ever-changing computer wallpaper to learn from.

<p align="center">
  <img src="https://github.com/Destaq/wallpaper-learn/blob/master/screenshots/display.gif?raw=true">
</p>

## Topics

This is a list of all of the topics, subtopics, and levels available to set as your wallpaper. If you see something missing here, just add your own, contributing takes only a few minutes!

This also serves as a place to view possible commands without having to explore the file tree, which is why the names may sound a bit weird. However, their purpose is detailed in italic to the right.

### languages

-   chinese
    - HSK-1 *(words required for HSK-1 level, in pinyin and hanyu characters, with a translation and category)*
-   spanish
    - top100 *(top 100 most used spanish words, their translation, and part of speech)*


### geography

-   countries *(all countries and territories of the world with capitals)*
-   states *(all 50 states of the USA with capitals and location)*

... and many more to come! It's very simple to contribute by opening a PR with your files, and a few minutes of finding and parsing the right URL could help more people than you may expect.

## Usage

`wallpaper-learn` can be run straight from the terminal, assuming that you have navigated to the root directory that holds `set_wallpaper.py`. From there, it takes a few simple arguments in order to find out which topic + subtopic + level you are interested in, and then creates an `images` folder which houses all of the images.

**`wallpaper-learn` also supports having multiple arguments (see bottom of this section for details).**

You can run this by running the command `python3 set_wallpaper.py` and any commands you'd like from the terminal. Arguments passed in are case-insensitive. The following commands are available:

-   `-t or --topic`: this is the main 'topic' of your Desktop background (i.e. the general subject; a directory in the root directory such as `languages`, `history`, or `geography`)
-   `-s or --subtopic`: this is the secondary, more specific topic for your wallpaper (i.e. a subcategory of the directory you chose above, such as `chinese`). It must be a child of the correct `topic` directory.
-   `-l or --level`: this is an optional argument, as not all subtopics go down to this level of detail. It corresponds to a subdirectory of the `subtopic`, such as `HSK-1` for `chinese`, and you can view all of them by exploring the file tree for this program or consulting the list.

Likewise, you can also view possible arguments by running `python3 set_wallpaper.py --help` which will give you a detailed breakdown of how to use this program or by referring back to this guide.

Once the command has finished running, all that you have to do is navigate to your settings/System Preferences and [set up a cycling wallpaper background](#setting-cycling-wallpaper), which takes all of 30 seconds.

*Simple Example: `python3 set_wallpaper.py -t languages -s chinese -l HSK-1`*

*Advanced Example (multiple arguments):* 
```
python3 set_wallpaper.py -t languages -s chinese -l HSK-1 \
-t languages -s spanish -l top100 \
-t geography -s countries
```
In essence, for the advanced examples all you have to do is list each of the paths to the 'content' you want to go to individually. For example, these paths are `languages -> chinese -> HSK-1`, `languages -> spanish -> top 100` and `geography -> states`. Note how for the geography there is *not* a `--level` argument; that is because there is no level below `states` and there is a CSV file in `geography -> states`.

You can also run it all as a one-line argument, but to keep it clear for yourself the multi-line one above is recommended.
`python3 set_wallpaper.py -t languages -s chinese -l HSK-1 -t languages -s spanish -l top100 -t geography -s countries`.

## Requirements

This program requires the `Pillow` library for image manipulation... and that's it! Everything else is built in.

You can install this requirement, available on PyPI, with `pip3 install Pillow` or `pip3 install -r requirements.txt`.

## Contribution

Please, if you would like to contribute, know that you are more than welcome to. I do not have the knowledge or the time to create dozens `.csv` files for various topics, but the more we have, the better for the community and users of this package.

Contributing to this repository is simple. All you have to do is create a CSV file with the appropriate columns in the appropriate format, and [open a pull request](https://opensource.com/article/19/7/create-pull-request-github), open an issue if you're having trouble with making one, or [shoot me an email](mailto:simon@simonilincev.com) if you are _really_ having trouble.

You can also contribute by finding a background image for various topics. These images should be named `default.jpg` or `default.png` and have dimensions of roughly 1920 x 1280 pixels. Likewise, you can help by adding custom fonts, more instructions are available at the README.md for that folder [here](/fonts/README.md).

### CSV Formatting

If you would like to add a list of words/information and their definitions/values, you need to submit a csv file.

This is the format for the `CSV` files, which are **4, 3 or 2 columns by _n_ rows wide**:

-   _first row_: left empty, or optional title
-   _second row_: titles for each of the columns in the following order:
    -   1st column **required**: the type of the main text that will be displayed (you can think of it as the question on the flashcard), such as _Chinese character_, _Medieval Event_, _Country_, and so on.
    -   2nd column **optional**: a second value for the first column (applicable for some topics). Mostly used in Asian languages, would be for example _Pinyin_ in Chinese as both _Pinyin_ and _Chinese Character_ would be displayed as a 'flashcard question'.
    -   3rd column **required**: the 'definitions' for each of the cards will be here. You can put something generic like _Definition_ or more specific things such as _English translation_, _Event_, _Country Flag_, etc. as fits the CSV file.<br>
        _note: if you didn't put a second column, this will be your second colum_
    -   4th colum **optional**: in this optional column you can put in categories for each of the key + value pairs you put in the 1st + 3rd columns. In most cases, the title for this will be something general like _Category_ or _Type_.
-   _third row and beyond_: this is when you start filling up your CSV file with the actual content. Below each of your columns, create a row with values that correspond to what is below the column name.

Once you have made your CSV file, you need to drop it in the appropriate folders. For example, if you chose to make a CSV file for the vocab for NP-1 in Japanese, you would:
1. Navigate to the root directory and then go into the `content` directory, this is where all content is stored for making the images
2. Go to the `languages` directory (if you were doing something completely new like music, you'd create a new folder here as it is a new topic)
3. Create a `japanese` directory in the `languages` directory if there is not already one (this represents the subtopic). Here, you _could_ make the csv file (naming it the same way as the subdirectory, i.e. `japanese.csv`, but since NP-1 is a specific part of the `japanese` course, I'd recommend making a `level` and dropping it there)
4. Create a directory (optional, see above) named `NP-1` which represents the level. Drop the csv file there and name it `np-1.csv` (must be lowercase and same name as directory it is in)

That's it! Users can now choose to add your csv key - value pairs to learn from as their wallpaper.

### Examples

Complete examples can be found by looking at CSV files in the repository or you can see a quick, partial example below.

#### 4-row example

| Ancient Events   |                     |            |           |
| ---------------- | ------------------- | ---------- | --------- |
| Event            | Ruler               | Date       | Category  |
| The Persian Wars | Darius the Great    | 492-442 BC | Wars      |
| Paper in Egypt   | Ptolemy V Epiphanes | 200 BC     | Invention |

#### 3-row example

| Ancient Events   |            |           |
| ---------------- | ---------- | --------- |
| Event            | Date       | Category  |
| The Persian Wars | 492-442 BC | Wars      |
| Paper in Egypt   | 200 BC     | Invention |

#### 2-row example

| Ancient Events   |            |
| ---------------- | ---------- |
| Event            | Date       |
| The Persian Wars | 492-442 BC |
| Paper in Egypt   | 200 BC     |

### Setting Cycling Wallpaper
Once you have your images set up, all you need to do is set them to cycle as your wallpaper in your settings. Below are some images demonstrating how you can do so in various operating systems.

#### Mac
Navigate to your `System Preferences -> Desktop & Screen Saver -> Desktop` and click the + button at the bottom left to add an images folder (your images folder in the root directory of this program). Set `change picture` to True, adjust your cycling time, and choose whether or not to enable random order.

**Please note**: it may take a few minutes after the images have finished being downloaded for them all to show up on your wallpaper as it takes time for the Mac system to read them.
<p align="center">
  <img src="https://github.com/Destaq/wallpaper-learn/blob/master/screenshots/mac.png?raw=true">
</p>

#### Windows
Similar procedure to Mac.
<p align="center">
  <img src="https://github.com/Destaq/wallpaper-learn/blob/master/screenshots/windows.png?raw=true">
</p>
