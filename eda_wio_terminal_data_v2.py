import pandas as pd
from tqdm import tqdm
from os.path import join

RECORDING_DIR = "recordings"
WIO_PROCESSED_FILE = "wio_processed.csv"
WIO_TERMINAL_FILE = "sound_log.txt"

with open(WIO_TERMINAL_FILE) as file:
    data = file.readlines()

data = data[:-1:2]

raw_audio = []
timestamps = []

df = pd.DataFrame()

for row in tqdm(data):
    timestamp = " ".join(row.split(" ")[:-1])
    reading = int(row.split(" ")[-1])
    raw_audio.append(reading)
    timestamps.append(timestamp)
   
df["timestamp"] = timestamps
df["raw_audio"] = raw_audio

df.to_csv(join(RECORDING_DIR, WIO_PROCESSED_FILE), index=False)

print(df["timestamp"].value_counts())