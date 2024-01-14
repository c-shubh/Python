from pdfminer.high_level import extract_text
from gtts import gTTS
import os
import tkinter as tk

# Globals -------------------------------------------------
FILE_PATH = "./sample.pdf"

FILE_PATH_FOR_TXT = os.path.join(
    os.path.dirname(FILE_PATH), os.path.split(FILE_PATH)[1].split(".")[0] + ".txt"
)

FILE_PATH_FOR_MP3 = os.path.join(
    os.path.dirname(FILE_PATH), os.path.split(FILE_PATH)[1].split(".")[0] + ".mp3"
)
# Globals -------------------------------------------------


def make_text():
    if os.path.exists(FILE_PATH_FOR_TXT):
        with open(FILE_PATH_FOR_TXT, "w+") as f:
            return f.read().replace("\n", " ")
    else:
        text = extract_text(FILE_PATH)
        text_single_line = text.replace("\n", " ")

        with open(FILE_PATH_FOR_TXT, "w+") as f:
            f.write(text)
            f.flush()
            f.seek(0)

        return text_single_line


def make_mp3():
    if os.path.exists(FILE_PATH_FOR_MP3):
        play_audio()
    else:
        reader = gTTS(make_text(), lang="en")
        reader.save(FILE_PATH_FOR_MP3)
        play_audio()


def play_audio():
    if os.name == "posix":
        os.system("open " + FILE_PATH_FOR_MP3)
    elif os.name == "nt":
        os.system(FILE_PATH_FOR_MP3)


make_mp3()
