import mover

def new(min_x, min_y, max_x, max_y):
	_min_x = -1 
	_min_y = -1
	_max_x = -1
	_max_y = -1
	(_min_x, _min_y, _max_x, _max_y) = (min_x, min_y, max_x, max_y)

	def ensure_tilled():
		if get_ground_type() != Grounds.Soil:
			till()
		
	def farm():
		ensure_tilled()
		if can_harvest():
			harvest()
		if get_entity_type() != Entities.Carrot:
			plant(Entities.Carrot)	
	

	def main():
		mover.move_to(_min_x,_min_y)
		
		dir = North
		
		while True:
			if dir == North:
				while get_pos_y() < _max_y-1:
					farm()
					move(dir)
				farm()
				move(East)
				
				dir = South
			elif dir == South:
				while get_pos_y() > 0:
					farm()
					move(dir)
				farm()
				move(East)
				
				dir = North
			if get_pos_x() >= _max_x-1 and get_pos_y() >= _max_y-1:
				mover.move_to(_min_x,_min_y)
				dir = North
	return (main)

if __name__ == "__main__":
	main = new(0, 0, 9, 9)
	main()
