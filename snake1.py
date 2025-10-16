import mover

def nearest_even(x):
	if x<= 0:
		return 0
	elif x%2==0:
		return x
	else:
		return x-1

def nearest_odd(x):
	if x<=1:
		return 0
	elif x%2==1:
		return x
	else:
		return x-1

next_apple = measure()
facing = North
next_facing = {North:East, East:South, South:West, West:North}
prev_facing = {East:North, South:East, West:South, North:West}
up_of = {North:(0, 1), East: (1, 0), South: (0, -1), West: (-1, 0)}
right = True

def is_edge(x,y, direction):
	if x == 0 and direction == West:
		return True
	elif x == get_world_size()-1 and direction == East:
		return True
	elif x == get_world_size()-1 and direction == South:
		return True
	
	elif y == 0 and direction == South:
		return True
	elif y == get_world_size()-1 and direction == North:
		return True
	elif x== get_world_size()-1 and y==get_world_size()-1:
		return True
	else:
		return False

op_dir = {North:South, South:North}

def move_dig(direction):
	global next_apple
	global apples
	global extra_apples
	
	if get_entity_type() == Entities.Apple:
		apples += 1
		extra_apples += 1
		next_apple = measure()
		
	return move(direction)
	
		

def walk(safe):
	global apples
	global next_apple
	global extra_apples
	extra_apples = 0
	next_apple = None
	applies = 0
	
	
	dir = North
	move_dig(dir)
	i = 0
	max_size = get_world_size()*2 - 3
	small_snake = apples <= max_size
	while i < get_world_size():
		j = 0
		while j < get_world_size()-2:
			move_dig(dir)
			j +=1
		if dir == North and small_snake and (not safe):
			if next_apple == None:
				break
			if get_pos_x() > next_apple[0]:
				while get_pos_x() < nearest_odd(get_world_size())-1:
					move_dig(East)
					i+=1
					
			
			while get_pos_x() < nearest_odd(next_apple[0])-1:
				if not move_dig(East):
					return None
				i+=1
		
		move_dig(East)
		dir = op_dir[dir]
		i+=1

	move_dig(South)
	if get_entity_type() == Entities.Apple:
		next_apple = measure()
	
	while get_pos_x() >0:
		if not move_dig(West):
			return extra_apples
		if get_entity_type() == Entities.Apple:
			next_apple = measure()
	move_dig(North)
	
	return extra_apples
	


next_apple = measure()
fails = 0
apples = 0

def main():	
	global fails
	global next_apple
	global apples
	
	harvest()
	dir = East
	#set_world_size(22)	
	change_hat(Hats.Carrot_Hat)
	change_hat(Hats.Dinosaur_Hat)
	while True:
		#mover.refresh_xy()
		mover.uncached_move_to(0,0)
		
		walk_res = walk(fails > 1)
		if walk_res == None or walk_res == 0:
			
			fails += 1
			if fails >= 3:
				change_hat(Hats.Carrot_Hat)
				change_hat(Hats.Dinosaur_Hat)
				next_apple = measure()
				fails = 0
				apples = 0
				continue
		else:
			fails = 0

if __name__ == "__main__":
	main()
	
def entry():
	while True:
		#while get_tick_count()%10000 != 0:
		#	pass
		main()
	
	
def make_drone():
	return entry	
		
	
						
		