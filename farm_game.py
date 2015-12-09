from sys import exit
import game_time

#Moved gtime out of the engine in order to make it globally accessible.
gtime = game_time.Time()

class Scene(object):

	def enter(self):
		print "This is a standard scene, used in many more to come."
		exit(1)


class Engine(object):

	def __init__(self, scene_map):
		self.scene_map = scene_map

	def play(self):
		current_scene = self.scene_map.opening_scene()
		last_scene = self.scene_map.next_scene('finished')
		while current_scene != last_scene:
			next_scene_name, hours = current_scene.enter()
			new_day = gtime.advance_tod(hours)
			if new_day:
				print "The sun decends below the horizon as you walk."
				print "It is time to go home."
				current_scene =  self.scene_map.next_scene('home')
			else:
				current_scene = self.scene_map.next_scene(next_scene_name)

		# be sure to print out the last scene
		current_scene.enter()




class House(Scene):
	
	def enter(self):
		print "You are in your house."
		
		cur_loc = Actions('home')
		action = cur_loc.user_prompt('home')
		return (action)

class Field(Scene):
	
	def enter(self):
		print "You walk to your farm just outside your home.  There is"
		print "a field and a brilliant red barn.  Nearby is a tractor"
		print "painted a deep blue."
		print "\n"
		print "From here you can go into your house, or you could walk into"
		print "town."

		cur_loc = Actions('farm')
		action = cur_loc.user_prompt('farm')
		return (action)

class TownArea(Scene):

	def enter(self):
		print "You are just outside of town.  From here"
		print "you can go to any of the places in town or"
		print "back home."

		cur_loc = Actions('town')
		action = cur_loc.user_prompt('town')
		return (action)

class TownShops(Scene):
	
	def enter(self):
		shop_close_time = 19

		if gtime.current_time >= shop_close_time:
			print "You go to the shops near the town square but everything is closed."
			print "A sign on the door of Farming Supplies says their open hours are"
			print "between 7:00 and 19:00."

			cur_loc = Actions('shops')
			action = cur_loc.user_prompt('shops')
			return (action)

		else:
			print "You go to the shops by the town square.  There are a number"
			print "of them, but only one of them has what you need for farming."
			print "Called simply Farming Supplies, it has everything you could"
			print "possibly need."

			cur_loc = Actions('shops')
			action = cur_loc.user_prompt('shops')
			return (action)


class TownSquare(Scene):
	
	def enter(self):
		print "The town square is located at the center of town.  Many festivals"
		print "are held here each year."

		cur_loc = Actions('square')
		action = cur_loc.user_prompt('square')
		return (action)

class Waterfront(Scene):
	
	def enter(self):
		print "The crashing of waves is audible as you approach, announcing the ocean's presence long"
		print "before it can be seen.  As you reach the apex of the sandy dune the cool ocean air"
		print "whips your face.  You stand in awe of the ocean's might for a while.  After about an"
		print "hour, you decide to head back."

		gtime.advance_tod(1)

		cur_loc = Actions('waterfront')
		action = cur_loc.user_prompt('waterfront')
		return (action)


class EndOfGame(Scene):
	#There is currently no end game at this time.
	def enter(self):
		pass

class Map(object):

	scenes = {
		'home': House(),
		'farm': Field(),
		'town': TownArea(),
		'shops': TownShops(),
		'square': TownSquare(),
		'waterfront': Waterfront(),
		'finished': EndOfGame(),
	}

	def __init__(self, start_scene):
		self.start_scene = start_scene

	def next_scene(self, scene_name):
		val = Map.scenes.get(scene_name)
		return val

	def opening_scene(self):
		return self.next_scene(self.start_scene)

class Actions(object):

	def __init__(self, location):
		self.location = location

	def user_prompt(self, location):

		choice = raw_input("> ").lower()

		while choice == 'time' or choice == 'check time':
			print gtime.current_time
			choice = raw_input("> ").lower()

		while self.location == 'home':
			travel = {'farm': 0, 'town': 1}
			for i in travel:
				if i == choice:
					return i, travel[choice]
			

			print "That is not a place that you can go from here."
			print "Try these locations:"
			print travel
			choice = raw_input("> ").lower()

					
		while self.location == 'farm':
			travel = {'home': 0, 'town': 1}
			for i in travel:
				if i == choice:
					return i, travel[choice]

			print "That is not a place that you can go from here."
			print "Try these locations:"
			print travel
			choice = raw_input("> ").lower()

		while self.location == 'town':
			travel = {'shops': 0, 'waterfront': 1, 'square': 0, 'home': 1, 'farm': 1}
			for i in travel:
				if i == choice:
					return i, travel[choice]

			print "That is not a place that you can go from here."
			print "Try these locations:"
			print travel
			choice = raw_input("> ").lower()
					
		while self.location == 'shops':
			travel = {'town': 0, 'square': 0, 'waterfront': 1}
			for i in travel:
				if i == choice:
					return i, travel[choice]

			print "That is not a place that you can go from here."
			print "Try these locations:"
			print travel
			choice = raw_input("> ").lower()
					
		while self.location == 'square':
			travel = {'shops': 0, 'waterfront': 1, 'town': 0}
			for i in travel:
				if i == choice:
					return i, travel[choice]

			print "That is not a place that you can go from here."
			print "Try these locations:"
			print travel
			choice = raw_input("> ").lower()
					
		while self.location == 'waterfront':
			travel = {'town': 1, 'shops': 1, 'square': 1}
			for i in travel:
				if i == choice:
					return i, travel[choice]

			print "That is not a place that you can go from here."
			print "Try these locations:"
			print travel
			choice = raw_input("> ").lower()
	
a_map = Map('home')
a_game = Engine(a_map)
a_game.play()