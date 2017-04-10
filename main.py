import RPi.GPIO as gp
from time import sleep
import display_commands as dc
gp.setmode(gp.BCM)
gp.setwarnings(False)


def sleepu(time):
	sleep(0.00001*time)

class pylps:
	global sleepm
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
	def sleepm(time):
		sleep(0.001*time)
	
	def init_pins(self,pin_d):
		print "setting pins as output:"
		for pin in self.pin_d:
			print "gpio" + str(pin_d[pin]) +" as " + str(pin)
			gp.setup(pin_d[pin],gp.OUT)
		
	def set_pin(self,pin,state):
		if state == 0:
			gp.output(self.pin_d[pin],gp.LOW)
		elif state == 1:
			gp.output(self.pin_d[pin],gp.HIGH)	
		
	def nibble(self,duration = 0.040 ):
		self.set_pin("en",1)
		sleepm(duration)
		self.set_pin("en",0)

	def send_set(self,data,delay = 0.04,init = False):	#set sent as rs,rw,d1,d2,d3,d4,d5,d6,d7
		data_l = self.hex_to_int_l(data,init)
		self.set_pin("rs",data_l[0])
		self.set_pin("rw",data_l[1])
		
		self.set_pin("d7",data_l[2])
		self.set_pin("d6",data_l[3])
		self.set_pin("d5",data_l[4])
		self.set_pin("d4",data_l[5])
		self.nibble()
		if init == False:
			self.set_pin("d3",data_l[6])
			self.set_pin("d2",data_l[7])
			self.set_pin("d1",data_l[8])
			self.set_pin("d0",data_l[9])
			self.nibble()
		sleepm(delay)

	def hex_to_int_l(self,data,db = False):
		data_l = list(map(int,"%010d"%int(bin(int(data,16))[2:])))
		if db == True:
			print "- hex: " + data + " = " + str(data_l)
		return data_l

	def init_4bit(self):
		print "Initializing 4 bit mode\n======================="
		sleepm(20)	#initialize 4 pins
		self.send_set("30",4.1,True)
		self.send_set("30",0.1,True)
		self.send_set("30",4.1,True)
		self.send_set("20",5,True)
		print "- Init done\n\nSetting display to normal state"		
		self.send_set("14")		#function set: 2 lines 4x8 font
		self.send_set("08")		#display off cursor off blink off
		self.send_set("01",1.7)		#clear screen and home
		self.send_set("06")		#inc cursor when writing
		self.send_set("0f")		#screen on blink on cursor on 
		print"- State set\nREADY...\n\n"
		#for x in range(80):
		#	self.send_set("241")

	def write(self,text):
		print "Writing: " + str(text)
		text_l = list(text)
		for i in range(len(text_l)):
			self.send_set(dc.get_char(text_l[i]))
	


#MAIN PROGRAM
#============
p = pylps(17,27,18,23,24,25,22)
p.init_4bit()
p.write("Testing.AaAaAaAaA...   hehe!#%&")
#GPIO pins
#PIN	GPIO

#D4	18
#D5	23
#D6	24
#D7	25
#RS	17
#RW	27
#EN	22

