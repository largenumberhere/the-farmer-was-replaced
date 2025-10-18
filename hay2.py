def make_drone(x):
	import mover
	mover.move_to(x, 0)
	def hay_task():
		while True:
			for i in [0]:
			#for i in range(get_world_size()):
				#if num_items(Items.Hay) >= 1000000:
					#return
				if can_harvest():
					harvest()
				move(North)
		#move(East)
	return hay_task
	
children = []
for x in range(get_world_size()):
	hay_task = make_drone(x)
	drone = spawn_drone(hay_task)
	if drone == None:
		break
	children.append(drone)

#hay_task = make_drone(0)
hay_task()
for drone in children:
	wait_for(drone)
	