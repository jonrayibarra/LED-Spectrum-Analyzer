#^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
import Adafruit_BBIO.GPIO as GPIO
import time

def initi():
    # this is the SERIAL_DATA
    GPIO.setup("P8_10",GPIO.OUT)
    #  this is the CLK_SIGNAL
    GPIO.setup("P8_12",GPIO.OUT)
    # this is the LATCH(Pushes the signals out to the LED Matrix)
    GPIO.setup("P8_14",GPIO.OUT)

#----------------------------------------------------------------------------------------------
# i = column number
# j = bit counter
i = 0
j = 0

highest = None
lowest = None

# range 1 for LEVEL 1
endrange1 = None

# range 2 for LEVEL 2
startrange2 = None
endrange2 = None

# range 3 for LEVEL 3
startrange3 = None
endrange3 = None

# range 4 for LEVEL 4
startrange4 = None

# highest value divided by 4
hdbfour = None
#----------------------------------------------------------------------------------------------

# THIS WILL CLEAR ALL THE LEDS ON THE SCREEN
'''
for i in range(16):
			GPIO.output("P8_10",GPIO.LOW)
			GPIO.output("P8_12",GPIO.HIGH)
			time.sleep(0.001)
			GPIO.output("P8_12",GPIO.LOW)
			time.sleep(0.001)
			i = i + 1
i = 0
'''

# function for extracting what I need from the array
def extract(list_A):
	# i = column number
	# j = bit counter
	i = 0
	j = 0
	
	highest = None
	lowest = None

	# range 1 for LEVEL 1
	endrange1 = None

	# range 2 for LEVEL 2
	startrange2 = None
	endrange2 = None

	# range 3 for LEVEL 3
	startrange3 = None
	endrange3 = None

	# range 4 for LEVEL 4
	startrange4 = None

	# highest value divided by 4
	hdbfour = None
	
	highest = max(list_A)
	lowest = min(list_A)
	hdbfour = highest / 4
	
	endrange1 = lowest + hdbfour
	
	startrange2 = endrange1 + 1
	endrange2 = startrange2 + hdbfour
	
	startrange3 = endrange2 + 1
	endrange3 = startrange3 + hdbfour
	
	startrange4 = endrange3 + 1
	
	while (i != 8):
		#if i == 8:
		#	i = 0
		
		# check amplitude
		if list_A[i] == 0:
			
			# check column
			if i == 0:
				
				# send the bits
				# row // latch 2
				while j in range(7):
					GPIO.output("P8_10",GPIO.HIGH)
					GPIO.output("P8_12",GPIO.HIGH)
					time.sleep(0.00000001)
					GPIO.output("P8_12",GPIO.LOW)
					time.sleep(0.00000001)
					j = j + 1
				
				j = 0
				
				while j in range(1):
					GPIO.output("P8_10",GPIO.LOW)
					GPIO.output("P8_12",GPIO.HIGH)
					time.sleep(0.00000001)
					GPIO.output("P8_12",GPIO.LOW)
					time.sleep(0.00000001)
					j = j + 1
						
				j = 0
				
				# column // latch 1
				while j in range(1):
					GPIO.output("P8_10",GPIO.HIGH)
					GPIO.output("P8_12",GPIO.HIGH)
					time.sleep(0.00000001)
					GPIO.output("P8_12",GPIO.LOW)
					time.sleep(0.00000001)
					j = j + 1
				
				j = 0
		
				while j in range(7):
					GPIO.output("P8_10",GPIO.LOW)
					GPIO.output("P8_12",GPIO.HIGH)
					time.sleep(0.00000001)
					GPIO.output("P8_12",GPIO.LOW)
					time.sleep(0.00000001)
					j = j + 1
				
				j = 0
					
				# display value
				GPIO.output("P8_14",GPIO.HIGH)
				time.sleep(0.00000001)
				GPIO.output("P8_14",GPIO.LOW)
				
				# increment column i
				i = i + 1
			
			# check column 
			elif i == 1:
				# send the bits
				# row // latch 2
				while j in range(8):
					GPIO.output("P8_10",GPIO.HIGH)
					GPIO.output("P8_12",GPIO.HIGH)
					time.sleep(0.00000001)
					GPIO.output("P8_12",GPIO.LOW)
					time.sleep(0.00000001)
					j = j + 1
						
				j = 0
					
				# column // latch 1
				while j in range(1):
					GPIO.output("P8_10",GPIO.LOW)
					GPIO.output("P8_12",GPIO.HIGH)
					time.sleep(0.00000001)
					GPIO.output("P8_12",GPIO.LOW)
					time.sleep(0.00000001)
					j = j + 1
				
				j = 0
				
				while j in range(1):
					GPIO.output("P8_10",GPIO.HIGH)
					GPIO.output("P8_12",GPIO.HIGH)
					time.sleep(0.00000001)
					GPIO.output("P8_12",GPIO.LOW)
					time.sleep(0.00000001)
					j = j + 1
				
				j = 0
		
				while j in range(6):
					GPIO.output("P8_10",GPIO.LOW)
					GPIO.output("P8_12",GPIO.HIGH)
					time.sleep(0.00000001)
					GPIO.output("P8_12",GPIO.LOW)
					time.sleep(0.00000001)
					j = j + 1
				
				j = 0
					
				# display value
				GPIO.output("P8_14",GPIO.HIGH)
				time.sleep(0.00000001)
				GPIO.output("P8_14",GPIO.LOW)
				
				# increment column i
				i = i + 1

			elif i == 2:
				# send the bits
				# row // latch 2
				while j in range(8):
					GPIO.output("P8_10",GPIO.HIGH)
					GPIO.output("P8_12",GPIO.HIGH)
					time.sleep(0.00000001)
					GPIO.output("P8_12",GPIO.LOW)
					time.sleep(0.00000001)
					j = j + 1
						
				j = 0
				
				# column // latch 1
				while j in range(2):
					GPIO.output("P8_10",GPIO.LOW)
					GPIO.output("P8_12",GPIO.HIGH)
					time.sleep(0.00000001)
					GPIO.output("P8_12",GPIO.LOW)
					time.sleep(0.00000001)
					j = j + 1
				
				j = 0
				
				while j in range(1):
					GPIO.output("P8_10",GPIO.HIGH)
					GPIO.output("P8_12",GPIO.HIGH)
					time.sleep(0.00000001)
					GPIO.output("P8_12",GPIO.LOW)
					time.sleep(0.00000001)
					j = j + 1
				
				j = 0
		
				while j in range(5):
					GPIO.output("P8_10",GPIO.LOW)
					GPIO.output("P8_12",GPIO.HIGH)
					time.sleep(0.00000001)
					GPIO.output("P8_12",GPIO.LOW)
					time.sleep(0.00000001)
					j = j + 1
				
				j = 0
					
				# display value
				GPIO.output("P8_14",GPIO.HIGH)
				time.sleep(0.00000001)
				GPIO.output("P8_14",GPIO.LOW)
				
				# increment column i
				i = i + 1

				################################################################################################################# i = 3
				
			elif i == 3:
				# send the bits
				# row // latch 2
				while j in range(8):
					GPIO.output("P8_10",GPIO.HIGH)
					GPIO.output("P8_12",GPIO.HIGH)
					time.sleep(0.00000001)
					GPIO.output("P8_12",GPIO.LOW)
					time.sleep(0.00000001)
					j = j + 1
						
				j = 0
				
				# column // latch 1
				while j in range(3):
					GPIO.output("P8_10",GPIO.LOW)
					GPIO.output("P8_12",GPIO.HIGH)
					time.sleep(0.00000001)
					GPIO.output("P8_12",GPIO.LOW)
					time.sleep(0.00000001)
					j = j + 1
				
				j = 0
				
				while j in range(1):
					GPIO.output("P8_10",GPIO.HIGH)
					GPIO.output("P8_12",GPIO.HIGH)
					time.sleep(0.00000001)
					GPIO.output("P8_12",GPIO.LOW)
					time.sleep(0.00000001)
					j = j + 1
				
				j = 0
		
				while j in range(4):
					GPIO.output("P8_10",GPIO.LOW)
					GPIO.output("P8_12",GPIO.HIGH)
					time.sleep(0.00000001)
					GPIO.output("P8_12",GPIO.LOW)
					time.sleep(0.00000001)
					j = j + 1
				
				j = 0
					
				# display value
				GPIO.output("P8_14",GPIO.HIGH)
				time.sleep(0.00000001)
				GPIO.output("P8_14",GPIO.LOW)
				
				# increment column i
				i = i + 1
			
			elif i == 4:
				# send the bits
				# row // latch 2
				while j in range(8):
					GPIO.output("P8_10",GPIO.HIGH)
					GPIO.output("P8_12",GPIO.HIGH)
					time.sleep(0.00000001)
					GPIO.output("P8_12",GPIO.LOW)
					time.sleep(0.00000001)
					j = j + 1
						
				j = 0
				
				# column // latch 1
				while j in range(4):
					GPIO.output("P8_10",GPIO.LOW)
					GPIO.output("P8_12",GPIO.HIGH)
					time.sleep(0.00000001)
					GPIO.output("P8_12",GPIO.LOW)
					time.sleep(0.00000001)
					j = j + 1
				
				j = 0
				
				while j in range(1):
					GPIO.output("P8_10",GPIO.HIGH)
					GPIO.output("P8_12",GPIO.HIGH)
					time.sleep(0.00000001)
					GPIO.output("P8_12",GPIO.LOW)
					time.sleep(0.00000001)
					j = j + 1
				
				j = 0
		
				while j in range(3):
					GPIO.output("P8_10",GPIO.LOW)
					GPIO.output("P8_12",GPIO.HIGH)
					time.sleep(0.00000001)
					GPIO.output("P8_12",GPIO.LOW)
					time.sleep(0.00000001)
					j = j + 1
				
				j = 0
					
				# display value
				GPIO.output("P8_14",GPIO.HIGH)
				time.sleep(0.00000001)
				GPIO.output("P8_14",GPIO.LOW)
				
				# increment column i
				i = i + 1
			
			elif i == 5:
				# send the bits
				# row // latch 2
				while j in range(8):
					GPIO.output("P8_10",GPIO.HIGH)
					GPIO.output("P8_12",GPIO.HIGH)
					time.sleep(0.00000001)
					GPIO.output("P8_12",GPIO.LOW)
					time.sleep(0.00000001)
					j = j + 1
						
				j = 0
				
				# column // latch 1
				while j in range(5):
					GPIO.output("P8_10",GPIO.LOW)
					GPIO.output("P8_12",GPIO.HIGH)
					time.sleep(0.00000001)
					GPIO.output("P8_12",GPIO.LOW)
					time.sleep(0.00000001)
					j = j + 1
				
				j = 0
				
				while j in range(1):
					GPIO.output("P8_10",GPIO.HIGH)
					GPIO.output("P8_12",GPIO.HIGH)
					time.sleep(0.00000001)
					GPIO.output("P8_12",GPIO.LOW)
					time.sleep(0.00000001)
					j = j + 1
				
				j = 0
		
				while j in range(2):
					GPIO.output("P8_10",GPIO.LOW)
					GPIO.output("P8_12",GPIO.HIGH)
					time.sleep(0.00000001)
					GPIO.output("P8_12",GPIO.LOW)
					time.sleep(0.00000001)
					j = j + 1
				
				j = 0
					
				# display value
				GPIO.output("P8_14",GPIO.HIGH)
				time.sleep(0.00000001)
				GPIO.output("P8_14",GPIO.LOW)
				
				# increment column i
				i = i + 1
				
				# #####################################################################################################################
				
			elif i == 6:
				# send the bits
				# row // latch 2
				while j in range(8):
					GPIO.output("P8_10",GPIO.HIGH)
					GPIO.output("P8_12",GPIO.HIGH)
					time.sleep(0.00000001)
					GPIO.output("P8_12",GPIO.LOW)
					time.sleep(0.00000001)
					j = j + 1
						
				j = 0
				
				# column // latch 1
				while j in range(6):
					GPIO.output("P8_10",GPIO.LOW)
					GPIO.output("P8_12",GPIO.HIGH)
					time.sleep(0.00000001)
					GPIO.output("P8_12",GPIO.LOW)
					time.sleep(0.00000001)
					j = j + 1
				
				j = 0
				
				while j in range(1):
					GPIO.output("P8_10",GPIO.HIGH)
					GPIO.output("P8_12",GPIO.HIGH)
					time.sleep(0.00000001)
					GPIO.output("P8_12",GPIO.LOW)
					time.sleep(0.00000001)
					j = j + 1
				
				j = 0
		
				while j in range(1):
					GPIO.output("P8_10",GPIO.LOW)
					GPIO.output("P8_12",GPIO.HIGH)
					time.sleep(0.00000001)
					GPIO.output("P8_12",GPIO.LOW)
					time.sleep(0.00000001)
					j = j + 1
				
				j = 0
					
				# display value
				GPIO.output("P8_14",GPIO.HIGH)
				time.sleep(0.00000001)
				GPIO.output("P8_14",GPIO.LOW)
				
				# increment column i
				i = i + 1
				
			elif i == 7:
				# send the bits
				# row // latch 2
				while j in range(8):
					GPIO.output("P8_10",GPIO.HIGH)
					GPIO.output("P8_12",GPIO.HIGH)
					time.sleep(0.00000001)
					GPIO.output("P8_12",GPIO.LOW)
					time.sleep(0.00000001)
					j = j + 1
						
				j = 0
				
				# column // latch 1
				while j in range(7):
					GPIO.output("P8_10",GPIO.LOW)
					GPIO.output("P8_12",GPIO.HIGH)
					time.sleep(0.00000001)
					GPIO.output("P8_12",GPIO.LOW)
					time.sleep(0.00000001)
					j = j + 1
				
				j = 0
				
				while j in range(1):
					GPIO.output("P8_10",GPIO.HIGH)
					GPIO.output("P8_12",GPIO.HIGH)
					time.sleep(0.00000001)
					GPIO.output("P8_12",GPIO.LOW)
					time.sleep(0.00000001)
					j = j + 1
				
				j = 0
				
				# display value
				GPIO.output("P8_14",GPIO.HIGH)
				time.sleep(0.00000001)
				GPIO.output("P8_14",GPIO.LOW)
				
				# increment column i
				i = i + 1
		#---------------------------------------------------------------------------------------------------------------------- PRINT NOTHING
		
		# check amplitude
		elif list_A[i] >= lowest and list_A[i] <= endrange1:
			
			# check column
			if i == 0:
				
				# send the bits
				# row // latch 2
				while j in range(6):
					GPIO.output("P8_10",GPIO.HIGH)
					GPIO.output("P8_12",GPIO.HIGH)
					time.sleep(0.00000001)
					GPIO.output("P8_12",GPIO.LOW)
					time.sleep(0.00000001)
					j = j + 1
						
				j = 0
					
				while j in range(2):
					GPIO.output("P8_10",GPIO.LOW)
					GPIO.output("P8_12",GPIO.HIGH)
					time.sleep(0.00000001)
					GPIO.output("P8_12",GPIO.LOW)
					time.sleep(0.00000001)
					j = j + 1
		
				j = 0
				
				# column // latch 1
				while j in range(1):
					GPIO.output("P8_10",GPIO.HIGH)
					GPIO.output("P8_12",GPIO.HIGH)
					time.sleep(0.00000001)
					GPIO.output("P8_12",GPIO.LOW)
					time.sleep(0.00000001)
					j = j + 1
				
				j = 0
		
				while j in range(7):
					GPIO.output("P8_10",GPIO.LOW)
					GPIO.output("P8_12",GPIO.HIGH)
					time.sleep(0.00000001)
					GPIO.output("P8_12",GPIO.LOW)
					time.sleep(0.00000001)
					j = j + 1
				
				j = 0
					
				# display value
				GPIO.output("P8_14",GPIO.HIGH)
				time.sleep(0.00000001)
				GPIO.output("P8_14",GPIO.LOW)
				
				# increment column i
				i = i + 1
			
			# check column 
			elif i == 1:
				# send the bits
				# row // latch 2
				while j in range(6):
					GPIO.output("P8_10",GPIO.HIGH)
					GPIO.output("P8_12",GPIO.HIGH)
					time.sleep(0.00000001)
					GPIO.output("P8_12",GPIO.LOW)
					time.sleep(0.00000001)
					j = j + 1
						
				j = 0
					
				while j in range(2):
					GPIO.output("P8_10",GPIO.LOW)
					GPIO.output("P8_12",GPIO.HIGH)
					time.sleep(0.00000001)
					GPIO.output("P8_12",GPIO.LOW)
					time.sleep(0.00000001)
					j = j + 1
		
				j = 0
				
				# column // latch 1
				while j in range(1):
					GPIO.output("P8_10",GPIO.LOW)
					GPIO.output("P8_12",GPIO.HIGH)
					time.sleep(0.00000001)
					GPIO.output("P8_12",GPIO.LOW)
					time.sleep(0.00000001)
					j = j + 1
				
				j = 0
				
				while j in range(1):
					GPIO.output("P8_10",GPIO.HIGH)
					GPIO.output("P8_12",GPIO.HIGH)
					time.sleep(0.00000001)
					GPIO.output("P8_12",GPIO.LOW)
					time.sleep(0.00000001)
					j = j + 1
				
				j = 0
		
				while j in range(6):
					GPIO.output("P8_10",GPIO.LOW)
					GPIO.output("P8_12",GPIO.HIGH)
					time.sleep(0.00000001)
					GPIO.output("P8_12",GPIO.LOW)
					time.sleep(0.00000001)
					j = j + 1
				
				j = 0
					
				# display value
				GPIO.output("P8_14",GPIO.HIGH)
				time.sleep(0.00000001)
				GPIO.output("P8_14",GPIO.LOW)
				
				# increment column i
				i = i + 1

			elif i == 2:
				# send the bits
				# row // latch 2
				while j in range(6):
					GPIO.output("P8_10",GPIO.HIGH)
					GPIO.output("P8_12",GPIO.HIGH)
					time.sleep(0.00000001)
					GPIO.output("P8_12",GPIO.LOW)
					time.sleep(0.00000001)
					j = j + 1
						
				j = 0
					
				while j in range(2):
					GPIO.output("P8_10",GPIO.LOW)
					GPIO.output("P8_12",GPIO.HIGH)
					time.sleep(0.00000001)
					GPIO.output("P8_12",GPIO.LOW)
					time.sleep(0.00000001)
					j = j + 1
		
				j = 0
				
				# column // latch 1
				while j in range(2):
					GPIO.output("P8_10",GPIO.LOW)
					GPIO.output("P8_12",GPIO.HIGH)
					time.sleep(0.00000001)
					GPIO.output("P8_12",GPIO.LOW)
					time.sleep(0.00000001)
					j = j + 1
				
				j = 0
				
				while j in range(1):
					GPIO.output("P8_10",GPIO.HIGH)
					GPIO.output("P8_12",GPIO.HIGH)
					time.sleep(0.00000001)
					GPIO.output("P8_12",GPIO.LOW)
					time.sleep(0.00000001)
					j = j + 1
				
				j = 0
		
				while j in range(5):
					GPIO.output("P8_10",GPIO.LOW)
					GPIO.output("P8_12",GPIO.HIGH)
					time.sleep(0.00000001)
					GPIO.output("P8_12",GPIO.LOW)
					time.sleep(0.00000001)
					j = j + 1
				
				j = 0
					
				# display value
				GPIO.output("P8_14",GPIO.HIGH)
				time.sleep(0.00000001)
				GPIO.output("P8_14",GPIO.LOW)
				
				# increment column i
				i = i + 1

				################################################################################################################# i = 3
				
			elif i == 3:
				# send the bits
				# row // latch 2
				while j in range(6):
					GPIO.output("P8_10",GPIO.HIGH)
					GPIO.output("P8_12",GPIO.HIGH)
					time.sleep(0.00000001)
					GPIO.output("P8_12",GPIO.LOW)
					time.sleep(0.00000001)
					j = j + 1
						
				j = 0
					
				while j in range(2):
					GPIO.output("P8_10",GPIO.LOW)
					GPIO.output("P8_12",GPIO.HIGH)
					time.sleep(0.00000001)
					GPIO.output("P8_12",GPIO.LOW)
					time.sleep(0.00000001)
					j = j + 1
		
				j = 0
				
				# column // latch 1
				while j in range(3):
					GPIO.output("P8_10",GPIO.LOW)
					GPIO.output("P8_12",GPIO.HIGH)
					time.sleep(0.00000001)
					GPIO.output("P8_12",GPIO.LOW)
					time.sleep(0.00000001)
					j = j + 1
				
				j = 0
				
				while j in range(1):
					GPIO.output("P8_10",GPIO.HIGH)
					GPIO.output("P8_12",GPIO.HIGH)
					time.sleep(0.00000001)
					GPIO.output("P8_12",GPIO.LOW)
					time.sleep(0.00000001)
					j = j + 1
				
				j = 0
		
				while j in range(4):
					GPIO.output("P8_10",GPIO.LOW)
					GPIO.output("P8_12",GPIO.HIGH)
					time.sleep(0.00000001)
					GPIO.output("P8_12",GPIO.LOW)
					time.sleep(0.00000001)
					j = j + 1
				
				j = 0
					
				# display value
				GPIO.output("P8_14",GPIO.HIGH)
				time.sleep(0.00000001)
				GPIO.output("P8_14",GPIO.LOW)
				
				# increment column i
				i = i + 1
			
			elif i == 4:
				# send the bits
				# row // latch 2
				while j in range(6):
					GPIO.output("P8_10",GPIO.HIGH)
					GPIO.output("P8_12",GPIO.HIGH)
					time.sleep(0.00000001)
					GPIO.output("P8_12",GPIO.LOW)
					time.sleep(0.00000001)
					j = j + 1
						
				j = 0
					
				while j in range(2):
					GPIO.output("P8_10",GPIO.LOW)
					GPIO.output("P8_12",GPIO.HIGH)
					time.sleep(0.00000001)
					GPIO.output("P8_12",GPIO.LOW)
					time.sleep(0.00000001)
					j = j + 1
		
				j = 0
				
				# column // latch 1
				while j in range(4):
					GPIO.output("P8_10",GPIO.LOW)
					GPIO.output("P8_12",GPIO.HIGH)
					time.sleep(0.00000001)
					GPIO.output("P8_12",GPIO.LOW)
					time.sleep(0.00000001)
					j = j + 1
				
				j = 0
				
				while j in range(1):
					GPIO.output("P8_10",GPIO.HIGH)
					GPIO.output("P8_12",GPIO.HIGH)
					time.sleep(0.00000001)
					GPIO.output("P8_12",GPIO.LOW)
					time.sleep(0.00000001)
					j = j + 1
				
				j = 0
		
				while j in range(3):
					GPIO.output("P8_10",GPIO.LOW)
					GPIO.output("P8_12",GPIO.HIGH)
					time.sleep(0.00000001)
					GPIO.output("P8_12",GPIO.LOW)
					time.sleep(0.00000001)
					j = j + 1
				
				j = 0
					
				# display value
				GPIO.output("P8_14",GPIO.HIGH)
				time.sleep(0.00000001)
				GPIO.output("P8_14",GPIO.LOW)
				
				# increment column i
				i = i + 1
			
			elif i == 5:
				# send the bits
				# row // latch 2
				while j in range(6):
					GPIO.output("P8_10",GPIO.HIGH)
					GPIO.output("P8_12",GPIO.HIGH)
					time.sleep(0.00000001)
					GPIO.output("P8_12",GPIO.LOW)
					time.sleep(0.00000001)
					j = j + 1
						
				j = 0
					
				while j in range(2):
					GPIO.output("P8_10",GPIO.LOW)
					GPIO.output("P8_12",GPIO.HIGH)
					time.sleep(0.00000001)
					GPIO.output("P8_12",GPIO.LOW)
					time.sleep(0.00000001)
					j = j + 1
		
				j = 0
				
				# column // latch 1
				while j in range(5):
					GPIO.output("P8_10",GPIO.LOW)
					GPIO.output("P8_12",GPIO.HIGH)
					time.sleep(0.00000001)
					GPIO.output("P8_12",GPIO.LOW)
					time.sleep(0.00000001)
					j = j + 1
				
				j = 0
				
				while j in range(1):
					GPIO.output("P8_10",GPIO.HIGH)
					GPIO.output("P8_12",GPIO.HIGH)
					time.sleep(0.00000001)
					GPIO.output("P8_12",GPIO.LOW)
					time.sleep(0.00000001)
					j = j + 1
				
				j = 0
		
				while j in range(2):
					GPIO.output("P8_10",GPIO.LOW)
					GPIO.output("P8_12",GPIO.HIGH)
					time.sleep(0.00000001)
					GPIO.output("P8_12",GPIO.LOW)
					time.sleep(0.00000001)
					j = j + 1
				
				j = 0
					
				# display value
				GPIO.output("P8_14",GPIO.HIGH)
				time.sleep(0.00000001)
				GPIO.output("P8_14",GPIO.LOW)
				
				# increment column i
				i = i + 1
				
				# #####################################################################################################################
				
			elif i == 6:
				# send the bits
				# row // latch 2
				while j in range(6):
					GPIO.output("P8_10",GPIO.HIGH)
					GPIO.output("P8_12",GPIO.HIGH)
					time.sleep(0.00000001)
					GPIO.output("P8_12",GPIO.LOW)
					time.sleep(0.00000001)
					j = j + 1
						
				j = 0
					
				while j in range(2):
					GPIO.output("P8_10",GPIO.LOW)
					GPIO.output("P8_12",GPIO.HIGH)
					time.sleep(0.00000001)
					GPIO.output("P8_12",GPIO.LOW)
					time.sleep(0.00000001)
					j = j + 1
		
				j = 0
				
				# column // latch 1
				while j in range(6):
					GPIO.output("P8_10",GPIO.LOW)
					GPIO.output("P8_12",GPIO.HIGH)
					time.sleep(0.00000001)
					GPIO.output("P8_12",GPIO.LOW)
					time.sleep(0.00000001)
					j = j + 1
				
				j = 0
				
				while j in range(1):
					GPIO.output("P8_10",GPIO.HIGH)
					GPIO.output("P8_12",GPIO.HIGH)
					time.sleep(0.00000001)
					GPIO.output("P8_12",GPIO.LOW)
					time.sleep(0.00000001)
					j = j + 1
				
				j = 0
		
				while j in range(1):
					GPIO.output("P8_10",GPIO.LOW)
					GPIO.output("P8_12",GPIO.HIGH)
					time.sleep(0.00000001)
					GPIO.output("P8_12",GPIO.LOW)
					time.sleep(0.00000001)
					j = j + 1
				
				j = 0
					
				# display value
				GPIO.output("P8_14",GPIO.HIGH)
				time.sleep(0.00000001)
				GPIO.output("P8_14",GPIO.LOW)
				
				# increment column i
				i = i + 1
				
			elif i == 7:
				# send the bits
				# row // latch 2
				while j in range(6):
					GPIO.output("P8_10",GPIO.HIGH)
					GPIO.output("P8_12",GPIO.HIGH)
					time.sleep(0.00000001)
					GPIO.output("P8_12",GPIO.LOW)
					time.sleep(0.00000001)
					j = j + 1
						
				j = 0
					
				while j in range(2):
					GPIO.output("P8_10",GPIO.LOW)
					GPIO.output("P8_12",GPIO.HIGH)
					time.sleep(0.00000001)
					GPIO.output("P8_12",GPIO.LOW)
					time.sleep(0.00000001)
					j = j + 1
		
				j = 0
				
				# column // latch 1
				while j in range(7):
					GPIO.output("P8_10",GPIO.LOW)
					GPIO.output("P8_12",GPIO.HIGH)
					time.sleep(0.00000001)
					GPIO.output("P8_12",GPIO.LOW)
					time.sleep(0.00000001)
					j = j + 1
				
				j = 0
				
				while j in range(1):
					GPIO.output("P8_10",GPIO.HIGH)
					GPIO.output("P8_12",GPIO.HIGH)
					time.sleep(0.00000001)
					GPIO.output("P8_12",GPIO.LOW)
					time.sleep(0.00000001)
					j = j + 1
				
				j = 0
				
				# display value
				GPIO.output("P8_14",GPIO.HIGH)
				time.sleep(0.00000001)
				GPIO.output("P8_14",GPIO.LOW)
				
				# increment column i
				i = i + 1
				
		#---------------------------------------------------------------------------------------------------------------------- end of level 1	
		
		# check amplitude
		elif list_A[i] >= startrange2 and list_A[i] <= endrange2:
			
			# check column
			if i == 0:
				
				# send the bits
				# row // latch 2
				while j in range(4):
					GPIO.output("P8_10",GPIO.HIGH)
					GPIO.output("P8_12",GPIO.HIGH)
					time.sleep(0.00000001)
					GPIO.output("P8_12",GPIO.LOW)
					time.sleep(0.00000001)
					j = j + 1
						
				j = 0
					
				while j in range(4):
					GPIO.output("P8_10",GPIO.LOW)
					GPIO.output("P8_12",GPIO.HIGH)
					time.sleep(0.00000001)
					GPIO.output("P8_12",GPIO.LOW)
					time.sleep(0.00000001)
					j = j + 1
		
				j = 0
				
				# column // latch 1
				while j in range(1):
					GPIO.output("P8_10",GPIO.HIGH)
					GPIO.output("P8_12",GPIO.HIGH)
					time.sleep(0.00000001)
					GPIO.output("P8_12",GPIO.LOW)
					time.sleep(0.00000001)
					j = j + 1
				
				j = 0
		
				while j in range(7):
					GPIO.output("P8_10",GPIO.LOW)
					GPIO.output("P8_12",GPIO.HIGH)
					time.sleep(0.00000001)
					GPIO.output("P8_12",GPIO.LOW)
					time.sleep(0.00000001)
					j = j + 1
				
				j = 0
					
				# display value
				GPIO.output("P8_14",GPIO.HIGH)
				time.sleep(0.00000001)
				GPIO.output("P8_14",GPIO.LOW)
				
				# increment column i
				i = i + 1
			
			# check column 
			elif i == 1:
				# send the bits
				# row // latch 2
				while j in range(4):
					GPIO.output("P8_10",GPIO.HIGH)
					GPIO.output("P8_12",GPIO.HIGH)
					time.sleep(0.00000001)
					GPIO.output("P8_12",GPIO.LOW)
					time.sleep(0.00000001)
					j = j + 1
						
				j = 0
					
				while j in range(4):
					GPIO.output("P8_10",GPIO.LOW)
					GPIO.output("P8_12",GPIO.HIGH)
					time.sleep(0.00000001)
					GPIO.output("P8_12",GPIO.LOW)
					time.sleep(0.00000001)
					j = j + 1
		
				j = 0
				
				# column // latch 1
				while j in range(1):
					GPIO.output("P8_10",GPIO.LOW)
					GPIO.output("P8_12",GPIO.HIGH)
					time.sleep(0.00000001)
					GPIO.output("P8_12",GPIO.LOW)
					time.sleep(0.00000001)
					j = j + 1
				
				j = 0
				
				while j in range(1):
					GPIO.output("P8_10",GPIO.HIGH)
					GPIO.output("P8_12",GPIO.HIGH)
					time.sleep(0.00000001)
					GPIO.output("P8_12",GPIO.LOW)
					time.sleep(0.00000001)
					j = j + 1
				
				j = 0
		
				while j in range(6):
					GPIO.output("P8_10",GPIO.LOW)
					GPIO.output("P8_12",GPIO.HIGH)
					time.sleep(0.00000001)
					GPIO.output("P8_12",GPIO.LOW)
					time.sleep(0.00000001)
					j = j + 1
				
				j = 0
					
				# display value
				GPIO.output("P8_14",GPIO.HIGH)
				time.sleep(0.00000001)
				GPIO.output("P8_14",GPIO.LOW)
				
				# increment column i
				i = i + 1

			elif i == 2:
				# send the bits
				# row // latch 2
				while j in range(4):
					GPIO.output("P8_10",GPIO.HIGH)
					GPIO.output("P8_12",GPIO.HIGH)
					time.sleep(0.00000001)
					GPIO.output("P8_12",GPIO.LOW)
					time.sleep(0.00000001)
					j = j + 1
						
				j = 0
					
				while j in range(4):
					GPIO.output("P8_10",GPIO.LOW)
					GPIO.output("P8_12",GPIO.HIGH)
					time.sleep(0.00000001)
					GPIO.output("P8_12",GPIO.LOW)
					time.sleep(0.00000001)
					j = j + 1
		
				j = 0
				
				# column // latch 1
				while j in range(2):
					GPIO.output("P8_10",GPIO.LOW)
					GPIO.output("P8_12",GPIO.HIGH)
					time.sleep(0.00000001)
					GPIO.output("P8_12",GPIO.LOW)
					time.sleep(0.00000001)
					j = j + 1
				
				j = 0
				
				while j in range(1):
					GPIO.output("P8_10",GPIO.HIGH)
					GPIO.output("P8_12",GPIO.HIGH)
					time.sleep(0.00000001)
					GPIO.output("P8_12",GPIO.LOW)
					time.sleep(0.00000001)
					j = j + 1
				
				j = 0
		
				while j in range(5):
					GPIO.output("P8_10",GPIO.LOW)
					GPIO.output("P8_12",GPIO.HIGH)
					time.sleep(0.00000001)
					GPIO.output("P8_12",GPIO.LOW)
					time.sleep(0.00000001)
					j = j + 1
				
				j = 0
					
				# display value
				GPIO.output("P8_14",GPIO.HIGH)
				time.sleep(0.00000001)
				GPIO.output("P8_14",GPIO.LOW)
				
				# increment column i
				i = i + 1

				################################################################################################################# i = 3
				
			elif i == 3:
				# send the bits
				# row // latch 2
				while j in range(4):
					GPIO.output("P8_10",GPIO.HIGH)
					GPIO.output("P8_12",GPIO.HIGH)
					time.sleep(0.00000001)
					GPIO.output("P8_12",GPIO.LOW)
					time.sleep(0.00000001)
					j = j + 1
						
				j = 0
					
				while j in range(4):
					GPIO.output("P8_10",GPIO.LOW)
					GPIO.output("P8_12",GPIO.HIGH)
					time.sleep(0.00000001)
					GPIO.output("P8_12",GPIO.LOW)
					time.sleep(0.00000001)
					j = j + 1
		
				j = 0
				
				# column // latch 1
				while j in range(3):
					GPIO.output("P8_10",GPIO.LOW)
					GPIO.output("P8_12",GPIO.HIGH)
					time.sleep(0.00000001)
					GPIO.output("P8_12",GPIO.LOW)
					time.sleep(0.00000001)
					j = j + 1
				
				j = 0
				
				while j in range(1):
					GPIO.output("P8_10",GPIO.HIGH)
					GPIO.output("P8_12",GPIO.HIGH)
					time.sleep(0.00000001)
					GPIO.output("P8_12",GPIO.LOW)
					time.sleep(0.00000001)
					j = j + 1
				
				j = 0
		
				while j in range(4):
					GPIO.output("P8_10",GPIO.LOW)
					GPIO.output("P8_12",GPIO.HIGH)
					time.sleep(0.00000001)
					GPIO.output("P8_12",GPIO.LOW)
					time.sleep(0.00000001)
					j = j + 1
				
				j = 0
					
				# display value
				GPIO.output("P8_14",GPIO.HIGH)
				time.sleep(0.00000001)
				GPIO.output("P8_14",GPIO.LOW)
				
				# increment column i
				i = i + 1
			
			elif i == 4:
				# send the bits
				# row // latch 2
				while j in range(4):
					GPIO.output("P8_10",GPIO.HIGH)
					GPIO.output("P8_12",GPIO.HIGH)
					time.sleep(0.00000001)
					GPIO.output("P8_12",GPIO.LOW)
					time.sleep(0.00000001)
					j = j + 1
						
				j = 0
					
				while j in range(4):
					GPIO.output("P8_10",GPIO.LOW)
					GPIO.output("P8_12",GPIO.HIGH)
					time.sleep(0.00000001)
					GPIO.output("P8_12",GPIO.LOW)
					time.sleep(0.00000001)
					j = j + 1
		
				j = 0
				
				# column // latch 1
				while j in range(4):
					GPIO.output("P8_10",GPIO.LOW)
					GPIO.output("P8_12",GPIO.HIGH)
					time.sleep(0.00000001)
					GPIO.output("P8_12",GPIO.LOW)
					time.sleep(0.00000001)
					j = j + 1
				
				j = 0
				
				while j in range(1):
					GPIO.output("P8_10",GPIO.HIGH)
					GPIO.output("P8_12",GPIO.HIGH)
					time.sleep(0.00000001)
					GPIO.output("P8_12",GPIO.LOW)
					time.sleep(0.00000001)
					j = j + 1
				
				j = 0
		
				while j in range(3):
					GPIO.output("P8_10",GPIO.LOW)
					GPIO.output("P8_12",GPIO.HIGH)
					time.sleep(0.00000001)
					GPIO.output("P8_12",GPIO.LOW)
					time.sleep(0.00000001)
					j = j + 1
				
				j = 0
					
				# display value
				GPIO.output("P8_14",GPIO.HIGH)
				time.sleep(0.00000001)
				GPIO.output("P8_14",GPIO.LOW)
				
				# increment column i
				i = i + 1
			
			elif i == 5:
				# send the bits
				# row // latch 2
				while j in range(4):
					GPIO.output("P8_10",GPIO.HIGH)
					GPIO.output("P8_12",GPIO.HIGH)
					time.sleep(0.00000001)
					GPIO.output("P8_12",GPIO.LOW)
					time.sleep(0.00000001)
					j = j + 1
						
				j = 0
					
				while j in range(4):
					GPIO.output("P8_10",GPIO.LOW)
					GPIO.output("P8_12",GPIO.HIGH)
					time.sleep(0.00000001)
					GPIO.output("P8_12",GPIO.LOW)
					time.sleep(0.00000001)
					j = j + 1
		
				j = 0
				
				# column // latch 1
				while j in range(5):
					GPIO.output("P8_10",GPIO.LOW)
					GPIO.output("P8_12",GPIO.HIGH)
					time.sleep(0.00000001)
					GPIO.output("P8_12",GPIO.LOW)
					time.sleep(0.00000001)
					j = j + 1
				
				j = 0
				
				while j in range(1):
					GPIO.output("P8_10",GPIO.HIGH)
					GPIO.output("P8_12",GPIO.HIGH)
					time.sleep(0.00000001)
					GPIO.output("P8_12",GPIO.LOW)
					time.sleep(0.00000001)
					j = j + 1
				
				j = 0
		
				while j in range(2):
					GPIO.output("P8_10",GPIO.LOW)
					GPIO.output("P8_12",GPIO.HIGH)
					time.sleep(0.00000001)
					GPIO.output("P8_12",GPIO.LOW)
					time.sleep(0.00000001)
					j = j + 1
				
				j = 0
					
				# display value
				GPIO.output("P8_14",GPIO.HIGH)
				time.sleep(0.00000001)
				GPIO.output("P8_14",GPIO.LOW)
				
				# increment column i
				i = i + 1
				
				# #####################################################################################################################
				
			elif i == 6:
				# send the bits
				# row // latch 2
				while j in range(4):
					GPIO.output("P8_10",GPIO.HIGH)
					GPIO.output("P8_12",GPIO.HIGH)
					time.sleep(0.00000001)
					GPIO.output("P8_12",GPIO.LOW)
					time.sleep(0.00000001)
					j = j + 1
						
				j = 0
					
				while j in range(4):
					GPIO.output("P8_10",GPIO.LOW)
					GPIO.output("P8_12",GPIO.HIGH)
					time.sleep(0.00000001)
					GPIO.output("P8_12",GPIO.LOW)
					time.sleep(0.00000001)
					j = j + 1
		
				j = 0
				
				# column // latch 1
				while j in range(6):
					GPIO.output("P8_10",GPIO.LOW)
					GPIO.output("P8_12",GPIO.HIGH)
					time.sleep(0.00000001)
					GPIO.output("P8_12",GPIO.LOW)
					time.sleep(0.00000001)
					j = j + 1
				
				j = 0
				
				while j in range(1):
					GPIO.output("P8_10",GPIO.HIGH)
					GPIO.output("P8_12",GPIO.HIGH)
					time.sleep(0.00000001)
					GPIO.output("P8_12",GPIO.LOW)
					time.sleep(0.00000001)
					j = j + 1
				
				j = 0
		
				while j in range(1):
					GPIO.output("P8_10",GPIO.LOW)
					GPIO.output("P8_12",GPIO.HIGH)
					time.sleep(0.00000001)
					GPIO.output("P8_12",GPIO.LOW)
					time.sleep(0.00000001)
					j = j + 1
				
				j = 0
					
				# display value
				GPIO.output("P8_14",GPIO.HIGH)
				time.sleep(0.00000001)
				GPIO.output("P8_14",GPIO.LOW)
				
				# increment column i
				i = i + 1
				
			elif i == 7:
				# send the bits
				# row // latch 2
				while j in range(4):
					GPIO.output("P8_10",GPIO.HIGH)
					GPIO.output("P8_12",GPIO.HIGH)
					time.sleep(0.00000001)
					GPIO.output("P8_12",GPIO.LOW)
					time.sleep(0.00000001)
					j = j + 1
						
				j = 0
					
				while j in range(4):
					GPIO.output("P8_10",GPIO.LOW)
					GPIO.output("P8_12",GPIO.HIGH)
					time.sleep(0.00000001)
					GPIO.output("P8_12",GPIO.LOW)
					time.sleep(0.00000001)
					j = j + 1
		
				j = 0
				
				# column // latch 1
				while j in range(7):
					GPIO.output("P8_10",GPIO.LOW)
					GPIO.output("P8_12",GPIO.HIGH)
					time.sleep(0.00000001)
					GPIO.output("P8_12",GPIO.LOW)
					time.sleep(0.00000001)
					j = j + 1
				
				j = 0
				
				while j in range(1):
					GPIO.output("P8_10",GPIO.HIGH)
					GPIO.output("P8_12",GPIO.HIGH)
					time.sleep(0.00000001)
					GPIO.output("P8_12",GPIO.LOW)
					time.sleep(0.00000001)
					j = j + 1
				
				j = 0
				
				# display value
				GPIO.output("P8_14",GPIO.HIGH)
				time.sleep(0.00000001)
				GPIO.output("P8_14",GPIO.LOW)
				
				# increment column i
				i = i + 1
		
		#---------------------------------------------------------------------------------------------------------------------- end of level 2
		
		# check amplitude
		elif list_A[i] >= startrange3 and list_A[i] <= endrange3:
		
			# check column
			if i == 0:
				
				# send the bits
				# row // latch 2
				while j in range(2):
					GPIO.output("P8_10",GPIO.HIGH)
					GPIO.output("P8_12",GPIO.HIGH)
					time.sleep(0.00000001)
					GPIO.output("P8_12",GPIO.LOW)
					time.sleep(0.00000001)
					j = j + 1
						
				j = 0
					
				while j in range(6):
					GPIO.output("P8_10",GPIO.LOW)
					GPIO.output("P8_12",GPIO.HIGH)
					time.sleep(0.00000001)
					GPIO.output("P8_12",GPIO.LOW)
					time.sleep(0.00000001)
					j = j + 1
		
				j = 0
				
				# column // latch 1
				while j in range(1):
					GPIO.output("P8_10",GPIO.HIGH)
					GPIO.output("P8_12",GPIO.HIGH)
					time.sleep(0.00000001)
					GPIO.output("P8_12",GPIO.LOW)
					time.sleep(0.00000001)
					j = j + 1
				
				j = 0
		
				while j in range(7):
					GPIO.output("P8_10",GPIO.LOW)
					GPIO.output("P8_12",GPIO.HIGH)
					time.sleep(0.00000001)
					GPIO.output("P8_12",GPIO.LOW)
					time.sleep(0.00000001)
					j = j + 1
				
				j = 0
					
				# display value
				GPIO.output("P8_14",GPIO.HIGH)
				time.sleep(0.00000001)
				GPIO.output("P8_14",GPIO.LOW)
				
				# increment column i
				i = i + 1
			
			# check column 
			elif i == 1:
				# send the bits
				# row // latch 2
				while j in range(2):
					GPIO.output("P8_10",GPIO.HIGH)
					GPIO.output("P8_12",GPIO.HIGH)
					time.sleep(0.00000001)
					GPIO.output("P8_12",GPIO.LOW)
					time.sleep(0.00000001)
					j = j + 1
						
				j = 0
					
				while j in range(6):
					GPIO.output("P8_10",GPIO.LOW)
					GPIO.output("P8_12",GPIO.HIGH)
					time.sleep(0.00000001)
					GPIO.output("P8_12",GPIO.LOW)
					time.sleep(0.00000001)
					j = j + 1
		
				j = 0
				
				# column // latch 1
				while j in range(1):
					GPIO.output("P8_10",GPIO.LOW)
					GPIO.output("P8_12",GPIO.HIGH)
					time.sleep(0.00000001)
					GPIO.output("P8_12",GPIO.LOW)
					time.sleep(0.00000001)
					j = j + 1
				
				j = 0
				
				while j in range(1):
					GPIO.output("P8_10",GPIO.HIGH)
					GPIO.output("P8_12",GPIO.HIGH)
					time.sleep(0.00000001)
					GPIO.output("P8_12",GPIO.LOW)
					time.sleep(0.00000001)
					j = j + 1
				
				j = 0
		
				while j in range(6):
					GPIO.output("P8_10",GPIO.LOW)
					GPIO.output("P8_12",GPIO.HIGH)
					time.sleep(0.00000001)
					GPIO.output("P8_12",GPIO.LOW)
					time.sleep(0.00000001)
					j = j + 1
				
				j = 0
					
				# display value
				GPIO.output("P8_14",GPIO.HIGH)
				time.sleep(0.00000001)
				GPIO.output("P8_14",GPIO.LOW)
				
				# increment column i
				i = i + 1

			elif i == 2:
				# send the bits
				# row // latch 2
				while j in range(2):
					GPIO.output("P8_10",GPIO.HIGH)
					GPIO.output("P8_12",GPIO.HIGH)
					time.sleep(0.00000001)
					GPIO.output("P8_12",GPIO.LOW)
					time.sleep(0.00000001)
					j = j + 1
						
				j = 0
					
				while j in range(6):
					GPIO.output("P8_10",GPIO.LOW)
					GPIO.output("P8_12",GPIO.HIGH)
					time.sleep(0.00000001)
					GPIO.output("P8_12",GPIO.LOW)
					time.sleep(0.00000001)
					j = j + 1
		
				j = 0
				
				# column // latch 1
				while j in range(2):
					GPIO.output("P8_10",GPIO.LOW)
					GPIO.output("P8_12",GPIO.HIGH)
					time.sleep(0.00000001)
					GPIO.output("P8_12",GPIO.LOW)
					time.sleep(0.00000001)
					j = j + 1
				
				j = 0
				
				while j in range(1):
					GPIO.output("P8_10",GPIO.HIGH)
					GPIO.output("P8_12",GPIO.HIGH)
					time.sleep(0.00000001)
					GPIO.output("P8_12",GPIO.LOW)
					time.sleep(0.00000001)
					j = j + 1
				
				j = 0
		
				while j in range(5):
					GPIO.output("P8_10",GPIO.LOW)
					GPIO.output("P8_12",GPIO.HIGH)
					time.sleep(0.00000001)
					GPIO.output("P8_12",GPIO.LOW)
					time.sleep(0.00000001)
					j = j + 1
				
				j = 0
					
				# display value
				GPIO.output("P8_14",GPIO.HIGH)
				time.sleep(0.00000001)
				GPIO.output("P8_14",GPIO.LOW)
				
				# increment column i
				i = i + 1

				################################################################################################################# i = 3
				
			elif i == 3:
				# send the bits
				# row // latch 2
				while j in range(2):
					GPIO.output("P8_10",GPIO.HIGH)
					GPIO.output("P8_12",GPIO.HIGH)
					time.sleep(0.00000001)
					GPIO.output("P8_12",GPIO.LOW)
					time.sleep(0.00000001)
					j = j + 1
						
				j = 0
					
				while j in range(6):
					GPIO.output("P8_10",GPIO.LOW)
					GPIO.output("P8_12",GPIO.HIGH)
					time.sleep(0.00000001)
					GPIO.output("P8_12",GPIO.LOW)
					time.sleep(0.00000001)
					j = j + 1
		
				j = 0
				
				# column // latch 1
				while j in range(3):
					GPIO.output("P8_10",GPIO.LOW)
					GPIO.output("P8_12",GPIO.HIGH)
					time.sleep(0.00000001)
					GPIO.output("P8_12",GPIO.LOW)
					time.sleep(0.00000001)
					j = j + 1
				
				j = 0
				
				while j in range(1):
					GPIO.output("P8_10",GPIO.HIGH)
					GPIO.output("P8_12",GPIO.HIGH)
					time.sleep(0.00000001)
					GPIO.output("P8_12",GPIO.LOW)
					time.sleep(0.00000001)
					j = j + 1
				
				j = 0
		
				while j in range(4):
					GPIO.output("P8_10",GPIO.LOW)
					GPIO.output("P8_12",GPIO.HIGH)
					time.sleep(0.00000001)
					GPIO.output("P8_12",GPIO.LOW)
					time.sleep(0.00000001)
					j = j + 1
				
				j = 0
					
				# display value
				GPIO.output("P8_14",GPIO.HIGH)
				time.sleep(0.00000001)
				GPIO.output("P8_14",GPIO.LOW)
				
				# increment column i
				i = i + 1
			
			elif i == 4:
				# send the bits
				# row // latch 2
				while j in range(2):
					GPIO.output("P8_10",GPIO.HIGH)
					GPIO.output("P8_12",GPIO.HIGH)
					time.sleep(0.00000001)
					GPIO.output("P8_12",GPIO.LOW)
					time.sleep(0.00000001)
					j = j + 1
						
				j = 0
					
				while j in range(6):
					GPIO.output("P8_10",GPIO.LOW)
					GPIO.output("P8_12",GPIO.HIGH)
					time.sleep(0.00000001)
					GPIO.output("P8_12",GPIO.LOW)
					time.sleep(0.00000001)
					j = j + 1
		
				j = 0
				
				# column // latch 1
				while j in range(4):
					GPIO.output("P8_10",GPIO.LOW)
					GPIO.output("P8_12",GPIO.HIGH)
					time.sleep(0.00000001)
					GPIO.output("P8_12",GPIO.LOW)
					time.sleep(0.00000001)
					j = j + 1
				
				j = 0
				
				while j in range(1):
					GPIO.output("P8_10",GPIO.HIGH)
					GPIO.output("P8_12",GPIO.HIGH)
					time.sleep(0.00000001)
					GPIO.output("P8_12",GPIO.LOW)
					time.sleep(0.00000001)
					j = j + 1
				
				j = 0
		
				while j in range(3):
					GPIO.output("P8_10",GPIO.LOW)
					GPIO.output("P8_12",GPIO.HIGH)
					time.sleep(0.00000001)
					GPIO.output("P8_12",GPIO.LOW)
					time.sleep(0.00000001)
					j = j + 1
				
				j = 0
					
				# display value
				GPIO.output("P8_14",GPIO.HIGH)
				time.sleep(0.00000001)
				GPIO.output("P8_14",GPIO.LOW)
				
				# increment column i
				i = i + 1
			
			elif i == 5:
				# send the bits
				# row // latch 2
				while j in range(2):
					GPIO.output("P8_10",GPIO.HIGH)
					GPIO.output("P8_12",GPIO.HIGH)
					time.sleep(0.00000001)
					GPIO.output("P8_12",GPIO.LOW)
					time.sleep(0.00000001)
					j = j + 1
						
				j = 0
					
				while j in range(6):
					GPIO.output("P8_10",GPIO.LOW)
					GPIO.output("P8_12",GPIO.HIGH)
					time.sleep(0.00000001)
					GPIO.output("P8_12",GPIO.LOW)
					time.sleep(0.00000001)
					j = j + 1
		
				j = 0
				
				# column // latch 1
				while j in range(5):
					GPIO.output("P8_10",GPIO.LOW)
					GPIO.output("P8_12",GPIO.HIGH)
					time.sleep(0.00000001)
					GPIO.output("P8_12",GPIO.LOW)
					time.sleep(0.00000001)
					j = j + 1
				
				j = 0
				
				while j in range(1):
					GPIO.output("P8_10",GPIO.HIGH)
					GPIO.output("P8_12",GPIO.HIGH)
					time.sleep(0.00000001)
					GPIO.output("P8_12",GPIO.LOW)
					time.sleep(0.00000001)
					j = j + 1
				
				j = 0
		
				while j in range(2):
					GPIO.output("P8_10",GPIO.LOW)
					GPIO.output("P8_12",GPIO.HIGH)
					time.sleep(0.00000001)
					GPIO.output("P8_12",GPIO.LOW)
					time.sleep(0.00000001)
					j = j + 1
				
				j = 0
					
				# display value
				GPIO.output("P8_14",GPIO.HIGH)
				time.sleep(0.00000001)
				GPIO.output("P8_14",GPIO.LOW)
				
				# increment column i
				i = i + 1
				
				# #####################################################################################################################
				
			elif i == 6:
				# send the bits
				# row // latch 2
				while j in range(2):
					GPIO.output("P8_10",GPIO.HIGH)
					GPIO.output("P8_12",GPIO.HIGH)
					time.sleep(0.00000001)
					GPIO.output("P8_12",GPIO.LOW)
					time.sleep(0.00000001)
					j = j + 1
						
				j = 0
					
				while j in range(6):
					GPIO.output("P8_10",GPIO.LOW)
					GPIO.output("P8_12",GPIO.HIGH)
					time.sleep(0.00000001)
					GPIO.output("P8_12",GPIO.LOW)
					time.sleep(0.00000001)
					j = j + 1
		
				j = 0
				
				# column // latch 1
				while j in range(6):
					GPIO.output("P8_10",GPIO.LOW)
					GPIO.output("P8_12",GPIO.HIGH)
					time.sleep(0.00000001)
					GPIO.output("P8_12",GPIO.LOW)
					time.sleep(0.00000001)
					j = j + 1
				
				j = 0
				
				while j in range(1):
					GPIO.output("P8_10",GPIO.HIGH)
					GPIO.output("P8_12",GPIO.HIGH)
					time.sleep(0.00000001)
					GPIO.output("P8_12",GPIO.LOW)
					time.sleep(0.00000001)
					j = j + 1
				
				j = 0
		
				while j in range(1):
					GPIO.output("P8_10",GPIO.LOW)
					GPIO.output("P8_12",GPIO.HIGH)
					time.sleep(0.00000001)
					GPIO.output("P8_12",GPIO.LOW)
					time.sleep(0.00000001)
					j = j + 1
				
				j = 0
					
				# display value
				GPIO.output("P8_14",GPIO.HIGH)
				time.sleep(0.00000001)
				GPIO.output("P8_14",GPIO.LOW)
				
				# increment column i
				i = i + 1
				
			elif i == 7:
				# send the bits
				# row // latch 2
				while j in range(2):
					GPIO.output("P8_10",GPIO.HIGH)
					GPIO.output("P8_12",GPIO.HIGH)
					time.sleep(0.00000001)
					GPIO.output("P8_12",GPIO.LOW)
					time.sleep(0.00000001)
					j = j + 1
						
				j = 0
					
				while j in range(6):
					GPIO.output("P8_10",GPIO.LOW)
					GPIO.output("P8_12",GPIO.HIGH)
					time.sleep(0.00000001)
					GPIO.output("P8_12",GPIO.LOW)
					time.sleep(0.00000001)
					j = j + 1
		
				j = 0
				
				# column // latch 1
				while j in range(7):
					GPIO.output("P8_10",GPIO.LOW)
					GPIO.output("P8_12",GPIO.HIGH)
					time.sleep(0.00000001)
					GPIO.output("P8_12",GPIO.LOW)
					time.sleep(0.00000001)
					j = j + 1
				
				j = 0
				
				while j in range(1):
					GPIO.output("P8_10",GPIO.HIGH)
					GPIO.output("P8_12",GPIO.HIGH)
					time.sleep(0.00000001)
					GPIO.output("P8_12",GPIO.LOW)
					time.sleep(0.00000001)
					j = j + 1
				
				j = 0
				
				# display value
				GPIO.output("P8_14",GPIO.HIGH)
				time.sleep(0.00000001)
				GPIO.output("P8_14",GPIO.LOW)
				
				# increment column i
				i = i + 1
				
		#---------------------------------------------------------------------------------------------------------------------- end of level 3
		
		# check amplitude
		elif list_A[i] >= startrange4 and list_A[i] <= highest:
		
			# check column
			if i == 0:
				
				# send the bits
				# row // latch 2
				while j in range(8):
					GPIO.output("P8_10",GPIO.LOW)
					GPIO.output("P8_12",GPIO.HIGH)
					time.sleep(0.00000001)
					GPIO.output("P8_12",GPIO.LOW)
					time.sleep(0.00000001)
					j = j + 1
		
				j = 0
				
				# column // latch 1
				while j in range(1):
					GPIO.output("P8_10",GPIO.HIGH)
					GPIO.output("P8_12",GPIO.HIGH)
					time.sleep(0.00000001)
					GPIO.output("P8_12",GPIO.LOW)
					time.sleep(0.00000001)
					j = j + 1
				
				j = 0
		
				while j in range(7):
					GPIO.output("P8_10",GPIO.LOW)
					GPIO.output("P8_12",GPIO.HIGH)
					time.sleep(0.00000001)
					GPIO.output("P8_12",GPIO.LOW)
					time.sleep(0.00000001)
					j = j + 1
				
				j = 0
					
				# display value
				GPIO.output("P8_14",GPIO.HIGH)
				time.sleep(0.00000001)
				GPIO.output("P8_14",GPIO.LOW)
				
				# increment column i
				i = i + 1
			
			# check column 
			elif i == 1:
				# send the bits
				# row // latch 2
				while j in range(8):
					GPIO.output("P8_10",GPIO.LOW)
					GPIO.output("P8_12",GPIO.HIGH)
					time.sleep(0.00000001)
					GPIO.output("P8_12",GPIO.LOW)
					time.sleep(0.00000001)
					j = j + 1
		
				j = 0
				
				# column // latch 1
				while j in range(1):
					GPIO.output("P8_10",GPIO.LOW)
					GPIO.output("P8_12",GPIO.HIGH)
					time.sleep(0.00000001)
					GPIO.output("P8_12",GPIO.LOW)
					time.sleep(0.00000001)
					j = j + 1
				
				j = 0
				
				while j in range(1):
					GPIO.output("P8_10",GPIO.HIGH)
					GPIO.output("P8_12",GPIO.HIGH)
					time.sleep(0.00000001)
					GPIO.output("P8_12",GPIO.LOW)
					time.sleep(0.00000001)
					j = j + 1
				
				j = 0
		
				while j in range(6):
					GPIO.output("P8_10",GPIO.LOW)
					GPIO.output("P8_12",GPIO.HIGH)
					time.sleep(0.00000001)
					GPIO.output("P8_12",GPIO.LOW)
					time.sleep(0.00000001)
					j = j + 1
				
				j = 0
					
				# display value
				GPIO.output("P8_14",GPIO.HIGH)
				time.sleep(0.00000001)
				GPIO.output("P8_14",GPIO.LOW)
				
				# increment column i
				i = i + 1

			elif i == 2:
				# send the bits
				# row // latch 2
				while j in range(8):
					GPIO.output("P8_10",GPIO.LOW)
					GPIO.output("P8_12",GPIO.HIGH)
					time.sleep(0.00000001)
					GPIO.output("P8_12",GPIO.LOW)
					time.sleep(0.00000001)
					j = j + 1
		
				j = 0
				
				# column // latch 1
				while j in range(2):
					GPIO.output("P8_10",GPIO.LOW)
					GPIO.output("P8_12",GPIO.HIGH)
					time.sleep(0.00000001)
					GPIO.output("P8_12",GPIO.LOW)
					time.sleep(0.00000001)
					j = j + 1
				
				j = 0
				
				while j in range(1):
					GPIO.output("P8_10",GPIO.HIGH)
					GPIO.output("P8_12",GPIO.HIGH)
					time.sleep(0.00000001)
					GPIO.output("P8_12",GPIO.LOW)
					time.sleep(0.00000001)
					j = j + 1
				
				j = 0
		
				while j in range(5):
					GPIO.output("P8_10",GPIO.LOW)
					GPIO.output("P8_12",GPIO.HIGH)
					time.sleep(0.00000001)
					GPIO.output("P8_12",GPIO.LOW)
					time.sleep(0.00000001)
					j = j + 1
				
				j = 0
					
				# display value
				GPIO.output("P8_14",GPIO.HIGH)
				time.sleep(0.00000001)
				GPIO.output("P8_14",GPIO.LOW)
				
				# increment column i
				i = i + 1

				################################################################################################################# i = 3
				
			elif i == 3:
				# send the bits
				# row // latch 2
				while j in range(8):
					GPIO.output("P8_10",GPIO.LOW)
					GPIO.output("P8_12",GPIO.HIGH)
					time.sleep(0.00000001)
					GPIO.output("P8_12",GPIO.LOW)
					time.sleep(0.00000001)
					j = j + 1
		
				j = 0
				
				# column // latch 1
				while j in range(3):
					GPIO.output("P8_10",GPIO.LOW)
					GPIO.output("P8_12",GPIO.HIGH)
					time.sleep(0.00000001)
					GPIO.output("P8_12",GPIO.LOW)
					time.sleep(0.00000001)
					j = j + 1
				
				j = 0
				
				while j in range(1):
					GPIO.output("P8_10",GPIO.HIGH)
					GPIO.output("P8_12",GPIO.HIGH)
					time.sleep(0.00000001)
					GPIO.output("P8_12",GPIO.LOW)
					time.sleep(0.00000001)
					j = j + 1
				
				j = 0
		
				while j in range(4):
					GPIO.output("P8_10",GPIO.LOW)
					GPIO.output("P8_12",GPIO.HIGH)
					time.sleep(0.00000001)
					GPIO.output("P8_12",GPIO.LOW)
					time.sleep(0.00000001)
					j = j + 1
				
				j = 0
					
				# display value
				GPIO.output("P8_14",GPIO.HIGH)
				time.sleep(0.00000001)
				GPIO.output("P8_14",GPIO.LOW)
				
				# increment column i
				i = i + 1
			
			elif i == 4:
				# send the bits
				# row // latch 2
				while j in range(8):
					GPIO.output("P8_10",GPIO.LOW)
					GPIO.output("P8_12",GPIO.HIGH)
					time.sleep(0.00000001)
					GPIO.output("P8_12",GPIO.LOW)
					time.sleep(0.00000001)
					j = j + 1
		
				j = 0
				
				# column // latch 1
				while j in range(4):
					GPIO.output("P8_10",GPIO.LOW)
					GPIO.output("P8_12",GPIO.HIGH)
					time.sleep(0.00000001)
					GPIO.output("P8_12",GPIO.LOW)
					time.sleep(0.00000001)
					j = j + 1
				
				j = 0
				
				while j in range(1):
					GPIO.output("P8_10",GPIO.HIGH)
					GPIO.output("P8_12",GPIO.HIGH)
					time.sleep(0.00000001)
					GPIO.output("P8_12",GPIO.LOW)
					time.sleep(0.00000001)
					j = j + 1
				
				j = 0
		
				while j in range(3):
					GPIO.output("P8_10",GPIO.LOW)
					GPIO.output("P8_12",GPIO.HIGH)
					time.sleep(0.00000001)
					GPIO.output("P8_12",GPIO.LOW)
					time.sleep(0.00000001)
					j = j + 1
				
				j = 0
					
				# display value
				GPIO.output("P8_14",GPIO.HIGH)
				time.sleep(0.00000001)
				GPIO.output("P8_14",GPIO.LOW)
				
				# increment column i
				i = i + 1
			
			elif i == 5:
				# send the bits
				# row // latch 2
				while j in range(8):
					GPIO.output("P8_10",GPIO.LOW)
					GPIO.output("P8_12",GPIO.HIGH)
					time.sleep(0.00000001)
					GPIO.output("P8_12",GPIO.LOW)
					time.sleep(0.00000001)
					j = j + 1
		
				j = 0
				
				# column // latch 1
				while j in range(5):
					GPIO.output("P8_10",GPIO.LOW)
					GPIO.output("P8_12",GPIO.HIGH)
					time.sleep(0.00000001)
					GPIO.output("P8_12",GPIO.LOW)
					time.sleep(0.00000001)
					j = j + 1
				
				j = 0
				
				while j in range(1):
					GPIO.output("P8_10",GPIO.HIGH)
					GPIO.output("P8_12",GPIO.HIGH)
					time.sleep(0.00000001)
					GPIO.output("P8_12",GPIO.LOW)
					time.sleep(0.00000001)
					j = j + 1
				
				j = 0
		
				while j in range(2):
					GPIO.output("P8_10",GPIO.LOW)
					GPIO.output("P8_12",GPIO.HIGH)
					time.sleep(0.00000001)
					GPIO.output("P8_12",GPIO.LOW)
					time.sleep(0.00000001)
					j = j + 1
				
				j = 0
					
				# display value
				GPIO.output("P8_14",GPIO.HIGH)
				time.sleep(0.00000001)
				GPIO.output("P8_14",GPIO.LOW)
				
				# increment column i
				i = i + 1
				
				# #####################################################################################################################
				
			elif i == 6:
				# send the bits
				# row // latch 2
				while j in range(8):
					GPIO.output("P8_10",GPIO.LOW)
					GPIO.output("P8_12",GPIO.HIGH)
					time.sleep(0.00000001)
					GPIO.output("P8_12",GPIO.LOW)
					time.sleep(0.00000001)
					j = j + 1
		
				j = 0
				
				# column // latch 1
				while j in range(6):
					GPIO.output("P8_10",GPIO.LOW)
					GPIO.output("P8_12",GPIO.HIGH)
					time.sleep(0.00000001)
					GPIO.output("P8_12",GPIO.LOW)
					time.sleep(0.00000001)
					j = j + 1
				
				j = 0
				
				while j in range(1):
					GPIO.output("P8_10",GPIO.HIGH)
					GPIO.output("P8_12",GPIO.HIGH)
					time.sleep(0.00000001)
					GPIO.output("P8_12",GPIO.LOW)
					time.sleep(0.00000001)
					j = j + 1
				
				j = 0
		
				while j in range(1):
					GPIO.output("P8_10",GPIO.LOW)
					GPIO.output("P8_12",GPIO.HIGH)
					time.sleep(0.00000001)
					GPIO.output("P8_12",GPIO.LOW)
					time.sleep(0.00000001)
					j = j + 1
				
				j = 0
					
				# display value
				GPIO.output("P8_14",GPIO.HIGH)
				time.sleep(0.00000001)
				GPIO.output("P8_14",GPIO.LOW)
				
				# increment column i
				i = i + 1
				
			elif i == 7:
				# send the bits
				# row // latch 2
				while j in range(8):
					GPIO.output("P8_10",GPIO.LOW)
					GPIO.output("P8_12",GPIO.HIGH)
					time.sleep(0.00000001)
					GPIO.output("P8_12",GPIO.LOW)
					time.sleep(0.00000001)
					j = j + 1
		
				j = 0
				
				# column // latch 1
				while j in range(7):
					GPIO.output("P8_10",GPIO.LOW)
					GPIO.output("P8_12",GPIO.HIGH)
					time.sleep(0.00000001)
					GPIO.output("P8_12",GPIO.LOW)
					time.sleep(0.00000001)
					j = j + 1
				
				j = 0
				
				while j in range(1):
					GPIO.output("P8_10",GPIO.HIGH)
					GPIO.output("P8_12",GPIO.HIGH)
					time.sleep(0.00000001)
					GPIO.output("P8_12",GPIO.LOW)
					time.sleep(0.00000001)
					j = j + 1
				
				j = 0
				
				# display value
				GPIO.output("P8_14",GPIO.HIGH)
				time.sleep(0.00000001)
				GPIO.output("P8_14",GPIO.LOW)
				
				# increment column i
				i = i + 1
	#^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
#initi()
#extract([105, 340, 400, 232, 19, 122, 236, 380])