#!/usr/bin/env python

'''
Quanta Ryan chen create this for draw the test chart
'''

from __future__ import print_function

import cv2
import numpy as np
import sys
import getopt
    
def resizefun(img):
    try:
        (col, row, channel) =img.shape
    except:
        pass
    
    '''
    try:
        (col, row) =img.shape
    except:
	      pass
    '''
    #    print(img.shape)
    small = cv2.resize(img, (int(row/2), int(col/2)))

    return small

def drawf1f2f3f4(img, h, w, b, f, x, y, divid, pupil_distance):

    if b == 'white':
        color = (255,255,255)
                    
    if b == 'blue':
        color = (255,0,0)
                        
    if b == 'green':
        color = (0,255,0)
                        
    if b == 'red':
        color = (0,0,255)
                        
    if b == 'yellow':
        color = (0,255,255)
        
    if b == 'black':
        color = (0,0,0)

    if f == 'white':
        colorf = (255,255,255)
                    
    if f == 'blue':
        colorf = (255,0,0)
                        
    if f == 'green':
        colorf = (0,255,0)
                        
    if f == 'red':
        colorf = (0,0,255)
                        
    if f == 'yellow':
        colorf = (0,255,255)
        
    if f == 'black':
        colorf = (0,0,0)

    left_half_width = w/2
    half_height = h/2
    half_pupil_distance =  pupil_distance/2
    
    left_x = left_half_width - half_pupil_distance
    left_y = half_height
    
#    left_x, left_y are the left pupil position
    
    print("!!!!!!! left_x:%s !!!!!!!!!!! left_y:%s"%(left_x, left_y))
    graduate_x = divid/2 - 1
    
    graduate_y = divid/2 - 1

    quotient_y = h / divid
    mod = h % divid
        
    if mod % 2 != 0:
        mod = mod - 1
            
    gap_y = mod/2
    print("gap_y:%s" %(gap_y))

    if left_x <= (left_half_width/2):
        print("Okay i can control this now")
        
        quotient_x = (left_x*2) / divid
        mod = (left_x*2) % divid
        
        if mod % 2 != 0:
            mod = mod - 1
            
        gap_x = mod/2
        print("gap_x:%s" %(gap_x))
                
        f13_x1 = quotient_x*graduate_x + gap_x
        f13_x2 = quotient_x*(graduate_x+1) + gap_x
        
        f12_y1 = quotient_y*graduate_y + gap_y
        f12_y2 = quotient_y*(graduate_y+1) + gap_y 
        
        f24_x1 = quotient_x*(graduate_x+2) + gap_x
        f24_x2 = quotient_x*(graduate_x+3) + gap_x
        
        f34_y1 = quotient_y*(graduate_y+2) + gap_y
        f34_y2 = quotient_y*(graduate_y+3) + gap_y
            
    else:
        print("I need more time to implement these !!!!!!!!!!!!!!!!!!!!!")

#draw f1
    cv2.rectangle(img,(f13_x1,f12_y1), (f13_x2,f12_y2), color, -1)
    smallrect_x = (f13_x1+f13_x2)/2 
    smallrect_y = (f12_y1+f12_y2)/2
    cv2.rectangle(img,(smallrect_x-5,smallrect_y-5), (smallrect_x+5,smallrect_y+5), colorf, -1)
    
#draw f2
    cv2.rectangle(img,(f24_x1,f12_y1), (f24_x2,f12_y2), color, -1)
    smallrect_x = (f24_x1+f24_x2)/2 
    smallrect_y = (f12_y1+f12_y2)/2
    cv2.rectangle(img,(smallrect_x-5,smallrect_y-5), (smallrect_x+5,smallrect_y+5), colorf, -1)
    
#draw f3
    cv2.rectangle(img,(f13_x1,f34_y1), (f13_x2,f34_y2), color, -1)
    smallrect_x = (f13_x1+f13_x2)/2 
    smallrect_y = (f34_y1+f34_y2)/2
    cv2.rectangle(img,(smallrect_x-5,smallrect_y-5), (smallrect_x+5,smallrect_y+5), colorf, -1)
    
#draw f4
    cv2.rectangle(img,(f24_x1,f34_y1), (f24_x2,f34_y2), color, -1)
    smallrect_x = (f24_x1+f24_x2)/2 
    smallrect_y = (f34_y1+f34_y2)/2
    cv2.rectangle(img,(smallrect_x-5,smallrect_y-5), (smallrect_x+5,smallrect_y+5), colorf, -1)

    
#draw f5
    cv2.rectangle(img,(f13_x1+(pupil_distance),f12_y1), (f13_x2+(pupil_distance),f12_y2), color, -1)
    smallrect_x = (f13_x1+f13_x2)/2 + pupil_distance
    smallrect_y = (f12_y1+f12_y2)/2
    cv2.rectangle(img,(smallrect_x-5,smallrect_y-5), (smallrect_x+5,smallrect_y+5), colorf, -1)
        
#draw f6
    cv2.rectangle(img,(f24_x1+(pupil_distance),f12_y1), (f24_x2+(pupil_distance),f12_y2), color, -1)
    smallrect_x = (f24_x1+f24_x2)/2 + pupil_distance
    smallrect_y = (f12_y1+f12_y2)/2
    cv2.rectangle(img,(smallrect_x-5,smallrect_y-5), (smallrect_x+5,smallrect_y+5), colorf, -1)    
    
#draw f7
    cv2.rectangle(img,(f13_x1+(pupil_distance),f34_y1), (f13_x2+(pupil_distance),f34_y2), color, -1)
    smallrect_x = (f13_x1+f13_x2)/2 + pupil_distance
    smallrect_y = (f34_y1+f34_y2)/2
    cv2.rectangle(img,(smallrect_x-5,smallrect_y-5), (smallrect_x+5,smallrect_y+5), colorf, -1)
    
#draw f8
    cv2.rectangle(img,(f24_x1+(pupil_distance),f34_y1), (f24_x2+(pupil_distance),f34_y2), color, -1)    
    smallrect_x = (f24_x1+f24_x2)/2 + pupil_distance
    smallrect_y = (f34_y1+f34_y2)/2
    cv2.rectangle(img,(smallrect_x-5,smallrect_y-5), (smallrect_x+5,smallrect_y+5), colorf, -1)    
    
    
#ryan try to checkout the pupil position  
    test_left_x = ((f13_x1+f13_x2)/2 + (f24_x1+f24_x2)/2)/2 
    test_left_y = ((f12_y1+f12_y2)/2 + (f34_y1+f34_y2)/2)/2
    print("test_left_x:%s test_left_y:%s"%(test_left_x, test_left_y))
    
    test_right_x = ((f13_x1+f13_x2+pupil_distance*2)/2 + (f24_x1+f24_x2+pupil_distance*2)/2)/2 
    test_right_y = ((f12_y1+f12_y2)/2 + (f34_y1+f34_y2)/2)/2
    print("test_right_x:%s test_right_y:%s"%(test_right_x, test_right_y))
#ryan try to checkout the pupil position  

    smallf1f2f3f4 = resizefun(img)
    if debug:
        cv2.imshow('f1f2f3f4', smallf1f2f3f4)
    return img 

def readpositionfile(img, h, w, x, y, centerx, centery):
    return 0

def positionfile(img, h, w, x, y, centerx, centery):
    
    string = ''
    gapx = w/x
    gapy = h/y
    
    gapx = gapx+1
    gapy = gapy+1
    
    
    for j in range(int(gapy)):
        if j != 0:
            if j == int(gapy-1):
                continue
            posy = y*j-1 
        else:
#            posy = 0
            continue
        for i in range(int(gapx)):
            if i != 0:
                if i == int(gapx-1):
                    continue
                posx = i*x-1
            else:
#                posx = 0
                continue
            string = string + 'point=' + str(posx+0.5) + ',' + str(posy+0.5) + '\n'

#below is debug circle            
#            cv2.circle(img, (int(posx), int(posy)), 1, (0,0,255), -1)

    return string
                
    

def oridrawchessboard(img, h, w, f, x, y, centerx, centery):
    
    posx = 0
    posy = 0
    posx2 = 0
    posy2 = 0
    color = (255,255,255)
    widthx = w/x
#    heighty = h/(2*y)
    heighty = h/y
    mod = True

#ryan test
#    left_half_width = w/2
#    half_height = h/2
#    half_pupil_distance =  pupil_distance/2
    
#    left_x = left_half_width - half_pupil_distance
#    left_y = half_height
    
#    left_x, left_y are the left pupil position
    
    print("!!!!!!! centerx:%s !!!!!!!!!!! centery:%s"%(centerx, centery))
#ryan test


    print("widthx:%s heighty:%s y:%s"%(widthx, heighty, y))
    
    if f == 'white':
        color = (255,255,255)
                    
    if f == 'blue':
        color = (255,0,0)
                        
    if f == 'green':
        color = (0,255,0)
                        
    if f == 'red':
        color = (0,0,255)
                        
    if f == 'yellow':
        color = (0,255,255)
    
    for i in range(widthx):
        posy = 0
        posy2 = 0
        posx = i*x
        posx2 = posx + (x-1)
#        print("posx:%s posx2:%s"%(posx, posx2))

        if posx2 < (w):
            if(mod):
                for j in range(heighty):
                    posy = j*2*y
                    posy2 = posy + (y-1)
#                    print("posy:%s posy2:%s"%(posy, posy2))
                    if posy2 < (h):
                        cv2.rectangle(img,(posx,posy), (posx2,posy2), color, -1)
                mod = False
            else:
                for j in range(heighty):
                    posy = (j*2*y) + y
                    posy2 = posy + (y-1)
                    print("posy:%s posy2:%s"%(posy, posy2))
                    if posy2 < (h):
                        cv2.rectangle(img,(posx,posy), (posx2,posy2), color, -1)
                mod = True
                 
#    smallrect = resizefun(img)
#    cv2.imshow('smallrect', smallrect)
    return img


def drawcross(img, center, length, color=(0,0,255)):
    (x,y) = center  
    point1 = (x-length, y)
    point2 = (x+length, y)
    point3 = (x, y-length)
    point4 = (x, y+length)
    cv2.line(img,point1,point2,color,1)
    cv2.line(img,point3,point4,color,1)

#ryan test new

def rotateandscaleimg(img, path, h, w, f, x, y, centerx, centery, centerx2,
                      centery2, scale = 1, savestandard = False):

    position_filepath = path.replace('.png','.txt')
    
    f = open(position_filepath, 'r')
    string = f.read()
    f.closed

       
    color = (255,255,255)

    standardimg = cv2.imread(path)
    standardimg = cv2.resize( standardimg, (0, 0), fx=scale, fy=scale)
    
    try:
        (col, row, channel) =standardimg.shape
    except:
        pass
        
    std_center_x = row/2
    std_center_y = col/2
    
    alignment_x =  centerx - std_center_x
    alignment_y =  centery - std_center_y    
    img[alignment_y:alignment_y+col, alignment_x:alignment_x+row] = standardimg[:,:]
  
        
    print("std_center_x:%s std_center_y:%s"%(std_center_x, std_center_y))

#ryan try to write the position file 
    fileoutstring = ''
    substring = string.split('\n')
    temp = 'point='
    for sub in substring:
        print("sub:%s"%(sub))
        index = sub.find(temp)
        if index != -1:
            pos = sub[index+len(temp):]
            pos = pos.split(',')
            posx = float(pos[0])+float(alignment_x)
            posy = float(pos[1])+float(alignment_y)
#below is debug circle
#            cv2.circle(img, (int(posx), int(posy)), 1, (0,0,255), -1)
            
            fileoutstring = fileoutstring + 'point=' + str(posx) + ',' + str(posy) + ',' + '0' +'\n'
            
    print("fileoutstring:%s"%(fileoutstring))
#ryan try to write the position file 
 
  
    if centerx2 != 0 and centery2 != 0:
        alignment_x =  centerx2 - std_center_x
        alignment_y =  centery2 - std_center_y    
        img[alignment_y:alignment_y+col, alignment_x:alignment_x+row] = standardimg[:,:]
        drawcross(img, (centerx2, centery2), 10, color=(0,0,255))
        
    if savestandard:
        cv2.imwrite('./scale_standard.png', standardimg)


 
    print("centerx:%s centery:%s"%(centerx, centery))
    print("centerx2:%s centery2:%s"%(centerx2, centery2))

   
    drawcross(img, (centerx, centery), 10, color=(0,0,255))
                     
    smallrotateandscaleimg = resizefun(img)
    cv2.imshow('smallrotateandscaleimg', smallrotateandscaleimg)
    cv2.imshow('standardimg', standardimg)
    return img, fileoutstring
#ryan test new


def drawchessboard(img, h, w, f, x, y, centerx, centery, centerx2 = 1, centery2 = 1):

    posx = 0
    posy = 0
    posx2 = 0
    posy2 = 0
    color = (255,255,255)
    mod = True


#ryan test
    if centerx2 != 0 and centery2 != 0:
        left_half_width = w/2
    else:
        left_half_width = w
    print("!!!!!!! centerx:%s !!!!!!!!!!! centery:%s"%(centerx, centery))
    print("!!!!!!! centerx2:%s !!!!!!!!!!! centery2:%s"%(centerx2, centery2))
#ryan test


#    widthx = left_half_width/x
    heighty = h/(2*y)
  
    print("!!!!!!! centerx:%s !!!!!!!!!!! centery:%s"%(centerx, centery))
    print("!!!!!!! centerx2:%s !!!!!!!!!!! centery2:%s"%(centerx2, centery2))
    

 
#ryan new test
    mod = h % y
        
    if mod % 2 != 0:
        mod = mod - 1
            
    gap_y = mod/2
    print("gap_y:%s" %(gap_y))

    if centerx <= (left_half_width/2):
        print("Okay i can control this now")
        widthx = (centerx*2) / x
        mod = (centerx*2) % x
        
        if mod % 2 != 0:
            mod = mod - 1
            
        gap_x = mod/2
        print("gap_x:%s" %(gap_x))
        
    print("widthx:%s heighty:%s y:%s"%(widthx, heighty, y))
#ryan new test 
    
    drawcross(img, (centerx, centery), 10, color=(0,0,255))
    
    if f == 'white':
        color = (255,255,255)
                    
    if f == 'blue':
        color = (255,0,0)
                        
    if f == 'green':
        color = (0,255,0)
                        
    if f == 'red':
        color = (0,0,255)
                        
    if f == 'yellow':
        color = (0,255,255)
    
    for i in range(widthx):
        posy = 0
        posy2 = 0
        posx = i*x + gap_x
        posx2 = posx + (x-1)
#        print("posx:%s posx2:%s"%(posx, posx2))

        if posx2 < (w):
            if(mod):
                for j in range(heighty):
                    posy = j*2*y + gap_y
                    posy2 = posy + (y-1)
#                    print("posy:%s posy2:%s"%(posy, posy2))
                    if posy2 < (h):
                        cv2.rectangle(img,(posx,posy), (posx2,posy2), color, -1)
                mod = False
            else:
                for j in range(heighty):
                    posy = (j*2*y) + y + gap_y
                    posy2 = posy + (y-1)
#                    print("posy:%s posy2:%s"%(posy, posy2))
                    if posy2 < (h):
                        cv2.rectangle(img,(posx,posy), (posx2,posy2), color, -1)
                mod = True
                 
#    smallrect = resizefun(img)
#    cv2.imshow('smallrect', smallrect)
    return img

def createbaseimg(h, w, b, f, x, y, path, centerx, centery, centerx2, centery2, chessboardonly):
    string = ''
    baseimg = np.zeros((int(h), int(w), 3), np.uint8)
    print("111 w:%s h:%s"%(w, h))
    
    if b == 'white':
        print("b white")
        baseimg[baseimg == 0] = 255
    
    if b == 'blue':
        baseimg[:,:] = (255,0,0)
        
    if b == 'green':
        baseimg[:,:] = (0,255,0)
        
    if b == 'red':
        baseimg[:,:] = (0,0,255)
        
    if b == 'yellow':
        baseimg[:,:] = (0,255,255)

    if chessboardonly == 0:
#        drawchessboard(baseimg, h, w, f, x, y, centerx, centery)
#        rotateandscaleimg(baseimg, path, h, w, f, x, y, centerx, centery, scale = 4.0, savestandard = True)
        _,string = rotateandscaleimg(baseimg, path, h, w, f, x, y, centerx, centery, centerx2, centery2)
    else:
        oridrawchessboard(baseimg, h, w, f, x, y, centerx, centery)
        string = positionfile(baseimg, h, w, x, y, centerx, centery)
        
    h, w = baseimg.shape[:2]
    print("222 w:%s h:%s"%(w, h))
     
    smallbaseimg = resizefun(baseimg)
    if debug:
        cv2.imshow('baseimg', smallbaseimg)
    return baseimg, string

if __name__ == '__main__':

    '''
    width: image width
    height: image height
    background: background color
    foreground: foreground color
    pixelsx: each rectangle x pixels
    pixelsy: each rectangle y pixels
    divide_into: divid ?? into the image , it decides the f1 f2 f3 f4 positions
    pupil_distance: pupil distance in the image
    '''

#    standardpath = './standard_w_70_h_40_b_black_f_green_x_10_y_10_test_chart.png'
#    standardpath = './standard_w_700_h_600_b_black_f_green_x_100_y_100_test_chart.png'
    standardpath = './standard_w_700_h_600_b_black_f_green_x_100_y_100_test_chart.png'
    
    debug = True
    
    args, img_mask = (getopt.getopt(sys.argv[1:], 'w:h:b:f:p:d:x:y:i:j:c:', ['width=', 'height=', 'background=', 'foreground=',
     'pixel=', 'pupil_distance=', 'centerx=', 'centery=', 'centerx2=', 'centery2=','chessboardonly=']))
     
    args = dict(args)
    
    print("img_mask:%s"%(img_mask))
    print("args:%s"%(args))
    args.setdefault('-w', '1920')
    args.setdefault('-h', '1080')
    args.setdefault('-b', 'black')
    args.setdefault('-f', 'white')
    args.setdefault('-p', '10')
    args.setdefault('-c', '0')
    
    args.setdefault('-i', '0')
    args.setdefault('-j', '0')    
    
    print("img_mask:%s"%(img_mask))
    print("args:%s"%(args))
    w = int(args.get('-w'))
    h = int(args.get('-h'))
    b = args.get('-b')
    f = args.get('-f')
    chessboardonly = int(args.get('-c'))
        
    side_length_x = int(args.get('-p'))
    side_length_y = side_length_x
 
    args.setdefault('-x', w/2)
    args.setdefault('-y', h/2)   
    
    centerx = int(args.get('-x'))
    centery = int(args.get('-y'))
    
    centerx2 = int(args.get('-i'))
    centery2 = int(args.get('-j'))

    print("centerx2:%s centery2:%s"%(centerx2, centery2))
        
    baseimg, string = createbaseimg(h, w, b, f, side_length_x, side_length_y, standardpath,centerx, centery, centerx2, centery2, chessboardonly)

    if chessboardonly == 0:
        filename = ("./calbration_w_" + str(w) + "_h_" + str(h) + "_b_" + b + "_f_" + f + "_x_" + str(centerx) +
         "_y_" + str(centery) + "_x2_" + str(centerx2) + "_y2_" + str(centery2) + "_test_chart.png")
         
        txtname = ("./calbration_w_" + str(w) + "_h_" + str(h) + "_b_" + b + "_f_" + f + "_x_" + str(centerx) +
         "_y_" + str(centery) + "_x2_" + str(centerx2) + "_y2_" + str(centery2) + "_test_chart.txt")
    else:
        filename = ("./standard_w_" + str(w) + "_h_" + str(h) + "_b_" + b + "_f_" + f + "_x_" + str(side_length_x) +
         "_y_" + str(side_length_y) + "_test_chart.png")
         
        txtname = ("./standard_w_" + str(w) + "_h_" + str(h) + "_b_" + b + "_f_" + f + "_x_" + str(side_length_x) +
         "_y_" + str(side_length_y) + "_test_chart.txt")
              
    print("filename:%s"%(filename))
    cv2.imwrite(filename, baseimg)

    file = open(txtname, 'w')
    file.write(string)
    file.closed  

    if debug:
        while True:
            ch = cv2.waitKey(2) & 0xFF
            if ch == 27:
                break
        
    cv2.destroyAllWindows() 
     

    