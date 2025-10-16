while True:
	for i in range(3):
		if not (get_ground_type() == Grounds.Grassland):
			till()
		if can_harvest():
			harvest()
		if not (get_entity_type() == Entities.Grass):
			plant(Entities.Grass)	
		move (East)
	move(North)