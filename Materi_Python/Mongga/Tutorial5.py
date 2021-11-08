is_tall=True
is_heavy=True

if not(is_tall and not(is_heavy)):
    print("Big")
elif is_tall and not(is_heavy):
    print("Tall")
elif not (is_tall) or is_heavy:
    print("human")

else:
    print("random")

a = "aiueo"
b= "a"
if b in a:
    print("yes")