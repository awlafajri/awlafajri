extends Area2D
var slime = true
var point = 0
var counter = 0
onready var node = $reset_pos
var play = false
var multiplier = 10

func _ready():
	$Sprite2.hide()


# Called every frame. 'delta' is the elapsed time since the previous frame.
func _process(delta): 
	node = get_parent().get_node("Minion2D").get_node(str(counter))
	if is_instance_valid(node):
		if node.get_global_position().x < 250:
			EventBus.point -= 10
			EventBus.level_point -= 10
			get_parent().get_node("ProgressBar").wrong()
			counter += 1
	else:
		node = $reset_pos
		if node.get_global_position().x < 250:
			counter += 1
	get_input()
	$AnimationPlayer.queue("Running")

func get_input():
	
	if Input.is_action_just_pressed("up_1"):
		get_overlap("up_1")
	elif Input.is_action_just_pressed("up_2"):
		get_overlap("up_2")
	elif Input.is_action_just_pressed("down_1"):
		get_overlap("down_1")
	elif Input.is_action_just_pressed("down_2"):
		get_overlap("down_2")

func input_miss(button):
	get_parent().get_node("hit").miss()
	if button == "up_1":
		$AnimationPlayer.stop()
		$AnimationPlayer.clear_queue()
		if slime:
			$AnimationPlayer.play("Attack_Miss_Up")
		else:
			change()
			$AnimationPlayer.play("Attack_Miss_Up")

	if button == "up_2":
		$AnimationPlayer.stop()
		$AnimationPlayer.clear_queue()
		if not(slime):
			$AnimationPlayer.play("Attack_Miss_Up")
		else:
			change()
			$AnimationPlayer.play("Attack_Miss_Up")

	if button == "down_1":
		$AnimationPlayer.stop()
		$AnimationPlayer.clear_queue()
		if slime:
			$AnimationPlayer.play("Attack_Miss_Down")
		else:
			change()
			$AnimationPlayer.play("Attack_Miss_Down")

	if button == "down_2":
		$AnimationPlayer.stop()
		$AnimationPlayer.clear_queue()
		if not(slime):
			$AnimationPlayer.play("Attack_Miss_Down")
		else:
			change()
			$AnimationPlayer.play("Attack_Miss_Down")

func input_success(button):
	get_parent().get_node("hit").hit()
	if button == "up_1":
		$AnimationPlayer.stop()
		$AnimationPlayer.clear_queue()
		if slime:
			$AnimationPlayer.play("Attack_Success_Up")
		else:
			change()
			$AnimationPlayer.play("Attack_Success_Up")

	if button == "up_2":
		$AnimationPlayer.stop()
		$AnimationPlayer.clear_queue()
		if not(slime):
			$AnimationPlayer.play("Attack_Success_Up")
		else:
			change()
			$AnimationPlayer.play("Attack_Success_Up")

	if button == "down_1":
		$AnimationPlayer.stop()
		$AnimationPlayer.clear_queue()
		if slime:
			$AnimationPlayer.play("Attack_Success_Down")
		else:
			change()
			$AnimationPlayer.play("Attack_Success_Down")

	if button == "down_2":
		$AnimationPlayer.stop()
		$AnimationPlayer.clear_queue()
		if not(slime):
			$AnimationPlayer.play("Attack_Success_Down")
		else:
			change()
			$AnimationPlayer.play("Attack_Success_Down")

func input_fail(button):
	get_parent().get_node("hit").miss()
	if button == "up_1":
		$AnimationPlayer.stop()
		$AnimationPlayer.clear_queue()
		if slime:
			$AnimationPlayer.play("Attack_Fail_Up")
		else:
			change()
			$AnimationPlayer.play("Attack_Fail_Up")

	if button == "up_2":
		$AnimationPlayer.stop()
		$AnimationPlayer.clear_queue()
		if not(slime):
			$AnimationPlayer.play("Attack_Fail_Up")
		else:
			change()
			$AnimationPlayer.play("Attack_Fail_Up")

	if button == "down_1":
		$AnimationPlayer.stop()
		$AnimationPlayer.clear_queue()
		if slime:
			$AnimationPlayer.play("Attack_Fail_Down")
		else:
			change()
			$AnimationPlayer.play("Attack_Fail_Down")

	if button == "down_2":
		$AnimationPlayer.stop()
		$AnimationPlayer.clear_queue()
		if not(slime):
			$AnimationPlayer.play("Attack_Fail_Down")
		else:
			change()
			$AnimationPlayer.play("Attack_Fail_Down")

func change():
	get_node("Sprite").hide()
	get_node("Sprite2").show()
	$AnimationPlayer2.play("Transform")
	yield($AnimationPlayer2,"animation_finished")
	get_node("Sprite2").hide()
	get_node("Sprite").show()
	if slime:
		$Sprite.texture = load("res://Chara/mcmarble.png")
		slime = false
	else:
		$Sprite.texture = load("res://Chara/ballsworth.png")
		slime = true

func get_overlap(button):
	
	var api : bool
	var direction : bool
	if button == "up_1":
		api = false
		direction = true
	if button == "up_2":
		api = true
		direction = true
	if button == "down_1":
		api = false
		direction = false
	if button == "down_2":
		api = true
		direction = false
		
	if node.get_global_position().x <= 460:
		if node.direction == direction:
			if node.api == api:
				input_success(button)
				get_parent().get_node("hitbox").perfect()
				counter += 1
				EventBus.point += 1.25*multiplier
				EventBus.level_point += 1.25*multiplier
				get_parent().get_node("ProgressBar").perfect()
				node.queue_free()
				return
			else:
				input_fail(button)
				get_parent().get_node("hitbox").wrong()
				get_parent().get_node("ProgressBar").wrong()
				counter +=1
				EventBus.point -= 10
				EventBus.level_point -= 10
				node.queue_free()
				return
		else:
			input_miss(button)
			return
		

			
	if node.get_global_position().x <= 840:
		if node.direction == direction:
			if node.api == api:
				input_success(button)
				get_parent().get_node("hitbox").right()
				get_parent().get_node("ProgressBar").right()
				counter += 1
				EventBus.point += multiplier
				EventBus.level_point += multiplier
				node.kill = true
				return
			else:
				input_fail(button)
				get_parent().get_node("hitbox").wrong()
				get_parent().get_node("ProgressBar").wrong()
				counter +=1
				EventBus.point -= 10
				EventBus.level_point -= 10
				node.kill = true
				return
		else:
			input_miss(button)
			return
	
	if node.get_global_position().x > 840:
		get_parent().get_node("ProgressBar").wrong()
		input_miss(button)
		return

