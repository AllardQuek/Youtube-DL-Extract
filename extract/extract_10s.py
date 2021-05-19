"""
Extract the first 10s of mp3 files.
"""

from pydub import AudioSegment
import os


def extract_10s(file_name):
    audio = AudioSegment.from_mp3("../FN-music/Deathmatch/" + file_name)
    first_10 = audio[:10000]
    output_folder = "../FN-music-10s/Deathmatch/" + file_name 
    first_10.export(output_folder, format="mp3")

for file_name in os.listdir("../FN-music/Deathmatch/"):
    print(file_name)
    extract_10s(file_name)
