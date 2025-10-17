import mover
change_hat(Hats.The_Farmers_Remains)
mover.move_to(0,0)
if get_ground_type() != Grounds.Grassland:
	till()
while True:
	if can_harvest():
		harvest()
	else:
		use_item(Items.Fertilizer)