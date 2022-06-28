extends Node2D


# Declare member variables here. Examples:
# var a = 2
# var b = "text"


# Called when the node enters the scene tree for the first time.
func _ready():
	$Minion2D.connect("done2",self,"_on_change_level_2")
	$ProgressBar.connect("dead",self,"_on_dead")
	$Transition/AnimationPlayer.play("Fade In")


# Called every frame. 'delta' is the elapsed time since the previous frame.
func _process(delta):
	pass

func _on_change_level_2():
	EventBus.level = 2
	yield(get_tree().create_timer(4),"timeout")
	$Transition/AnimationPlayer.play("Fade Out")
	yield($Transition/AnimationPlayer,"animation_finished")
	get_tree().change_scene("res://Level Clear.tscn")

func _on_dead():
	$Transition/AnimationPlayer.play("Fade Out")
	yield($Transition/AnimationPlayer,"animation_finished")
	get_tree().change_scene("res://Game Over.tscn")
