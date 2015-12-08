#This module tracks and advances time as activities are done.

class Time(object):

	def __init__(self):
		self.day = 1
		self.current_time = 8
		#print self.day
		#print self.current_time

#This function advances the time of day by the number of specified hours.
#In the even that an activity takes more than one, it can accommodate.
#Condensed the two functions in this class into just this one.
	def advance_tod(self, hours):  
		self.current_time = self.current_time + hours
		new_day = False
		if self.current_time >= 21:
			self.day = self.day + 1
			self.current_time = 8
			new_day = True
		return new_day

