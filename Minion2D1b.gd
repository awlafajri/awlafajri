extends Node2D

var air = preload("res://Air.tscn")
var api = preload("res://Api.tscn")
var music1 = [1966,2333,2466,2833,3266,3433,3933,4300,4466,4900,5300,5466,5933,6300,6433,6866,7266,7433,7933,8366,8866,9266,9400,9900,10300,10466,10900,11300,11466,11900,12300,12466,12900,13266,13400,13933,14300,14433,14933,15300,15433,15933,16366,16833,17300,18466,18933,19466,19933,20066,20233,20433,20933,21433,21933,22100,22300,22466,22900,23433,23933,24100,24266,24466,24966,25433,25966,26100,26300,26433,26933,27433,27933,28100,28266,28433,28966,29466,29966,30133,30266,30433,30933,31433,31933,32100,32266,32466,32933,33433,33966,34100,34266,34400,34966,35433,35966,36100,36300,36433,36966,37466,37933,38133,38266,38433,38933,39433,39933,40100,40233,40433,40933,41433,41933,42100,42266,42400,42933,43433,43933,44066,44266,44400,44900,45400,45900,46066,46266,46433,46933,47400,47900,48100,48266,48433,48900,49400,49900,50433,50833,51233,51400,51866,52300,52466,52900,53266,53433,53900,54266,54466,54866,55300,55466,55866,56366,56866,57266,57933,58333,58500,58900,59300,59466,59900,60300,60500,60866,61266,61466,61933,62300,62433,62933,63333,63500,63900,64366,64866,65300,65466,66400,66866,67266,67466,67900,68300,68466,68866,69266,69466,69900,70300,70500,70900,71300,71466,71900,72366,72900,73300
]
signal done2()

var music = []

var direction = [true,true,true,true,true,true,true,true,true,true,true,true,true,true,true,true,true,true,false,true,false,false,false,false,false,false,false,false,false,false,false,false,false,false,false,false,false,false,false,false,false,false,false,false,true,false,true,false,true,true,true,true,false,true,false,false,false,false,true,false,true,true,true,true,false,true,false,false,false,false,true,false,true,true,true,true,false,true,false,false,false,false,true,false,true,true,true,true,false,true,false,false,false,false,true,true,false,true,false,true,false,false,true,false,true,false,true,false,true,true,true,true,false,true,false,false,false,false,true,true,false,true,false,true,false,false,true,false,true,false,true,false,true,true,true,true,false,true,false,true,false,true,true,false,true,true,false,true,true,false,true,true,false,true,true,false,true,false,true,false,true,true,true,true,true,true,true,true,true,true,true,true,true,true,true,true,true,true,true,true,true,true,true,false,true,true,false,true,true,false,true,true,false,true,true,false,true,true,false,true,false,true]
var element = [true,true,true,true,true,true,true,true,true,true,true,true,true,true,true,true,true,true,false,false,false,false,false,false,false,false,false,false,false,false,false,false,false,false,false,false,false,false,false,false,false,true,true,true,true,true,true,true,true,true,true,true,true,true,false,false,false,false,false,false,true,true,true,true,true,true,false,false,false,false,false,false,true,true,true,true,true,true,false,false,false,false,false,false,true,true,true,true,true,true,true,true,true,true,true,true,false,false,false,false,false,false,false,false,false,false,false,false,true,true,true,true,true,true,true,true,true,true,true,true,false,false,false,false,false,false,false,false,false,false,false,false,true,true,true,true,false,false,true,true,true,true,true,true,true,true,false,false,false,false,false,false,false,false,false,true,false,false,true,true,false,false,true,false,false,true,false,false,true,false,false,true,false,false,true,false,false,true,false,false,true,true,true,true,true,true,false,false,false,false,false,false,true,false,false,true,false,false,true,false,true,false]
var timer1 = -4050
var speed = 1250
var index = 0

func _ready():
	music = music1.duplicate()

# Called every frame. 'delta' is the elapsed time since the previous frame.
func _process(delta):
	timer1 += delta*speed
	if music.size() == 0:
		emit_signal("done2")
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

