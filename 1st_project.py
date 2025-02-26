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

    threading.Thread(target=task,).start()

def update_quality_options(*args):                     # 4. Create a funtion that will implement that quality of what the user want
    global quality_var, quality_dropdown

    quality_dropdown["menu"].delete(0, "end")

    if format_var.get() == "mp4":
        options = ["144p", "240p", "360p", "480p", "720p", "1080p", "Best"]
    else:
        options = ["64kbps", "128kbps", "192kbps", "256kbps", "320kbps", "Best"]

    middle_index = len(options) // 2 
    quality_var.set(options[middle_index])  

    for option in options:
        quality_dropdown["menu"].add_command(label=option, command=tk._setit(quality_var, option))

def create_gui():                                      # 5. Create a GUI of the project (Height, Width, Button, and Input Box)
    global url_entry, format_var, quality_var, quality_dropdown
    root = tk.Tk()
    root.title("Quickieverter")
    root.geometry("400x300")
    root.configure(bg="#2C3E50")
    root.option_add("*Font", "Helvetica 12")

    tk.Label(root, text="Youtube Link/URL", font=("Helvetica", 12), bg="#2C3E50", fg="white").pack(pady=5)
    url_entry = tk.Entry(root, width=50, font=("Helvetica", 10))
    url_entry.pack(pady=5)

    format_var = tk.StringVar(value="mp4")
    format_var.trace_add("write", update_quality_options)
    quality_var = tk.StringVar()

    options_frame = tk.Frame(root, bg="#2C3E50")
    options_frame.pack()
    tk.Radiobutton(options_frame, text="MP4", variable=format_var, value="mp4", bg="#2C3E50", fg="white", selectcolor="#34495E", font=("Futura", 10)).pack(side=tk.LEFT, padx=10)
    tk.Radiobutton(options_frame, text="MP3", variable=format_var, value="mp3", bg="#2C3E50", fg="white", selectcolor="#34495E", font=("Futura", 10)).pack(side=tk.LEFT)

    tk.Label(root, text="Select Quality:", font=("Helvetica", 12), bg="#2C3E50", fg="white").pack(pady=5)
    quality_dropdown = tk.OptionMenu(root, quality_var, "")
    quality_dropdown.pack(pady=5)
    update_quality_options()

    tk.Button(root, text="Download", command=dl_youtube, font=("Helvetica", 12, "bold"), width=20, bg="#27AE60", fg="white", relief="flat").pack(pady=10)
    tk.Button(root, text="Exit", command=root.quit, font=("Helvetica", 12, "bold"), width=20, bg="#E74C3C", fg="white", relief="flat").pack()

    root.mainloop()

if __name__ == "__main__":
    create_gui()