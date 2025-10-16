import mover

_op_facing = {North : South, South : North, West : East, East : West}

def move2(direction):
	return mover.wrapped_move(direction, _min_x, _min_y, _max_x, _max_y)

def farm():
	entity = get_entity_type()
	ground = get_ground_type()
	x = mover.cached_x()
	y = mover.cached_y()
	if x <= _min_x+1:
		if entity != Entities.Bush:
			plant(Entities.Bush)
		if can_harvest():
			if num_items(Items.Weird_Substance) > num_items(Items.Gold):
				use_item(Items.Weird_Substance, 3)
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
			use_item(Items.Weird_Substance, 1)
			harvest()
			plant(Entities.Bush)
	elif (y >= _max_y-9):
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
		
	
def main(min_x, min_y, max_x, max_y):
	width_x = max_x - min_x
	width_y = max_y - min_y
	
	global _min_x
	global _max_x
	global _min_y
	global _max_y
	
	_min_x = min_x
	_max_x = max_x
	_max_y = max_y
	_min_y = min_y
	
	
	mover.move_to(min_x, min_y)
	
	facing = North
	while True:
		for i in range(min_x, width_x+min_x):
			for j in range(min_y, width_y+min_y):
				
				farm()
				
				if j != max_y-1:
					move2(facing)
				else:
					move2(East)
			
			facing = _op_facing[facing]


_set_min_x = -1
_set_min_y = -1
_set_max_x = -1
_set_max_y = -1

def main2():
	main(_set_min_x, _set_min_y, _set_max_x, _set_max_y)
		
def make_drone(min_x, min_y, max_x, max_y):
	global _set_min_x
	global _set_min_y
	global _set_max_x
	global _set_max_y
	
	_set_max_x = max_x
	_set_min_x = min_x
	_set_max_y = max_y
	_set_min_y = min_y
	return main2

if __name__ == "__main__":
	main(6, 0, 16, 16)