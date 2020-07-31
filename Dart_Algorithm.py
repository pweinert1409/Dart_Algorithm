# Author: Samuel Lamb
# Camera Dimensions : 1280 x 720 (720p HD)

import math
import time

import cv2
import imutils
from skimage.metrics import structural_similarity


##########################################################################################################################################
# Starts to capture the video feed from the camera, also initialized some key variables that need to be present outside of the main loop #
##########################################################################################################################################
cap = cv2.VideoCapture(0)
finalScore = 301
img_count = 1
Cache = 0
largeArea = 0
boxCount = 0
Points2 = 0
#############################################################
# Function to return an integer score given x-y coordinates # 
#############################################################

def Score(x,y):
	# ################################################################################################################################## xNew and yNew will be the central point of the image, allowing for us to center the camera and view the dart board as a circle. # ##################################################################################################################################
	xNew = x - 640/2
	yNew = y - 480/2
	# print ("X,Y              : ",xNew,",",yNew)

	######################
	# Calculating radius #
	######################

	xyInterim = (xNew ** 2) + (yNew ** 2)
	R = math.sqrt(xyInterim)
	# print ("Radius           : ",R)
	Theta = -1 * math.atan2(yNew,xNew)
	# print ("Theta in Radians : ",Theta)
	Theta =  math.degrees(Theta)
	# print ("Theta in Degrees : ",Theta)


	#####################################################################################################################
	# The inner and outer bullseye are straight distances from the center of the circle, regardless of the theta value. # 
	#####################################################################################################################

	# Inner Bullseye
	if (R <= 10):
		Points = 50
		return Points

	# Outer Bullseye
	if (10 < R <= 20):
		Points = 25
		return Points

	#################################################################################################################################################################################################
	# For each point segment of the dart board there is a theta correlation. By assigning the correct point values to the angle range you can get a point value baased on the x-y coordinates given # 
	#################################################################################################################################################################################################

	if (-9 < Theta <= 9):
		# 6 point region
		Points = 6

	if (9 < Theta <= 27):
		# 13 point region
		Points = 13

	if (27 < Theta <= 45):
		# 4 point region
		Points = 4

	if (45 < Theta <= 63):
		# 18 point region
		Points = 18

	if (63 < Theta <= 81):
		# 1 point region
		Points = 1

	if (81 < Theta <= 99):
		# 20 point region
		Points = 20

	if (99 < Theta <= 117):
		# 5 point region
		Points = 5

	if (117 < Theta <= 135):
		# 12 point region
		Points = 12

	if (135 < Theta <= 153):
		# 9 point region
		Points = 9

	if (153 < Theta <= 171):
		# 14 point region
		Points = 14

	if (171 < Theta or Theta < -171):
		# 11 point region
		Points = 11

	if (-171 < Theta <= -153):
		# 8 point region
		Points = 8

	if (-153 < Theta <= -135):
		# 16 point region
		Points = 16

	if (-135 < Theta <= -117):
		# 7 point region
		Points = 7

	if (-117 < Theta <= -99):
		# 19 point region
		Points = 19
		
	if (-99 < Theta <= -81):
		# 3 point region
		Points = 3

	if (-81 < Theta <= -63):
		# 17 point region
		Points = 17

	if (-63 < Theta <= -45):
		# 2 point region
		Points = 2

	if (-45 < Theta <= -27):
		# 15 point region
		Points = 15

	if (-27 < Theta <= -9):
		# 10 point region
		Points = 10

while (img_count < 15):

	##############################################
	# Pause for 5 seconds between image captures #
	##############################################
	# time.sleep(5)

	###################################################
	# Capture the current frame and save it as a file #
	###################################################
	ret, frame = cap.read()
	# ret is a boolean variable that returns true if the frame is available.
	# frame is an image array vector captured based on the default frames per second defined explicitly or implicitly
	img_name = "Dart_Image_{}.png".format(img_count)
	cv2.imwrite(img_name, frame)
	print("{} written!".format(img_name))

	#####################################################################################
	# Add to count after taking capture, if 13 images are seen then reset to save space #
	#####################################################################################
	img_count += 1
	if (img_count == 14):
		print("Reset!")
		img_count = 1
	
	################################################################
	# Load in images, convert to grayscale, and get the difference #
	################################################################

	path1 = r'/home/pi/PycharmProjects/Dart_Algorithm/Dart_Image_0.png'
	imageA = cv2.imread(path1)
	imageB = cv2.imread("Dart_Image_{}.png".format(img_count-1))


	grayA = cv2.cvtColor(imageA, cv2.COLOR_BGR2GRAY)
	grayB = cv2.cvtColor(imageB, cv2.COLOR_BGR2GRAY)

	(score, diff) = structural_similarity(grayA, grayB, full=True)
	diff = (diff * 255).astype("uint8")
	print("SSIM: {}".format(score))

	

	thresh = cv2.adaptiveThreshold(diff, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY_INV,11,30)
	cnts = cv2.findContours(thresh.copy(), cv2.RETR_EXTERNAL,  cv2.CHAIN_APPROX_SIMPLE)
	cnts = imutils.grab_contours(cnts)
	cv2.imwrite("Thresh_{}.png".format(img_count-1), thresh)
	##############################################################################################################################
	# Takes the difference images and creates a box around the difference. This is used to calculate the central point and score # 
	##############################################################################################################################

	for c in cnts:
		(x, y, w, h) = cv2.boundingRect(c)
		
		xNew = x + w/2 - 640/2
		yNew = y + h/2 - 480/2
		xyInterim = (xNew ** 2) + (yNew ** 2)
		R = math.sqrt(xyInterim)

		if (R > 155): #155
			area = 0
			# print("Gottem")
		else:
			area = w * h
		if (area > largeArea): 
			largeArea = area
			xcoord = x + w/2
			ycoord = y + h/2
		cv2.rectangle(imageA, (x, y), (x + w, y + h), (0, 0, 255), 2)
		cv2.rectangle(imageB, (x, y), (x + w, y + h), (0, 0, 255), 2)
	cv2.imwrite("ImageBoxes_{}.png".format(img_count-1), imageB)
	cv2.imwrite("Result_{}.png".format(img_count-1), diff)
	Points = Score (xcoord,ycoord)
	if (Cache > 4):
		if (Points == Points2):
			Points = 0
		if (Points != 0):
			Points2 = Points	

	# newPoints = (Points,img_count)
	# print(newPoints)
	# If points == points (new) & img_count != img_count (new) then points = 0
	boxCount = 0
	area = 0

	####################################################
	# Gives the camera a chance to "warm up" and focus #
	####################################################
	if (Cache < 5):
		print("Clearing cache, please wait")
	else:
		#####################################################################################################
		# If images are too similar then don't count the difference as a score. Helps mitigate interference #
		#####################################################################################################
		if (score > 0.98 or Points == 0):
			print("New hit not registered")
		else:
			print("You scored            : ",Points)
			finalScore = finalScore - Points
	Cache += 1


	########################################################################################################################
	# If the final score hits 0, the player has won the game. Otherwise, if the player overshoots, the loop will continue. # 
	########################################################################################################################
	if (finalScore == 0):
		print("Winner!")
		break
	if (finalScore < 0):
		print("Score exceeded...try again")
		finalScore = finalScore + Points
	print ("Your current score is : {}".format(finalScore))
	time.sleep(15)
	
	