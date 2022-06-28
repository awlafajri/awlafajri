extends Node2D

var air = preload("res://Air.tscn")
var api = preload("res://Api.tscn")
var music1 = [2593,3197,3438,4005,4448,4642,5249,5672,5893,7699,8105,8374,8993,9992,10262,10715,10954,11503,12637,13028,13273,13859,14504,15112,15653,17522,17971,18203,18755,19780,20039,20494,20711,21322,22420,22804,23032,23663,24295,24922,25472,27409,27895,28121,28639,29632,29897,30331,30584,31190,32297,32657,32912,33484,34081,34658,35357,36532,37210,37607,37858,38510,39107,39758,40351,41534,42185,42559,42835,43409,44036,44635,45211,47042,47584,47834,48410,48914,49135,49736,50210,50488,50911,51364,51587,52111,52511,52763,53317,53762,54014,54562,55087,55312,56612,57190,57565,57818,58387,58816,59063,59687,60113,60362,60964,61367,61646,62218,62615,62896,63440,64067,64643,65189,65416,66716,67369,67766,68015,68590,68966,69215,69791,70189,70442,71041,71467,71717,72265,72665,72943,73469,73892,74138,74692,75043,75293,76463,77116,77468,77689,78290,78674,78941,79496,79840,80119,80714,81092,81338,81893,82243,82514,83117,83516,83792,84365,84769,85018,86266,86882,87245,87469,88093,88474,88717,89300,89621,89884,90469,90919,91141,91702,92066,92302,92918,93271,93527,94138,94468,94735,95957,96614,96997,97231,97846,98192,98456,99059,99353,99619,100243,100592,100811,101383,101744,102020,102695,103096,103330,104134,104903,105596,107194
]
signal done3()

var music = []

var direction = [true,false,false,false,true,true,true,false,false,true,false,false,true,true,true,false,false,true,false,false,false,false,false,false,false,false,true,true,false,false,false,true,true,false,false,true,true,true,true,true,true,true,false,false,true,true,true,false,false,true,true,false,false,true,false,true,false,true,false,true,true,false,false,true,true,false,true,false,false,true,false,true,false,false,false,false,false,false,false,false,false,false,false,false,false,true,true,true,true,true,true,true,true,true,true,true,false,false,true,false,false,true,false,false,true,false,false,false,true,true,false,false,false,true,true,true,false,true,true,false,true,true,false,true,true,false,true,true,true,false,false,true,false,false,false,true,true,false,false,false,false,false,false,false,false,false,false,true,true,true,true,true,true,true,true,true,false,true,true,false,false,false,false,false,false,false,true,true,true,true,true,true,false,true,true,false,true,true,true,false,false,false,true,false,false,false,true,true,true,false,false,false,true,true,true,false,false,false,false,false,true,true,true,false]
var element = [true,true,true,false,false,false,true,true,true,false,false,false,false,true,true,true,true,true,false,false,false,false,false,false,false,false,false,false,false,true,true,true,true,true,false,false,false,true,false,true,false,true,true,true,true,false,false,false,false,false,true,true,true,true,true,true,true,true,false,false,false,false,false,true,true,true,false,false,false,false,true,true,true,true,false,false,true,false,false,true,false,false,true,false,false,false,true,true,false,true,true,false,true,true,false,true,true,true,false,false,false,true,true,true,false,false,false,true,true,true,false,true,false,false,false,true,false,false,false,true,true,true,false,false,false,true,true,true,false,false,false,true,true,true,false,false,false,true,true,false,false,true,false,false,true,false,false,false,true,true,false,true,true,false,true,true,false,false,false,true,true,false,false,true,false,false,false,true,true,false,true,true,false,true,true,false,true,true,true,false,false,true,false,true,true,true,false,false,false,true,true,true,false,false,false,true,true,true,false,false,false,true,false,true]
var timer1 = -4100
var speed = 1500
var index = 0

func _ready():
	music = music1.duplicate()
		

# Called every frame. 'delta' is the elapsed time since the previous frame.
func _process(delta):
	timer1 += delta*speed
	if music.size() == 0:
		emit_signal("done3")
		return
		
	elif timer1 >= music[0]:
		music.pop_front()
		if not element[0]:
			var air_instance = air.instance()
			if direction[0]:
				air_instance.position = get_parent().get_node("Spawner/SpawnerAtas").get_global_position()
				air_instance.set_name(str(index))
				add_child(air_instance)
				air_instance.direction = direction[0]
				air_instance.speed = 1250
				index += 1
			else:
				air_instance.position = get_parent().get_node("Spawner/SpawnerBawah").get_global_position()
				air_instance.set_name(str(index))
				add_child(air_instance)
				air_instance.direction = direction[0]
				air_instance.speed = 1250
				index += 1
			
		else:
			var api_instance = api.instance()
			if direction[0]:
				api_instance.position = get_parent().get_node("Spawner/SpawnerAtas").get_global_position()
				api_instance.set_name(str(index))
				add_child(api_instance)
				api_instance.direction = direction[0]
				api_instance.speed = 1250
				index += 1
			else:
				api_instance.position = get_parent().get_node("Spawner/SpawnerBawah").get_global_position()
				api_instance.set_name(str(index))
				add_child(api_instance)
				api_instance.direction = direction[0]
				api_instance.speed = 1250
				index += 1
			
		element.pop_front()
		direction.pop_front()

