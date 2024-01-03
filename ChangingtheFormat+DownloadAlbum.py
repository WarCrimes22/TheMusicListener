import subprocess, eyed3, requests, pytube

def convert_video_to_audio(video_file_path, audio_file_path):
    subprocess.run(
        ["ffmpeg", "-i", video_file_path, "-vn", "-ar", "44100", "-ac", "2", "-b:a", "192k", audio_file_path])

video_file = r"The Siege and Investiture of Baron von Frankensteins Castle at Weisseria.webm"
audio_file = r"The Siege and Investiture of Baron von Frankensteins Castle at Weisseria.mp3"

convert_video_to_audio(video_file, audio_file)
yt = pytube.YouTube("https://youtube.com/watch?v=0aOKnEAcYzY")
audio = eyed3.load("The Siege and Investiture of Baron von Frankensteins Castle at Weisseria.mp3")
url = yt.thumbnail_url
resp = requests.get(url)
with open("Cover.jpg", "wb") as f:
    f.write(resp.content)