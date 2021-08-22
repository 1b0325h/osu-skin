import os
import glob
import shutil

from PIL import Image



def build():
    def _name():
        with open("../skin.ini", encoding="utf_8") as f:
            for i in f.read().splitlines():
                if i[:5] == "Name:":
                    return i.lstrip("Name: ")
            else:
                return "No_title"

    def _ignore():
        with open("../export/ignore.txt", encoding="utf_8") as f:
            return f.read().splitlines()

    def _copy(path, name):
        for i in glob.glob(path):
            shutil.copy(i, name)

    name = _name()
    ignore = _ignore()

    os.mkdir(name)
    shutil.copy("../skin.ini", name)

    img = Image.new("RGBA", (1, 1), (0, 0, 0, 0))
    for i in ignore:
        img.save(f"{name}/{i}")

    for path in ["../export/**/*.[pj][np]g", "../sound/*.[wm][ap][v3]"]:
        _copy(path, name)



if __name__ == "__main__":
    os.chdir(os.path.dirname(os.path.abspath(__file__)))
    build()
