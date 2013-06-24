import os
import glob
import sys


for path in glob.iglob("css/*.css"):
    sys.stdout.write(os.path.abspath(path) + " ")
