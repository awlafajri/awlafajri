extends Node2D


var bar_green = preload("res://bar.png")
var wr_vl = 10
var play = true
var dead = 50
signal dead


# Called when the node enters the scene tree for the first time.
func _ready():
	
	
	$TextureProgress.texture_progress = bar_green
	$TextureProgress.value = 20
	

func perfect():
	dead = 50
	$TextureProgress.value += 5

func right():
	dead = 50
	$TextureProgress.value += 3

func wrong():
	$TextureProgress.value -= wr_vl
	if $TextureProgress.value <= 0:
		if dead <= -50:
			emit_signal("dead")
		dead -= 10
		
	
func _process(delta):
	if $TextureProgress.value >= 100:
		get_parent().get_node("Chara/Pngegg").show()
		get_parent().get_node("Chara").multiplier = 15
		get_parent().get_node("Fever").show()
		if play:
			get_parent().get_node("Fever2").play()
			play = false
		wr_vl = 50
	else:
		get_parent().get_node("Chara/Pngegg").hide()
		get_parent().get_node("Chara").multiplier = 10
		get_parent().get_node("Fever").hide()
		wr_vl = 10
		play = true
