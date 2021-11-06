from pathlib import Path

"""
We can use inheritance with polymorphism to simplify the design. 
Each type of file can be represented by a different subclass of AudioFile, 
for example, WavFile and MP3File. Each of these would have a play() method 
that would be implemented differently for each file to ensure that 
the correct extraction procedure is followed. The media player object 
would never need to know which subclass of AudioFile it is referring to; 
it just calls play() and polymorphically lets the object take care 
of the actual details of playing.
"""


class AudioFile:
    ext: str

    def __init__(self, filepath: Path) -> None:
        
        if not filepath.suffix == self.ext:
            raise ValueError("Invalid file format!")
        self.filepath = filepath

    

class MP3File(AudioFile):
    ext = ".mp3"

    def play(self) -> None:
        print(f"playing {self.filepath} as mp3")



class WavFile(AudioFile):
    ext = ".wav"

    def play(self) -> None:
        print(f"playing {self.filepath} as wav")



class OggFile(AudioFile):
    ext = ".ogg"

    def play(self) -> None:
        print(f"playing {self.filepath} as ogg")



p_1 = MP3File(Path("Pink_Floyd-Wish_You_Were_Here.mp3"))
p_1.play()

p_2 = WavFile(Path("Pink_Floyd-Comfortably_Numb.wav"))
p_2.play()

p_3 = OggFile(Path("Pink_Floyd-Money.ogg"))
p_3.play()

# playing Pink_Floyd-Wish_You_Were_Here.mp3 as mp3
# playing Pink_Floyd-Comfortably_Numb.wav as wav
# playing Pink_Floyd-Money.ogg as ogg
