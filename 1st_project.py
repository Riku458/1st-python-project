# 1. Import important modules

import os # this is for directory of the file downloaded
import threading # this is for running download process without complications
import tkinter as tk # this is for the GUI library
from tkinter import messagebox, filedialog # this will be important for notification of what happened in the file and downloading process
import yt_dlp # this is for downloading the youtube links (I changed it into yt_dlp)

def dl_youtube():                                       # 2. Create a funtion that will get the youtube link
    def task():
        url = url_entry.get()
        if not url:
            messagebox.showerror("Error", "Please enter a YouTube Link/URL")
            return
        format_choice = format_var.get()
        quality_choice = quality_var.get()
        
        download_folder = filedialog.askdirectory(title="Select Download Folder")
        if not download_folder:
            messagebox.showerror("Error", "Please select or create a download folder")
            return

        os.makedirs(download_folder, exist_ok=True)

        video_quality_map = {                            # 3. Create a function that will find the quality and format of file of what the user's want to download        
            "144p": "bv*[height=144]+ba/b[height=144]",
            "240p": "bv*[height=240]+ba/b[height=240]",
            "360p": "bv*[height=360]+ba/b[height=360]",
            "480p": "bv*[height=480]+ba/b[height=480]",
            "720p": "bv*[height=720]+ba/b[height=720]",
            "1080p": "bv*[height=1080]+ba/b[height=1080]",
            "Best": "bestvideo+bestaudio/best"
        }

        audio_quality_map = {
            "64kbps": "64",
            "128kbps": "128",
            "192kbps": "192",
            "256kbps": "256",
            "320kbps": "320",
            "Best": "best"
        }

        if format_choice == "mp4":
            selected_format = video_quality_map.get(quality_choice, "bestvideo+bestaudio/best")
            yt_opts = {
                'outtmpl': os.path.join(download_folder, f'%(title)s_{quality_choice}.%(ext)s'),
                'format': selected_format,
                'merge_output_format': 'mp4',
                'postprocessor_args': ['-c:a', 'aac']
            }
        else:
            selected_quality = audio_quality_map.get(quality_choice, "192")
            yt_opts = {
                'outtmpl': os.path.join(download_folder, f'%(title)s_{quality_choice}kbps.%(ext)s'),
                'format': 'bestaudio',
                'postprocessors': [{'key': 'FFmpegExtractAudio', 'preferredcodec': 'mp3', 'preferredquality': selected_quality}]
            }

        try:
            with yt_dlp.YoutubeDL(yt_opts) as ydl:
                ydl.download([url])
            
            messagebox.showinfo("Success", f"Downloaded {format_choice.upper()} in {quality_choice} quality in {download_folder}! Compatible with mobile and standard media players.")
        except Exception as e:
            messagebox.showerror("Error", f"Download failed: {str(e)}")

    threading.Thread(target=task).start()


# 4. Create a funtion that will implement that quality of what the user want

def update_quality_options(*args):
    quality_dropdown["menu"].delete(0, "end ")



# 5. Create a GUI of the project (Height, Width, Button, and Input Box)

