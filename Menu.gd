extends Node2D


# Declare member variables here. Examples:
# var a = 2
# var b = "text"


# Called when the node enters the scene tree for the first time.
func _ready():
	pass # Replace with function body.


# Called every frame. 'delta' is the elapsed time since the previous frame.
#func _process(delta):
#	pass


func _on_Button2_pressed():
	get_tree().change_scene("res://Tutorial.tscn")


func _on_Button_pressed():
	EventBus.point = 0
	EventBus.level_point = 0
	EventBus.level = 0
	EventBus.a = 0
	EventBus.s = 0
	EventBus.game_over = false
	get_tree().change_scene("res://Scene1.tscn")
