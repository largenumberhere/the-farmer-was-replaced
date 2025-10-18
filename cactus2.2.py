import mover

#set_world_size(16)
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

def sort_column(x):
    # sort the column
    mover.move_to(x, max_pos-1)
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

def sort_columns():
    drones = []
    
    for col in range(max_pos-1):
        def sort_column_n():
            sort_column(col)
            
        drone = spawn_drone(sort_column_n)
        if drone == None:
            error("not enough drones")
        
        drones.append(drone)
    
    sort_column(max_pos-1)
    for drone in drones:
        wait_for(drone)


def sort_row(y):
    mover.move_to(max_pos-1, y)

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
def error(data):
    while True:
        print("Error")
        print(data)
        

def sort_rows():
    drones = []
    
    for row in range(max_pos-1):
        def sort_row_n():
            sort_row(row)
            
        drone = spawn_drone(sort_row_n)
        if drone == None:
            error("not enough drones")
        
        drones.append(drone)
    
    sort_row(max_pos-1)
    for drone in drones:
        wait_for(drone)

def prepare_cactus():
    if get_ground_type() != Grounds.Soil:
                till()
            
    if get_entity_type() != Entities.Cactus:
        plant(Entities.Cactus)

def plant_row(x):
    mover.move_to(x, 0)
    for i in range(get_world_size()):
        prepare_cactus()
        move(North)
    
def plant_farm():
    drones = []
    for row in range(get_world_size()-1):
        def plant_row_n():
            plant_row(row)
        
        drone = spawn_drone(plant_row_n)
        if drone == None:
            error("not enough drones")
        drones.append(drone)
    plant_row(get_world_size()-1)
    
    for drone in drones:
        wait_for(drone)

def main():
    mover.move_to(0,0)
	while True:
        plant_farm()
        mover.move_to(0,0)
        sort_columns()
        mover.move_to(0,0)
        sort_rows()
        mover.move_to(0,0)
        harvest()

main()