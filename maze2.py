def delay(ticks):
	for i in range(ticks):
		pass

import mover
def main(id):
	
	mover.move_to(id,0)
	delay(8000)
	if get_ground_type() != Grounds.Soil:
		till()
	plant(Entities.Bush)
	
	while True:
		use_item(Items.Weird_Substance, 2 ** num_unlocked(Unlocks.Mazes) -1)
		harvest()
		plant(Entities.Bush)
		

def run_drones_to_completion(func_func, count):
	drones = []
	for i in range(count-1):
		drone = spawn_drone(func_func(i))
		if drone == None:
			return False
		drones.append(drone)
	
	func = func_func(count-1)
	func()
	for d in drones:
		wait_for(drone)
			
	return True
	
	
def main_ctor(size):
	def f():
		main(size)
	return f
	
run_drones_to_completion(main_ctor, 32)