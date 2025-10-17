import mover

set_world_size(3)
set_execution_speed(1)

directions = [North, East, South, West]

def dir_to_coord(dir):
	x = get_pos_x()
	y = get_pos_y()
	
	if dir == North:
		y += 1
	elif dir == South:
		y -= 1
	elif dir == West:
		x -= 1
	elif dir == East:
		x += 1

	if x < 0:
		x = None
	elif x >= get_world_size()-1:
		x = North
	
	if y < 0:
		y = None
	elif y >= get_world_size()-1:
		y = None
	
	if x==None or y==None:
		return None

	return (x, y)

def goto(coords):
	mover.move_to(coords[0], coords[1])

visited = []
def explore(list):
	for dir in directions:
		if dir_to_coord(dir) not in visited:
			if move(dir):
				list.append(dir)
				explore(list)
		visited.append(dir_to_coord(dir))
	list.pop()			
	
	

chest = measure()
while True:
	goto((0,0))
	plant(Entities.Bush)
	n = 2 ** (num_unlocked(Unlocks.Mazes)-1)
	use_item(Items.Weird_Substance, get_world_size() * n)

	if get_entity_type() == Entities.Treasure:
		harvest()
		continue

	
	while get_entity_type() != Entities.Treasure:
		dir_pos = random() * 4 // 1
		dir = directions[dir_pos]
		move(dir)
			
	harvest()

	

	# item = stack.pop()
	# worked = move(item)
	# if worked:
		# facing = item
		# if get_entity_type() != Entities.Hedge:
			# harvest()
			# break
			
		# for dir in directions:
			# if dir == facing:
				# stack.append(dir)
		

goto((0, 0))
while True:
	
		
	pass