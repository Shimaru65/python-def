import cv2 as cv
import sys
import os

argLen = len(sys.argv)

assert (argLen == 3), "Invalid amount of arguments!"

fileD = sys.argv[1]

files = []

isD = False

if(os.path.isfile(fileD)):
    files = [fileD]
elif(os.path.isdir(fileD)):
    files = [f for f in os.listdir(fileD) if ((".PNG" in f) or (".png" in f) or (".JPG" in f) or (".jpg" in f) or (".bmp" in f) or (".BMP" in f))]
    isD = True

outD = sys.argv[2]


for f in files:

    fileDir = f
    if(isD):
        fileDir = os.path.join(fileD, f)

    img = cv.imread(fileDir)
    cv.imwrite(os.path.join(outD, f[:-4]+".png"), img)
