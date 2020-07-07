import argparse
from create_images import form_images, empty_directory
import itertools

parser = argparse.ArgumentParser()

parser.add_argument(
    "--topic",
    "-t",
    # nargs = '+',
    action = 'append',
    help="main topic(s) for your wallpaper; choose from:\n-languages\n-history\n-geography",
)

parser.add_argument(
    "--subtopic",
    "-s",
    # nargs = '+',
    action = 'append',
    help="the specific subtopic(s) for your wallpaper; choose from:\n-chinese\n-japanese\n-spanish",
)

parser.add_argument(
    "--level",
    "-l",
    nargs = '?',
    action = 'append',
    default = None,
    help="granularly specific sub-subtopic(s) for your wallpaper; consult README or view filetree to see exact names",
)

args = parser.parse_args()
args_dict = vars(args)

topic = args_dict.get("topic")
subtopic = args_dict.get("subtopic")
level = args_dict.get("level")


print("Please note: writing images takes time (approx. 1 second = 5 images). Please be patient, this process may take a few minutes.")

try:
    empty_directory()
    for (t, s, l) in (itertools.zip_longest(topic, subtopic, level)):
        if l is not None:
            form_images(t, s, l)
        else:
            form_images(t, s)
except KeyboardInterrupt:
    print("You have interrupted the program.")
except:
    print("One or more of your arguments are incorrect! Please consult the filetree or REAME.md for the supported topics, subtopics, and levels.")