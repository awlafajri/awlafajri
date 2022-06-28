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
	get_tree().change_scene("res://Menu.tscn")


func _on_Button_pressed():
	EventBus.level_point = 0
	if $Label5.text == "A":
		EventBus.a += 1
	if $Label5.text == "S":
		EventBus.s += 1
	if EventBus.level == 2:
		get_tree().change_scene("res://Scene2.tscn")
	elif EventBus.level == 4:
		get_tree().change_scene("res://Scene3.tscn")
	else:
		get_tree().change_scene("res://End Level.tscn")