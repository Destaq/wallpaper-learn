# wallpaper-learn

With wallpaper learn, you can effortlessly learn new phrases, countries, or really anything you want... straight from your wallpaper.

Curated phrases and educational material are available for a wide range of subjects and languages, and all you have to do is create a new folder and click a few buttons in settings before being able to have an educational background for your device.

## Topics

### Languages

-   Chinese
-   Spanish
-   English

### History

-   Ancient
-   Medieval
-   Modern

### Geography

-   Countries
-   States

... and many more to come! It's very simple to contribute by opening a PR with your files, and a few minutes finding and parsing the right URL could help more than you might expect.

## Usage

`wallpaper-learn` can be run straight from the terminal, assuming that you have navigated to the root directory that holds `select_folder.py`. From there, it takes a few simple arguments in order to find out which topic + subtopic you are interested in, and then creates an `images` folder which houses all of the images.

You can run this by running the command `python3 select_folder.py` and any commands you'd like from the terminal. The following commands are available:

-   `-t or --topic`: this is the main 'topic' of your Desktop background (i.e. the general subject; a directory in the root directory such as `languages`, `history`, or `geography`)
-   `-s or --subtopic`: this is the secondary, more specific topic for your wallpaper (i.e. a subcategory of the directory you chose above, such as `chinese`). It must be a child of the correct `topic` directory.
-   `-l or --level`: this is an optional argument, as not all subtopics go down to this level of detail. It corresponds to a subdirectory of the `subtopic`, such as `HSK-1` for `chinese`, and you can view all of them by exploring the file tree for this program or consulting the list.

Likewise, you can also view possible arguments by running `python3 select_folder.py --help` which will give you a detailed breakdown of how to use this program or by referring back to this guide.

Once the command has finished running, all that you have to do is navigate to your settings/System Preferences and set up a cycling wallpaper background.

## Requirements

This program requires the `Pillow` library for image manipulation... and that's it! Everything else is built in.

You can install this requirement, available on PyPI, with `pip3 install Pillow` or `pip3 install -r requirements.txt`.

## Contribution

Please, if you would like to contribute, know that you are more than welcome to. I do not have the knowledge or the time to create dozens `.csv` files for various topics, but the more we have, the better for the community and users of this package.

Contributing to this repository is simple. All you have to do is create a CSV file with the appropriate columns in the appropriate format, and [open a pull request](https://opensource.com/article/19/7/create-pull-request-github), open an issue if you're having trouble with making one, or [shoot me an email](mailto:simon@simonilincev.com) if you are _really_ having trouble.

### CSV Formatting

This is the format for the `CSV` files, which are **4, 3 or 2 columns by _n_ rows wide**:

-   _first row_: left empty, or optional title
-   _second row_: titles for each of the columns in the following order:
    -   1st column **required**: the type of the main text that will be displayed (you can think of it as the question on the flashcard), such as _Chinese character_, _Medieval Event_, _Country_, and so on.
    -   2nd column **optional**: a second value for the first column (applicable for some topics). Mostly used in Asian languages, would be for example _Pinyin_ in Chinese as both _Pinyin_ and _Chinese Character_ would be displayed as a 'flashcard question'.
    -   3rd column **required**: the 'definitions' for each of the cards will be here. You can put something generic like _Definition_ or more specific things such as _English translation_, _Event_, _Country Flag_, etc. as fits the CSV file.<br>
        _note: if you didn't put a second column, this will be your second colum_
    -   4th colum **optional**: in this optional column you can put in categories for each of the key + value pairs you put in the 1st + 3rd columns. In most cases, the title for this will be something general like _Category_ or _Type_.
-   _third row and beyond_: this is when you start filling up your CSV file with the actual content. Below each of your columns, create a row with values that correspond to what is below the column name.

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