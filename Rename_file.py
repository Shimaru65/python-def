import os
import random
import re
import math

def rename(fileDir, prefix, zCount, cont=False):
    
    files = os.listdir(fileDir)
    
    templateF = re.compile(f'{prefix}_{"[0-9]{"+str(zCount)+"}"}')
    templateC = re.compile(f'[0-9]{"{"+str(zCount)+"}"}')
    
    fileName = []
    contC = 0
    if(cont):
        for f in files:
            if(templateF.match(f) is None):
                fileName.append(f)
            else:
                c = templateC.search(f).group(0)
                if(int(c) > contC):
                    contC = int(c)
        
    else:
        fileName = files
    
    for i in range(len(fileName)):
        
        os.rename(os.path.join(fileDir, fileName[i]), os.path.join(fileDir, f"{prefix}_{str.zfill((str(contC+i+1)),zCount)}.png"))

def rename2(fileDir, prefix, zCount, fileDirout):
    files = os.listdir(fileDir)
    fileName = []
    contC = 0
    fileName = files
    for i in range(len(fileName)):
        im1 = Image.open(fileDir+fileName[i])
        im1.save(fileDirout+prefix+'_'+str.zfill((str(contC+i+1)),zCount)+'.png')

from PIL import Image
rename2('good(all)/','Good',4,'good_test/')