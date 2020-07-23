import os
import numpy as np
import cv2
from matplotlib import pyplot as plt
import json

def loadArrayFromFile(inrange=10):
    #arr=[]
    all_arr=[]
    maxxy=[]
    minxy=[]
    for i in range(inrange):
        with open(f"temp/Ring_{i}.txt",'r') as f:
            content=f.read()
            #arr=json.dumps(content)
            a=json.loads(content)
            #print(a)
            arr=np.array(a)
            #print(np.shape(arr))

            maxInColumns = np.amax(arr,axis=0)
            minInColumns = np.amin(arr,axis=0)

            maxxy.append(maxInColumns)
            minxy.append(minInColumns)

            all_arr.append(arr)
    all_arr=np.array(all_arr)
    #print(np.shape(all_arr))
    print(maxxy,minxy)
    maxInColumns = np.amax(maxxy,axis=0)
    minInColumns = np.amin(minxy,axis=0)
    #print(maxInColumns,minInColumns)
    discol = maxInColumns[0]-minInColumns[0]
    disrow = maxInColumns[1]-minInColumns[1]
    print(maxInColumns,minInColumns,discol,disrow)

    imgarr=[]
    img_h,img_w=760,1024
    wratio=img_w/discol
    hratio=img_h/disrow
    for iarr in all_arr:
        tarr=[]
        for item in iarr:
            x=(item[0]-minInColumns[0])*wratio
            y=(item[1]-minInColumns[1])*hratio
            tarr.append([x,y])
        tarr=np.array(tarr).astype(int)
        imgarr.append(tarr)
    #imgarr=np.array(imgarr,dtype=np.uint8)
    #print(imgarr[0])
    return imgarr

def LoadVoronoi():
    with open(f"temp/voronoiori.txt",'r') as f:
            content=f.read()
            a=json.loads(content)
            arr=np.array(a)
    return
def ContorImage(contours):
    #the first one is the largest
    img_h,img_w=760,1024
    background=np.zeros(shape=[img_h,img_w,3],dtype=np.uint8)
    #imgcountor=cv2.drawContours(background, contours, -1, (0,255,0), 1)
    #imgcountor=cv2.fillPoly(background, pts =[contours[0]], color=(255,255,255))
    #cv2.imshow("image", imgcountor)
    colorindex=1
    for item in contours:
        colorweigth=colorindex*20
        background=cv2.fillPoly(background, pts =[item], color=(0,colorweigth,0))
        colorindex+=1
    cv2.imshow("image", background)
    cv2.waitKey()

    return
if __name__ == '__main__':
    imgarr=loadArrayFromFile(10)
    ContorImage(imgarr)
