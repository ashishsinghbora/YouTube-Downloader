from pytube import YouTube

def download_video(url, path, resolution=None):
    try:
        yt = YouTube(url)
        if resolution:
            video = yt.streams.filter(res=resolution).first()
        else:
            video = yt.streams.get_highest_resolution()
        video.download(path)
        print("Download completed successfully!")
    except Exception as e:
        print(f"An error occurred: {str(e)}")

if __name__ == "__main__":
    video_url = input("Enter the YouTube video URL: ")
    download_path = input("Enter the download path: ")
    resolution_choice = input("Enter the desired resolution (e.g., 720p, 1080p), or leave blank for highest resolution: ")

    download_video(video_url, download_path, resolution_choice)
