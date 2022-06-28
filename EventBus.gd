extends Node


var point = 0.0
var level_point = 0.0
var level = 0
var game_over = false
var a = 0
var s = 0

func _process(delta):
	if point<=0:
		point = 0
	if level_point<=0:
		level_point = 0
