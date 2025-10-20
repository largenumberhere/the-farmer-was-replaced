def create_node(value, prio):
	return (value, prio)

def create_priority_queue():
	return []

def clear(pq):
	pq = []

def enqueue(data, value, prio):
	node = create_node(value, prio)
	inserted = False
	i = 0
	while i < len(data):
		if prio < data[i][1]:
			data.insert(i, node)
			inserted = True
			break
		i += 1
	if not inserted:
		data.append(node)

def dequeue(data):
	if len(data) == 0:
		return None
	return data.pop(0)

def peek(data):
	if len(data) == 0:
		return None
	return data[0]

def is_empty(pq):
	return len(pq) == 0