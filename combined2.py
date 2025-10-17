import pumpkin_task
import basics_task
import carrots_task
import hay_task

def task1():
	while True:
		# print("meow")
		move(North)
		do_a_flip()
		move(South)
		do_a_flip()

#set_world_size(22)

drones = []
tasks = [
	pumpkin_task.make_drone(0,0,8,8), 
	pumpkin_task.make_drone(0,9,8,17), 
	basics_task.make_drone(10,0,24,16),
	basics_task.make_drone(0, 17, 8, 32),
	basics_task.make_drone(8, 17, 16, 32),
	basics_task.make_drone(16, 17, 24, 32),
	hay_task.make_drone(24,17,28,21)
]
for i in range(len(tasks)):
	drone = spawn_drone(tasks[i])
	if drone == None:
		break
	drones.append(drone)

for d in drones:
	print(d)
	
while True:
	main = basics_task.new(24,0,32,16)
	main()
	pass
