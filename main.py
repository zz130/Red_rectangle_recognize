#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
import cv2
import time
import numpy as np
import math
from rect import minRect
from gate_dec import process
import serial


ser = serial.Serial(
	port = '/dev/ttyUSB0',
	baudrate = 115200,
	parity = serial.PARITY_NONE,
	stopbits = serial.STOPBITS_ONE,
	bytesize = serial.EIGHTBITS,
	timeout = 1
	)
if __name__ == "__main__":
	cap = cv2.VideoCapture(0) #捕获摄像头的帧
	cap.set(3,1280)#设置分辨率
	cap.set(4,720)
	success,frame = cap.read()
	flag_gate = 0;
	Dxy=[0,0];
	num = 0;
	dxy_num = 0
	while success:
		a1 = frame.shape[0];
		b1 = frame.shape[1];
		rect = process(frame)

		if rect is not None:
			flag_gate = 1;
			Dxy[0]=math.atan(2.0*(rect.center[0]-b1/2)*math.tan(35.0*math.pi/180.0)/b1)*180.0/math.pi;
			Dxy[1]=math.atan(-2.0*(rect.center[1]-a1/2)*math.tan(9.0*35.0*math.pi/180.0/16.0)/a1)*180.0/math.pi;
			dxy_num = dxy_num + 1;
			scale = float(rect.length) / b1
			
		else:
			flag_gate = 0;
			Dxy=[0,0];
			dxy_num = dxy_num + 1;
			num = num + 1;
			print("data is 0:{}",num);
		out = [0, 0, 0, 0, 0]
		p = Dxy[0]+90
		q = int(p)
		print(q)
		r = int((p-q)*100)
		s = Dxy[1]+90
		t = int(s)
		u = int((s-t)*100)#print(q)
		out[0] = q
		out[1] = r
		out[2] = t
		out[3] = u
		out[4] = flag_gate
		print(out)
		ser.write(out)
		#out = bytearray(out)
		#print(out)	
		success,frame = cap.read()

		c = cv2.waitKey(2)
		if c & 0xFF == ord('q'):
			break
	cap.release()
	


