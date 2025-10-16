if False and x == _min_x+1 and y == _min_y:
		
		while get_water() < 0.75:
			if not use_item(Items.Water):
				break
			
			
		for i in range(40):
			if num_items(Items.Weird_Substance) > num_items(Items.Gold):
				if num_items(Items.Fertilizer) >= 1:
					plant(Entities.Grass)
					if not use_item(Items.Fertilizer):
						break
					while not can_harvest():
						pass
					harvest()	
				else:
					break
		
			plant(Entities.Bush)
			use_item(Items.Fertilizer)
			while not can_harvest():
				pass
			use_item(Items.Weird_Substance, 3)
			harvest()