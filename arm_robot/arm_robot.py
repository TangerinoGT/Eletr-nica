#https://github.com/adafruit/Adafruit_Python_PCA9685/tree/master/examples

# Simple demo of of the PCA9685 PWM servo/LED controller library.
# This will move channel 0 from min to max position repeatedly.
# Author: Tony DiCola
# License: Public Domain
from __future__ import division
import time

# Import the PCA9685 module.
import Adafruit_PCA9685

# leitura teclado
import termios, tty, sys

# The getch method can determine which key has been pressed
# by the user on the keyboard by accessing the system files
# It will then return the pressed key as a variable
def getch():
	fd = sys.stdin.fileno()
	old_settings = termios.tcgetattr(fd)
	try:
		tty.setraw(sys.stdin.fileno())
		ch = sys.stdin.read(1)
	finally:
		termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
	return ch

# Uncomment to enable debug output.
#import logging
#logging.basicConfig(level=logging.DEBUG)

# Initialise the PCA9685 using the default address (0x40).
pwm = Adafruit_PCA9685.PCA9685()

# Alternatively specify a different address and/or bus:
#pwm = Adafruit_PCA9685.PCA9685(address=0x41, busnum=2)

# Configure min and max servo pulse lengths
servo_min = 150  # Min pulse length out of 4096
servo_max = 600  # Max pulse length out of 4096


# Helper function to make setting a servo pulse width simpler.
def set_servo_pulse(channel, pulse):
    pulse_length = 1000000    # 1,000,000 us per second
    pulse_length //= 60       # 60 Hz
    print('{0}us per period'.format(pulse_length))
    pulse_length //= 4096     # 12 bits of resolution
    print('{0}us per bit'.format(pulse_length))
    pulse *= 1000
    pulse //= pulse_length
    pwm.set_pwm(channel, 0, pulse)

# Set frequency to 60hz, good for servos.
pwm.set_pwm_freq(60)

meio=(servo_max-servo_min)//2+servo_min
j1 = meio
j2 = meio
j3 = meio
j4 = meio
j5 = meio
garra = meio

passo=5

print('J1:q/a, J2:w/s, J3:e/d, J4:r/f, J5:t/g, garra: y/h, press x, then Ctrl-C to quit...')
while True:

	k = getch()
	#print(k)
	
	if k == 'q':
		if j1 < (servo_max-passo):
			j1 +=passo
		else:
			j1 = servo_max
		pwm.set_pwm(0, 0, j1)
		print "Junta 1 = ", j1

		
	if k == 'a':
		if j1 > (servo_min+passo):
			j1 -=passo
		else:
			j1 = servo_min
		pwm.set_pwm(0, 0, j1)
		print "Junta 1 = ", j1

	if k == 's':
		if j2 < (servo_max-passo):
			j2 +=passo
		else:
			j2 = servo_max
		pwm.set_pwm(1, 0, j2)
		pwm.set_pwm(2, 0, j2)
		print "Junta 2 = ", j2

		
	if k == 'w':
		if j2 > (servo_min+passo):
			j2 -=passo
		else:
			j2 = servo_min
		pwm.set_pwm(1, 0, j2)
		pwm.set_pwm(2, 0, j2)
		print "Junta 2 = ", j2

	if k == 'd':
		if j3 < (servo_max-passo):
			j3 +=passo
		else:
			j3 = servo_max
		pwm.set_pwm(3, 0, j3)
		print "Junta 3 = ", j3

		
	if k == 'e':
		if j3 > (servo_min+passo):
			j3 -=passo
		else:
			j3 = servo_min
		pwm.set_pwm(3, 0, j3)
		print "Junta 3 = ", j3

	if k == 'r':
		if j4 < (servo_max-passo):
			j4 +=passo
		else:
			j4 = servo_max
		pwm.set_pwm(4, 0, j4)
		print "Junta 4 = ", j4

		
	if k == 'f':
		if j4 > (servo_min+passo):
			j4 -=passo
		else:
			j4 = servo_min
		pwm.set_pwm(4, 0, j4)
		print "Junta 4 = ", j4
		
	if k == 't':
		if j5 < (servo_max-passo):
			j5 +=passo
		else:
			j5 = servo_max
		pwm.set_pwm(5, 0, j5)
		print "Junta 5 = ", j5

		
	if k == 'g':
		if j5 > (servo_min+passo):
			j5 -=passo
		else:
			j5 = servo_min
		pwm.set_pwm(5, 0, j5)
		print "Junta 5 = ", j5

	if k == 'y':
		if garra < (servo_max-passo):
			garra +=passo
		else:
			garra = servo_max
		pwm.set_pwm(6, 0, garra)
		print "Garra = ", garra

		
	if k == 'h':
		if garra > (servo_min+passo):
			garra -=passo
		else:
			garra = servo_min
		pwm.set_pwm(6, 0, garra)
		print "Garra = ", garra

	if k == 'x':
		print "Programa encerrado"
		exit()


    # Move servo on channel O between extremes.
    #pwm.set_pwm(0, 0, servo_min)
    #pwm.set_pwm(1, 0, servo_min)
    #time.sleep(1)
    #pwm.set_pwm(0, 0, servo_max)
    #pwm.set_pwm(1, 0, servo_max)
    #time.sleep(1)

