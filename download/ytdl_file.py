#!/usr/bin/env python

import sys
from subprocess import call

def main():
    if (len(sys.argv) - 1 != 1):
        print("Please provide a file!")
        return 1;

    # Output path to save results to
    path = "~/Desktop/FN-GTS/FN-music/"
    file = sys.argv[1]

    with open(file) as f:
        lines = f.readlines()

    command = "youtube-dl -ciw --extract-audio --audio-format mp3  --audio-quality 0 --output " + path + "%(title)s.%(ext)s " 

    for line in lines:
        line_command = command + line
        call(line_command.split(), shell=False)

if __name__ == "__main__":
    main()
