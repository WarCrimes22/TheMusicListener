import pytube, webbrowser
from pathlib import Path
from mutagen.mp3 import MP3
from mutagen.id3 import ID3, APIC, TPE1, TIT2
import subprocess, requests, os


#A very hideous way of making sure the title is file-friendly.
def spring_cleaning(wantname):
    wantname = wantname.replace("'", "")
    wantname = wantname.replace(":", "")
    wantname = wantname.replace("<", "")
    wantname = wantname.replace(">", "")
    wantname = wantname.replace("/", "")
    wantname = wantname.replace("\\", "")
    wantname = wantname.replace("|", "")
    wantname = wantname.replace('"', "")
    wantname = wantname.replace("?", "")
    wantname = wantname.replace("*", "")
    return wantname
def convert_video_to_audio(video_file_path, audio_file_path):
    subprocess.run(
        ["ffmpeg", "-i", video_file_path, "-vn", "-ar", "44100", "-ac", "2", "-b:a", "192k", audio_file_path])
def setcovertothefile(filename, author, title):
    audio = MP3(filename, ID3=ID3)
    audio.tags.add(
        APIC(
            encoding=3,
            mime="image/jpeg",
            type=3,
            desc='Cover',
            data=open("Cover.jpg", mode='rb').read()
        )
    )
    audio.tags.add(TPE1(encoding=3, text=author))  # TPE1 is for artist/author
    audio.tags.add(TIT2(encoding=3, text=title))
    audio.save()
print("Witaj w programie The Listener... Co pragniesz dzisiaj pobrać?")
name = input("Podaj nazwę utworu, który pragniesz pobrać...\n(For best results, please use the band name as well): ")
s = pytube.Search(name)
i = 0
directory = Path(r"C:\Users\student\PycharmProjects\server")
#Szukanie utworu na YT
while 1:
    idszuk = str(s.results[i])
    idszuk = idszuk.removeprefix("<pytube.__main__.YouTube object: videoId=")
    idszuk = idszuk.removesuffix(">")
    webbrowser.open("https://www.youtube.com/watch?v=" + idszuk)
    czytoszuk = input("Czy to jest to czego szukasz? Y/N/Wpisz liczbę do której chcesz wrócić.  ")
    try:
        if czytoszuk.lower() == "y":
            chciana = pytube.YouTube("https://www.youtube.com/watch?v=" + idszuk)
            wantname = chciana.title
            wantname = spring_cleaning(wantname)
            break
        elif czytoszuk.lower() == "n":
            i = i + 1
        else:
            i = int(czytoszuk)
    except ValueError:
        czytoszuk = input("Podaj liczbę lub Y/N, tutaj: ")
tytul = str(chciana.title)
    # Kontynuuacja procesu pobierania
ifwanttodown = input("Po znalezieniu żądanego utworu, czy pragniesz go pobrać? Y/N ")
if ifwanttodown.lower() == "y":
    #downloads the wanted song
    chciana.streams.get_by_itag(251).download()
    #preparation to change the extension
    webmfile = wantname + ".webm"
    mp3file = wantname + ".mp3"
    #prep complete, moving to conversion
    convert_video_to_audio(webmfile, mp3file)
    os.remove(webmfile)
    #prep to downloading cover based on the youTube thumbnail
    url = chciana.thumbnail_url
    cover = requests.get(url)
    with open("Cover.jpg", "wb") as f:
        f.write(cover.content)
    #with the cover downloaded, we can put it into the thing, eh?
    setcovertothefile(mp3file, chciana.title, chciana.author)
    os.remove("Cover.jpg")
    ifwanttosee = input("Czy chesz pobrać samą muzykę? Sama/Dodatek ")
    if ifwanttosee.lower() == "sama":
        print("Thank you for using the program. We threw in the album cover, as a lil' treat.")
    #elif ifwanttosee.lower() == "dodatek":



