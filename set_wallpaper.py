import argparse
from create_images import form_images, empty_directory
import itertools

parser = argparse.ArgumentParser()

# create command line arguments
parser.add_argument(
    "--topic",
    "-t",
    action = 'append',
    help="main topic(s) for your wallpaper; choose from:\n-languages\n-geography",
)

parser.add_argument(
    "--subtopic",
    "-s",
    action = 'append',
    help="the specific subtopic(s) for your wallpaper; choose from:\n-chinese\n-spanish",
)

parser.add_argument(
    "--level",
    "-l",
    nargs = '?', # this is an optional argument
    action = 'append',
    default = None, # if nothing is provided, it will default to None
    help="granularly specific sub-subtopic(s) for your wallpaper; consult README or view filetree to see exact names (examples include HSK-1 for chinese or top100 for spanish)",
)


args = parser.parse_args()
args_dict = vars(args) # convert to dictionary

topic = args_dict.get("topic")
subtopic = args_dict.get("subtopic")
level = args_dict.get("level")


print("Please note: writing images takes time (approx. 1 second = 5 images). Please be patient, this process may take a few minutes.")

try:
    empty_directory() # remove previous images from directory
    for (t, s, l) in (itertools.zip_longest(topic, subtopic, level)):
        if l is not None:
            form_images(t, s, l)
        else:
            form_images(t, s)
except KeyboardInterrupt:
    print("You have interrupted the program.")
except:
    print("One or more of your arguments are incorrect! Please consult the filetree or REAME.md for the supported topics, subtopics, and levels.")