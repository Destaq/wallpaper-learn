import argparse
from create_images import form_images

parser = argparse.ArgumentParser()
parser.add_argument(
    "--topic",
    "-t",
    help="main topic(s) for your wallpaper; choose from:\n-languages\n-history\n-geography",
)

parser.add_argument(
    "--subtopic",
    "-s",
    help="the specific subtopic(s) for your wallpaper; choose from:\n-chinese\n-japanese\n-spanish",
)

parser.add_argument(
    "--level",
    "-l",
    nargs = '?',
    const = None,
    help="granularly specific sub-subtopics for your wallpaper; consult README or view filetree to see exact names",
)

args = parser.parse_args()

print("Please note: writing images takes time (approx. 1 second = 5 images). Please be patient, this process may take up to 10 minutes.")

try:
    form_images(args.topic, args.subtopic, args.level)
except:
    print("One or more of your arguments are incorrect! Please consult the filetree or REAME.md for the supported topics, subtopics, and levels.")