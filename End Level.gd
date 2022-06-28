extends Node2D


# Declare member variables here. Examples:
# var a = 2
# var b = "text"


# Called when the node enters the scene tree for the first time.
func _ready():
	pass


# Called every frame. 'delta' is the elapsed time since the previous frame.
func _process(delta):

	if EventBus.s == 3:
		$Label2.text = "You are a certified banana gang, here some gold banana (goldana)"
		$Lock.texture = load("res://goldana.png")
	
	if EventBus.a == 3:
		$Label2.text = "You are a hardcore man, here some banana (banana)"
		$Lock.texture = load("res://banana.png")

	if not EventBus.game_over:
		$Label2.text = "Congrats you beat the game (ez), here some green banana (grenana)"
		$Lock.texture = load("res://greenana.png")


func _on_Button_pressed():
	get_tree().change_scene("res://Menu.tscn")
