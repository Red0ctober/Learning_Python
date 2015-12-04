from sys import exit
import time

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
			next_scene_name = current_scene.enter()
			current_scene = self.scene_map.next_scene(next_scene_name)

		# be sure to print out the last scene
		current_scene.enter()


class House(Scene):
	
	def enter(self):
		pass

class Field(Scene):
	
	def enter(self):
		pass

class TownShops(Scene):
	
	def enter(self):
		pass

class TownSquare(Scene):
	
	def enter(self):
		pass

class TownWaterfront(Scene):
	
	def enter(self):
		pass

class Map(object):

	scenes = {
		'home': House(),
		'farm': Field(),
		'shops': TownShops(),
		'Square': TownSquare(),
		'Waterfront': TownWaterfront(),
	}

	def __init__(self, start_scene):
		self.start_scene = start_scene

	def next_scene(self, scene_name):
		val = Map.scenes.get(scene_name)
		return val

	def opening_scene(self):
		return self.next_scene(self.start_scene)

a_map = Map()
a_game = Engine(a_map)
a_game.play()