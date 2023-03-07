import os
import yt_dlp

print("ENTER 1 TO DOWNLOAD PLAYLIST AS MP3")
print("ENTER 2 TO DOWNLOAD PLAYLIST AS VIDEO")
choice = input("==> ")
playlist = input("ENTER THE URL OF THE PLAYLIST: ")

output_dir = "YTPlaylistDownloader"

if not os.path.exists(output_dir):
    os.makedirs(output_dir)

def as_audio():
    # Replace <playlist_url> with the URL of the YouTube playlist you want to download
    playlist_url = playlist

    # Set options for downloading audio only and extracting the best quality
    ydl_opts = {
        "format": "bestaudio",
        "postprocessors": [
            {
                "key": "FFmpegExtractAudio",
                "preferredcodec": "mp3",
                "preferredquality": "192",
            }
        ],
        "outtmpl": os.path.join(output_dir, "%(title)s.%(ext)s"),
    }

    # Create a yt_dlp instance and download the playlist with the given options
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.download([playlist_url])

def as_video():
    # Replace <playlist_url> with the URL of the YouTube playlist you want to download
    playlist_url = playlist

    # Prompt the user to choose a quality option
    print("ENTER 1 FOR BEST QUALITY")
    print("ENTER 2 FOR 720P")
    print("ENTER 3 FOR 480P")
    print("ENTER 4 FOR 360P")
    print("ENTER 5 FOR 240P")
    quality_choice = input("==> ")

    # Set options for downloading video and extracting the chosen quality
    if quality_choice == "1":
        ydl_opts = {
            "format": "bestvideo[ext=mp4]+bestaudio[ext=m4a]/best[ext=mp4]/best",
            "outtmpl": os.path.join(output_dir, "%(title)s.%(ext)s"),
        }
    elif quality_choice == "2":
        ydl_opts = {
            "format": "bestvideo[height=720][ext=mp4]+bestaudio[ext=m4a]/best[height=720][ext=mp4]/best",
            "outtmpl": os.path.join(output_dir, "%(title)s.%(ext)s"),
        }
    elif quality_choice == "3":
        ydl_opts = {
            "format": "bestvideo[height=480][ext=mp4]+bestaudio[ext=m4a]/best[height=480][ext=mp4]/best",
            "outtmpl": os.path.join(output_dir, "%(title)s.%(ext)s"),
        }
    elif quality_choice == "4":
        ydl_opts = {
            "format": "bestvideo[height=360][ext=mp4]+bestaudio[ext=m4a]/best[height=360][ext=mp4]/best",
            "outtmpl": os.path.join(output_dir, "%(title)s.%(ext)s"),
        }
    elif quality_choice == "5":
        ydl_opts = {
            "format": "bestvideo[height=240][ext=mp4]+bestaudio[ext=m4a]/best[height=240][ext=mp4]/best",
            "outtmpl": os.path.join(output_dir, "%(title)s.%(ext)s"),
        }
    else:
        print("Invalid choice. Defaulting to best quality.")
        ydl_opts = {
            "format": "bestvideo[ext=mp4]+bestaudio[ext=m4a]/best[ext=mp4]/best",
            "outtmpl": os.path.join(output_dir, "%(title)s.%(ext)s"),
        }

    # Create a yt_dlp instance and download the playlist with the given options
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.download([playlist_url])


if choice == "1":
    as_audio()
    input()
elif choice == "2":
    as_video()
    input()
else:
    print("INVALID INPUT, PLEASE TRY AGAIN")
    input()