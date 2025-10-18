
def new(x):
	def run():
		import mover
		mover.move_to(x, 0)
		while True:
			#if num_items(Items.Cactus) >= 1000000:
			#    return
			
			if get_water() < 0.75:
				use_item(Items.Water)
			move(North)
			if get_ground_type() != Grounds.Soil:
				till()
			if can_harvest():
				harvest()
			plant(Entities.Cactus)
	return run
clear()

drones = []
for i in range(get_world_size()):
	if i == get_world_size()-1:
		continue
	run = new(i)
	drone = spawn_drone(run)
	if drone != None:
		drones.append(drone)
run = new(get_world_size()-1)
run()
for drone in drones:
	wait_for(drone)

