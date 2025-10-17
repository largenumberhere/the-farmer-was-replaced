import mover

def new(min_x, min_y, max_x, max_y):
	def main():
		while True:
			mover.move_to(min_x, min_y)
			for i in range(max_y- min_y):
				for j in range(max_x - min_x):
					
					if not (get_ground_type() == Grounds.Grassland):
						till()
					if can_harvest():
						harvest()
					if not (get_entity_type() == Entities.Grass):
						plant(Entities.Grass)	
					move (East)
				move(North)
				for j in range(max_y - min_y):
					move(West)
			move(North)
	return main
			
if __name__ == "__main__":
	main = new(24,17,28,21)
	main()

	
def make_drone(min_x, min_y, max_x, max_y):
	main = new(min_x, min_y, max_x, max_y)
	return main