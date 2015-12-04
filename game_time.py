#This module tracks and advances time as activities are done.

class Time(object):

	def __init__(self):
		self.day = 1
		self.current_time = 8
		print self.day
		print self.current_time

#This function advances the time of day by the number of specified hours.
#In the even that an activity takes more than one, it can accommodate.
	def advance_tod(self, hours):  
		self.current_time = self.current_time + hours
		#print self.current_time

#This should advance the player to the next day and set the time to be 8 again.
#Need to test in actual system.
	def advance_day(self):
		if self.current_time >= 21:
			self.day = self.day + 1
			self.current_time = 8
			return 'home'

x = Time()
#x.advance_tod(12)
#x.advance_day()
#print x.day
#print x.current_time