# 1. Import important modules

import os # this is for directory of the file downloaded
import threading # this is for running download process without complications
import tkinter as tk # this is for the GUI library
from tkinter import messagebox # this will be important for notification of what happened in the file and downloading process
import yt_dlp # this is for downloading the youtube links (I changed it into yt_dlp)

# 2. Create a funtion that will get the youtube link

def dl_youtube():
    def task():
        url = url_entry.get()
        if not url:
            messagebox.showerror("Error", "Please enter a YouTube Link/URL")
            return
        format_choice = format_var.get()
        quality_choice = quality_var.get()
        download_folder = "Downloads"
        os.makedirs(download_folder, exist_ok=True)

        

# 3. Create a function that will find the quality and format of file of what the user's want to download



# 4. Create a funtion that will implement that quality of what the user want



# 5. Create a GUI of the project (Height, Width, Button, and Input Box)

