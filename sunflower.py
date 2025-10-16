while True:
	
	for i in range(5):
		if get_ground_type() != Grounds.Soil:
			till()
		
		if get_entity_type() != Entities.Sunflower:
			plant(Entities.Sunflower)
		
		if can_harvest():
			harvest()
		
		move(North)
		