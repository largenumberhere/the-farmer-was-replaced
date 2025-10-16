import mover


set_world_size(16)
max_pos = get_world_size()

op_dir = {North:South, South:North, East:West, West:East}

def ensure_tilled():
	if get_ground_type() != Grounds.Soil:
		till()

def ensure_planted():
	if get_entity_type() != Entities.Cactus:
		plant(Entities.Cactus)

def measure2(direction=None):
	max = 999999999
	min = -1
	if direction==North and get_pos_y() == get_world_size() -1:
		return max
	elif direction==East and get_pos_x() == get_world_size()-1:
		return max
	
	elif direction == West and get_pos_x() == 0:
		return min
	
	elif direction == South and get_pos_y() == 0:
		return min
	else:
		return measure(direction)

def sort_h():
	actioned = False
	l = measure2(West)
	r = measure2(East)
	h = measure2()
	
	if l!=None and h!=None and h < l:
		actioned = True
		swap(West)
		(h, l) = (l,h)
	
	if r!=None and h!=None and r < h:
		actioned = True
		swap(East)
		(r, h) = (h, r)
	
	if h!=None and l!=None and h < l:
		actioned = True
		swap(West)
		(h, l) = (l, h)
	
	return actioned

def sort_v():
	actioned = False
	u = measure2(North)
	h = measure2()
	d = measure2(South)
	
	if h!=None and d!=None and h < d:
		actioned = True
		swap(South)
		(h, d) = (d, h)
		
	if u!=None and h!=None and u < h:
		actioned = True
		swap(North)
		(u, h) = (h, u)
	
	if h!=None and d!=None and h < d:
		actioned = True
		swap(South)
		(h, d) = (d, h)
	
	return actioned

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
	# sort columns
	for col in range(max_pos):
		# plant the column
		while get_pos_y() < max_pos:
			ensure_tilled()
			ensure_planted()
			if get_pos_y() != max_pos-1:
				sort_v()
				move(North)
			else:
				break
		
		# sort the column
		bad = True
		while bad:
			bad = False
			while get_pos_y() >0:
				actioned = sort_v()
				if actioned:
					bad = True
					
				move(South)
			if not bad:
				break
			
			bad = False
			while get_pos_y() < max_pos-1:
				actioned = sort_v()
				if actioned:
					bad = True
				
				move(North)
				
				
			
		move_y_start()
		move(East)
		
	# sort rows
	for row in range(max_pos):
		while get_pos_x() >0:
			move(West)
			sort_h()
		bad = True
		while bad:
			bad = False
			
			for col in range(max_pos):
				actioned = sort_h()
				if actioned:
					bad = True
				
				if col != max_pos-1:
					move(East)
				
			if not bad:
				break
			
			for col in range(max_pos):
				actioned = sort_h()
				if actioned:
					bad = True
				
				if col != max_pos-1:
					move(West)
			
		move(North)
		
	move_x_start()
	move_y_start()
	harvest()
