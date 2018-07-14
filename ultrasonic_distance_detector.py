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
import requests

server_url = 'http://localhost:9090'
threshold_distance = 1.5

sensor = DistanceSensor(echo=18, trigger=17, threshold_distance=threshold_distance)

while True:
	sensor.wait_for_in_range()
	r = requests.post(server_url, data={'distance': (sensor.distance * 100)});
	if r.status_code == 200:
		print('Pushed distance of ', sensor.distance * 100, ' to the server')
	else:
		print('Failed to push distance to server')
	print('Detected Distance: ', sensor.distance * 100)