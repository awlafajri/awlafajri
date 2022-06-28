extends Node2D


# Declare member variables here. Examples:
# var a = 2
# var b = "text"


# Called when the node enters the scene tree for the first time.
func _ready():
	$Transition/AnimationPlayer.play("Fade In")
	yield($Transition/AnimationPlayer,"animation_finished")
	remove_child($Transition)


# Called every frame. 'delta' is the elapsed time since the previous frame.
#func _process(delta):
#	pass


func _on_Button_pressed():
	add_child(load("res://Transition.tscn").instance())
	$Transition/AnimationPlayer.play("Fade Out")
	yield($Transition/AnimationPlayer,"animation_finished")
	get_tree().change_scene("res://Level3.tscn")
