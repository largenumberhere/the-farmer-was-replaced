import pumpkin_task
import basics_task
import snake_task

def task1():
	while True:
		# print("meow")
		move(North)
		do_a_flip()
		move(South)
		do_a_flip()

set_world_size(22)

drones = []
tasks = [pumpkin_task.make_drone(0,0,8,8), basics_task.make_drone(8,0,16,16), pumpkin_task.make_drone(0,9,8,17)]
for i in range(len(tasks)):
	drone = spawn_drone(tasks[i])
	if drone == None:
		break
	drones.append(drone)

for d in drones:
	print(d)
	
while True:
	#basics_task.make_drone(8,0,16,20)()
	pass
