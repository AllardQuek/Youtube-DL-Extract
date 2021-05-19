import sys
from pydub import AudioSegment


file = sys.argv[1]
audio = AudioSegment.from_mp3(file)
first_10 = audio[:10000]
first_10.export("../FN-music-10s/Normal/output.mp3", format="mp3")

