kata = "Fuad"
OUT_OF_GUESS=False
ANSWER_CORRECT=False
max_guess = 3
guess=0

while not(OUT_OF_GUESS) and not(ANSWER_CORRECT):
    jawaban_orang=input("Apa tebakannya?")
    if jawaban_orang.lower() == kata.lower():
        ANSWER_CORRECT=True

    guess += 1
    print("Kamu sisa punya "+ str(max_guess-guess)+"/"+str(max_guess)+" nyawa")
    if guess == max_guess:
        OUT_OF_GUESS=True

if OUT_OF_GUESS :
    print("Kamu Kalah")
else:
    print("Kamu menang")