extends Node2D


var change: bool


# Called when the node enters the scene tree for the first time.
func _ready():
	EventBus.game_over = true
	change = true


# Called every frame. 'delta' is the elapsed time since the previous frame.
#func _process(delta):
#	pass


func _on_Button_pressed():
	if change:
		EventBus.point = EventBus.point - EventBus.level_point
		EventBus.level_point = 0
		change = false
	if EventBus.level == 0:
		get_tree().change_scene("res://Level1.tscn")
	if EventBus.level == 1:
		get_tree().change_scene("res://Level2.tscn")
	if EventBus.level == 2:
		get_tree().change_scene("res://Level3.tscn")
	if EventBus.level == 3:
		get_tree().change_scene("res://Level4.tscn")
	if EventBus.level == 4:
		get_tree().change_scene("res://Level5.tscn")

func _on_Button3_pressed():
	EventBus.level +=1
	if change:
		EventBus.level_point = 0
		change = false
	if EventBus.level == 1:
		get_tree().change_scene("res://Level2.tscn")
	if EventBus.level == 2:
		get_tree().change_scene("res://Scene2.tscn")
	if EventBus.level == 3:
		get_tree().change_scene("res://Level4.tscn")
	if EventBus.level == 4:
		get_tree().change_scene("res://Scene3.tscn")
	if EventBus.level == 5:
		get_tree().change_scene("res://End Level.tscn")


func _on_Button2_pressed():
	get_tree().change_scene("res://Menu.tscn")
