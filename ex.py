
def create_dict():
	countries = {
	"usa":"newyork",
	"palestine":"jerusalem",
	"jorden":"amman",	}
	return countries

def sound_dict():
	animal={
	"cat":"miaw",
	"dog":"aw",
	}	
	return animal 
"""
def print_put(capital, country):
	print country + " " +capital[country]
"""
def put( animals,sounds):
	print sounds  +" "+sounds[animals]

def main ():
	capital = create_dict()
	animals = sound_dict()
	# for country in capital:
		 
		# print_put(capital,country)
	"""
	greetings=["hi","nihau","ahlan","ciao","bonjour"]

	for greeting in greetings:
		print greeting
	for i in range(len(greetings)):
		print greetings[i]+" number "+str(i)
	greetings_dict={"usa":"hi",
	"france":"bonjour",
	"palestine":"ahlan", }
	"""

	
	sound=raw_input("enter your sounds, or enter to quit:")
	while (sound != ""):
		if sound in animals:
			print animals[sound]+" form " + sound
			 
		else:
			print "no sounds found , try again"
		sound=raw_input("enter your sounds, or enter to quit:") 
 

	coun=raw_input("enter your coun, or enter to quit:")
	while (coun != ""):
		if (coun in  greetings_dict):
			print greetings_dict[coun]+" form " + coun
			 
		else:
			print "no coun found , try again"
		coun=raw_input("enter your coun, or enter to quit:") 
	#print greetings_dict[coun]+" " + coun



if __name__ == "__main__":
	main()

