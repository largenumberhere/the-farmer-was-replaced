import mover
#clear()
#if not get_ground_type() == Grounds.Soil:
#	till()
#while get_pos_x() > 0:
#	move(West)
#while get_pos_y() > 0:
#	move(South)
	
harvest()
n = 3
if get_entity_type() != Entities.Hedge:
	plant(Entities.Bush)
	useitem(Items.Weird_Substance, 9)
	


while False:
	for i in range (n):
		for j in range(n):
			if get_ground_type() != Grounds.Soil:
				till()
			if get_entity_type() != Entities.Bush:
				plant(Entities.Bush)
				use_item(Items.Weird_Substance, 2)
			move(North)
			
			if can_harvest():
				harvest()
		for j in range(n):
			move(South)
		move(East)
	for i in range(n):
		move(West)
	
#while True:


#	plant(Entities.Bush)
#	use_item(Items.Weird_Substance, 1)
#	harvest()