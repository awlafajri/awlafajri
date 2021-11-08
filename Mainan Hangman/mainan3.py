from soal import *

prompt_soal=[
    "1. Siapa yang laki-laki? \n a. Awla \n b. Chintya \n c. Aninda",
    "2. Apa warna kesukaan Bambang? \n a. Merah \n b. Biru \n c. Ungu",
    "3. 1+1= \n a.2 \n b.3 \n c.4"
]


pertanyaan=[
    soal(prompt_soal[0],"a"),
    soal(prompt_soal[1],"b"),
    soal(prompt_soal[2],"a")
]

score = 0
for f in pertanyaan:
    jawaban = input(f.soal + "\n")
    if jawaban == f.jawaban:
        score += 1

print(score)