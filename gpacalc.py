'''
# GPA CALC 
# Constructor ()
# initializes GPA to 0 and an empty list of scores
# 
# Convert Score (string a)
# defines the letterMap for Letter Grades (Very Rough, school values can be different, A+,F,D-,D+ Not included but are trivial to add. You would need to change return 0 to NULL if F was included.
)
# Returns Float value of letter Grade

# Add Score ( string x)
# Checks that the score can be converted then
# appends the converted score of x to the list

# Update
# Changes the GPA based on the new number of grades
# Iterates scores, adds to a running total, divides by total


'''

import unittest

class gpaCalc(object):
	def __init__(self):
		self.gpa = 0
		self.scores = []
		
	def convertScore(self,a):
		letterMap = {"a":4.0,"b":3.0,"c":2.0,"d":1.0, "a-":3.5,"b+":3.25,"b-":2.75,"c+":2.5,"c-":1.5}
		if letterMap.has_key(a.lower()):
			return letterMap[a.lower()]
		else:
			print "Incorrect letter grade \n"
			return 0

	def addScore(self,x):	
		if self.convertScore(x) != 0:
			self.scores.append(self.convertScore(x))			
			self.update()
			return 1
		else:
			return 0
	def update(self):
		length = len(self.scores)
		total = 0
		for x in self.scores:
			total = total + x
		self.gpa = float(total / length)
		return total

class gpaCalcTest(unittest.TestCase):
	def setUp(self):
		self.gpa = gpaCalc()
	def test_a(self):
		self.gpa.addScore("a")
		value = self.gpa.gpa
		self.assertEquals(4, value)
	def test_ab(self):
		self.gpa.addScore("a")
		self.gpa.addScore("b")
		value = self.gpa.gpa
		self.assertEquals(3.5, value)
	def test_abcpluscminus(self):
		self.gpa.addScore("a")
		self.gpa.addScore("b")		
		self.gpa.addScore("c+")
		self.gpa.addScore("c-")
		value = self.gpa.gpa
		self.assertEquals(2.75, value)
	def test_zero(self):
		value = self.gpa.gpa
		self.assertEquals(0, value)
	def test_total(self):
		self.gpa.addScore("a")
		self.gpa.addScore("b")		
		self.gpa.addScore("b")
		self.gpa.addScore("b+")		
		self.gpa.addScore("a")		
		self.gpa.addScore("a")	
		value = self.gpa.update()
		self.assertEquals(21.25, value)
	
