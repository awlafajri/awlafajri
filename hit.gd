extends AudioStreamPlayer


# Declare member variables here. Examples:
# var a = 2
# var b = "text"


# Called when the node enters the scene tree for the first time.
func _ready():
	pass # Replace with function body.


func miss():
	play()
	pitch_scale = 1.8

func hit():
	play()
	pitch_scale =1
