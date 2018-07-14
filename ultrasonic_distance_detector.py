# ::Board Layout::
# 
#    GND --------------------------------------+
#    GPIO17 ----------------------+      470ohm|
#    GPIO18 ----------------------)-----+-ZZZZ-+
#    5V ----------------------+   |     |      |
#                             |   |     |      |                               
#                             |   |     |      |                                
#                             |   |     Z      |                                
#                             |   |     Z 330ohm                         
#                             |   |     Z      |
#                             |   |     |      |
#                             |   |     |      | 
#                             |   |     |      | 
#                             |   |     |      | 
#                             |   |     |      |
#                             5V  trig echo   GND
#                             ___________________
#                            |                   |
#                            |  (   )    (  )    |
#                             ___________________
#
#



from gpiozero import DistanceSensor
from time import sleep

sensor = DistanceSensor(echo=18, trigger=17, threshold_distance=1.5)
while True:
	senson.wait_for_in_range()
	print('Detected Distance: ', sensor.distance * 100)