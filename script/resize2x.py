import os
import glob

from PIL import Image



def resize2x():
    """Resize of the @2x png file to half its original size and rename file."""
    for files in glob.glob("*@2x.png"):
        img = Image.open(files)
        halve = img.resize((int(img.width * 0.5), int(img.height * 0.5)))
        halve.save(files.replace("@2x.png", "") + ".png")



if __name__ == "__main__":
    # Place the png files you want to resize in same
    # folder as this script file and run it.
    os.chdir(os.path.dirname(os.path.abspath(__file__)))
    resize2x()
