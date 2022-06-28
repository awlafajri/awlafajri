extends Sprite


# Declare member variables here. Examples:
# var a = 2
# var b = "text"


# Called when the node enters the scene tree for the first time.
func _ready():
	pass # Replace with function body.


# Called every frame. 'delta' is the elapsed time since the previous frame.
func perfect():
	texture = load("res://bg/perfect.png")
	yield(get_tree().create_timer(0.1),"timeout")
	texture = load("res://bg/idle.png")

func right():
	texture = load("res://bg/right.png")
	yield(get_tree().create_timer(0.1),"timeout")
	texture = load("res://bg/idle.png")
	
func wrong():
	texture = load("res://bg/wrong.png")
	yield(get_tree().create_timer(0.1),"timeout")
	texture = load("res://bg/idle.png")
