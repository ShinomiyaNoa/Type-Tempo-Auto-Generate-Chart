def generateSonginfo(songName, bpm):
    data = {
        "title": f"{songName}",
        "artist": "",
        "genre": "",
        "music": f"{songName}.ogg",
        "coverart": "",
        "bpmtext": f"{int(bpm)}",
        "musicPreviewStart": 33.099998474121094,
        "musicPreviewStop": 62.06999969482422
    }
    return data
