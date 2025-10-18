#leaderboard_run(Leaderboards.Hay_Single, "f1", 100000)
#unlock8 = {Unlocks.Expand: 5, Unlocks.Fertilizer:0, 
# Unlocks.Speed:2, Unlocks.Grass:1, Unlocks.Polyculture:1}
#simulate("f1", unlock8, {}, {}, -1, 1)
all_unlocks = {
	Unlocks.Auto_Unlock, 
	Unlocks.Cactus, 
	Unlocks.Carrots,
	Unlocks.Costs,
	Unlocks.Debug,
	Unlocks.Debug_2,
	Unlocks.Dictionaries,
	Unlocks.Dinosaurs,
	Unlocks.Expand,
	Unlocks.Fertilizer,
	Unlocks.Functions,
	Unlocks.Grass,
	Unlocks.Hats,
	Unlocks.Import,
	Unlocks.Leaderboard,
	Unlocks.Lists,
	Unlocks.Loops,
	Unlocks.Mazes,
	Unlocks.Megafarm,
	Unlocks.Operators,
	Unlocks.Plant,
	Unlocks.Polyculture,
	Unlocks.Pumpkins,
	Unlocks.Polyculture,
	Unlocks.Senses,
	Unlocks.Simulation,
	Unlocks.Speed,
	Unlocks.Sunflowers,
	Unlocks.The_Farmers_Remains,
	Unlocks.Timing,
	Unlocks.Top_Hat,
	Unlocks.Trees,
	Unlocks.Utilities,
	Unlocks.Variables,
	Unlocks.Watering
}


	
res = simulate("cactus1", all_unlocks, {Items.Pumpkin: 10**10}, {}, 0 , 1000)
print(res)
quick_print(res)
