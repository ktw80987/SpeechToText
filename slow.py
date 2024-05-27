import os
import speech_recognition as sr
from tqdm import tqdm

with open("C:/Opensource/opensource-424514-4fda75a13bce.json") as f:
    GOOGLE_CLOUD_SPEECH_CREDENTIALS = f.read()

r = sr.Recognizer()
files = sorted(os.listdir('C:/Opensource/'))

all_text = []

for f in tqdm(files):
    if not f.endswith('.wav'):  # Skip non-audio files
        continue
    name = "C:/Opensource/" + f
    # Load audio file
    with sr.AudioFile(name) as source:
        audio = r.record(source)
    # Transcribe audio file
    text = r.recognize_google_cloud(audio, credentials_json=GOOGLE_CLOUD_SPEECH_CREDENTIALS)
    all_text.append(text)

transcript = ""
for i, t in enumerate(all_text):
    total_seconds = i * 30
    m, s = divmod(total_seconds, 60)
    h, m = divmod(m, 60)

    # Format time as h:m:s - 30 seconds of text
    transcript = transcript + "{:0>2d}:{:0>2d}:{:0>2d} {}\n".format(h, m, s, t)

print(transcript)

with open("transcript(slow).txt", "w") as f:
    f.write(transcript)