import cv2
import numpy as np
import glob

height = 854
width = 480

images = list()


ylist = list()
heightCount = 0

while heightCount*8 <= height-8:
    ylist.append( 8*heightCount )
    heightCount += 1



readImages = list()

video = cv2.VideoCapture('videoplayback.mp4')
success,image = video.read()
count = 0
success = True
while success:
    readImages.append(image)
    #cv2.imwrite("project.jpg", image)    
    success,image = video.read()
    print ('Read a new frame: ', success)
    count += 1
 
 
bits = ''
print(len(readImages))
with open('sonuc.txt', 'wb') as f2: 
    for image in readImages:
        for w in ylist:
            for x in list(range(0,width)):
                for y in list(range(w+0,w+8)):
                    val,b,c = image[x,y] 
                    if val > 128:
                        bits += '1'
                    else:
                        bits += '0'
                    #print (bits)
                deger = int(bits, 2)
                f2.write(bytes((deger,)))
                #print (bytes((deger,)))
                bits = ''
