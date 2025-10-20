import priority_queue

directions = {North, East, South, West}
opposites = {North:South, East:West, South:North, West:East}

def create_virtual_maze():
	field = { }
	return field

def create_cell(walkable, visited):
	cell = { 1: walkable, 0: visited }
	return cell

def add_coordinates(position, direction):
	x, y = position
	if direction == None:
		return (x, y)
	if direction == North:
		return (x, y + 1)
	if direction == South:
		return (x, y - 1)
	if direction == East:
		return (x + 1, y)
	if direction == West:
		return (x - 1, y)

def get_pos_():
	return (get_pos_x(), get_pos_y())

def get_pos(direction):
	return add_coordinates((get_pos_x(), get_pos_y()), direction)


def get_cell_or_none(field, position):
	cell = None
	if position in field:
		cell = field[position]
	return cell

def create_or_update_cell(field, position, direction_enterable, visited):
	cell = get_cell_or_none(field, position)
	new_ways = False
	if not cell:
		direction_enterable_list = {direction_enterable}
		field[position] = create_cell(direction_enterable_list, visited)
		return True
	if direction_enterable not in field[position][1]:
		field[position][1].add(direction_enterable)
		new_ways = True
	if cell and not cell[0] and visited:
		field[position][0] = True
	return new_ways        

def create_or_update_current_cell(field):
	new_ways = False
	create_or_update_cell(field, get_pos_(), None, True)
	for direction in directions:
		if can_move(direction):
			nnew_ways = create_or_update_cell(field, get_pos_(), direction, False)
			new_ways = new_ways or nnew_ways
		create_or_update_cell(field, get_pos(direction), None, False)
	return new_ways

def get_walkable_directions_for_position(field, position):
	cell = get_cell_or_none(field, position)
	if cell == None or (len(cell[1]) == 1 and cell[1] == {None}):
		return {}
	return cell[1]

def get_walkable_directions(field):
	return get_walkable_directions_for_position(field, get_pos_())

def manhatten_distance(position):
	goal = measure()
	x = abs(goal[0] - position[0])
	y = abs(goal[1] - position[1])
	return x + y

def move_to(field, pos):
	goal = get_cell_or_none(field, pos)
	if goal == None:
		return False
	else:
		#fast path check
		goal_directions = get_walkable_directions_for_position(field, goal)
		if len(goal_directions) == 0:
			has_any_way = False
			for dir in directions:
				next_to_goal = get_walkable_directions_for_position(field, add_coordinates(pos, dir))
				has_any_way = has_any_way or opposites[dir] in next_to_goal
			if not has_any_way:
				return False

	start = get_pos_()
	pq = priority_queue.create_priority_queue()
	came_from = {}
	cost_so_far = {}

	priority_queue.enqueue(pq, start, 0)
	came_from[start] = None
	cost_so_far[start] = 0

	found = False

	while not priority_queue.is_empty(pq):
		node = priority_queue.dequeue(pq)
		cur = node[0]
		#print(cur)
		if cur == pos:
			found = True
			break

		cur_cell = get_cell_or_none(field, cur)
		if not cur_cell:
			continue

		for d in cur_cell[1]:
			nbr = add_coordinates(cur, d)
			nbr_cell = get_cell_or_none(field, nbr)
			if not nbr_cell:
				continue

			new_cost = cost_so_far[cur] + 1
			if nbr not in cost_so_far or new_cost < cost_so_far[nbr]:
				cost_so_far[nbr] = new_cost
				priority = new_cost + manhatten_distance(nbr)
				priority_queue.enqueue(pq, nbr, priority)
				came_from[nbr] = (cur, d)

	if not found:
		return False

	path = []
	cur = pos
	while came_from[cur] != None:
		prev, dir_taken = came_from[cur]
		path.insert(0, dir_taken)
		cur = prev

	for d in path:
		if can_move(d):
			move(d)
			if create_or_update_current_cell(field):
				return move_to(field, pos)
		else:
			break
	return True

def explore_maze(field):
	q = []
	start = get_pos_()
	q.append(start)
	visited = {start}

	while q != []:
		cur = q.pop()
		
		if get_pos_() != cur:
			move_to(field, cur)
		visited.add(cur)
		create_or_update_current_cell(field)

		for d in directions:
			if can_move(d):
				nxt = add_coordinates(cur, d)
				if nxt not in visited:
					q.append(nxt)
	print("Exploration complete.")

def main(iteration = 0, field = None):
	if iteration == 303 or num_items(Items.Gold) >= 10**6:
		return
	iteration += 1
	substance = get_world_size() * 2**(num_unlocked(Unlocks.Mazes) - 1)
	use_item(Items.Weird_Substance, substance)
	if iteration == 1:
		field = create_virtual_maze()
		explore_maze(field)
	else:
		for cell in field:
			field[cell][0] = False
	pq = priority_queue.create_priority_queue()

	while (get_entity_type() != Entities.Treasure):
		if move_to(field, measure()):
			break
		create_or_update_current_cell(field)
		walkable_directions = get_walkable_directions(field)

		for dir in walkable_directions:
			if dir == None:
				continue
			new_pos = get_pos(dir)
			cell = get_cell_or_none(field, new_pos)
			if cell and cell[0]:
				continue
			priority_queue.enqueue(pq, new_pos, manhatten_distance(new_pos))

		node = priority_queue.dequeue(pq)
		if node != None:
			move_to(field, node[0])
		else:
			for position in field:
				move_to(field, position)
				if create_or_update_current_cell(field):
					break
			
	main(iteration, field)

if __name__ == "__main__":
	while num_items(Items.Gold) < 10 ** 6:
		set_world_size(6)
		harvest()
		plant(Entities.Bush)
		main()
		harvest()
	