from gpacalc import gpaCalc
from parse import parseGPAFile

##########	#########	   ##
#		#	#	  #  #
#		#	#	 #    #
#		#	#	#      #
#    ######	#########      ##########
#	#	#	      #		 #
#	#	#	     #		  #
#########	#	    #		   #

''' A no frills driver for calculating a very rough gpa '''



def main():
	gpafile = raw_input("Input file: ")
	openfile = 0 
	try:
		openfile = open(gpafile,'r')		
	except (IOError, ValueError, TypeError):
		print "File cannot be opened. \n"
	else:
		calculator = gpaCalc()
		parser = parseGPAFile(openfile)
		parser.parse()
		for x in parser.seperate():
			calculator.addScore(x)
		print calculator.gpa
		

if __name__ == "__main__":
	main()	



