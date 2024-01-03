from mutagen.mp3 import MP3
from mutagen.id3 import ID3, APIC, error

audio = MP3('The Siege and Investiture of Baron von Frankensteins Castle at Weisseria.mp3', ID3=ID3)
try:
    audio.add_tags()
except error:
    print("FUCK")
audio.tags.add(
    APIC(
        encoding=3,  # 3 is for utf-8
        mime="image/jpeg",  # can be image/jpeg or image/png
        type=3,  # 3 is for the cover image
        desc='Cover',
        data=open("Cover.jpg", mode='rb').read()
    )
)
audio.save()