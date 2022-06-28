extends Node2D


var bar_green = preload("res://barHorizontal_green.png")


# Called when the node enters the scene tree for the first time.
func _ready():
	position = get_parent().get_node("Chara").get_global_position()
	
	texture_progress = bar_green
	value = 20


func perfect():
	value += 10

func right():
	value += 5

func wrong():
	value -= 8

