#!/usr/bin/env python3
# File name   : servo.py
# Description : Control Servos
# Author      : William
# Date        : 2019/11/21
from __future__ import division
import time
import Adafruit_PCA9685

'''
change this form 1 to 0 to reverse servos
'''
pwm0_direction = -1
pwm1_direction = 1
pwm2_direction = -1

pwm = Adafruit_PCA9685.PCA9685()
pwm.set_pwm_freq(50)

pwm0_init = 300
pwm0_range = 100
pwm0_max  = 500
pwm0_min  = 100
pwm0_pos  = pwm0_init

pwm1_init = 300
pwm1_range = 150
pwm1_max  = 450
pwm1_min  = 150
pwm1_pos  = pwm1_init

pwm2_init = 300
pwm2_range = 150
pwm2_max  = 450
pwm2_min  = 150
pwm2_pos  = pwm2_init


def turnLeft(coe=1):
	global pwm0_pos
	pwm0_pos = pwm0_init + int(coe*pwm0_range*pwm0_direction)
	pwm0_pos = ctrl_range(pwm0_pos, pwm0_max, pwm0_min)
	pwm.set_pwm(0, 0, pwm0_pos)


def turnRight(coe=1):
	global pwm0_pos
	pwm0_pos = pwm0_init - int(coe*pwm0_range*pwm0_direction)
	pwm0_pos = ctrl_range(pwm0_pos, pwm0_max, pwm0_min)
	pwm.set_pwm(0, 0, pwm0_pos)


def turnMiddle():
	global pwm0_pos
	pwm0_pos = pwm0_init
	pwm.set_pwm(0, 0, pwm0_pos)


def setPWM(num, pos):
	global pwm0_init, pwm1_init, pwm2_init, pwm0_pos, pwm1_pos, pwm2_pos
	pwm.set_pwm(num, 0, pos)
	if num == 0:
		pwm0_init = pos
		pwm0_pos = pos
	elif num == 1:
		pwm1_init = pos
		pwm1_pos = pos
	elif num == 2:
		pwm2_init = pos
		pwm2_pos = pos


def ctrl_range(raw, max_genout, min_genout):
	if raw > max_genout:
		raw_output = max_genout
	elif raw < min_genout:
		raw_output = min_genout
	else:
		raw_output = raw
	return int(raw_output)


def lookleft(speed):
	global pwm1_pos
	pwm1_pos += speed*pwm1_direction
	pwm1_pos = ctrl_range(pwm1_pos, pwm1_max, pwm1_min)
	pwm.set_pwm(1, 0, pwm1_pos)


def lookright(speed):
	global pwm1_pos
	pwm1_pos -= speed*pwm1_direction
	pwm1_pos = ctrl_range(pwm1_pos, pwm1_max, pwm1_min)
	pwm.set_pwm(1, 0, pwm1_pos)


def up(speed):
	global pwm2_pos
	pwm2_pos -= speed*pwm2_direction
	pwm2_pos = ctrl_range(pwm2_pos, pwm2_max, pwm2_min)
	pwm.set_pwm(2, 0, pwm2_pos)


def down(speed):
	global pwm2_pos
	pwm2_pos += speed*pwm2_direction
	pwm2_pos = ctrl_range(pwm2_pos, pwm2_max, pwm2_min)
	pwm.set_pwm(2, 0, pwm2_pos)


def servo_init():
	try:
		pwm.set_all_pwm(0, 300)
	except:
		pass
	pwm.set_pwm(0, 0, pwm0_init)
	pwm.set_pwm(1, 0, pwm1_init)
	pwm.set_pwm(2, 0, pwm2_init)


def clean_all():
	global pwm
	pwm = Adafruit_PCA9685.PCA9685()
	pwm.set_pwm_freq(50)
	pwm.set_all_pwm(0, 0)


def ahead():
	global pwm1_pos, pwm2_pos
	pwm.set_pwm(1, 0, pwm1_init)
	pwm.set_pwm(2, 0, pwm2_init)
	pwm1_pos = pwm1_init
	pwm2_pos = pwm2_init


def get_direction():
	return (pwm1_pos - pwm1_init)


if __name__ == '__main__':
	# print('%s/servo.py'%sys.path[0])
	# radar_scan()
	# turnRight()
	# time.sleep(1)
	# turnLeft()
	# time.sleep(1)
	# turnMiddle()
	# pwm.set_pwm(0, 0, 370)
	# for i in range(0,100):
	# 	up(1)
	# 	time.sleep(0.1)
	# 	print('1')
	pass