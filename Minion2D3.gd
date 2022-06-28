extends Node2D

var air = preload("res://Air.tscn")
var api = preload("res://Api.tscn")
var music1 = [5315,5472,5778,5927,6289,6433,6727,6905,7230,7403,7691,7862,8373,8887,9341,9842,10307,10792,11258,11785,12307,12671,12814,13325,13820,14271,14453,14613,14804,15097,15264,15420,15589,15771,16240,16403,16573,16754,17308,17473,17638,17825,18320,18820,18989,19157,19306,19492,19639,19838,20273,20454,20623,20805,21289,21456,21624,21791,22339,22825,23292,23774,24290,24823,25329,25841,26310,26710,26858,27373,27940,28358,28825,29293,29808,30292,30444,30595,30792,31329,31476,31679,31827,32327,32802,33280,33793,34299,34460,34665,34776,35278,35426,35593,35782,36293,36793,37309,37484,37685,37810,38286,38448,38635,38807,39329,39506,39689,39845,40317,40796,41316,41762,42267,42443,42646,42816,43344,43495,43647,43821,44289,44478,44667,44814,44984,45152,45333,45536,45660,45841,46336,46784,47289,47771,48287,48462,48666,48811,49319,49496,49630,49833,50306,50817,51283,51781,52273,52439,52613,52801,53308,53471,53627,53839,54253,54815,55021,55210,55839,56099,56242,56372,56847,57092,57250,57366,57849,58297,58804,59290,59765,60250,60395,60548,60712,60937,61047,61224,61379,61555,61771,62192,62273,62421,62791,63190,63297,63459,63812,64093,64249,64415,64830,65042,65256,65337,65853,66332,66792,67298,67756,68276,68456,68604,68822,69320,71619,71724,71928,72027,72268,72364,72560,72679,72896,73011,73203,73317,73658,74000,74303,74637,74947,75270,75581,75932,76280,76523,76618,76959,77289,77590,77711,77818,77945,78140,78252,78356,78468,78590,78902,79011,79124,79245,79614,79724,79834,79959,80289,80622,80735,80847,80946,81070,81168,81301,81591,81712,81824,81946,82268,82380,82492,82603,82968,83292,83604,83925,84269,84624,84962,85303,85616,85882,85981,86324,86702,86981,87292,87604,87948,88270,88372,88472,88604,88962,89060,89195,89294,89627,89944,90262,90604,90942,91049,91186,91260,91594,91693,91804,91930,92271,92604,92948,93065,93199,93282,93600,93708,93832,93947,94295,94413,94535,94639,94954,95273,95620,95917,96254,96371,96506,96620,96972,97072,97174,97290,97602,97728,97854,97952,98065,98177,98298,98433,98516,98636,98966,99265,99602,99923,100267,100384,100520,100616,100955,101073,101162,101298,101613,101954,102264,102596,102924,103035,103151,103276,103614,103723,103827,103968,104244,104619,104756,104882,105302,105475,105570,105657,105974,106137,106242,106320,106642,106940,107278,107602,107919,108242,108339,108441,108550,108700,108774,108892,108995,109112,109256,109537,109591,109690,109936,110202,110274,110382,110617,110804,110908,111019,111296,111437,111580,111634,111978,112297,112604,112941,113246,113593,113713,113812,113957,114289]
signal done2()

var music = []

var direction = [true,true,true,true,true,true,true,true,true,true,true,true,true,true,true,true,true,true,true,true,true,true,true,true,true,true,true,true,true,true,true,true,true,true,true,true,true,true,true,true,true,true,true,true,true,true,true,true,true,true,true,true,true,true,true,true,true,true,true,true,true,true,true,true,true,true,true,true,true,true,true,true,true,true,true,true,true,true,true,true,true,true,true,true,true,true,true,true,true,true,true,true,true,true,true,true,true,true,true,true,true,true,true,true,true,true,true,true,true,true,true,true,true,true,true,true,true,true,true,true,true,true,true,true,true,true,true,true,true,true,true,true,true,true,true,true,true,true,true,true,true,true,true,true,true,true,true,true,true,true,true,true,true,true,true,true,true,true,true,true,true,true,true,true,true,true,true,true,true,true,true,true,true,true,true,true,true,true,true,true,true,true,true,true,true,true,true,true,true,true,true,true,true,true,true,true,true,true,true,true,true,true,true,true,true,true,true,true,true,true,true,true,true,true,true,true,true,true,true,true,true,true,true,true,true,true,true,true,true,true,true,true,true,true,true,true,true,true,true,true,true,true,true,true,true,true,true,true,true,true,true,true,true,true,true,true,true,true,true,true,true,true,true,true,true,true,true,true,true,true,true,true,true,true,true,true,true,true,true,true,true,true,true,true,true,true,true,true,true,true,true,true,true,true,true,true,true,true,true,true,true,true,true,true,true,true,true,true,true,true,true,true,true,true,true,true,true,true,true,true,true,true,true,true,true,true,true,true,true,true,true,true,true,true,true,true,true,true,true,true,true,true,true,true,true,true,true,true,true,true,true,true,true,true,true,true,true,true,true,true,true,true,true,true,true,true,true,true,true,true,true,true,true,true,true,true,true,true,true,true,true,true,true,true,true,true,true,true,true,true,true,true,true,true,true,true,true,true,true,true,true,true,true,true,true,true,true,true,true,true,true,true,true,true]
var element = [true,true,true,true,true,true,true,true,true,true,true,true,true,true,true,true,true,true,true,true,true,true,true,true,true,true,true,true,true,true,true,true,true,true,true,true,true,true,true,true,true,true,true,true,true,true,true,true,true,true,true,true,true,true,true,true,true,true,true,true,true,true,true,true,true,true,true,true,true,true,true,true,true,true,true,true,true,true,true,true,true,true,true,true,true,true,true,true,true,true,true,true,true,true,true,true,true,true,true,true,true,true,true,true,true,true,true,true,true,true,true,true,true,true,true,true,true,true,true,true,true,true,true,true,true,true,true,true,true,true,true,true,true,true,true,true,true,true,true,true,true,true,true,true,true,true,true,true,true,true,true,true,true,true,true,true,true,true,true,true,true,true,true,true,true,true,true,true,true,true,true,true,true,true,true,true,true,true,true,true,true,true,true,true,true,true,true,true,true,true,true,true,true,true,true,true,true,true,true,true,true,true,true,true,true,true,true,true,true,true,true,true,true,true,true,true,true,true,true,true,true,true,true,true,true,true,true,true,true,true,true,true,true,true,true,true,true,true,true,true,true,true,true,true,true,true,true,true,true,true,true,true,true,true,true,true,true,true,true,true,true,true,true,true,true,true,true,true,true,true,true,true,true,true,true,true,true,true,true,true,true,true,true,true,true,true,true,true,true,true,true,true,true,true,true,true,true,true,true,true,true,true,true,true,true,true,true,true,true,true,true,true,true,true,true,true,true,true,true,true,true,true,true,true,true,true,true,true,true,true,true,true,true,true,true,true,true,true,true,true,true,true,true,true,true,true,true,true,true,true,true,true,true,true,true,true,true,true,true,true,true,true,true,true,true,true,true,true,true,true,true,true,true,true,true,true,true,true,true,true,true,true,true,true,true,true,true,true,true,true,true,true,true,true,true,true,true,true,true,true,true,true,true,true,true,true,true,true,true,true,true,true,true,true]
var timer1 = -800
var speed = 1000
var index = 0
var rng = RandomNumberGenerator.new()

func _ready():
	rng.randomize()
	music = music1.duplicate()
	
	for f in range(direction.size()):
		var boole = rng.randi_range(0,10)
		if boole %2 == 0:
			direction[f] = true
		else:
			direction[f] = false
	
	for f in range(element.size()):
		var boole2 = rng.randi_range(0,20)
		if boole2 %2 == 0:
			element[f] = true
		else:
			element[f] = false

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
				air_instance.speed = 1500
				index += 1
			else:
				air_instance.position = get_parent().get_node("Spawner/SpawnerBawah").get_global_position()
				air_instance.set_name(str(index))
				add_child(air_instance)
				air_instance.direction = direction[0]
				air_instance.speed = 1500
				index += 1
			
		else:
			var api_instance = api.instance()
			if direction[0]:
				api_instance.position = get_parent().get_node("Spawner/SpawnerAtas").get_global_position()
				api_instance.set_name(str(index))
				add_child(api_instance)
				api_instance.direction = direction[0]
				api_instance.speed = 1500
				index += 1
			else:
				api_instance.position = get_parent().get_node("Spawner/SpawnerBawah").get_global_position()
				api_instance.set_name(str(index))
				add_child(api_instance)
				api_instance.direction = direction[0]
				api_instance.speed = 1500
				index += 1
			
		element.pop_front()
		direction.pop_front()

