# Youtube-DL-Extract-mp3

An attempt to automate:

1. Downloading of mp3 Files from Youtube
2. Extracting of excerpts from downloaded mp3 files

When I needed to download 30 songs off Youtube for a [Guess The Song](https://songtrivia2.io/) game 🙃


## 1. Downloading mp3 from Youtube
Install youtube-dl: `pip install youtube-dl`

Navigate to Youtube download folder:
`cd download`

### Download by Passing Command-line Arguments
Pass youtube link(s) as arguments. Arguments must be space-separated.

`pythoon args_ytdl.py <link1> <link2> <link3> ...` 

### Download by Passing Input File as Argument
`python file_ytdl.py input_files/files.txt`


## 2. Manipulation of Audio Files
Install pydub: `pip install pydub`

Navigate to Youtube extract folder: `cd extract`

### Extract First 10s Using File Path
Pass the filepath as an argument.

`python single_extract.py sample-audio.mp3`

### Extract First 10s of All Files in a Directory
Specifiy input and output directories in `extract_10s.py`.

`python extract_10s.py`

#### Using command line tool:
First, make sure folders used are already created (they may be empty).

Pass in the input directory path, output directory path, and duration in seconds to extract.

Note that all paths should **end with a forward slash** so that the correct file paths can be constructed using string concatenation.
`python args_extract_10s.py -in ./outputs/10s/ -out ./outputs/5s/ -dur 5`
