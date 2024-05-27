import os
import openai
from tqdm import tqdm
from multiprocessing.dummy import Pool
from imutils import paths
pool = Pool(8) # Number of concurrent threads

# Set your OpenAI API key
openai.api_key = ''

# Define the directory containing your audio files
directory = 'C:/Opensource/'

# Get a list of all files in the directory
exts = (".mp3", ".wav")
files = list(paths.list_files(directory, validExts=exts))

def transcribe(data):
    idx, file = data
    name = os.path.join(directory, file)
    print(name + " started")
    # Open the file in read-binary mode
    with open(name, 'rb') as f:
        # Transcribe the audio file
        response = openai.Audio.transcribe("whisper-1", f)
    print(name + " done")
    return {
        "idx": idx,
        "text": response['text']
    }

all_text = pool.map(transcribe, enumerate(files))
pool.close()
pool.join()

transcript = ""
for t in sorted(all_text, key=lambda x: x['idx']):
    transcript = transcript + "{}\n".format(t['text'])
print(transcript)

with open("transcript with Whisper.txt", "w") as f:
    f.write(transcript)