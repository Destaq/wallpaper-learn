## wallpaper-learn/fonts

All fonts used for writing on the default images are stored here. Several different types of fonts are included because there is no one font that supports all languages well, and diffferent fonts suit different topics, subtopics, or levels.

These fonts have been taken from the Google Fonts library, and are OFL-licensed, meaning they can be used publicly for free. If you would like to add a font for your CSV file or image, please make sure that it can be distributed and used for free. One great place to look for such fonts is in the [Google Fonts database](https://fonts.google.com/). Make sure that you type in some example text and make sure that the font works with the CSV file's text that you want to add to this repository. Once you have done so, all that's left is to click on the font, click `download family`, unzip it, and add the `.ttf` or `.otf` file and its directory to this folder.

In order to associate your font with the correct topic or subtopic, you need to edit the `font_dictionary.py` file in the root directory. This is a simple dictionary that holds the name of the topic/subtopic as a key and the font as a value (example: `"spanish": "fonts/Courgette/Courgette-Regular.ttf",`).
