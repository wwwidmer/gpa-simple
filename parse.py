
'''
# Parse GPA File
# Constructor ( file openfile ) *
# Can also be a list because the iteration is just (for x in y)

# Parse ()
# Checks file is valid and appends all 'lines' in file to a class variable. 
# rstrip removes whitespace and new line characters
# Returns all lines in a list
# If file is not open / invalid Returns 0

# Seperate ()
# Splits all lines with by " " and appends to a local variable
# Returns one list of all lines split. 

# Example:
 File f = file.txt
 file.txt = a b c
  d ab a a d 
 d b+

parse returns
["a b c"]
[" d ab a a d"]
["d b+"]

seperate returns
["a","b","c","d","ab","a","a","d","d","b+"]

Incorrect values are not filtered out but do not create errors in other parts of code.

'''
class parseGPAFile(object):
	def __init__(self,openfile):
		self.file = openfile
		self.lines = []

	def parse(self):
		if self.file:
			for line in self.file:
				self.lines.append(line.rstrip())
			return self.lines
		else:
			print "No file open. "
			return 0
	def seperate(self):
		seperatedLines = []
		for line in self.lines:
			seperatedLines = seperatedLines + line.split(" ")
		return seperatedLines
