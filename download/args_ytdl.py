import sys
from subprocess import call

# Output path: Need to end with a '/'!
path = "./outputs/"

num_args = len(sys.argv) - 1
base_command = "youtube-dl -ciw --extract-audio --audio-format mp3  --audio-quality 0 --output " + path + "%(title)s.%(ext)s "

# This will run 0 times if no arguments are passed
for i in range(num_args):
    command = base_command + sys.argv[i + 1]
    call(command.split(), shell=False)
