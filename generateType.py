import sys
import json
from pydub import AudioSegment
import os
import re
from mutagen.oggvorbis import OggVorbis
from pydub import AudioSegment
import generateSonginfo as gs
import generateNotes as gn
AudioSegment.converter = "E:\\Code\\ffmpeg-master-latest-win64-gpl-shared\\bin\\ffmpeg.exe"
AudioSegment.ffmpeg = "E:\\Code\\ffmpeg-master-latest-win64-gpl-shared\\bin\\ffmpeg.exe"
AudioSegment.ffprobe = "E:\\Code\\ffmpeg-master-latest-win64-gpl-shared\\bin\\ffprobe.exe"


def changeToOgg(audioFile):
    # Get the file extension
    file_ext = os.path.splitext(audioFile)[1].lower()

    # Load the audio file using the appropriate method
    if file_ext == '.mp3':
        sound = AudioSegment.from_mp3(audioFile)
    elif file_ext == '.wav':
        sound = AudioSegment.from_wav(audioFile)
    elif file_ext == '.flac':
        sound = AudioSegment.from_file(audioFile, format='flac')
    else:
        raise ValueError(f'Unsupported audio format: {file_ext}')

    # Export the audio file in OGG format
    return sound


def addTimeinfo(data, pos, tempo, beatsPerMeasure, interpolateBeatDuration):
    data["timeinfo"].append({"pos": pos, "tempo": tempo, "beatsPerMeasure": beatsPerMeasure,
                            "interpolateBeatDuration": interpolateBeatDuration})


def addNotes():
    pass


data = {
    "typist": "Shinomu_py",
    "keyboard": "QWERTY",
    "difficulty": "easy",
    "level": 1,
    "offsetMS": 0,
    "timeinfo": [],
    "stops": [],
    "skips": [],
    "notes": []
}

print("enter songs_name beatPerBar bpm to_4_8_16_32_orSomeOther randomtype(0 for no random, 1 for yes)")
if len(sys.argv) > 5:
    audioFile = sys.argv[1]
    beatPerBar = sys.argv[2]
    bpm = sys.argv[3]
    to_8_16_32 = sys.argv[4]
    randomtype = sys.argv[5]
    print(f'Audio file: {audioFile}')

    # create a folder of songs name
    songName = os.path.splitext(audioFile)[0]
    result = re.findall(r'[a-zA-Z0-9]+', songName)
    songName = ' '.join(result)
    os.mkdir(songName)

    # get songs length(and song use in output ogg)
    song = changeToOgg(audioFile)
    print(f'./{songName}/{songName}.ogg')
    song.export(f'./{songName}/{songName}.ogg', format="ogg")

    audio = OggVorbis(f'./{songName}/{songName}.ogg')
    song_length_in_sec = audio.info.length

    data["timeinfo"].append({"pos": [0, 1, 0], "bpm": int(bpm),
                            "beatsPerMeasure": int(beatPerBar), "interpolateBeatDuration": 0.0})

    number_of_bars = float(
        bpm) * (float(song_length_in_sec) / float(60)) / float(beatPerBar)

    notes = gn.generateNotes(int(number_of_bars), to_8_16_32, randomtype)
    data["notes"] = notes

    # save type
    with open(f'./{songName}/{songName}.type', 'w') as f:
        json.dump(data, f)

    with open(f'./{songName}/songinfo.json', 'w') as f:
        json.dump(gs.generateSonginfo(songName, bpm), f)
else:
    print('No songs_name beatPerBar bpm to_4_8_16_32_orSomeOther randomtype(0 for no random, 1 for yes) provided')
