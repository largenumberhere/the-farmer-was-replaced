

_x = -1
_y = -1

def move_to(x,y):
	return uncached_move_to(x, y)

	global _x
	global _y
	
	if _x == -1:
		_x = get_pos_x()
	if _y == -1:
		_y = get_pos_y()
	
	while _x > x:
		move(West)
		_x  -=1
	while _y > y:
		move(South)
		_y -= 1
	while _x < x:
		move(East)
		_x += 1
	while _y < y:
		move(North)
		_y += 1

def uncached_move_to(x,y):
	while get_pos_x() > x:
		if not move(West):
			return False
	while get_pos_y() > y:
		if not move(South):
			return False
	while get_pos_x() < x:
		if not move(East):
			return False
	while get_pos_y() < y:
		if not move(North):
			return False
	
	return True
	

def cached_x():
	return _x
	
def refresh_xy():
	global _x
	global _y
	_x = get_pos_x()
	_y = get_pos_y()

def cached_y():
	return _y

def wrapped_move(direction, min_x, min_y, max_x, max_y):
	#global _x
	#global _y	
	
	#if _x == -1:
	_x = get_pos_x()
	#if _y == -1:
	_y = get_pos_y()

	dest_x = _x
	dest_y = _y

	wrapped = False
	if direction == North:
		dest_y += 1
	elif direction == South:
		dest_y -= 1
	elif direction == West:
		dest_x -= 1
	elif direction == East:
		dest_x += 1
		
	if dest_x >= max_x:
		dest_x = min_x
		wrapped = True
	elif dest_x < min_x:
		dest_x = max_x-1
		wrapped = True
	elif dest_y >= max_y:
		dest_y = min_y
		wrapped = True
	elif dest_y < min_y:
		dest_y = max_y-1
		wrapped = True
	
	if wrapped:
		uncached_move_to(dest_x, dest_y)
	else:
		move(direction)
		
	_x = dest_x
	_y = dest_y