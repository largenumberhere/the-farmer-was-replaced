import mover
def new(min_x, min_y, max_x, max_y):
	(_min_x, _min_y, _max_x, _max_y) = (min_x, min_y, max_x, max_y)

	_op_facing = {North : South, South : North, West : East, East : West}

	def move2(direction):
		return mover.wrapped_move(direction, _min_x, _min_y, _max_x, _max_y)
	
	def make_maze():
		use_item(Items.Weird_Substance, 2**num_unlocked(Unlocks.Mazes)-1)
	
	def farm():
		entity = get_entity_type()
		ground = get_ground_type()
		x = get_pos_x()
		y = get_pos_y()
		if x <= _min_x+1:
			if entity != Entities.Bush:
				plant(Entities.Bush)
			if can_harvest():
				if num_items(Items.Weird_Substance) > num_items(Items.Gold):
					make_maze()
				harvest()
				plant(Entities.Bush)
		elif x == _max_x-1:
			if ground != Grounds.Soil:
				till()
			if can_harvest():
				harvest()
				plant(Entities.Cactus)
			if entity != Entities.Cactus:
				plant(Entities.Cactus)
		elif x <= _min_x+2:
			if entity != Entities.Bush:
				plant(Entities.Bush)
			if can_harvest():
				use_item(Items.Weird_Substance)
				harvest()
				plant(Entities.Bush)
		elif (y >= _max_y-4):
			if can_harvest():
				harvest()
				plant(Entities.Sunflower)
			if ground != Grounds.Soil:
				till()
			if entity != Entities.Sunflower:
				plant(Entities.Sunflower)
				
		elif (x + y) %2 == 0:
			if can_harvest():
				harvest()
				plant(Entities.Tree)
			if entity != Entities.Tree:
				plant(Entities.Tree)
		elif x %3:
			if ground != Grounds.Soil:
				till()
			if can_harvest():
				harvest()
				plant(Entities.Carrot)
			if entity != Entities.Carrot:
				plant(Entities.Carrot)
		elif x %7:
			if can_harvest():
				harvest()
			if ground != Grounds.Grassland:
				till()
			
		
	def main():
		width_x = _max_x - _min_x
		width_y = _max_y - _min_y
		
		global _min_x
		global _max_x
		global _min_y
		global _max_y
		
   
		
		
		mover.move_to(_min_x, _min_y)
		
		facing = North
		while True:
			for i in range(_min_x, width_x + _min_x):
				for j in range(_min_y, width_y + _min_y):
					farm()
					
					if j != _max_y-1:
						move2(facing)
					else:
						move2(East)
				
				facing = _op_facing[facing]
	
	return (main)
		
def make_drone(min_x, min_y, max_x, max_y):
	main = new(min_x, min_y, max_x, max_y)
	return main

if __name__ == "__main__":
	main = new(6, 0, 16, 16)
	main()