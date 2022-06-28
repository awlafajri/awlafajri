extends Node2D


# Declare member variables here. Examples:
# var a = 2
# var b = "text"


# Called when the node enters the scene tree for the first time.
func _ready():
	$Minion2D.connect("done3",self,"_on_change_level_3")
	$ProgressBar.connect("dead",self,"_on_dead")
	$Transition/AnimationPlayer.play("Fade In")


# Called every frame. 'delta' is the elapsed time since the previous frame.
func _process(delta):
	pass

func _on_change_level_3():
	EventBus.level = 3
	yield(get_tree().create_timer(2),"timeout")
	$Transition/AnimationPlayer.play("Fade Out")
	yield($Transition/AnimationPlayer,"animation_finished")
	get_tree().change_scene("res://Level4.tscn")

func _on_dead():
	$Transition/AnimationPlayer.play("Fade Out")
	yield($Transition/AnimationPlayer,"animation_finished")
	get_tree().change_scene("res://Game Over.tscn")
