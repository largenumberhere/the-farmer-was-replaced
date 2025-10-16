

def make_tilled():
	if get_ground_type() == Grounds.Grassland:
		till()

		
def make_untilled():
	if get_ground_type() == Grounds.Soil:
		till()


def watering():
	water = get_water()
	f = 0
	while water < 0.75:
		worked = use_item(Items.Water)	
		if not worked:
			break
		water = get_water()
		f += 1

def try_plant(entity):
	if get_entity_type() != entity:
		plant(entity)

def try_harvest():
	if get_entity_type() != None:
		if can_harvest():
			harvest()

def checkergrid(x, y):
	# Returns True if the tile (x, y) should be "white" in a checkerboard, False otherwise
	return (x + y) % 2 == 0

bad_pumpkins = 0
def try_harvest_pumpkin(x,y):
	global bad_pumpkins
	if bad_pumpkins == 0:
		harvest()
		do_a_flip()
	
			

def farm(x, y):
	if get_entity_type() == Entities.Dead_Pumpkin:
		global bad_pumpkins
		bad_pumpkins += 1
	
	make_tilled()
		
	if get_entity_type() != Entities.Pumpkin:
		try_harvest()
	
	if x == 0 and y == 0:
		try_harvest_pumpkin(x,y)
		if bad_pumpkins == 0:
			try_harvest()
		if get_entity_type() == None or get_entity_type() == Entities.Dead_Pumpkin:
			plant(Entities.Pumpkin)
			
			
	elif x == 7 and y == 7:
		make_untilled()
		for i in range (0, 20):
			while not can_harvest():
				pass
			harvest()	
			try_plant(Entities.Grass)
	elif x <= 6 and y <= 6:
		if get_entity_type() != Entities.Pumpkin:
			try_plant(Entities.Pumpkin)
			bad_pumpkins += 1
		
		else:
			plant(Entities.Pumpkin)	
	elif x <= 5 and y <= 6:
		try_plant(Entities.Carrot)

			
	else:
		if checkergrid(x,y):
			try_plant(Entities.Tree)
		else:
			try_plant(Entities.Carrot)
	watering()


def move_to_origin():
	x = get_pos_x()
	while x > 0:
		move(West)
		x = get_pos_x()
	
	y = get_pos_y()
	while y > 0:
		move(South)
		y = get_pos_y()


hat_no = 0
def switch_hat():
	global hat_no
	if hat_no == None:
		hat_no = 0
	hats = [Hats.Brown_Hat, Hats.Carrot_Hat, Hats.Traffic_Cone, Hats.Straw_Hat, Hats.Purple_Hat, Hats.Tree_Hat]
	change_hat(hats[hat_no])
	hat_no += 1
	if hat_no >= len(hats):
		hat_no = 0
	
	
move_to_origin()
crop = "carrot"
while True:		
	x = 0
	y = 0
	bad_pumpkins = 0
	
	for n in range(get_world_size()):
		if crop == "carrot":
			crop = "wood"
		elif crop == "wood":
			crop = "hay"
		elif crop == "hay":
			crop = "pumpkin"
		elif crop == "pumpkin":
			crop = "carrot"
			
		y = 0		
		for i in range(get_world_size()):		
			farm(x, y)
			y += 1
			move(North)
		switch_hat()
		move(East)
		x += 1
	
		


		