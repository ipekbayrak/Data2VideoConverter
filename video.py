import cv2
import numpy as np
import glob

#bin(int('A', base=16))[2:].zfill(8)

img_array = []
#for filename in glob.glob('C:/New folder/Images/*.jpg'):
#cv2.imread(filename)

#854x480

height = 854
width = 480

images = list()



countX = 853
countY = 479

ylist = list()
heightCount = 0

while heightCount*8 <= height-8:
    ylist.append( 8*heightCount )
    heightCount += 1

def dataToimage(binaryfile,blank_image):
    for y in ylist:
        for x in list(range(0,width)):
            chunk = binaryfile.read(1)
            if not chunk:
                break
            val = int.from_bytes(chunk,byteorder='big') #int(chunk.hex(),16)  
            c = bin(val)[2:].zfill(8)
            #print (chunk)
            #print (c)
            for i in list(range(0,8)):
                value = c[i]
                if value == '1':
                    blank_image[x,y+i] = (255,255,255)
                else:
                    blank_image[x,y+i] = (0,0,0)
                
    return blank_image
                
                
with open("openh264-1.8.0-win64.dll", "rb") as binaryfile : #32760 byte
    while True:
        #blank_image = np.zeros((width,height,3), np.uint8)
        blank_image = np.zeros((width,height,3), np.uint8)
        img = dataToimage(binaryfile, blank_image)
        gray = np.zeros((width,height,3), np.uint8)
        gray[0:840,0:854] = 128, 128, 128
        white = np.zeros((width,height,3), np.uint8)
        white[0:840,0:854] = 255, 255, 255
        images.append(blank_image)
        images.append(gray)
        images.append(white)
        chunk = binaryfile.read(1)
        if not chunk:
            break

        
readImages = list()
        
img = blank_image
height, width, layers = img.shape
size = (width,height)
img_array.append(img)
img_array = images
out = cv2.VideoWriter('project.mp4',cv2.VideoWriter_fourcc(*'H264'), 3, size)
 
for i in range(len(img_array)):
    out.write(img_array[i])
out.release()


vidcap = cv2.VideoCapture('project.mp4')
success,image = vidcap.read()
count = 0
success = True
while success:
    readImages.append(image)
    cv2.imwrite("project000.jpg", image)    
    success,image = vidcap.read()
    print ('Read a new frame: ', success)
    count += 1
  
print()

i = 0
bits = ''
print(len(readImages))
with open('openh264-1.8.0-win64.dll_', 'wb') as f2: 
    for image in readImages:
        if ( (i % 3) == 0):
            i += 1
            print ("yaz")
            for w in ylist:
                for x in list(range(0,height)):
                    for y in list(range(w+0,w+8)):
                        a,b,c = image[x,y] 
                        if b > 128:
                            bits += '1'
                        else:
                            bits += '0'
                        #print (bits)
                    deger = int(bits, 2)
                    by = bytes((deger,))
                    #if b'\x00' in by:
                    #    bits = ''
                    #    continue
                    f2.write(by)
                    #print (bytes((deger,)))
                    bits = ''                
        else:
            i += 1
            continue


        
