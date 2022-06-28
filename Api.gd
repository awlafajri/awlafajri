extends Area2D

var kill = false
var speed = 1000
var api = true
var direction : bool


# Called when the node enters the scene tree for the first time.
func _ready():
	pass # Replace with function body.


func _physics_process(delta):
	position += transform.x * speed * delta *(-1)
	
	if position.x <= 450 :
		if kill:
			queue_free()

	if position.x <= -20:
		queue_free()
