import pytube, webbrowser
from pathlib import Path
class MusicFile():
    def __init__(self,pathfile, name, artist, album, year, duration, image, favour):
        self.pathfile = pathfile
        self.name = name
        self.artist = artist
        self.album = album
        self.year = year
        self.duration = duration
        self.image = image
        self.favour = favour



print("Witaj w programie The Listener... Co pragniesz dzisiaj pobrać?")
name = input("Podaj nazwę utworu, który pragniesz pobrać...\n(For best results, please use the band name as well): ")
s = pytube.Search(name)
i = 0
directory = Path(r"C:\Users\psuch\PycharmProjects\pythonProject\TheMusicListener")
    # Szukanie utworu na YT
while 1:
    idszuk = str(s.results[i])
    idszuk = idszuk.removeprefix("<pytube.__main__.YouTube object: videoId=")
    idszuk = idszuk.removesuffix(">")
    webbrowser.open("https://www.youtube.com/watch?v=" + idszuk)
    czytoszuk = input("Czy to jest to czego szukasz? Y/N/Wpisz liczbę do której chcesz wrócić.  ")
    try:
        if czytoszuk.lower() == "y":
            chciana = pytube.YouTube("https://www.youtube.com/watch?v=" + idszuk)
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
    ifwanttosee = input("Czy chesz pobrać samą muzykę? Czy także wyszukać i obraz? Sama/Dodatek ")
    if ifwanttosee.lower() == "sama":
        chciana.streams.get_by_itag(251).download()
    #TODO DODATEK, MY N;WAH

plik = tytul + ".webm"
plik = plik.replace("'", "")
file_path = next(directory.rglob(plik), None)
new_file_path = file_path.replace(file_path.with_suffix(".mp3"))
