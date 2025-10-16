import mover

def new():
	_min_x = -1
	_max_x = -1
	_max_y = -1
	_min_y = -1

	world_size = get_world_size()


	op_facing = {North : South, South : North, West : East, East : West}

	def move2(direction):
		return mover.wrapped_move(direction, _min_x, _min_y, _max_x, _max_y)
		
	def main(min_x, min_y, max_x, max_y):
		global _min_x
		global _max_x
		global _min_y
		global _max_y
		
		_min_x = min_x
		_max_x = max_x
		_max_y = max_y
		_min_y = min_y
		
		mover.move_to(min_x, min_y)
		width_x = max_x - min_x
		width_y = max_y - min_y
		facing = North
		while True:
			bad_count = 0
			for i in range(width_x):
				for j in range(width_y):
					ground_type = get_ground_type()		
					if ground_type != Grounds.Soil:
						till()
					entity_type = get_entity_type()	
					if entity_type == Entities.Dead_Pumpkin:
						bad_count += 1
					if entity_type != Entities.Pumpkin:
						if can_harvest():
							harvest()
						plant(Entities.Pumpkin)			
					
					if j != width_y-1:
						move2(facing)
					
				facing = op_facing[facing]
				move2(East)
				
								
				
			if bad_count == 0:
				while get_entity_type() == Entities.Pumpkin and not can_harvest():
					pass
				if get_entity_type() != Entities.Dead_Pumpkin:
					harvest()
				else:
					plant(Entities.Pumpkin)
	return (main)

#_set_min_x = -1
#_set_min_y = -1
#_set_max_x = -1
#_set_max_y = -1

#def main2():
	#main(_set_min_x, _set_min_y, _set_max_x, _set_max_y)
		
def make_drone(min_x, min_y, max_x, max_y):
	def main2():
		main = new()
		main(min_x, min_y, max_x, max_y)
	return main2
	
	#global _set_min_x
	##global _set_min_y
	#global _set_max_x
	#global _set_max_y
	
	#_set_max_x = max_x
	#_set_min_x = min_x
	#_set_max_y = max_y
	#_set_min_y = min_y
	#return main2

if __name__ == "__main__":
	main = new()
	
	main(0, 0, 8, 8)