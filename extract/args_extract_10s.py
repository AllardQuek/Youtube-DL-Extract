"""
Extract the first 10s of mp3 files.
"""

from pydub import AudioSegment
import os
import argparse

# * INITIALISE PARSER
parser = argparse.ArgumentParser(
    description="Pass in your directory paths"
)

# Add positional/optional arguments (short form, long form, help text, default value)
parser.add_argument('-in', '--inputdir', help="path to directory containing input audio files", \
                        default='../download/new/')
parser.add_argument('-out', '--outputdir', help="path to directory containing output audio files", \
                        default='./outputs/10s/')
parser.add_argument('-dur', '--duration', help="duration of clip to extract in seconds", \
                        default=10)

# Parse arguments: make sure paths have / appended to them
args = parser.parse_args()
INPUT_DIR = args.inputdir
OUTPUT_DIR = args.outputdir
DURATION = int(args.duration) * 1000


def extract_10s(file_name):
    print(INPUT_DIR + file_name)
    audio = AudioSegment.from_mp3(INPUT_DIR + file_name)
    first_10 = audio[:DURATION]
    output_path = OUTPUT_DIR + file_name 
    first_10.export(output_path, format="mp3")

for file_name in os.listdir(INPUT_DIR):
    print(file_name)
    extract_10s(file_name)
