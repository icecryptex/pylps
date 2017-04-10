import RPi.GPIO as gp
from time import sleep
gp.setmode(gp.BCM)
gp.setwarnings(False)

def sleepm(time):
	sleep(0.001*time)

def sleepu(time):
	sleep(0.00001*time)

class pylps:

	def __init__(self,*pins):	#TODO 8bit interfacing
		print "\ninitializing LCD\n================\n"
		if len(pins)==7:
			self.pin_d={
				"rs":pins[0],
				"rw":pins[1],
				"d0":pins[2],
				"d1":pins[3],
				"d2":pins[4],
				"d3":pins[5],
				"d4":pins[2],
				"d5":pins[3],
				"d6":pins[4],
				"d7":pins[5],
				"en":pins[6]
			}
			self.init_pins(self.pin_d)
		elif len(pins)==11:
			pass
	
	def init_pins(self,pin_d):
		print "setting pins as output:"
		for pin in self.pin_d:
			print "gpio" + str(pin_d[pin]) +" as " + str(pin)
			gp.setup(pin_d[pin],gp.OUT)
		
	def set_pin(self,pin,state):
		if state == 0:
			gp.output(pins[pin],gp.LOW)
		elif state == 1:
			gp.output(pins[pin],gp.HIGH)	
		
	def nibble(self,duration = 0.040 ):
		self.set_pin("en",1)
		sleepm(duration)
		self.set_pin("en",0)

	def send_set(self,data,delay = 0.04,init = False):	#set sent as rs,rw,d1,d2,d3,d4,d5,d6,d7
		data_l = self.hex_to_int_l(data)
		
		self.set_pin("rs",data[0])
		self.set_pin("rw",data[1])
		
		self.set_pin("d0",data[2])
		self.set_pin("d1",data[3])
		self.set_pin("d2",data[4])
		self.set_pin("d3",data[5])
		self.nibble()
		if init == False:
			self.set_pin("d4",data[6])
			self.set_pin("d5",data[7])
			self.set_pin("d6",data[8])
			self.set_pin("d7",data[9])
		 	self.nibble()
		sleepm(delay)

	def hex_to_int_l(self,data):
		data_l = list(map(int,"%011d"%int(bin(int(data,16))[2:])))
		print "hex: " + data + " = " + str(data_l)
		return data_l

	
#MAIN PROGRAM
#============
p = pylps(17,27,18,23,24,25,22)

p.hex_to_int_l("0x01")

#GPIO pins
#PIN	GPIO

#D4	18
#D5	23
#D6	24
#D7	25
#RS	17
#RW	27
#EN	22

