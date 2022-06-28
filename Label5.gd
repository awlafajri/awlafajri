extends Label


# Declare member variables here. Examples:
# var a = 2
# var b = "text"


# Called when the node enters the scene tree for the first time.
func _ready():
	if EventBus.level == 2:
		if EventBus.level_point >= (4040*1.5):
			text = "S"
		elif EventBus.level_point >= (4040*1.2):
			text = "A"
		elif EventBus.level_point >= (4040*0.8):
			text = "B"
		elif EventBus.level_point >= (4040*0.5):
			text = "C"
		else:
			text = "F"
	
	if EventBus.level == 4:
		if EventBus.level_point >= (4040*1.5):
			text = "S"
		elif EventBus.level_point >= (4040*1.2):
			text = "A"
		elif EventBus.level_point >= (4040*0.8):
			text = "B"
		elif EventBus.level_point >= (4040*0.5):
			text = "C"
		else:
			text = "F"
	
	if EventBus.level == 5:
		if EventBus.level_point >= (4140*1.5):
			text = "S"
		elif EventBus.level_point >= (4140*1.2):
			text = "A"
		elif EventBus.level_point >= (4140*0.8):
			text = "B"
		elif EventBus.level_point >= (4140*0.5):
			text = "C"
		else:
			text = "F"


# Called every frame. 'delta' is the elapsed time since the previous frame.
func _process(delta):
	pass
