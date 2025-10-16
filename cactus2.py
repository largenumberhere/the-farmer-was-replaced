import mover

max_pos = get_world_size()

op_dir = {North:South, South:North, East:West, West:East}

def ensure_tilled():
	if get_ground_type() != Grounds.Soil:
		till()

def ensure_planted():
	if get_entity_type() != Entities.Cactus:
		plant(Entities.Cactus)

def measure2(direction=None):
	if direction==North and get_pos_y() == get_world_size() -1:
		return 999999999
	
	if direction == West and get_pos_x() == 0:
		return -1
	
	return measure(direction)

def delay(ticks):
	for i in range(ticks):
		pass

def move_y_start():
	while get_pos_y() > 0:
		move(South)	
	
def move_y_end():
	while get_pos_y() < get_world_size()-1:
		move(North)

def move_x_start():
	while get_pos_x() > 0:
		move(West)

def move_x_end():
	while get_pos_x() < get_world_size()-1:
		move(East)

mover.move_to(0,0)
while True:
	#set_execution_speed(10)
	# sort columns
	for col in range(max_pos):
		while get_pos_y() < max_pos:
			ensure_tilled()
			ensure_planted()
			if get_pos_y() != max_pos-1:
				move(North)
			else:
				break
		
		delay(10)

		bad = True
		while bad:
			bad = False
			while get_pos_y() >0:
				north = measure2(North)
				here = measure2()
				south = measure2(South)
				
				if not north >= south:
					swap(South)
					swap(North)
					bad = True
					south = measure2()
					north = measure2()
				
				if not here >= south:
					swap(South)
					south = measure2()
					here = measure2()
					bad = True
					
				move(South)
			 
			move_y_end()
			
		move_y_start()
		move(East)
		
	# sort rows
	for row in range(max_pos):
		here = measure2()       
		move_x_start()
		bad = True
		while bad:
			bad = False
			
			for col in range(max_pos):
				if measure2() < measure2(West):
					swap(West)
					bad = True
				
				move(East)
				
				
				
		move(North)
	   
	harvest()
	move_x_start()
	move_y_start()
	
