while True:
	move(North)
	for i in range(3):
		if (not get_ground_type() == Grounds.Grassland):
			till()
		if can_harvest():
			harvest()
		if (not get_entity_type() == Entities.Bush):
			plant(Entities.Bush)
		
		move(East)