import math

Points = 0
x = 1280
y = 0
xNew = x - 1280/2
yNew = y - 720/2
# print ("X,Y              : ",xNew,",",yNew)
# Calculating radius
xyInterim = (xNew ** 2) + (yNew ** 2)
R = math.sqrt(xyInterim)
# print ("Radius           : ",R)
Theta = -1 * math.atan2(yNew,xNew)
# print ("Theta in Radians : ",Theta)
Theta =  math.degrees(Theta)
print ("Theta in Degrees : ",Theta)

if (-9 < Theta <= 9):
  # 6 point region
  Points += 6

if (9 < Theta <= 27):
  # 13 point region
  Points += 13

if (27 < Theta <= 45):
  # 4 point region
  Points += 4

if (45 < Theta <= 63):
  # 18 point region
  Points += 18

if (63 < Theta <= 81):
  # 1 point region
  Points += 1

if (81 < Theta <= 99):
  # 20 point region
  Points += 20

if (99 < Theta <= 117):
  # 5 point region
  Points += 5

if (117 < Theta <= 135):
  # 12 point region
  Points += 12

if (135 < Theta <= 153):
  # 9 point region
  Points += 9

if (153 < Theta <= 171):
  # 14 point region
  Points += 14

if (171 < Theta or Theta < -171):
  # 11 point region
  Points += 11

if (-171 < Theta <= -153):
  # 8 point region
  Points += 8

if (-153 < Theta <= -135):
  # 16 point region
  Points += 16

if (-135 < Theta <= -117):
  # 7 point region
  Points += 7

if (-117 < Theta <= -99):
  # 19 point region
  Points += 19
  
if (-99 < Theta <= -81):
  # 3 point region
  Points += 3

if (-81 < Theta <= -63):
  # 17 point region
  Points += 17

if (-63 < Theta <= -45):
  # 2 point region
  Points += 2

if (-45 < Theta <= -27):
  # 15 point region
  Points += 15

if (-27 < Theta <= -9):
  # 10 point region
  Points += 10

print ("Points           : ",Points)