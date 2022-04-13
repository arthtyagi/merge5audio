import sys
import os
import tkinter
import webbrowser
from pydub import AudioSegment
# merge audio files

# AudioSegment.converter = "/usr/local/bin/ffmpeg"


def start():
    # tkinter window
    window()
    # get the path of the audio files
    """
    path = sys.argv[1]
    # get the name of the output file
    output = sys.argv[2]
    # get the list of files
    files = os.listdir(path)
    # get the length of the list
    length = len(files)
    # check if the files have .wav extension
    try:
        check_wav(files)  # exit if not
        merge(files, output)
    except Exception as e:
        print(e)
    """


def check_wav(files):
    for i in range(len(files)):
        if not files[i].endswith(".wav"):
            print("Please use .wav files")
            sys.exit()


def merge(path, output_path):
    # get the length of the list
    files = os.listdir(path)
    length = len(files)
    # check if the files have .wav extension
    check_wav(files)  # exit if not
    # create a list of batches of 5
    batches = [files[i:i + 4] for i in range(0, length, 5)]
    print(batches)  # debug
    # create a list of audio segments
    audio_segments = []
    # loop through the batches
    try:
        for i in range(len(batches)):
            # loop through the files in the batch
            audio_segments.extend(AudioSegment.from_file(
                f'{path}/{batches[i][j]}') for j in range(len(batches[i])))
            # merge the audio segments
            merged = AudioSegment.empty()
            for audio_segment in audio_segments:
                merged += audio_segment
            # export the merged audio file
            merged.export(
                f'{output_path}/mergedit{str(i)}.wav', format="wav")
            # clear the audio segments
            audio_segments.clear()
            print(f"Merged batch {str(i)}")

    except Exception as e:
        print(e)

# to-do: add a simple GUI


def window():
    # create a window
    root = tkinter.Tk(baseName="Audio Merger")
    # set the title
    root.title("Merge5Audio: An audio Merge App")
    # set the size
    root.geometry("500x300")
    # add a beautiful description label
    description = tkinter.Label(root, text="Merge 5 AUDIO FILES")
    description.pack()
    readme_button = tkinter.Button(root, text="README",
                                   command=lambda: call_back(
                                       "https://github.com/mattcarrelo/Maremoto_Audio_Merger/blob/master/merge5audio/readme.md"))
    readme_button.pack()
    tkinter.Label(root, text="").pack()
    # create a label
    label = tkinter.Label(
        root, text="Please enter the path of the audio files")
    output_path = tkinter.Label(root, text="Please enter the output path")
    # label2 = tkinter.Label(
    #    root, text="Please enter the name of the output file")
    # create a text box
    path = tkinter.Entry(root)
    output = tkinter.Entry(root)
    # create a button
    merge_button = tkinter.Button(
        root, text="Merge",
        command=lambda: merge(path.get(), output.get()))
    # pack the widgets
    label.pack()
    path.pack()
    output_path.pack()
    output.pack()
    merge_button.pack()
    tkinter.Label(root, text="").pack()
    created_by = tkinter.Button(
        root, text="Created by: Arth", compound=tkinter.LEFT, cursor="hand2", fg="blue",
        command=lambda: call_back("https://github.com/arthtyagi"))
    created_by.pack()

    # start the main loop
    root.mainloop()


def call_back(url):
    webbrowser.open_new(url)


def unittest(): # todo: make unittest better
    input_path = input("Enter the path of the audio files: ")
    output_path = input("Enter the output path: ")
    files = os.listdir(input_path)
    try:
        check_wav(files)
        merge(input_path, output_path)
    except Exception as e:
        print(e)


debug = False

if __name__ == '__main__':
    if debug:
        unittest()
    else:
        start()
