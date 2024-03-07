from pytube import YouTube
import tkinter as tk
from tkinter import filedialog

def download_video(url, save_path):
    try:
        yt = YouTube(url)
        streams = yt.streams.filter(progressive=True,file_extension="mp4")
        highest_re_stream = streams.get_highest_resolution()
        highest_re_stream.download(output_path=save_path)
        print("Video Downloaded Successfully!")
    except Exception as e:
        print(e)

def open_file_dialog():
    folder = filedialog.askdirectory()
    if folder:
        print(f"Select Folder: {folder}")
    return folder

if __name__ == "__main__":
    root = tk.Tk()
    root.withdraw()

    video_url = input("Please enter a Youtube url: ")
    save_dir = open_file_dialog()

    if save_dir:
        print("Started download.")
        download_video(video_url, save_dir)        
    else:
        print("Please select a folder to save!")