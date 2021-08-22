import os
import glob



def rename2x():
    """Add @2x to end of png file name."""
    for files in glob.glob("*.png"):
        os.rename(files, files.replace(".png", "@2x") + ".png")



if __name__ == "__main__":
    # Place the png files you want to rename in same
    # folder as this script file and run it.
    os.chdir(os.path.dirname(os.path.abspath(__file__)))
    rename2x()
