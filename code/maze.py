import cv2
import numpy as np
#open image 
image_array = np.array(cv2.imread("maze.png"))
#specifying the starting position colour and target colour 
black=([0,0,0])
red=([0,0,255])
def find_position(colour):
	xposition=1
	yposition=1
	for y in image_array:
		for x in y:
			if (x==colour).all():
				#if mod results into 0 then we are at 8th postion on x axis
				if xposition%8==0:
					gridX=8
				else:
					gridX=xposition%8
				print(x,gridX,yposition)
				return gridX, yposition
			xposition+=1
		yposition+=1
#specified starting point, current point, target point
StartX,StartY = find_position(black)
TargetX,TargetY = find_position(red)
CurrentX,CurrentY = StartX,StartY
def manhatten_distance(StartX,StartY,CurrentX,CurrentY,TargetX,TargetY):
	G_cost = abs(StartX-CurrentX)+abs(StartY-CurrentY)
	H_cost = abs(CurrentX-TargetX)+abs(CurrentY-TargetY)
	F_cost = G_cost+H_cost
	return F_cost
def check_neighbours(StartX,StartY,CurrentX,CurrentY,TargetX,TargetY):
	p1 =[CurrentX-1,CurrentY-1]
	p2 =[CurrentX, CurrentY-1]
	p3 =[CurrentX+1,CurrentX-1]
	p4 =[CurrentX-1,CurrentY]
	p5 =[CurrentX+1,CurrentY]
	p6 =[CurrentX-1,CurrentY+1]
	p7 =[CurrentX,CurrentY+1]
	p8 =[CurrentX+1,CurrentY+1]
	Fcost=manhatten_distance(StartX,StartY,p1[0],p1[1],TargetX,TargetY)
	new_current=[p1[0],p1[1]]
	Fcost1 =manhatten_distance(StartX,StartY,p2[0],p2[1],TargetX,TargetY)
	if Fcost1<=Fcost:
		new_current=[p2[0],p2[1]]
		Fcost=Fcost1
	Fcost1 =manhatten_distance(StartX,StartY,p3[0],p3[1],TargetX,TargetY)
	if Fcost1<=Fcost:
		new_current=[p3[0],p3[1]]
		Fcost=Fcost1
	Fcost1 =manhatten_distance(StartX,StartY,p4[0],p4[1],TargetX,TargetY)
	if Fcost1<=Fcost:
		new_current=[p4[0],p4[1]]
		Fcost=Fcost1
	Fcost1 =manhatten_distance(StartX,StartY,p5[0],p5[1],TargetX,TargetY)
	if Fcost1<=Fcost:
		new_current=[p5[0],p5[1]]
		Fcost=Fcost1
	Fcost1 =manhatten_distance(StartX,StartY,p6[0],p6[1],TargetX,TargetY)
	if Fcost1<=Fcost:
		new_current=[p6[0],p6[1]]
		Fcost=Fcost1
	Fcost1 =manhatten_distance(StartX,StartY,p7[0],p7[1],TargetX,TargetY)
	if Fcost1<=Fcost:
		new_current=[p7[0],p7[1]]
		Fcost=Fcost1
	Fcost1 =manhatten_distance(StartX,StartY,p8[0],p8[1],TargetX,TargetY)
	if Fcost1<=Fcost:
		new_current=[p8[0],p8[1]]
		Fcost=Fcost1
	return new_current[0],new_current[1]
#inserting visited node into a path 
path1=[]
path1.insert(0,[CurrentX,CurrentY])
print(CurrentX,CurrentY)
print(TargetX,TargetY)
while CurrentX!=TargetX or CurrentY!=TargetY:
	CurrentX,CurrentY = check_neighbours(StartX,StartY,CurrentX,CurrentY,TargetX,TargetY)
	print(StartX,StartY,CurrentX,CurrentY,TargetX,TargetY)
	path1.insert(0,[CurrentX,CurrentY])
print(path1)
length=len(path1)
for pixel in range(1,length-1):
	image_array[path1[pixel][1]-1,path1[pixel][0]-1]=(0,255,0)
cv2.imwrite("wow.png",image_array)