#!/usr/bin/env python3        
# -*- coding: utf-8 -*- 
import cv2

img=cv2.imread("5.png")  
gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)  
gray=cv2.GaussianBlur(gray, (3, 3), 0)  
gray=cv2.Canny(gray,100,300)  
ret, binary = cv2.threshold(gray,127,255,cv2.THRESH_BINARY)  
binary,contours,hierarchy= cv2.findContours(binary,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)  
cv2.drawContours(img,contours,-1,(0,0,255),3)  
cv2.imshow("0",binary)  
cv2.imshow("win10",img)  

for i in range(1,len(contours)):
	point = []
	for item in contours[i]:
		point.append(item[0])
	index = []
	arrStr = 'a'+ str(i) +'=['
	for i in range(0, len(point)):  
	   	if i % 2 == 0:
	   		arrStr += '['+ str(point[i][0]) + ','+ str(point[i][1]) + '],'
	arrStr += ']' + '\r\n\n'
	fo = open("demo.txt", "a")
	fo.write(arrStr)
	fo.close()

cv2.waitKey()
cv2.destroyAllWindows()