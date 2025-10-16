

def run():
	while True:
		
		if get_water() < 0.75:
			use_item(Items.Water)
		move(North)
		if get_ground_type() != Grounds.Soil:
			till()
		if can_harvest():
			harvest()
		plant(Entities.Cactus)
	
clear()
spawn_drone(run)
move(East)
run()

