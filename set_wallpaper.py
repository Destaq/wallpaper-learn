import argparse
from create_images import form_images

parser = argparse.ArgumentParser()
parser.add_argument(
    "--topic",
    "-t",
    nargs = '+',
    help="main topic(s) for your wallpaper; choose from:\n-languages\n-history\n-geography",
)

parser.add_argument(
    "--subtopic",
    "-s",
    nargs = '+',
    help="the specific subtopic(s) for your wallpaper; choose from:\n-chinese\n-japanese\n-spanish",
)

parser.add_argument(
    "--level",
    "-l",
    nargs = '+',
    help="granularly specific sub-subtopic(s) for your wallpaper; consult README or view filetree to see exact names",
    required = False,
)

args = parser.parse_args()

print("Please note: writing images takes time (approx. 1 second = 5 images). Please be patient, this process may take up to 10 minutes.")

print(args.topic, type(args.topic))
try:
    if args.level is not None:
        form_images(args.topic, args.subtopic, args.level)
    else:
        form_images(args.topic, args.subtopic)
except:
    print("One or more of your arguments are incorrect! Please consult the filetree or REAME.md for the supported topics, subtopics, and levels.")