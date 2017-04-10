def available_commands():	#TODO
	pass

characters_d={
	"c_a":"0x261",
	"c_b":"0x262",
	"c_c":"0x263",
	"c_d":"0x264",
	"c_e":"0x265",
	"c_f":"0x266",
	"c_g":"0x267",
	"c_h":"0x268",
	"c_i":"0x269",
	"c_j":"0x26A",
	"c_k":"0x26B",
	"c_l":"0x26C",
	"c_m":"0x26D",
	"c_n":"0x26E",
	"c_o":"0x26F",
	"c_p":"0x270",
	"c_q":"0x271",
	"c_r":"0x272",
	"c_s":"0x273",
	"c_t":"0x274",
	"c_u":"0x275",
	"c_v":"0x276",
	"c_w":"0x277",
	"c_x":"0x278",
	"c_y":"0x279",
	"c_z":"0x27A",
	"c_.":"0x22E",
	"c_ ":"0x220",
	"c_err":"0x2DB",

}

def get_char(c):
	##print "print:'" + c + "'" 
	char = "c_" + c.lower()
	try:
		 char_hex = characters_d[char]
	except:
		char_hex = characters_d["c_err"]
		print "-Unknown character '" + str(c) + "' replacing with square"
	if c.isupper() == True:
		return up(char_hex)
	else:
		return char_hex

def up(data):
	return hex(int(data,16) - int("0x020",16))
def goto(x,y)
	pass
